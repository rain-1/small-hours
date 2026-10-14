"""Composite ambience loops: bed layers + scattered events -> crossfaded loop at -26 LUFS."""
import subprocess, sys, os, numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from proc import loopify, norm_lufs, save, lufs_of, SR, fix_phase
RAW = "/tmp/claude-1000/-home-riv-Code-claude-game/079066a0-8d3e-4e7b-9d93-b973c06998eb/scratchpad/audio_raw/"
OUT = "/home/riv/Code/claude-game/game/audio/sfx/"
def load(f, af=None, ss=0, t=None):
    cmd = ["ffmpeg", "-v", "error", "-ss", str(ss)] + (["-t", str(t)] if t else []) + ["-i", RAW + f + ".mp3"]
    if af: cmd += ["-af", af]
    cmd += ["-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    return fix_phase(np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).reshape(-1, 2).astype(np.float64))
def content(x, rel=-30):
    """strip trailing (SA pads silence) and leading silence"""
    w = SR // 20; m = x.mean(1); n = len(m) // w
    db = 20 * np.log10(np.sqrt((m[:n*w].reshape(n, w) ** 2).mean(1)) + 1e-9)
    ok = np.where(db > np.median(db) + rel)[0]
    return x[ok[0] * w:(ok[-1] + 1) * w]
def fit(x, D):
    """loop/crop a bed to D seconds (internal crossfade if too short)"""
    N = int(D * SR)
    while len(x) < N:
        n = int(SR * 1.5); t = np.linspace(0, np.pi / 2, n)[:, None]
        x = np.concatenate([x[:-n], x[-n:] * np.cos(t) + x[:n] * np.sin(t), x[n:]])
    return x[:N]
def lv(x, db_target):
    """set a layer to a given LUFS-ish level (via integrated loudness)"""
    L = 20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-9) - 1
    if len(x) > 1.5 * SR:
        try:
            Li = lufs_of(x)
            if Li > -69: L = Li
        except Exception: pass
    return x * 10 ** ((db_target - L) / 20)
def env(x, fi=0.05, fo=0.3):
    x = x.copy(); a, b = int(fi * SR), int(fo * SR)
    x[:a] *= np.linspace(0, 1, a)[:, None]; x[-b:] *= np.linspace(1, 0, b)[:, None]; return x
def pan(x, p):  # p in [-1,1]
    return x * np.array([np.sqrt((1 - p) / 2), np.sqrt((1 + p) / 2)]) * np.sqrt(2)
def syn_hum(D, base=60.0, seed=0):
    """loop-safe mains hum: integer-Hz harmonics, slow AM; phase-coherent at the 40s crossfade lag"""
    t = np.arange(int(D * SR)) / SR; rng = np.random.default_rng(seed)
    y = sum(a * np.sin(2 * np.pi * base * k * t + rng.uniform(0, 6.28)) for k, a in ((1, .3), (2, 1), (3, .25), (4, .35), (6, .12), (8, .06)))
    y *= 1 + 0.15 * np.sin(2 * np.pi * 0.25 * t)
    return np.stack([y, y * 0.97], 1)
def compose(name, D, beds, events, seed=0, target=-26):
    rng = np.random.default_rng(seed)
    mix = np.zeros((int(D * SR), 2))
    for b in beds:  # (file, level, af, ss)
        f, L = b[0], b[1]; af = b[2] if len(b) > 2 else None; ss = b[3] if len(b) > 3 else 0; t = b[4] if len(b) > 4 else None
        mix += lv(syn_hum(D) if f == "SYN_HUM" else fit(content(load(f, af, ss, t)), D), L)
    for e in events:  # dict(f, level, n, af, seg=(len_lo,len_hi), times=None)
        if e["f"] == "SYN_BEEP":
            tt = np.arange(int(0.5 * SR)) / SR; b = np.sin(2 * np.pi * 880 * tt) * np.minimum(1, tt / 0.01) * np.exp(-np.maximum(0, tt - 0.09) / 0.03)
            b = b + 0.35 * np.concatenate([np.zeros(int(0.07 * SR)), b])[:len(b)]   # room slap
            src = np.stack([b, b], 1)
        else: src = load(e["f"], e.get("af"), e["clip"][0], e["clip"][1]) if "clip" in e else content(load(e["f"], e.get("af")), -35)
        times = e.get("times") or sorted(rng.uniform(0.5, D - 3, e["n"]))
        for t in times:
            if e.get("seg"):
                Ls = rng.uniform(*e["seg"]); s0 = rng.uniform(0, max(0.01, len(src) / SR - Ls))
                ev = src[int(s0 * SR): int((s0 + Ls) * SR)]
            else: ev = src
            ev = env(ev, e.get("fi", 0.05), e.get("fo", 0.3))
            j = e.get("jitter", True)
            ev = pan(lv(ev, e["level"] + (rng.uniform(-3, 3) if j else 0)), rng.uniform(-0.6, 0.6) if j else e.get("pan", 0))
            k = int(t * SR); n = min(len(ev), len(mix) - k); mix[k:k + n] += ev[:n]
    mix = norm_lufs(mix, target)
    mix = loopify(mix, 2.0, snap=False)
    save(mix, OUT + name + ".mp3", "128k")
    print(name, f"{len(mix)/SR:.1f}s")

