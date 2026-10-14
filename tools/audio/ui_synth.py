import numpy as np, wave, subprocess, os
SR = 44100
OUT = "/home/riv/Code/claude-game/game/audio/ui"
TMP = "/tmp/claude-1000/-home-riv-Code-claude-game/079066a0-8d3e-4e7b-9d93-b973c06998eb/scratchpad/ui_wav"
os.makedirs(OUT, exist_ok=True); os.makedirs(TMP, exist_ok=True)
def t(d): return np.arange(int(SR * d)) / SR
def tri(f, d): x = t(d); return 2 * np.abs(2 * ((x * f) % 1) - 1) - 1
def sine(f, d): return np.sin(2 * np.pi * f * t(d))
def env(n, a=0.003, dec=0.05):
    x = np.arange(n) / SR
    e = np.minimum(1, x / max(a, 1e-4)) * np.exp(-np.maximum(0, x - a) / dec)
    return e
def bell(f, d, dec=0.6, partials=((1, 1), (2.0, 0.35), (3.01, 0.12), (4.2, 0.05))):
    x = t(d); y = np.zeros_like(x)
    for r, a in partials: y += a * np.sin(2 * np.pi * f * r * x) * np.exp(-x / (dec / r ** 0.7))
    k = int(len(x) * 0.4); y[-k:] *= np.cos(np.linspace(0, np.pi / 2, k)) ** 2
    return y * np.minimum(1, x / 0.004)
def lp(y, fc):
    a = np.exp(-2 * np.pi * fc / SR); out = np.zeros_like(y); s = 0.0
    for i, v in enumerate(y): s = (1 - a) * v + a * s; out[i] = s
    return out
def echo(y, delays=((0.11, 0.25), (0.23, 0.12), (0.37, 0.06)), tail=0.5):
    out = np.concatenate([y, np.zeros(int(SR * tail))])
    for d, g in delays:
        k = int(SR * d); out[k:k + len(y)] += g * lp(y, 2500)[:len(out) - k]
    return out
def place(total, *items):
    out = np.zeros(int(SR * total))
    for start, y in items:
        k = int(SR * start); n = min(len(y), len(out) - k); out[k:k + n] += y[:n]
    return out
def save(name, y, peak_db):
    y = y / (np.max(np.abs(y)) + 1e-9) * 10 ** (peak_db / 20)
    fade = min(len(y) // 4, int(SR * 0.01)); y[-fade:] *= np.linspace(1, 0, fade)
    st = np.stack([y, y], 1)
    w = f"{TMP}/{name}.wav"
    with wave.open(w, "wb") as f:
        f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR)
        f.writeframes((st * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", w, "-ar", "44100", "-ac", "2", "-b:a", "128k", f"{OUT}/{name}.mp3"], check=True)

# blip: ~30ms triangle 1200Hz, soft lowpassed
d = 0.03; y = lp(tri(1200, d) * env(int(SR * d), 0.002, 0.012), 3500); save("blip", np.concatenate([y, np.zeros(int(SR*0.01))]), -14)
y = lp(tri(820, d) * env(int(SR * d), 0.002, 0.013), 3000); save("blip_low", np.concatenate([y, np.zeros(int(SR*0.01))]), -14)
# click: soft pluck 660 + 1320 short, small echo
d = 0.12; y = (sine(660, d) + 0.3 * sine(1320, d)) * env(int(SR * d), 0.002, 0.025); save("click", echo(lp(y, 4000), ((0.07, 0.15),), 0.12), -12)
# hover: very faint tick
d = 0.025; y = lp(tri(2000, d) * env(int(SR * d), 0.001, 0.006), 5000); save("hover", y, -24)
# discover: rising 3-note chime (D5 F#5 A5)
notes = [587.33, 739.99, 880.0]
y = place(1.2, *[(i * 0.11, bell(f, 1.0, 0.45)) for i, f in enumerate(notes)]); save("discover", echo(y, tail=0.6), -9)
# word: warm two-note bell (G4 -> D5)
y = place(1.3, (0, bell(392.0, 1.2, 0.7)), (0.16, bell(587.33, 1.1, 0.7))); save("word", echo(y, tail=0.6), -9)
# order: ticket bell ding (desk bell inharmonic)
y = bell(1568, 1.4, 0.55, ((1, 1), (2.76, 0.4), (5.4, 0.15), (8.9, 0.05))); save("order", echo(y, ((0.09, 0.15), (0.19, 0.07)), 0.3), -8)
# journal: soft page whoosh (filtered noise) + gentle chime
rng = np.random.default_rng(3); n = int(SR * 0.35)
nz = lp(lp(rng.standard_normal(n), 1800), 1800) * np.sin(np.pi * np.arange(n) / n) ** 2 * 0.6
y = place(1.2, (0, nz), (0.18, 0.5 * bell(1046.5, 0.9, 0.5))); save("journal", echo(y, tail=0.4), -12)
# time: low soft clock chime (two low bells)
y = place(2.2, (0, bell(261.63, 2.0, 1.1)), (0.55, bell(196.0, 1.8, 1.1))); save("time", echo(lp(y, 2500), ((0.15, 0.2), (0.31, 0.1)), 0.6), -10)
print("ok")
