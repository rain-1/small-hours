"""Render SVG art to dithered pixel-art PNGs.

  python3 tools/art/render.py <in.svg> <out.png> [--raw out_raw.png] [--nodither]

Pipeline: headless Chromium rasterises the SVG at its native size (transparent
background), then every opaque pixel is mapped onto the shared PALETTE with a
4x4 ordered (Bayer) dither. Alpha is thresholded so sprites keep hard edges.
"""
import argparse, subprocess, sys, tempfile, re
from pathlib import Path
import numpy as np
from PIL import Image

# Shared game palette: night indigos, teals, neon, lantern ambers, steam, skin.
PALETTE_HEX = """
0d0b1a 1b1630 262043 332a57 463a70 5d4f8c 7d6fae a99ad0
0f1f2b 173a4a 1f5260 2b6e78 3f8f8f 63b3a8 9bd6c4 d2f0e2
1a1d2b 2a2f45 3b4260 525a7a 6f7896 949bb3 bec2d1 e6e8ef
2a0f24 4a1538 7a1f52 b02d6f e0458e ff5fa2 ff9cc6 ffd3e6
1a3a5a 1f5f8a 2f8fc0 4fc0e8 4ff0e6 a8fff6
3a1a10 5e2a12 8a3f16 b85c1c e0802a ffb347 ffd27a fff0b8
f6e7c8 fffaf0 ffffff
4a0f12 7a1a1e b02a2a e04a3a ff7a5a
14301e 1f4a2a 2f6a35 4f8f45 7fb85a b8de7a
f3d1b3 e3b48f c98d6a a86a4a 8a5236 6b3f2a 4e2c1e
3a2a22 5a4334 7d6450 a08870 c9b49a
"""
PALETTE = np.array([[int(h[i:i + 2], 16) for i in (0, 2, 4)] for h in PALETTE_HEX.split()], dtype=np.float32)

BAYER4 = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]], dtype=np.float32) / 16 - 0.5


def rasterise(svg: Path, png: Path):
    txt = svg.read_text()
    w = int(float(re.search(r'width="([\d.]+)"', txt).group(1)))
    h = int(float(re.search(r'height="([\d.]+)"', txt).group(1)))
    with tempfile.TemporaryDirectory() as td:
        html = Path(td) / "page.html"
        html.write_text(f'<html><body style="margin:0;background:transparent">{txt}</body></html>')
        subprocess.run(["chromium", "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--default-background-color=00000000", f"--window-size={w},{h}",
                        "--force-device-scale-factor=1", f"--screenshot={png}", html.as_uri()],
                       check=True, capture_output=True)
    return w, h


def to_lab_ish(c):
    # cheap perceptual weighting
    return c * np.array([0.30, 0.59, 0.11], dtype=np.float32) ** 0.5


def dither(img: Image.Image, strength=34.0) -> Image.Image:
    a = np.asarray(img.convert("RGBA")).astype(np.float32)
    h, w = a.shape[:2]
    rgb = a[..., :3]
    th = np.tile(BAYER4, (h // 4 + 1, w // 4 + 1))[:h, :w][..., None]
    rgb = np.clip(rgb + th * strength, 0, 255)
    flat = to_lab_ish(rgb.reshape(-1, 3))
    pal = to_lab_ish(PALETTE)
    out = np.empty((flat.shape[0],), dtype=np.int32)
    for i in range(0, flat.shape[0], 65536):
        d = ((flat[i:i + 65536, None, :] - pal[None, :, :]) ** 2).sum(-1)
        out[i:i + 65536] = d.argmin(1)
    q = PALETTE[out].reshape(h, w, 3)
    alpha = np.where(a[..., 3] > 127, 255, 0)
    return Image.fromarray(np.dstack([q, alpha]).astype(np.uint8), "RGBA")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("svg")
    p.add_argument("out")
    p.add_argument("--raw")
    p.add_argument("--nodither", action="store_true")
    p.add_argument("--strength", type=float, default=34.0)
    a = p.parse_args()
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".tmp.png")
    rasterise(Path(a.svg), tmp)
    img = Image.open(tmp)
    if a.raw:
        img.save(a.raw)
    (img.convert("RGBA") if a.nodither else dither(img, a.strength)).save(out)
    tmp.unlink()
    print("wrote", out)


if __name__ == "__main__":
    main()