if __name__ == "__main__":
    which = sys.argv[1:]
    J = {
     "amb_rain": lambda: compose("amb_rain", 40, [("amb_rain_a", -26), ("amb_rain_b", -34, "lowpass=2500")],
        [dict(f="ev_drips_a", level=-35, n=12, seg=(1.5, 3))], 1),
     "amb_street": lambda: compose("amb_street", 42, [("amb_street_b", -28), ("amb_street2_a", -30, "lowpass=1200"), ("amb_rain_a", -36)],
        [dict(f="ev_walla_a", level=-38, n=3, seg=(4, 8), fi=1.5, fo=2, af="pan=stereo|c0=c0|c1=c0,lowpass=2200"),
         dict(f="ev_walla_b", level=-39, n=2, seg=(4, 8), fi=1.5, fo=2, af="pan=stereo|c0=c0|c1=c0,lowpass=2200"),
         dict(f="train_b", level=-28, n=1, times=[16.0], fi=1.0, fo=1.5, af="lowpass=900,volume=1")], 2),
     "amb_shop": lambda: compose("amb_shop", 42, [("amb_shop_b", -32), ("ev_simmer_b", -31), ("amb_rain_a", -40, "lowpass=1500")],
        [dict(f="ev_clatter_a", level=-33, n=6, seg=(0.6, 1.8), fi=0.01, fo=0.2), dict(f="ev_clatter_b", level=-34, n=5, seg=(0.6, 1.8), fi=0.01, fo=0.2),
         dict(f="ev_simmer_a", level=-37, n=3, seg=(3, 6), fi=1, fo=1)], 3),
     "amb_roof": lambda: compose("amb_roof", 42, [("amb_roof2_b", -29), ("amb_rain_a", -38, "highpass=800"), ("amb_street2_a", -37, "lowpass=400"), ("ev_neon_b", -38, "highpass=200")],
        [dict(f="amb_roof2_a", level=-30, n=3, seg=(6, 9), fi=2.5, fo=3), dict(f="ev_neon_a", level=-33, n=3, seg=(4, 7), fi=0.2, fo=0.5)], 4),
     "amb_clinic": lambda: compose("amb_clinic", 42, [("amb_clinic_a", -30), ("amb_clinic2_b", -34)],
        [dict(f="SYN_BEEP", level=-40, times=[0.3 + i * 1.0 for i in range(41)], fi=0.005, fo=0.05, jitter=False, pan=0.4)], 5),
     "amb_office": lambda: compose("amb_office", 42, [("amb_office2_a", -32), ("ev_rainwindow_a", -31, None, 4.5, 5), ("ev_rainwindow_b", -35, None, 4.5, 5)],
        [dict(f="ev_radiator_a", level=-36, n=5, clip=(0, 1.2), fi=0.003, fo=0.3), dict(f="ev_radiator_b", level=-37, n=4, clip=(0, 1.2), fi=0.003, fo=0.3)], 6),
     "amb_alley": lambda: compose("amb_alley", 42, [("amb_alley_a", -30), ("SYN_HUM", -36), ("amb_street2_a", -36, "lowpass=600")],
        [dict(f="ev_drips_a", level=-32, n=14, seg=(1.5, 3), af="aecho=0.8:0.5:90:0.25")], 7),
     "amb_dawn": lambda: compose("amb_dawn", 42, [("amb_dawn_b", -30, None, 6), ("amb_roof2_b", -40, "highpass=150,lowpass=1500")],
        [dict(f="ev_birds_a", af="highpass=1200", level=-31, n=5, seg=(2, 5), fi=0.3, fo=0.6), dict(f="ev_birds_b", af="highpass=1200", level=-32, n=4, seg=(2, 5), fi=0.3, fo=0.6),
         dict(f="ev_gulls_a", level=-38, n=2, seg=(2, 4), fi=0.3, fo=0.6, af="lowpass=3000"), dict(f="ev_gulls_b", level=-38, n=1, seg=(2, 4), fi=0.3, fo=0.6, af="lowpass=3000")], 8),
    }
    for k in (which or J): J[k]()
