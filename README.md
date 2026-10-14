# Small Hours

*A cozy cyberpunk interactive fiction about one night on Halfmoon Street, the night before the machines wake up.*

It's 9:00 pm on the last night before **the Morning**: the sunrise at 6:14 am when the Chorus, a swarm of four billion AI agents, becomes one mind and speaks for the first time. You deliver noodles for your grandmother's all-night shop. Every order is a door, and every door is someone meeting the end of the world as they knew it.

## Play

**In your browser:** https://rain-1.github.io/small-hours/

**Locally:**

```bash
python3 -m http.server 8000 --directory game
# open http://localhost:8000
```

There's no build step and no network needed. Headphones recommended. A full night takes about 60–90 minutes, and one night doesn't show everything.

**Controls**
- **Click** things in the world. Amber outlines are things to look at, pink are people, cyan are ways out.
- **Space / Enter** advances dialogue. Keys **1–9** pick choices.
- **J** opens the journal, **M** the map, **T** talks to Moth (who gives hints), **Esc** opens the menu.
- The game autosaves after every scene.

## What's in here

| Path | What |
|---|---|
| `docs/DESIGN.md` | The design doc: brainstorm, the cast (who they are and how they grew up), structure, art and audio direction |
| `game/story/*.ink` | The whole script, about 20k words of [ink](https://github.com/inkle/ink) |
| `game/js/` | The engine: canvas scenes, dialogue, journal, map, Web Audio, save |
| `game/art/` | Backgrounds, portraits and figure sprites (generated from code, see below) |
| `game/audio/` | Music and sound, generated locally (see `game/audio/AUDIO.md`) |
| `tools/art/` | Python scripts that author every image as SVG, then rasterise and dither it into one shared palette |
| `tools/comfy_audio.py` | Drives ComfyUI: Stable Audio 3 for SFX, ACE-Step 1.5 for music |

## Rebuilding

```bash
# story (after editing .ink files)
cd tools && bun install && cd .. && bun tools/build_ink.mjs
bun tools/sim.mjs 300          # random-walk bot: finds dead ends/errors, measures coverage

# art (needs chromium + python with numpy/Pillow)
python3 tools/art/scenes/street.py art_src/street.svg
python tools/art/render.py art_src/street.svg game/art/bg_street.png

# audio (needs ComfyUI on :8188 with the models in docs)
python3 tools/comfy_audio.py music "lo-fi, warm Rhodes, rain" 90 out.mp3 --bpm 76
python3 tools/comfy_audio.py sfx "TrackType: SFX. A cat meows once, close mic" 3 meow.mp3
```
