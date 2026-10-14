"""Teo's room above the laundromat. 640x360, figure scale.

Cramped, lit mostly by three monitors (blue) with warm fairy lights and pink
neon through the rainy window. Teo stands around x=420, feet ~y338.
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from svg import *
from props import *

defs = (
    lin_grad("twall", [(0, "#1b1630"), (0.6, "#262043"), (1, "#173a4a")]) +
    lin_grad("tfloor", [(0, "#3b4260"), (1, "#0d0b1a")]) +
    lin_grad("scr", [(0, "#2f8fc0"), (1, "#1a3a5a")])
)

FLOOR = 300
b = []
b.append(rect(0, 0, W, H, "url(#twall)"))
# faded wallpaper stripes
for x in range(0, W, 18):
    b.append(rect(x, 0, 8, FLOOR, "#332a57", opacity=0.25))
# sloped ceiling on the right
b.append(poly([(360, 0), (W, 0), (W, 46)], "#0d0b1a"))
b.append(line(360, 0, W, 46, "#463a70", 1.5))
# skirting
b.append(rect(0, FLOOR - 6, W, 6, "#1a1d2b"))

# ---- big monitor glow on the wall (behind everything)
b.append(glow_pool(280, 180, 170, 90, "#2f8fc0", 0.55))
b.append(glow_pool(280, 190, 90, 50, "#4fc0e8", 0.4))

# ---- door (left)
b.append(rect(14, 152, 78, FLOOR - 152, "#0d0b1a"))
b.append(rect(18, 156, 70, FLOOR - 156, "#332a57"))
b.append(rect(24, 162, 58, 50, "#262043")); b.append(rect(24, 220, 58, 70, "#262043"))
b.append(circle(80, 228, 3, "#c9b49a"))
b.append(rect(40, 172, 30, 26, "#fffaf0"))                          # note on door
b.append(text(55, 181, "BACK IN", "#3a2a22", 4.5)); b.append(text(55, 188, "5 POEMS", "#3a2a22", 4.5))
b.append(text(55, 195, "— T", "#b02d6f", 4))
b.append(rect(52, 169, 6, 4, "#ffd27a", opacity=0.9))
# cardigan on a hook
b.append(circle(30, 162, 2, "#c9b49a"))
b.append(path("M24,164 l12,0 l4,40 l-6,2 l-2,-20 l-2,22 l-8,0 z", fill="#7d6450"))
b.append(ellipse(37, 192, 3, 4, "#5a4334"))    # elbow patch
# light under the door
b.append(rect(18, FLOOR - 3, 70, 2, "#ffb347", opacity=0.6))

# ---- bookshelf of poetry
bx = 98
b.append(rect(bx, 60, 60, FLOOR - 60, "#3a2a22"))
b.append(rect(bx + 3, 63, 54, FLOOR - 66, "#1a1d2b"))
for i, sy in enumerate(range(96, FLOOR, 38)):
    b.append(books(bx + 4, sy, 52, 28, seed=40 + i,
                   colors=("#7a1f52", "#1f5260", "#c9b49a", "#463a70", "#4f8f45", "#b85c1c", "#2f8fc0", "#f6e7c8", "#5a4334")))
    b.append(rect(bx + 3, sy, 54, 3, "#5a4334"))
b.append(rect(bx, 58, 60, 4, "#5a4334"))
# things on top of the bookshelf: tiny lamp, a cactus, a framed poem
b.append(rect(bx + 6, 46, 10, 12, "#ffd27a", opacity=0.9)); b.append(rect(bx + 10, 52, 2, 6, "#3a2a22"))
b.append(glow_pool(bx + 11, 52, 20, 14, "#ffb347", 0.5))
b.append(rect(bx + 24, 40, 22, 18, "#c9b49a")); b.append(rect(bx + 26, 42, 18, 14, "#fff0b8"))
for j in range(4):
    b.append(rect(bx + 28, 45 + j * 3, 12 - (j % 2) * 4, 0.8, "#3a2a22", opacity=0.6))
b.append(potted_plant(bx + 52, 58, 0.5, pot="#e0802a", seed=5))
b.append(text(bx + 30, 132, "", "#000"))

# ---- pinboard of sticky notes above the desk
px0, py0, pw, ph = 170, 40, 96, 72
b.append(rect(px0 - 3, py0 - 3, pw + 6, ph + 6, "#5a4334"))
b.append(rect(px0, py0, pw, ph, "#a08870"))
b.append(rect(px0, py0, pw, ph, "#2f8fc0", opacity=0.18))
rnd = random.Random(14)
cols = ["#ffd27a", "#ff9cc6", "#9bd6c4", "#b8de7a", "#fff0b8", "#a8fff6"]
for r in range(4):
    for c in range(6):
        if rnd.random() < 0.85:
            x = px0 + 3 + c * 15.5 + rnd.uniform(-1.5, 1.5)
            y = py0 + 3 + r * 17 + rnd.uniform(-1.5, 1.5)
            b.append(sticky(round(x, 1), round(y, 1), rnd.choice(cols), rot=rnd.choice([-8, -4, 0, 3, 6]), s=11, lines=3))
            b.append(circle(round(x + 5.5, 1), round(y + 1, 1), 0.9, rnd.choice(["#e04a3a", "#2f8fc0", "#4f8f45"])))
# a polaroid of the cat and a red string between two notes
b.append(rect(248, 76, 14, 17, "#fffaf0")); b.append(rect(249.5, 77.5, 11, 10, "#525a7a"))
b.append(ellipse(255, 84, 4, 2.5, "#6f7896")); b.append(circle(258, 82, 1.8, "#6f7896"))
b.append(text(255, 92, "SIR", "#3a2a22", 3))
b.append(path("M178,52 Q210,70 252,80", stroke="#e04a3a", stroke_width=0.6))

# poetry-night poster above the door
b.append(rect(22, 60, 54, 58, "#f6e7c8"))
b.append(rect(25, 63, 48, 34, "#173a4a"))
b.append(circle(49, 76, 7, "#ffd27a"))
for i in range(5):
    b.append(bird(30 + i * 9, 88 - (i % 2) * 3, 0.7, "#f6e7c8"))
b.append(text(49, 105, "POETRY NIGHT", "#3a2a22", 4.5))
b.append(text(49, 112, "every thursday", "#7a1f52", 3.5, weight="normal"))
# ---- fairy lights along the wall top
b.append(string_lights(150, 30, 360, 22, 10, 14, colors=("#ffd27a", "#ffb347", "#ffd27a", "#ff9cc6"), r=1.3, seed=2))

# ---- shelf with mug collection above the window side
b.append(rect(290, 104, 76, 3, "#5a4334"))
for i, c in enumerate(["#f6e7c8", "#e04a3a", "#4f8f45", "#ffd27a", "#2f8fc0", "#ff9cc6"]):
    b.append(mug(293 + i * 12, 104, c, h=8, w=7))
b.append(text(328, 115, "", "#000"))

# ---- window with rain and neon outside
wx, wy, ww, wh = 420, 52, 150, 136
b.append(rect(wx - 6, wy - 6, ww + 12, wh + 12, "#3a2a22"))
b.append(night_view(wx, wy, ww, wh, seed=21, sky=("#0d0b1a", "#332a57", "#7a1f52")))
# outside: neon sign of the shop across the street, rail beam
b.append(rect(wx, wy + 8, ww, 10, "#1a1d2b"))
b.append(rect(wx, wy + 18, ww, 2, "#ffb347", opacity=0.5))
b.append(rect(wx + 70, wy + 92, 70, 18, "#2a0f24"))
b.append(neon(wx + 105, wy + 105, "NOODLE", "#ffb347", 10))
b.append(glow_pool(wx + 105, wy + 100, 50, 20, "#ffb347", 0.35))
b.append(neon(wx + 30, wy + 70, "♥", "#ff5fa2", 12))
b.append(rain_glass(wx, wy, ww, wh, seed=8, n=150))
b.append(rect(wx + ww / 2 - 2, wy, 4, wh, "#3a2a22"))
b.append(rect(wx, wy + wh / 2 - 2, ww, 4, "#3a2a22"))
b.append(rect(wx - 10, wy + wh + 4, ww + 20, 6, "#5a4334"))          # sill
b.append(rect(wx - 10, wy + wh + 4, ww + 20, 1.5, "#a08870"))
# curtain
b.append(path(f"M{wx + ww + 2},{wy - 10} q-14,40 -4,80 q8,40 -6,{wh - 50} l22,0 l0,-{wh + 30} z", fill="#7a1f52"))
b.append(path(f"M{wx + ww + 6},{wy - 10} q-8,60 0,{wh + 20}", stroke="#4a1538", stroke_width=1.5))
b.append(rect(wx - 14, wy - 12, ww + 36, 3, "#525a7a"))
# pink neon spill from the window
b.append(glow_pool(wx + 75, wy + 100, 110, 70, "#ff5fa2", 0.22))
# beloved plant on the sill — big trailing pothos, with a name tag
b.append(potted_plant(wx + 34, wy + wh + 4, 1.9, pot="#e0802a", leaf="#4f8f45", leaf2="#7fb85a", seed=11))
for i in range(3):
    b.append(path(f"M{wx + 26 + i * 6},{wy + wh + 2} q{-4 + i * 3},14 {-2 + i * 4},{26 + i * 6}", stroke="#2f6a35", stroke_width=0.9))
    for j in range(4):
        yy = wy + wh + 6 + j * 6 + i * 1.5
        b.append(ellipse(wx + 24 + i * 6 + (j % 2) * 2, yy, 2.4, 1.6, "#7fb85a" if (i + j) % 2 else "#4f8f45"))
b.append(rect(wx + 36, wy + wh - 4, 20, 6, "#fffaf0")); b.append(text(wx + 46, wy + wh + 0.5, "GERALD", "#3a2a22", 3.5))
b.append(mug(wx + 60, wy + wh + 4, "#9bd6c4", h=7))   # watering mug

# ---- desk
DTOP = 236
b.append(rect(150, DTOP, 260, 6, "#5a4334"))
b.append(rect(150, DTOP, 260, 1.5, "#a08870"))
b.append(rect(156, DTOP + 6, 6, FLOOR - DTOP - 6, "#3a2a22"))
b.append(rect(398, DTOP + 6, 6, FLOOR - DTOP - 6, "#3a2a22"))
b.append(rect(330, DTOP + 6, 68, 34, "#3a2a22"))      # drawers
b.append(rect(332, DTOP + 9, 64, 14, "#5a4334")); b.append(rect(332, DTOP + 25, 64, 13, "#5a4334"))
b.append(rect(360, DTOP + 15, 8, 1.5, "#c9b49a")); b.append(rect(360, DTOP + 30, 8, 1.5, "#c9b49a"))
b.append(rect(170, DTOP + 8, 30, 50, "#1a1d2b"))        # PC tower under desk
b.append(circle(185, DTOP + 16, 1.5, "#4ff0e6", filter="url(#glow)"))
for i in range(5):
    b.append(rect(174, DTOP + 24 + i * 4, 22, 1, "#2a2f45"))

# three monitors with rating UI
def monitor(x, y, w, h, kind):
    o = [rect(x - 3, y - 3, w + 6, h + 6, "#0d0b1a"), rect(x, y, w, h, "url(#scr)")]
    if kind == "compare":
        o.append(rect(x + 3, y + 3, w - 6, 5, "#1a3a5a"))
        o.append(text(x + w / 2, y + 7, "WHICH IS KINDER?", "#a8fff6", 4))
        for k, cx in enumerate((x + 4, x + w / 2 + 2)):
            o.append(rect(cx, y + 11, w / 2 - 6, h - 24, "#d2f0e2"))
            for j in range(6):
                o.append(rect(cx + 2, y + 14 + j * 3.6, w / 2 - 12 - (j * 5 + k * 3) % 8, 1.1, "#173a4a", opacity=0.7))
            o.append(rect(cx + 4, y + h - 11, w / 2 - 14, 6, "#4ff0e6" if k == 1 else "#3f8f8f"))
            o.append(text(cx + w / 4 - 3, y + h - 6.5, "AB"[k], "#0d0b1a", 5))
    elif kind == "sliders":
        o.append(text(x + w / 2, y + 8, "QUEUE 412/412", "#a8fff6", 4))
        for j, (lab, v) in enumerate([("HONEST", 0.8), ("KIND", 0.9), ("HELPFUL", 0.6), ("SAFE", 0.7)]):
            yy = y + 15 + j * 9
            o.append(text(x + 4, yy + 2, lab, "#d2f0e2", 3.5, anchor="start"))
            o.append(rect(x + 26, yy, w - 32, 2, "#1a3a5a"))
            o.append(rect(x + 26, yy, (w - 32) * v, 2, "#4ff0e6"))
            o.append(circle(x + 26 + (w - 32) * v, yy + 1, 1.8, "#fffaf0"))
        o.append(text(x + w / 2, y + h - 4, "★★★★☆", "#ffd27a", 5))
    else:
        o.append(text(x + w / 2, y + 8, "JUSTIFICATION", "#a8fff6", 4))
        o.append(rect(x + 3, y + 11, w - 6, h - 22, "#0f1f2b"))
        for j in range(8):
            o.append(rect(x + 5, y + 13 + j * 3.4, w - 12 - (j * 7) % 12, 1, "#9bd6c4", opacity=0.8))
        o.append(rect(x + 5, y + 13 + 8 * 3.4, 2, 2.5, "#fffaf0"))   # cursor
        o.append(text(x + w / 2, y + h - 3.5, "23:41  ·  CONTRACT ENDS 00:00", "#ff9cc6", 3))
    o.append(rect(x, y, w, 3, "#fffaf0", opacity=0.08))
    return "".join(o)

b.append(rect(274, 220, 12, 16, "#1a1d2b")); b.append(rect(262, 233, 36, 3, "#1a1d2b"))
b.append(monitor(236, 154, 88, 64, "compare"))
b.append(tr(monitor(172, 162, 58, 52, "sliders"), rot=0))
b.append(rect(198, 214, 6, 22, "#1a1d2b")); b.append(rect(190, 233, 22, 3, "#1a1d2b"))
b.append(monitor(330, 162, 58, 52, "notes"))
b.append(rect(356, 214, 6, 22, "#1a1d2b")); b.append(rect(348, 233, 22, 3, "#1a1d2b"))
# screen light on desk
b.append(glow_pool(280, DTOP, 130, 10, "#4fc0e8", 0.5))
# keyboard, mouse, headphones, notebook
b.append(rect(246, 230, 62, 6, "#2a2f45")); b.append(rect(248, 231, 58, 3, "#525a7a", opacity=0.6))
b.append(ellipse(320, 233, 4, 2.5, "#2a2f45"))
b.append(path("M206,232 q8,-14 16,0", stroke="#1a1d2b", stroke_width=2))
b.append(ellipse(206, 233, 3, 3, "#1a1d2b")); b.append(ellipse(222, 233, 3, 3, "#1a1d2b"))
b.append(tr(rect(160, 228, 24, 8, "#c9b49a") + rect(172, 228, 1, 8, "#7d6450"), rot=-6, cx=172, cy=232))
# MANY mugs
for mx_, c, st in [(166, "#e04a3a", False), (230, "#f6e7c8", True), (314, "#2f8fc0", False), (326, "#ffd27a", False),
                   (378, "#4f8f45", False), (388, "#ff9cc6", True), (296, "#fffaf0", False)]:
    b.append(mug(mx_, DTOP, c, steam=st))
b.append(mug(372, DTOP - 7, "#b85c1c", h=6))  # stacked
# small desk lamp (warm)
b.append(rect(400, DTOP - 8, 6, 8, "#f6e7c8")); b.append(ellipse(403, DTOP - 10, 1.2, 2, "#ffd27a", filter="url(#glow)"))
b.append(glow_pool(403, DTOP - 10, 18, 14, "#ffb347", 0.55))   # little candle
# cables snaking down from the desk
b.append(path("M240,242 q-6,40 20,52 q40,8 90,4", stroke="#0d0b1a", stroke_width=1.5))
b.append(path("M300,242 q4,30 -20,50", stroke="#0d0b1a", stroke_width=1.2))

# ---- office chair (at desk)
b.append(ellipse(274, 312, 26, 4, "#000", opacity=0.4))
b.append(line(274, 290, 274, 306, "#1a1d2b", 3))
for dx_ in (-20, -8, 8, 20):
    b.append(line(274, 306, 274 + dx_, 312, "#1a1d2b", 2))
    b.append(circle(274 + dx_, 312, 2, "#0d0b1a"))
b.append(rect(252, 284, 46, 8, "#1f5260"))
b.append(path("M254,284 l4,-40 q16,-6 32,0 l4,40 z", fill="#1f5260"))
b.append(path("M258,284 l3,-36 q13,-4 26,0", stroke="#3f8f8f", stroke_width=1, opacity=0.6))
b.append(path("M256,250 q-10,14 -2,30 l4,0 l-2,-30", fill="#c9b49a", opacity=0.9))   # blanket draped

# ---- bed corner (right)
b.append(rect(478, 236, 162, 60, "#1a1d2b"))                # frame
b.append(rect(478, 226, 162, 18, "#3f8f8f"))                # mattress/blanket top
b.append(path("M478,236 q40,-18 80,-4 q40,12 82,-6 l0,40 l-162,0 z", fill="#1f5260"))
b.append(path("M500,232 q30,-12 60,0", stroke="#63b3a8", stroke_width=1, opacity=0.6))
b.append(rect(478, 262, 162, 34, "#173a4a"))
b.append(rect(600, 206, 40, 22, "#d2f0e2"))                 # pillow
b.append(rect(600, 206, 40, 22, "#2f8fc0", opacity=0.25))
b.append(tr(rect(530, 222, 18, 4, "#7a1f52") + rect(538, 222, 1, 4, "#fff0b8"), rot=-8, cx=539, cy=224))   # book face-down
b.append(rect(472, 196, 6, 100, "#3a2a22"))                 # bed post
# radiator under the window
for i in range(9):
    b.append(rect(436 + i * 5, 206, 3.5, 28, "#525a7a"))
b.append(rect(434, 204, 46, 3, "#6f7896"))
b.append(rect(452, 216, 10, 6, "#ff9cc6", opacity=0.8))     # sock drying

# ---- floor
b.append(rect(0, FLOOR, W, H - FLOOR, "url(#tfloor)"))
for i in range(1, 8):
    yy = FLOOR + (H - FLOOR) * (i / 8) ** 1.4
    b.append(line(0, yy, W, yy, "#1a1d2b", 0.8, opacity=0.6))
b.append(ellipse(300, 334, 130, 18, "#463a70"))               # round rug
b.append(ellipse(300, 334, 118, 14, "none", stroke="#7d6fae", stroke_width=1, stroke_dasharray="3 2"))
b.append(ellipse(300, 330, 140, 22, "#4fc0e8", opacity=0.12, filter="url(#soft)"))
# floor clutter: books stack, laundry basket, a mug, cable to the window
for i, c in enumerate(["#7a1f52", "#c9b49a", "#1f5260", "#b85c1c"]):
    b.append(rect(118 + (i % 2) * 2, 340 - i * 5, 26 - i * 2, 5, c))
b.append(rect(540, 300, 44, 30, "#c9b49a")); b.append(rect(540, 300, 44, 3, "#a08870"))
for i in range(5):
    b.append(rect(543 + i * 8, 306, 4, 20, "#7d6450"))
b.append(path("M540,302 q10,-12 20,-2 q8,-10 18,0 q6,-4 6,2", fill="#ff9cc6"))
b.append(text(562, 322, "SUDS", "#3a2a22", 4))
b.append(mug(456, 344, "#f6e7c8"))
b.append(ellipse(460, 345, 5, 1, "#000", opacity=0.3))

# cool overall tint
b.append(rect(0, 0, W, H, "#0d0b1a", opacity=0.12))

out = svg(W, H, "".join(b), defs)
open(sys.argv[1], "w").write(out)
