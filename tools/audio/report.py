import subprocess, json, re, glob, os, numpy as np
ROOT = "/home/riv/Code/claude-game/game/audio"
rows = {}
for f in sorted(glob.glob(ROOT + "/*/*.mp3")):
    pr = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", f], capture_output=True, text=True).stdout)
    st = pr["streams"][0]; dur = float(pr["format"]["duration"]); br = int(pr["format"]["bit_rate"]) // 1000
    e = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", f, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    I = re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]; P = re.findall(r"Peak:\s+(-?[\d.]+|-inf) dBFS", e)[-1]
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "f32le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.float32).reshape(-1, 2)
    corr = float(np.corrcoef(x[:, 0], x[:, 1])[0, 1]) if x.std() > 0 else 1
    pk = 20 * np.log10(np.abs(x).max() + 1e-9)
    rel = os.path.relpath(f, ROOT)
    rows[rel] = dict(dur=round(dur, 2), sr=st["sample_rate"], ch=st["channels"], kbps=br, lufs=float(I), tp=P, peak=round(float(pk), 1), lr_corr=round(float(corr), 2))
    print(f"{rel:28s} {dur:7.2f}s {st['sample_rate']} ch{st['channels']} {br:4d}k  I={I:>6} TP={P:>6} pk={pk:6.1f} corr={corr:5.2f}")
json.dump(rows, open("/tmp/claude-1000/-home-riv-Code-claude-game/079066a0-8d3e-4e7b-9d93-b973c06998eb/scratchpad/report.json", "w"), indent=1)
