"""Post-processing: python proc.py <mode> <in> <out> [opts]
modes: loop (music/ambience), song (non-loop, fade end), shot (one-shot)"""
import argparse, subprocess, re, numpy as np
SR = 44100
def load(f):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return fix_phase(np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64))
def fix_phase(x):
    """flip R polarity if the channels are substantially anti-phase (mono-compat)"""
    if len(x) > 100 and x.std() > 0 and np.corrcoef(x[:, 0], x[:, 1])[0, 1] < -0.1: x = x * np.array([1, -1])
    return x
def lufs_of(x):
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-",
                        "-af", "ebur128=peak=true", "-f", "null", "-"], input=x.astype(np.float32).tobytes(), capture_output=True)
    e = p.stderr.decode(); I = re.findall(r"I:\s+(-?[\d.]+) LUFS", e)
    return float(I[-1])
def win_db(x, w):
    m = x.mean(1); n = len(m) // w
    return 20 * np.log10(np.sqrt((m[:n * w].reshape(n, w) ** 2).mean(1)) + 1e-9)
def trim_music(x, head_rel=-14, tail_rel=-9):
    w = SR // 4; db = win_db(x, w); med = np.median(db)
    ok = np.where(db > med + head_rel)[0]; s = ok[0]
    ok2 = np.where(db > med + tail_rel)[0]; e = ok2[-1] + 1
    return x[s * w: e * w]
def limiter(x, ceil_db=-1.0):
    c = 10 ** (ceil_db / 20); pk = np.abs(x).max(1)
    if pk.max() <= c: return x
    # smooth gain envelope: instant attack via running max over 5ms lookahead, 80ms release
    g = np.minimum(1, c / (pk + 1e-12))
    la = int(0.005 * SR)
    from numpy.lib.stride_tricks import sliding_window_view
    gp = np.concatenate([g, np.ones(la)]); gmin = sliding_window_view(gp, la + 1).min(1)[:len(g)]
    rel = np.exp(-1 / (0.08 * SR)); out = np.empty_like(gmin); s = 1.0
    for i, v in enumerate(gmin):
        s = v if v < s else rel * s + (1 - rel) * v; out[i] = s
    return x * out[:, None]
def norm_lufs(x, target):
    g = 10 ** ((target - lufs_of(x)) / 20)
    return limiter(x * g)
def snap_len(x, n, search=4.0, W=3.0):
    """choose loop length L so content at L-n matches content at 0 (beat/bar phase)."""
    h = SR // 100; m = np.abs(x.mean(1)); k = len(m) // h
    e = np.sqrt((m[:k * h].reshape(k, h) ** 2).mean(1)); o = np.maximum(0, np.diff(np.log(e + 1e-6), prepend=0))
    w = int(W * 100); a = o[:w] - o[:w].mean(); best, bD = -9, None
    Dmax = (len(x) - n) // h - w
    for D in range(max(w, Dmax - int(search * 100)), Dmax + 1):
        b = o[D:D + w] - o[D:D + w].mean(); c = (a * b).sum() / (np.sqrt((a * a).sum() * (b * b).sum()) + 1e-9)
        if c > best: best, bD = c, D
    print(f"  snap: corr={best:.2f}")
    return bD * h + n
def loopify(x, xf, snap=True):
    n = int(xf * SR)
    if snap: x = x[:snap_len(x, n)]
    L = len(x)
    t = np.linspace(0, np.pi / 2, n)[:, None]
    head = x[:n] * np.sin(t) + x[L - n:] * np.cos(t)
    return np.concatenate([head, x[n:L - n]])
def save(x, out, br):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-",
                    "-c:a", "libmp3lame", "-b:a", br, out], input=np.clip(x, -1, 1).astype(np.float32).tobytes(), check=True)
def fades(x, fi, fo):
    x = x.copy(); a = int(fi * SR); b = int(fo * SR)
    if a: x[:a] *= np.linspace(0, 1, a)[:, None]
    if b: x[-b:] *= (np.cos(np.linspace(0, np.pi, b)) * 0.5 + 0.5)[:, None]
    return x
if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("mode"); p.add_argument("inp"); p.add_argument("out")
    p.add_argument("--lufs", type=float, default=-18); p.add_argument("--br", default="160k")
    p.add_argument("--xf", type=float, default=2.0); p.add_argument("--start", type=float, default=None)
    p.add_argument("--end", type=float, default=None); p.add_argument("--fadeout", type=float, default=6)
    p.add_argument("--peak", type=float, default=-3); p.add_argument("--maxdur", type=float, default=None)
    p.add_argument("--notrim", action="store_true"); p.add_argument("--nosnap", action="store_true"); p.add_argument("--headrel", type=float, default=-14); p.add_argument("--tailrel", type=float, default=-9); p.add_argument("--gate", type=float, default=-40)
    a = p.parse_args()
    x = load(a.inp)
    if a.start is not None or a.end is not None:
        x = x[int((a.start or 0) * SR): int(a.end * SR) if a.end else None]
    if a.mode in ("loop", "song"):
        if not a.notrim: x = trim_music(x, a.headrel, a.tailrel)
        x = norm_lufs(x, a.lufs)
        if a.mode == "loop": x = loopify(x, a.xf, not a.nosnap)
        else: x = fades(x, 0.02, a.fadeout)
    else:  # shot
        w = SR // 100; db = win_db(x, w); thr = db.max() + a.gate
        ok = np.where(db > thr)[0]; s = max(0, ok[0] - 1); e = min(len(db), ok[-1] + 3)
        x = x[s * w: e * w]
        if a.maxdur and len(x) > a.maxdur * SR: x = x[:int(a.maxdur * SR)]
        x = fades(x, 0.004, min(a.fadeout, len(x) / SR / 3))
        x = x / np.abs(x).max() * 10 ** (a.peak / 20)
    save(x, a.out, a.br)
    if a.mode == "shot":   # mp3 encoding can overshoot: correct to target peak
        for _ in range(3):
            pk = 20 * np.log10(np.abs(load(a.out)).max())
            if pk <= a.peak + 0.3: break
            x = x * 10 ** ((a.peak - pk) / 20); save(x, a.out, a.br)
        print(f"  peak {pk:.1f}")
    print(f"{a.out}: {len(x)/SR:.1f}s")
