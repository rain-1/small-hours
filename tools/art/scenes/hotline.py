"""Humans Only Hotline — office above the pharmacy. 640x360, figure scale.

Warm lamplight, pink neon through the rainy window. Hollis ~x330, feet ~y336.
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from svg import *
from props import *

defs = (
    lin_grad("hwall", [(0, "#2a0f24"), (0.5, "#4a1538"), (1, "#5e2a12")]) +
    lin_grad("hfloor", [(0, "#7d6450"), (1, "#2a0f24")])
)

FLOOR = 300
b = []
b.append(rect(0, 0, W, H, "url(#hwall)"))
# wallpaper: little dotted diamonds
for y in range(30, 230, 14):
    for x in range((y // 14) % 2 * 9, W, 18):
        b.append(rect(x, y, 2, 2, "#7a1f52", opacity=0.45))
b.append(rect(0, 0, W, 22, "#1a1d2b"))
b.append(rect(0, 22, W, 3, "#3a2a22"))
# exposed pipe along the ceiling
b.append(rect(0, 30, W, 4, "#8a3f16")); b.append(rect(0, 30, W, 1, "#e0802a", opacity=0.6))
# wainscot
b.append(rect(0, 230, W, FLOOR - 230, "#3a1a10"))
b.append(rect(0, 228, W, 4, "#5e2a12")); b.append(rect(0, 228, W, 1, "#b85c1c"))
for x in range(0, W, 26):
    b.append(rect(x, 234, 22, FLOOR - 240, "#4a1538", opacity=0.35))

# ---- rainy window (left) with pink neon outside
wx, wy, ww, wh = 22, 58, 112, 130
b.append(rect(wx - 6, wy - 6, ww + 12, wh + 12, "#3a2a22"))
b.append(night_view(wx, wy, ww, wh, seed=33, sky=("#0d0b1a", "#332a57", "#7a1f52")))
# the hotline's own neon sign just outside, seen from behind
b.append(rect(wx, wy + wh - 30, ww, 22, "#2a0f24"))
b.append(neon(wx + ww / 2, wy + wh - 14, "ENILTOH", "#ff5fa2", 12, transform=f"translate({2 * (wx + ww / 2)},0) scale(-1,1)"))
b.append(glow_pool(wx + ww / 2, wy + wh - 18, 80, 30, "#ff5fa2", 0.55))
b.append(rain_glass(wx, wy, ww, wh, seed=19, n=160))
b.append(rect(wx + ww / 2 - 2, wy, 4, wh, "#3a2a22"))
b.append(rect(wx, wy + 46, ww, 3, "#3a2a22"))
b.append(rect(wx - 10, wy + wh + 4, ww + 20, 6, "#5e2a12")); b.append(rect(wx - 10, wy + wh + 4, ww + 20, 1.5, "#b85c1c"))
b.append(glow_pool(wx + ww / 2, wy + wh + 30, 100, 50, "#ff5fa2", 0.3))
# string of paper stars across the window
for i in range(6):
    sx_ = wx + 8 + i * 19
    b.append(line(sx_, wy - 6, sx_, wy + 10 + (i % 3) * 6, "#c9b49a", 0.5))
    b.append(circle(sx_, wy + 12 + (i % 3) * 6, 2.4, ["#ffd27a", "#fffaf0", "#ff9cc6"][i % 3]))
b.append(potted_plant(wx + 16, wy + wh + 4, 0.8, pot="#e0802a", seed=7))
b.append(mug(wx + 80, wy + wh + 4, "#4fc0e8", h=7))

# ---- floor lamp + sofa
b.append(line(160, FLOOR, 160, 160, "#3a2a22", 2)); b.append(ellipse(160, FLOOR, 10, 2, "#3a2a22"))
b.append(poly([(146, 160), (174, 160), (168, 140), (152, 140)], "#e0802a"))
b.append(poly([(146, 160), (174, 160), (168, 140), (152, 140)], "#ffd27a", opacity=0.4))
b.append(light_cone(160, 160, 28, 120, 140, "#ffd27a", 0.2))
b.append(glow_pool(160, 152, 40, 30, "#ffb347", 0.6))
SB = FLOOR + 4
b.append(rect(10, 228, 136, 44, "#1f5260"))                    # back
b.append(rect(10, 228, 136, 4, "#2b6e78"))
for i in range(3):
    b.append(rect(14 + i * 44, 234, 40, 34, "#2b6e78", opacity=0.5))
b.append(rect(4, 262, 148, 22, "#1f5260"))                     # seat
b.append(rect(4, 262, 148, 3, "#3f8f8f"))
b.append(rect(0, 244, 14, 42, "#173a4a")); b.append(rect(142, 244, 14, 42, "#173a4a"))   # arms
b.append(rect(10, 284, 6, SB - 284, "#3a2a22")); b.append(rect(140, 284, 6, SB - 284, "#3a2a22"))
b.append(path("M20,262 q6,-24 26,-20 l4,22 z", fill="#ffd27a"))                     # cushion
b.append(path("M96,262 q10,-22 30,-16 l-2,18 z", fill="#e0458e"))
b.append(path("M60,262 q20,-6 40,0 l6,24 l-50,0 z", fill="#b85c1c"))                 # crocheted blanket
for i in range(4):
    b.append(rect(62 + i * 11, 268, 8, 8, ["#ffd27a", "#e0458e", "#4fc0e8", "#7fb85a"][i], opacity=0.8))
b.append(rect(120, 256, 14, 6, "#fffaf0")); b.append(text(127, 261, "zzz", "#7a1f52", 3))  # a note: nap here

# ---- the hand-made switchboard light panel
SX0, SY0, SW, SH = 214, 52, 236, 96
b.append(rect(SX0 - 4, SY0 - 4, SW + 8, SH + 8, "#3a2a22"))
b.append(rect(SX0, SY0, SW, SH, "#5a4334"))
b.append(rect(SX0, SY0, SW, 14, "#3a2a22"))
b.append(text(SX0 + SW / 2, SY0 + 10, "SOMEONE SHOULD ALWAYS PICK UP", "#ffd27a", 7))
rnd = random.Random(4)
for r in range(4):
    for c in range(12):
        lx = SX0 + 14 + c * 18.5
        ly = SY0 + 26 + r * 17
        state = rnd.random()
        col = "#ffb347" if state < 0.55 else ("#e04a3a" if state < 0.7 else ("#7fb85a" if state < 0.85 else "#3a2a22"))
        b.append(circle(lx, ly, 3.4, "#1a1d2b"))
        b.append(circle(lx, ly, 2.4, col, filter="url(#glow)" if col != "#3a2a22" else None))
        if r == 0:
            b.append(rect(lx - 6, ly - 10, 12, 4, "#fffaf0")); b.append(text(lx, ly - 7, str(c + 1), "#3a2a22", 3.4))
        b.append(circle(lx, ly + 7, 1.2, "#c9b49a"))     # jack
# patch cables looping between jacks
for (a, c, col) in [(1, 5, "#e04a3a"), (3, 9, "#2f8fc0"), (6, 11, "#ffd27a"), (2, 4, "#7fb85a")]:
    x1, x2 = SX0 + 14 + a * 18.5, SX0 + 14 + c * 18.5
    b.append(path(f"M{x1},{SY0 + 33} Q{(x1 + x2) / 2},{SY0 + SH + 18} {x2},{SY0 + 50}", stroke=col, stroke_width=1.3))
b.append(glow_pool(SX0 + SW / 2, SY0 + SH / 2, 140, 50, "#ffb347", 0.3))
b.append(rect(SX0 + SW - 30, SY0 + SH - 10, 26, 6, "#c9b49a"))
b.append(text(SX0 + SW - 17, SY0 + SH - 5.5, "LINES FULL", "#7a1a1e", 3.3))
b.append(cable(SX0 + 10, SY0 + SH + 4, SX0 - 20, 240, 20, "#1a1d2b", 1.2))

# ---- three desks with old phones, headsets, lamps
def desk(x, seed, phone_col, lamp=True):
    rr = random.Random(seed)
    o = []
    o.append(rect(x, 250, 92, 5, "#8a3f16")); o.append(rect(x, 250, 92, 1.5, "#e0802a"))
    o.append(rect(x + 4, 255, 4, FLOOR - 255, "#3a1a10")); o.append(rect(x + 84, 255, 4, FLOOR - 255, "#3a1a10"))
    o.append(rect(x + 56, 255, 28, 26, "#5e2a12")); o.append(rect(x + 66, 262, 8, 1.5, "#c9b49a"))
    # phone (old desk phone with coiled cord)
    o.append(path(f"M{x + 24},{250} l2,-10 l22,0 l2,10 z", fill=phone_col))
    o.append(rect(x + 22, 236, 30, 5, phone_col)); o.append(ellipse(x + 23, 237, 4, 3, phone_col)); o.append(ellipse(x + 51, 237, 4, 3, phone_col))
    o.append(rect(x + 30, 243, 14, 5, "#fffaf0", opacity=0.6))
    for i in range(3):
        o.append(rect(x + 31 + i * 4.5, 244, 3, 1.4, "#3a2a22"))
    o.append(path(f"M{x + 22},{240} q-4,6 -2,10 q-3,2 -1,4 q-3,2 -1,4", stroke=phone_col, stroke_width=0.8))
    # headset hung on the lamp / mug
    if lamp:
        o.append(rect(x + 70, 246, 14, 4, "#14301e"))
        o.append(line(x + 77, 246, x + 77, 232, "#c9b49a", 1.2))
        o.append(path(f"M{x + 66},{232} q11,-10 22,0 z", fill="#2f6a35"))
        o.append(ellipse(x + 77, 232, 10, 2, "#ffd27a", filter="url(#glow)"))
        o.append(light_cone(x + 77, 232, 18, 70, 20, "#ffd27a", 0.35))
        o.append(glow_pool(x + 77, 248, 40, 8, "#ffb347", 0.6))
        o.append(glow_pool(x + 77, 226, 30, 18, "#ffb347", 0.35))
    o.append(path(f"M{x + 6},{238} q8,-12 16,0", stroke="#1a1d2b", stroke_width=1.8))
    o.append(rect(x + 4, 237, 4, 6, "#1a1d2b")); o.append(rect(x + 20, 237, 4, 6, "#1a1d2b"))
    o.append(line(x + 6, 243, x + 4, 249, "#1a1d2b", 0.8))
    # notepad, pen, mug, thermos with stickers, tissues
    o.append(tr(rect(x + 54, 244, 14, 6, "#fff0b8"), rot=rr.choice([-6, 4]), cx=x + 61, cy=247))
    o.append(mug(x + 10, 250, rr.choice(["#e04a3a", "#4fc0e8", "#ffd27a"])))
    return "".join(o)

b.append(desk(178, 1, "#c9b49a"))
b.append(desk(290, 2, "#e04a3a"))
b.append(desk(402, 3, "#3f8f8f"))
# Hollis's sticker-covered thermos and a box of tissues on the middle desk
b.append(rect(350, 232, 7, 18, "#bec2d1"))
for i, c in enumerate(["#ff5fa2", "#ffd27a", "#4ff0e6"]):
    b.append(circle(352 + (i % 2) * 3, 236 + i * 4, 1.8, c))
b.append(rect(194, 244, 14, 6, "#fffaf0")); b.append(path("M199,244 q2,-4 4,0", fill="#fffaf0"))
# chairs pushed in at the desks
for x in (210, 322, 434):
    b.append(rect(x - 12, 262, 24, 4, "#1a1d2b"))
    b.append(rect(x - 10, 266, 3, FLOOR - 266, "#1a1d2b")); b.append(rect(x + 7, 266, 3, FLOOR - 266, "#1a1d2b"))
    b.append(rect(x - 11, 238, 22, 6, "#262043"))
b.append(path("M434,238 q-14,6 -10,24 l6,0 z", fill="#e0458e"))   # scarf over a chair

# ---- wall of thank-you sticky notes
rnd = random.Random(11)
cols = ["#ffd27a", "#ff9cc6", "#9bd6c4", "#b8de7a", "#fff0b8", "#a8fff6", "#ffd3e6"]
for i in range(70):
    x = 478 + rnd.uniform(0, 100)
    y = 48 + rnd.uniform(0, 160)
    b.append(sticky(round(x, 1), round(y, 1), rnd.choice(cols), rot=rnd.choice([-10, -5, 0, 4, 8]), s=11, lines=3))
for (x, y) in [(488, 70), (540, 120), (520, 180), (566, 60)]:
    b.append(text(x + 5, y + 7, "♥", "#e04a3a", 6))
b.append(rect(484, 36, 92, 10, "#fffaf0"))
b.append(text(530, 43.5, "THANK YOU WALL", "#7a1f52", 6))

# ---- kettle cabinet
kx = 486
b.append(rect(kx, 252, 92, FLOOR - 252, "#5e2a12"))
b.append(rect(kx, 248, 92, 5, "#a08870")); b.append(rect(kx, 248, 92, 1.5, "#c9b49a"))
b.append(rect(kx + 4, 258, 40, 38, "#4a1538", opacity=0.5)); b.append(rect(kx + 48, 258, 40, 38, "#4a1538", opacity=0.5))
b.append(circle(kx + 40, 276, 1.5, "#c9b49a")); b.append(circle(kx + 52, 276, 1.5, "#c9b49a"))
# kettle with steam
b.append(path(f"M{kx + 10},{248} l2,-16 q8,-4 16,0 l2,16 z", fill="#bec2d1"))
b.append(path(f"M{kx + 12},{234} q8,-10 16,0", stroke="#3a2a22", stroke_width=1.5))
b.append(path(f"M{kx + 28},{240} l8,-6", stroke="#bec2d1", stroke_width=2.5))
b.append(rect(kx + 13, 236, 4, 10, "#fffaf0", opacity=0.5))
b.append(circle(kx + 14, 245, 1, "#e04a3a", filter="url(#glow)"))
b.append(ellipse(kx + 40, 214, 10, 18, "#f6e7c8", opacity=0.3, filter="url(#soft)"))
b.append(path(f"M{kx + 36},{232} q-4,-8 2,-14 q4,-6 -1,-14", stroke="#f6e7c8", stroke_width=1.2, opacity=0.5))
# mug tree + mugs + tea tins + biscuit tin
b.append(rect(kx + 50, 222, 2, 26, "#3a2a22"))
for i, (dx, dy, c) in enumerate([(-6, 228, "#ffd27a"), (4, 232, "#4fc0e8"), (-6, 238, "#e04a3a"), (4, 242, "#7fb85a")]):
    b.append(mug(kx + 51 + dx, dy + 6, c, h=6, w=5))
for i, c in enumerate(["#b02a2a", "#2f6a35", "#1f5f8a"]):
    b.append(rect(kx + 62 + i * 8, 236, 7, 12, c)); b.append(rect(kx + 62 + i * 8, 236, 7, 2, "#ffd27a"))
b.append(ellipse(kx + 70, 302, 0.1, 0.1, "#000"))
b.append(rect(kx + 64, 232, 22, 4, "#fff0b8", opacity=0.0))

# ---- exit door (right)
ex = 590
b.append(rect(ex, 104, 46, FLOOR - 104, "#3a1a10"))
b.append(rect(ex + 4, 108, 38, FLOOR - 108, "#5e2a12"))
b.append(rect(ex + 8, 114, 30, 60, "#4a1538", opacity=0.6)); b.append(rect(ex + 8, 184, 30, 100, "#4a1538", opacity=0.6))
b.append(circle(ex + 10, 210, 2.5, "#ffd27a"))
b.append(rect(ex + 12, 124, 22, 28, "#fffaf0"))
b.append(text(ex + 23, 133, "BREAK", "#3a2a22", 4)); b.append(text(ex + 23, 140, "ROOM", "#3a2a22", 4))
b.append(text(ex + 23, 148, "→ stairs", "#7a1f52", 3.2, weight="normal"))
b.append(circle(ex + 8, 98, 3, "#c9b49a"))
b.append(path(f"M{ex + 4},{100} l8,0 l3,30 l-14,0 z", fill="#2b6e78"))   # raincoat on a hook

# ---- floor: worn boards with a rug
b.append(floor_planks(0, FLOOR, W, H - FLOOR, "#5a4334", "#3a1a10", 7))
b.append(rect(0, FLOOR, W, H - FLOOR, "url(#hfloor)", opacity=0.6))
b.append(path("M200,316 L470,316 L500,356 L170,356 Z", fill="#7a1f52"))
b.append(path("M206,320 L464,320 L490,352 L180,352 Z", fill="none", stroke="#ffb347", stroke_width=1, opacity=0.6))
b.append(path("M240,330 L430,330 L444,344 L226,344 Z", fill="#b02d6f", opacity=0.6))
for x in (255, 367, 479):
    b.append(ellipse(x, FLOOR + 8, 44, 4, "#ffb347", opacity=0.35, filter="url(#soft)"))
b.append(ellipse(78, FLOOR + 14, 70, 6, "#ff5fa2", opacity=0.25, filter="url(#soft)"))
# a phone cord trailing on the floor and a dropped sticky
b.append(path("M300,300 q20,14 60,8 q30,-4 50,6", stroke="#1a1d2b", stroke_width=1))
b.append(tr(rect(530, 330, 8, 8, "#ffd27a"), rot=20, cx=534, cy=334))
b.append(rect(0, 0, W, H, "#2a0f24", opacity=0.06))

out = svg(W, H, "".join(b), defs)
open(sys.argv[1], "w").write(out)
