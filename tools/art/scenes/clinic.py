"""Halfmoon Night Clinic — waiting room. 640x360, figure scale.

Cool mint fluorescent light; warm accents from the labour-room window and the
coffee machine. Nkechi ~x420, Dev ~x300, feet ~y332.
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from svg import *
from props import *

defs = (
    lin_grad("cwall", [(0, "#9bd6c4"), (0.7, "#63b3a8"), (1, "#3f8f8f")]) +
    lin_grad("cfloor", [(0, "#6f7896"), (1, "#2a2f45")]) +
    lin_grad("lddoor", [(0, "#d2f0e2"), (1, "#9bd6c4")])
)

FLOOR = 300
b = []
b.append(rect(0, 0, W, H, "url(#cwall)"))
# ceiling with fluorescent panels
b.append(rect(0, 0, W, 22, "#bec2d1"))
b.append(rect(0, 20, W, 3, "#949bb3"))
for x in (60, 250, 440):
    b.append(rect(x, 6, 110, 10, "#fffaf0"))
    b.append(rect(x, 6, 110, 10, "#d2f0e2", opacity=0.5))
    b.append(light_cone(x + 55, 16, 110, 260, 160, "#d2f0e2", 0.22))
for x in range(0, W, 40):
    b.append(rect(x, 0, 1, 20, "#949bb3", opacity=0.6))
# lower wainscot
b.append(rect(0, 214, W, FLOOR - 214, "#2b6e78"))
b.append(rect(0, 212, W, 4, "#1f5260"))
b.append(rect(0, 212, W, 1, "#d2f0e2", opacity=0.6))
for x in range(0, W, 32):
    b.append(rect(x, 216, 1, FLOOR - 216, "#1f5260", opacity=0.6))
b.append(rect(0, FLOOR - 5, W, 5, "#173a4a"))

# ---- reception desk (left)
b.append(rect(14, 120, 156, 90, "#d2f0e2", opacity=0.35))          # glass partition
b.append(rect(14, 120, 156, 2, "#fffaf0"))
b.append(rect(14, 120, 2, 120, "#949bb3")); b.append(rect(168, 120, 2, 120, "#949bb3"))
b.append(line(30, 130, 60, 200, "#fffaf0", 1, opacity=0.4)); b.append(line(40, 130, 66, 190, "#fffaf0", 0.6, opacity=0.4))
b.append(rect(66, 196, 52, 10, "#173a4a", opacity=0.5))             # speaking slot
# behind glass: back wall cabinet, files, a clock, a computer
b.append(rect(22, 134, 60, 50, "#bec2d1", opacity=0.7))
for i in range(3):
    b.append(rect(24, 136 + i * 16, 56, 14, "#949bb3", opacity=0.7)); b.append(rect(48, 142 + i * 16, 8, 2, "#525a7a"))
b.append(circle(140, 142, 9, "#fffaf0")); b.append(circle(140, 142, 9, "none", stroke="#173a4a", stroke_width=1.5))
b.append(line(140, 142, 140, 136, "#173a4a", 1.2)); b.append(line(140, 142, 145, 145, "#173a4a", 1))
b.append(rect(96, 180, 30, 22, "#2a2f45")); b.append(rect(98, 182, 26, 17, "#4fc0e8", opacity=0.8))
b.append(rect(108, 202, 6, 6, "#2a2f45"))
# desk body
b.append(rect(8, 236, 168, 74, "#e6e8ef"))
b.append(rect(8, 236, 168, 74, "#9bd6c4", opacity=0.35))
b.append(rect(4, 230, 176, 8, "#fffaf0"))
b.append(rect(4, 237, 176, 2, "#949bb3"))
b.append(rect(8, 250, 168, 4, "#2b6e78"))
b.append(text(92, 274, "RECEPTION", "#1f5260", 9))
b.append(text(92, 284, "night desk · ring for help", "#3f8f8f", 4.5, weight="normal"))
# desk-top items: bell, sign-in clipboard, pen on a chain, hand sanitiser, take-a-number
b.append(path("M30,230 q6,-10 12,0 z", fill="#ffd27a")); b.append(rect(34, 218, 4, 3, "#ffd27a")); b.append(rect(28, 229, 16, 2, "#b85c1c"))
b.append(tr(rect(56, 222, 18, 10, "#c9b49a") + rect(58, 224, 14, 8, "#fffaf0") + rect(62, 221, 6, 3, "#949bb3"), rot=-4, cx=65, cy=228))
b.append(path("M74,230 q8,8 14,-2", stroke="#949bb3", stroke_width=0.6))
b.append(rect(150, 218, 8, 12, "#a8fff6", opacity=0.8)); b.append(rect(152, 214, 4, 4, "#fffaf0"))
b.append(rect(122, 212, 20, 18, "#e04a3a")); b.append(rect(126, 216, 12, 6, "#fffaf0"))
b.append(text(132, 228, "TAKE #", "#fffaf0", 3.5))
# now-serving display
b.append(rect(44, 92, 90, 22, "#0f1f2b"))
b.append(text(70, 107, "NOW", "#a8fff6", 6))
b.append(text(112, 108, "47", "#e04a3a", 13, family="DejaVu Sans Mono", filter="url(#glow)"))
b.append(rect(86, 86, 2, 6, "#525a7a")); b.append(rect(92, 86, 2, 6, "#525a7a"))
b.append(potted_plant(162, 230, 0.6, pot="#fffaf0", leaf="#4f8f45", seed=31))

# ---- vending coffee machine
vx = 182
b.append(rect(vx, 172, 40, 128, "#7a1a1e"))
b.append(rect(vx, 172, 40, 4, "#b02a2a"))
b.append(rect(vx + 4, 182, 32, 40, "#3a1a10"))
b.append(rect(vx + 6, 184, 28, 36, "#ffb347", opacity=0.85))
b.append(path(f"M{vx + 12},{200} l16,0 l-2,12 l-12,0 z", fill="#fffaf0"))
b.append(path(f"M{vx + 28},{202} q4,0 4,3 q0,3 -4,3", stroke="#fffaf0", stroke_width=1.5))
b.append(path(f"M{vx + 16},{196} q-2,-4 1,-8 M{vx + 22},{196} q2,-4 -1,-8", stroke="#fffaf0", stroke_width=1))
b.append(text(vx + 20, 191, "HOT", "#7a1a1e", 4.5))
for i in range(4):
    b.append(rect(vx + 6, 228 + i * 7, 18, 5, "#262043")); b.append(rect(vx + 7, 229 + i * 7, 3, 3, "#ffd27a"))
b.append(rect(vx + 28, 228, 8, 12, "#2a2f45")); b.append(rect(vx + 31, 230, 2, 6, "#0d0b1a"))
b.append(rect(vx + 8, 262, 24, 22, "#0d0b1a")); b.append(rect(vx + 16, 274, 8, 10, "#f6e7c8"))
b.append(rect(vx + 4, 290, 32, 4, "#3a1a10"))
b.append(sticky(vx + 26, 246, "#ffd27a", rot=6, s=10, lines=3))            # "kicks: 2, then pray"
b.append(glow_pool(vx + 20, 205, 40, 40, "#ffb347", 0.45))

# ---- wall of baby photos
rnd = random.Random(8)
b.append(text(318, 52, "OUR HALFMOON BABIES", "#1f5260", 8))
b.append(text(318, 62, "2,014 and counting · love, Nkechi", "#2b6e78", 4.5, weight="normal"))
b.append(path("M232,40 Q318,30 404,40", stroke="#e0458e", stroke_width=0.8))
for i, c in enumerate(["#ff9cc6", "#ffd27a", "#4fc0e8", "#b8de7a", "#ff9cc6", "#ffd27a", "#4fc0e8"]):
    x = 236 + i * 26
    b.append(poly([(x, 38 - abs(3 - i) * 0.6), (x + 8, 38 - abs(3 - i) * 0.6), (x + 4, 46)], c))
skins = ["#f3d1b3", "#e3b48f", "#c98d6a", "#a86a4a", "#8a5236", "#6b3f2a"]
for r in range(5):
    for c in range(9):
        if rnd.random() < 0.88:
            fx = 236 + c * 19 + rnd.uniform(-2, 2)
            fy = 70 + r * 26 + rnd.uniform(-2, 2)
            fr = rnd.choice(["#fffaf0", "#fffaf0", "#ffd27a", "#ff9cc6", "#a8fff6"])
            ph = (rect(fx, fy, 15, 19, fr) + rect(fx + 1.5, fy + 1.5, 12, 12, rnd.choice(["#d2f0e2", "#ffd3e6", "#fff0b8", "#a8fff6"])) +
                  ellipse(fx + 7.5, fy + 9, 3.5, 3.2, rnd.choice(skins)) +
                  path(f"M{fx + 3},{fy + 13.5} q4.5,-4 9,0 z", fill=rnd.choice(["#ff9cc6", "#4fc0e8", "#fff0b8", "#b8de7a"])))
            if rnd.random() < 0.3:
                ph += ellipse(fx + 7.5, fy + 6, 3.5, 1.5, rnd.choice(["#ff9cc6", "#4fc0e8", "#ffd27a"]))  # knitted hat
            ph += rect(fx + 3, fy + 15.5, 9 - (c % 3), 1, "#3a2a22", opacity=0.5)
            b.append(tr(ph, rot=rnd.choice([-4, -2, 0, 2, 3]), cx=fx + 7, cy=fy + 9))
b.append(rect(390, 160, 15, 19, "#fffaf0", opacity=0.6))
b.append(text(397, 172, "?", "#e0458e", 9))           # empty frame waiting for tonight's baby
b.append(text(397, 186, "6:14?", "#1f5260", 3.5))

# ---- plastic chairs (joined row)
CY = 272
b.append(rect(236, CY + 6, 166, 3, "#525a7a"))
for i in range(5):
    cx_ = 244 + i * 32
    col = ["#e0802a", "#2f8fc0", "#e0802a", "#2f8fc0", "#e0802a"][i]
    b.append(path(f"M{cx_},{CY - 32} q13,-4 26,0 l-2,28 l-22,0 z", fill=col))
    b.append(rect(cx_ - 2, CY - 4, 30, 7, col))
    b.append(rect(cx_ - 2, CY - 4, 30, 1.5, "#fffaf0", opacity=0.4))
    b.append(rect(cx_ + 2, CY - 26, 22, 1, "#fffaf0", opacity=0.3))
for x in (240, 320, 398):
    b.append(rect(x, CY + 9, 3, FLOOR - CY - 4 + 14, "#525a7a"))
# a jacket left on a chair, a magazine, a paper cup, a phone charging, a teddy for the baby
b.append(path("M278,248 q10,-6 18,2 l2,28 l-6,10 l-8,-10 z", fill="#4a1538"))
b.append(tr(rect(318, 270, 16, 10, "#ffd27a") + rect(320, 272, 12, 3, "#e04a3a"), rot=-10, cx=326, cy=275))
b.append(text(326, 279, "", "#000"))
b.append(rect(348, 268, 5, 8, "#fffaf0")); b.append(rect(348, 268, 5, 1.5, "#b02a2a"))
b.append(ellipse(386, 268, 7, 7, "#a08870")); b.append(circle(386, 258, 5, "#a08870"))
b.append(circle(382, 254, 2, "#a08870")); b.append(circle(390, 254, 2, "#a08870"))
b.append(rect(383, 264, 6, 2, "#e04a3a"))
b.append(circle(384, 258, 0.7, "#3a2a22")); b.append(circle(388, 258, 0.7, "#3a2a22"))

# ---- potted palm
b.append(potted_plant(420, FLOOR + 2, 1.5, pot="#e6e8ef", leaf="#2f6a35", leaf2="#4f8f45", seed=4, kind="palm"))

# ---- LABOUR & DELIVERY door (double door, small glowing window)
dx0, dx1, dtop = 444, 538, 120
b.append(rect(dx0 - 6, dtop - 6, dx1 - dx0 + 12, FLOOR - dtop + 6, "#1f5260"))
b.append(rect(dx0, dtop, dx1 - dx0, FLOOR - dtop, "url(#lddoor)"))
b.append(rect((dx0 + dx1) / 2 - 1, dtop, 2, FLOOR - dtop, "#3f8f8f"))
for x_ in (dx0 + 12, (dx0 + dx1) / 2 + 12):
    b.append(rect(x_, dtop + 22, 22, 30, "#1f5260"))
    b.append(rect(x_ + 2, dtop + 24, 18, 26, "#ffd27a", filter="url(#glow)"))
    b.append(rect(x_ + 2, dtop + 38, 18, 12, "#ff9cc6", opacity=0.7))
    b.append(rect(x_ + 4, dtop + 26, 5, 22, "#fffaf0", opacity=0.6))
    b.append(rect(x_ + 12, dtop + 30, 6, 10, "#e0802a", opacity=0.5))   # a shape moving behind
b.append(glow_pool((dx0 + dx1) / 2, dtop + 38, 60, 30, "#ffb347", 0.55))
b.append(rect(dx0 + 4, dtop + 90, 38, 6, "#bec2d1")); b.append(rect((dx0 + dx1) / 2 + 6, dtop + 90, 38, 6, "#bec2d1"))   # push plates
b.append(rect(dx0, FLOOR - 26, dx1 - dx0, 22, "#bec2d1", opacity=0.6))  # kick plates
b.append(rect(dx0 - 4, dtop - 24, dx1 - dx0 + 8, 14, "#173a4a"))
b.append(text((dx0 + dx1) / 2, dtop - 13.5, "LABOUR &amp; DELIVERY", "#d2f0e2", 7.5))
b.append(circle(dx1 + 2, dtop - 32, 4, "#e04a3a", filter="url(#glow)"))
b.append(text(dx1 - 18, dtop - 30, "IN USE", "#b02a2a", 4.5))
b.append(rect(dx0 + 52, dtop + 60, 30, 16, "#fffaf0"))                    # handwritten sign
b.append(text(dx0 + 67, dtop + 67, "QUIET PLEASE", "#b02d6f", 3.6))
b.append(text(dx0 + 67, dtop + 73, "someone's arriving", "#3a2a22", 2.8, weight="normal"))
b.append(ellipse((dx0 + dx1) / 2, FLOOR + 3, 46, 3, "#ffb347", opacity=0.35, filter="url(#soft)"))   # light under door

# ---- posters
b.append(rect(548, 64, 40, 54, "#fffaf0"))
b.append(text(568, 76, "BREATHE", "#1f5260", 6))
b.append(circle(568, 92, 9, "none", stroke="#63b3a8", stroke_width=2))
b.append(text(568, 112, "in 4 · out 6", "#2b6e78", 4.5, weight="normal"))
b.append(rect(548, 128, 40, 50, "#e6e8ef"))
b.append(rect(550, 130, 36, 18, "#2f8fc0"))
b.append(text(568, 141, "AI TRIAGE", "#fffaf0", 5))
for i in range(3):
    b.append(rect(552, 152 + i * 5, 30 - i * 4, 1.4, "#525a7a"))
b.append(tr(rect(556, 158, 26, 12, "#ffd27a") + text(569, 166, "ask a human", "#3a2a22", 3.2), rot=-12, cx=569, cy=164))
b.append(rect(548, 188, 40, 20, "#ff9cc6"))
b.append(text(568, 197, "WASH", "#7a1f52", 5)); b.append(text(568, 204, "YOUR HANDS", "#7a1f52", 3.6))

# ---- exit (front glass door, rain outside)
ex = 596
b.append(rect(ex, 96, 46, FLOOR - 96, "#1f5260"))
b.append(night_view(ex + 4, 100, 40, FLOOR - 104, seed=12, sky=("#0d0b1a", "#262043", "#7a1f52")))
b.append(rain_glass(ex + 4, 100, 40, FLOOR - 104, seed=2))
b.append(rect(ex + 4, 196, 40, 4, "#1f5260"))
b.append(rect(ex + 6, 74, 32, 14, "#14301e"))
b.append(neon(ex + 22, 85, "EXIT", "#7fb85a", 9))

# ---- floor: speckled linoleum with reflections of the lights
b.append(rect(0, FLOOR, W, H - FLOOR, "url(#cfloor)"))
for i in range(260):
    b.append(rect(rnd.uniform(0, W), rnd.uniform(FLOOR, H), 1, 1, rnd.choice(["#9bd6c4", "#6f7896", "#1a1d2b"]), opacity=0.5))
for x in (115, 305, 495):
    b.append(ellipse(x, FLOOR + 24, 60, 4, "#d2f0e2", opacity=0.35, filter="url(#soft)"))
b.append(ellipse(202, FLOOR + 14, 20, 3, "#ffb347", opacity=0.3, filter="url(#soft)"))
b.append(rect(0, FLOOR + 30, W, 2, "#e0458e", opacity=0.25))          # wayfinding stripe
b.append(text(520, FLOOR + 44, "→ L&amp;D", "#e0458e", 6, opacity=0.6))
b.append(rect(180, FLOOR + 40, 44, 8, "#ffd27a", opacity=0.75))        # wet floor sign
b.append(poly([(186, FLOOR + 40), (202, FLOOR + 12), (218, FLOOR + 40)], "#ffd27a"))
b.append(text(202, FLOOR + 34, "!", "#3a2a22", 9))

out = svg(W, H, "".join(b), defs)
open(sys.argv[1], "w").write(out)
