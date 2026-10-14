"""QA: python qa.py file... -> prints metrics, writes spectrogram png to qa/"""
import subprocess, sys, re, os, numpy as np
QA = "/tmp/claude-1000/-home-riv-Code-claude-game/079066a0-8d3e-4e7b-9d93-b973c06998eb/scratchpad/qa"
def load(f, sr=22050):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32), sr
def loud(f):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", f, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    I = re.findall(r"I:\s+(-?[\d.]+|-inf) LUFS", e); P = re.findall(r"Peak:\s+(-?[\d.]+|-inf) dBFS", e)
    return float(I[-1]) if I else None, float(P[-1]) if P else None
def sil(f, th=-50, d=0.7):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", f, "-af", f"silencedetect=n={th}dB:d={d}", "-f", "null", "-"], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", e)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", e)]
    return list(zip(st, en + [None] * (len(st) - len(en))))
def metrics(f):
    x, sr = load(f)
    dur = len(x) / sr
    n = 2048; hop = 1024
    if len(x) < n: return dict(dur=dur)
    fr = np.lib.stride_tricks.sliding_window_view(x, n)[::hop] * np.hanning(n)
    S = np.abs(np.fft.rfft(fr, axis=1)) + 1e-9
    flat = np.exp(np.mean(np.log(S), 1)) / np.mean(S, 1)   # 1 = noise, 0 = tonal
    freqs = np.fft.rfftfreq(n, 1 / sr)
    cent = (S * freqs).sum(1) / S.sum(1)
    # per-second rms dB envelope
    sec = int(dur)
    env = [20 * np.log10(np.sqrt(np.mean(x[i*sr:(i+1)*sr]**2)) + 1e-9) for i in range(max(sec, 1))]
    return dict(dur=round(dur, 2), flat=round(float(np.median(flat)), 3), cent=int(np.median(cent)),
                env=" ".join(f"{int(v)}" for v in env))
if __name__ == "__main__":
    spec = "--spec" in sys.argv
    for f in [a for a in sys.argv[1:] if not a.startswith("--")]:
        I, P = loud(f); m = metrics(f); s = sil(f)
        print(f"{os.path.basename(f)}: dur={m.get('dur')} I={I} TP={P} flat={m.get('flat')} cent={m.get('cent')} sil={[(round(a,1), round(b,1) if b else None) for a,b in s]}")
        print(f"   env: {m.get('env')}")
        if spec:
            out = f"{QA}/{os.path.basename(f)}.png"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-lavfi", "showspectrumpic=s=800x300:legend=1:scale=log:fscale=log", out])
