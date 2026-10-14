import json, os, subprocess, sys, time, urllib.request
sys.path.insert(0, os.path.dirname(__file__))
from jobs import J
RAW = "/tmp/claude-1000/-home-riv-Code-claude-game/079066a0-8d3e-4e7b-9d93-b973c06998eb/scratchpad/audio_raw"
LOG = RAW + "/gen_log.jsonl"
only = sys.argv[1:]
def alive():
    try: urllib.request.urlopen("http://127.0.0.1:8188/system_stats", timeout=10); return True
    except Exception: return False
for j in J:
    if only and not any(j["name"].startswith(o) for o in only): continue
    out = f"{RAW}/{j['name']}.mp3"
    if os.path.exists(out): continue
    for attempt in range(3):
        if not alive():
            print("comfy down, restarting", flush=True)
            subprocess.Popen("cd ~/comfy/ComfyUI && nohup ~/Code/Eidoverse/comfy-env/bin/python main.py --listen 127.0.0.1 --port 8188 > /tmp/claude-1000/-home-riv-Code-claude-game/079066a0-8d3e-4e7b-9d93-b973c06998eb/scratchpad/comfy.log 2>&1 &", shell=True)
            for _ in range(60):
                time.sleep(5)
                if alive(): break
        cmd = ["python3", "tools/comfy_audio.py", j["kind"], j["prompt"], str(j["sec"]), out, "--seed", str(j["seed"])]
        if j["kind"] == "sfx": cmd += ["--neg", j["neg"]]
        else:
            cmd += ["--bpm", str(j["bpm"]), "--key", j["key"]]
            if j.get("lyrics"): cmd += ["--lyrics", j["lyrics"]]
        r = subprocess.run(cmd, cwd="/home/riv/Code/claude-game", capture_output=True, text=True)
        print(j["name"], r.stdout.strip().replace("\n", " | "), r.stderr.strip()[-300:], flush=True)
        if os.path.exists(out):
            with open(LOG, "a") as f: f.write(json.dumps(j) + "\n")
            break
