"""Generate game audio through a local ComfyUI (http://127.0.0.1:8188).

  python tools/comfy_audio.py sfx   "<prompt>" <seconds> <out.mp3> [--seed N] [--neg "..."]
  python tools/comfy_audio.py music "<tags>"   <seconds> <out.mp3> [--seed N] [--bpm 80]
                                    [--key "D major"] [--lyrics "[instrumental]"]

sfx   -> Stable Audio 3 medium (prompt sent verbatim; start with "TrackType: SFX.")
music -> ACE-Step 1.5 turbo (instrumental unless --lyrics given)
"""
import argparse, json, os, random, sys, time, urllib.parse, urllib.request
from pathlib import Path

COMFY = os.environ.get("COMFYUI_URL", "http://127.0.0.1:8188")


def sfx_graph(prompt, seconds, seed, neg):
    return {
        "ckpt": {"class_type": "CheckpointLoaderSimple",
                 "inputs": {"ckpt_name": "stable_audio_3_medium_base.safetensors"}},
        "clip": {"class_type": "CLIPLoader",
                 "inputs": {"clip_name": "t5gemma_b_b_ul2.safetensors", "type": "stable_audio", "device": "default"}},
        "pos": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["clip", 0]}},
        "neg": {"class_type": "CLIPTextEncode", "inputs": {"text": neg, "clip": ["clip", 0]}},
        "lat": {"class_type": "EmptyLatentAudio", "inputs": {"seconds": seconds, "batch_size": 1}},
        "ks": {"class_type": "KSampler",
               "inputs": {"seed": seed, "steps": 50, "cfg": 7.0, "sampler_name": "lcm", "scheduler": "simple",
                          "denoise": 1.0, "model": ["ckpt", 0], "positive": ["pos", 0], "negative": ["neg", 0],
                          "latent_image": ["lat", 0]}},
        "dec": {"class_type": "VAEDecodeAudio", "inputs": {"samples": ["ks", 0], "vae": ["ckpt", 2]}},
        "save": {"class_type": "SaveAudioMP3",
                 "inputs": {"filename_prefix": "audio/smallhours", "quality": "V0", "audio": ["dec", 0]}},
    }


def music_graph(tags, seconds, seed, bpm, key, lyrics, timesig):
    return {
        "unet": {"class_type": "UNETLoader",
                 "inputs": {"unet_name": "acestep_v1.5_turbo.safetensors", "weight_dtype": "default"}},
        "clip": {"class_type": "DualCLIPLoader",
                 "inputs": {"clip_name1": "qwen_0.6b_ace15.safetensors", "clip_name2": "qwen_1.7b_ace15.safetensors",
                            "type": "ace", "device": "default"}},
        "vae": {"class_type": "VAELoader", "inputs": {"vae_name": "ace_1.5_vae.safetensors"}},
        "msa": {"class_type": "ModelSamplingAuraFlow", "inputs": {"shift": 3, "model": ["unet", 0]}},
        "enc": {"class_type": "TextEncodeAceStepAudio1.5",
                "inputs": {"clip": ["clip", 0], "tags": tags, "lyrics": lyrics, "seed": seed, "bpm": bpm,
                           "duration": seconds, "timesignature": timesig, "language": "en", "keyscale": key,
                           "generate_audio_codes": True, "cfg_scale": 2.0, "temperature": 0.85, "top_p": 0.9,
                           "top_k": 0, "min_p": 0.0}},
        "zero": {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["enc", 0]}},
        "lat": {"class_type": "EmptyAceStep1.5LatentAudio", "inputs": {"seconds": seconds, "batch_size": 1}},
        "ks": {"class_type": "KSampler",
               "inputs": {"seed": seed, "steps": 8, "cfg": 1.0, "sampler_name": "euler", "scheduler": "simple",
                          "denoise": 1.0, "model": ["msa", 0], "positive": ["enc", 0], "negative": ["zero", 0],
                          "latent_image": ["lat", 0]}},
        "dec": {"class_type": "VAEDecodeAudio", "inputs": {"samples": ["ks", 0], "vae": ["vae", 0]}},
        "save": {"class_type": "SaveAudioMP3",
                 "inputs": {"filename_prefix": "audio/smallhours", "quality": "V0", "audio": ["dec", 0]}},
    }


def run(graph, out, timeout=900):
    req = urllib.request.Request(f"{COMFY}/prompt", data=json.dumps({"prompt": graph}).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        pid = json.loads(urllib.request.urlopen(req, timeout=30).read())["prompt_id"]
    except urllib.error.HTTPError as e:
        sys.exit(f"ComfyUI rejected graph: {e.read().decode()[:2000]}")
    t0 = time.time()
    while time.time() - t0 < timeout:
        time.sleep(2)
        try:
            hist = json.loads(urllib.request.urlopen(f"{COMFY}/history/{pid}", timeout=15).read())
        except OSError:
            continue
        entry = hist.get(pid)
        if not entry:
            continue
        if entry.get("status", {}).get("status_str") == "error":
            sys.exit("ERROR: " + json.dumps(entry["status"])[:2000])
        for o in entry.get("outputs", {}).values():
            for a in o.get("audio", []):
                q = urllib.parse.urlencode({"filename": a["filename"], "subfolder": a.get("subfolder", ""),
                                            "type": a.get("type", "output")})
                data = urllib.request.urlopen(f"{COMFY}/view?{q}", timeout=60).read()
                Path(out).parent.mkdir(parents=True, exist_ok=True)
                Path(out).write_bytes(data)
                print(f"saved {out} ({len(data)//1024} KB) in {time.time()-t0:.0f}s")
                return
    sys.exit(f"TIMEOUT; prompt {pid} may still be running")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("kind", choices=["sfx", "music"])
    p.add_argument("prompt")
    p.add_argument("seconds", type=float)
    p.add_argument("out")
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--neg", default="")
    p.add_argument("--bpm", type=int, default=80)
    p.add_argument("--key", default="D major")
    p.add_argument("--timesig", default="4")
    p.add_argument("--lyrics", default="[instrumental]")
    a = p.parse_args()
    seed = a.seed if a.seed is not None else random.randrange(2**32)
    if a.kind == "sfx":
        g = sfx_graph(a.prompt, a.seconds, seed, a.neg)
    else:
        g = music_graph(a.prompt, a.seconds, seed, a.bpm, a.key, a.lyrics, a.timesig)
    print(f"seed {seed}")
    run(g, a.out)


if __name__ == "__main__":
    main()
