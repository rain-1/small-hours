"""Halfmoon Noodle — interior. 640x360, figure scale (~110px adult).

Lu stands behind the counter at about x=300 (feet ~y318, hidden by counter).
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from svg import *
from props import *

defs = (
    lin_grad("wall", [(0, "#5e2a12"), (0.5, "#8a3f16"), (1, "#5e2a12")]) +
    lin_grad("ceil", [(0, "#1a1d2b"), (1, "#3a1a10")]) +
    lin_grad("floor", [(0, "#7d6450"), (1, "#3a1a10")]) +
    lin_grad("counter", [(0, "#c9b49a"), (1, "#7d6450")]) +
    lin_grad("steamv", [(0, "#f6e7c8", 0), (0.4, "#f6e7c8", 0.55), (1, "#f6e7c8", 0)]) +
    lin_grad("crt", [(0, "#1f5f8a"), (1, "#0f1f2b")]) +
    lin_grad("doorout", [(0, "#0d0b1a"), (0.6, "#332a57"), (1, "#7a1f52")])
)

COUNTER_TOP = 272
FLOOR = 326

b = []
# ---- back wall
b.append(rect(0, 0, W, H, "url(#wall)"))
# vertical wood battens on upper wall
for x in range(0, W, 46):
    b.append(rect(x, 24, 2, 180, "#3a1a10", opacity=0.35))
# cream tile splashback behind the kitchen line
b.append(tiles(130, 176, 470, 64, 8, "#f6e7c8", "#fff0b8", "#c9b49a", seed=4))
b.append(rect(130, 176, 470, 64, "#b85c1c", opacity=0.25))
b.append(rect(130, 174, 470, 3, "#3a1a10"))
# ceiling
b.append(rect(0, 0, W, 26, "url(#ceil)"))
for x in range(-10, W, 64):
    b.append(rect(x, 18, 50, 8, "#3a2a22"))
b.append(rect(0, 25, W, 2, "#1a1d2b"))

# ---- front-of-house left wall & front door (rain beyond)
b.append(rect(0, 26, 130, FLOOR - 26, "#4a1538"))
b.append(rect(0, 26, 130, FLOOR - 26, "#5e2a12", opacity=0.55))
b.append(rect(128, 26, 3, FLOOR - 26, "#3a1a10"))
# door frame
b.append(rect(22, 120, 86, FLOOR - 120, "#3a1a10"))
b.append(night_view(28, 126, 74, 150, seed=7, sky=("#0d0b1a", "#332a57", "#b02d6f")))
b.append(rect(28, 276, 74, FLOOR - 276, "#2a2f45"))             # wet street outside
b.append(rect(28, 276, 74, 2, "#525a7a"))
b.append(ellipse(56, 300, 22, 3, "#ff5fa2", opacity=0.35))       # neon puddle outside
b.append(ellipse(80, 312, 14, 2, "#4ff0e6", opacity=0.3))
b.append(rain_glass(28, 126, 74, 190, seed=3))
b.append(rect(63, 126, 4, FLOOR - 126, "#3a1a10"))                # mullion
b.append(rect(28, 220, 74, 5, "#3a1a10"))                          # push bar rail
b.append(rect(70, 214, 10, 3, "#c9b49a"))
# reversed lettering on the glass
b.append(text(46, 160, "ELDOON", "#ffb347", 7, opacity=0.7, transform="scale(-1,1) translate(-92,0)"))
b.append(path("M37,148 a5,5 0 1,0 5,-5 a3.8,3.8 0 1,1 -5,5", fill="#ffb347", opacity=0.6))
b.append(text(84, 240, "OPEN", "#ff5fa2", 6, filter="url(#glow)", opacity=0.9))
# door bell
b.append(line(65, 106, 65, 116, "#3a2a22", 1))
b.append(path("M60,122 q5,-10 10,0 z", fill="#ffd27a"))
b.append(circle(65, 123, 1.3, "#b85c1c"))
b.append(glow_pool(65, 200, 60, 90, "#b02d6f", 0.25))
# umbrella stand with a dripping umbrella
b.append(rect(108, 300, 14, 26, "#1f5260"))
b.append(rect(108, 300, 14, 2, "#3f8f8f"))
b.append(line(112, 300, 108, 262, "#3a2a22", 1.5))
b.append(path("M108,262 q-5,8 -4,22 l8,0 q-1,-14 -4,-22 z", fill="#e04a3a"))
b.append(path("M108,262 q-2,-6 3,-6", stroke="#3a2a22", stroke_width=1.5))
b.append(ellipse(115, 327, 9, 1.5, "#4fc0e8", opacity=0.4))
# small posters on the left wall
b.append(rect(8, 44, 40, 54, "#f6e7c8"))
b.append(rect(10, 46, 36, 30, "#7a1f52"))
b.append(circle(28, 61, 9, "#ffb347"))
b.append(text(28, 85, "LAST SLOW", "#3a2a22", 4.5))
b.append(text(28, 91, "NIGHT 87.9", "#b02d6f", 4.5))
b.append(rect(58, 50, 50, 40, "#fff0b8"))     # hand-written menu specials
b.append(text(83, 60, "TONIGHT", "#b02a2a", 6))
for i in range(4):
    b.append(rect(62, 65 + i * 6, 32 + (i * 7) % 10, 1.5, "#3a2a22", opacity=0.7))
b.append(rect(80, 46, 6, 5, "#ff9cc6", opacity=0.9))  # tape

# ---- back wall details
# high shelf with old CRT TV (countdown)
b.append(rect(132, 118, 112, 5, "#3a2a22"))
b.append(rect(132, 123, 112, 2, "#000", opacity=0.3))
b.append(path("M138,123 l6,10 l2,0 l-4,-10 z", fill="#3a2a22"))
b.append(path("M236,123 l-6,10 l-2,0 l4,-10 z", fill="#3a2a22"))
b.append(glow_pool(172, 96, 60, 40, "#4fc0e8", 0.35))
b.append(rect(140, 70, 66, 48, "#a08870"))            # TV body
b.append(rect(140, 70, 66, 3, "#c9b49a"))
b.append(rect(144, 75, 46, 38, "#1a1d2b"))
b.append(rect(146, 77, 42, 34, "url(#crt)"))
b.append(text(167, 86, "THE MORNING", "#a8fff6", 4.5))
b.append(text(167, 100, "09:14", "#4ff0e6", 12, family="DejaVu Sans Mono", filter="url(#glow)"))
b.append(text(167, 107, "· · ·", "#a8fff6", 4))
for yy in range(78, 111, 2):
    b.append(rect(146, yy, 42, 0.6, "#000", opacity=0.25))   # scanlines
b.append(rect(146, 77, 14, 6, "#fffaf0", opacity=0.12))
b.append(circle(198, 82, 2.5, "#5a4334")); b.append(circle(198, 90, 2.5, "#5a4334"))
for i in range(4):
    b.append(rect(194, 98 + i * 3, 8, 1, "#5a4334"))
b.append(line(160, 70, 150, 54, "#3a2a22", 1)); b.append(line(186, 70, 198, 52, "#3a2a22", 1))  # rabbit ears
b.append(circle(150, 54, 1.2, "#c9b49a")); b.append(circle(198, 52, 1.2, "#c9b49a"))
# bowls stacked and jars on the same shelf
for i in range(4):
    b.append(ellipse(222, 116 - i * 4, 11, 2.5, ["#f6e7c8", "#2f8fc0", "#f6e7c8", "#e04a3a"][i]))
    b.append(rect(212, 113 - i * 4, 20, 3, ["#f6e7c8", "#2f8fc0", "#f6e7c8", "#e04a3a"][i]))
b.append(rect(234, 104, 8, 14, "#9bd6c4", opacity=0.7)); b.append(rect(234, 102, 8, 3, "#e04a3a"))

# stopped wall clock (hands at 4:47, glass cracked)
cx, cy = 262, 60
b.append(circle(cx, cy + 1, 17, "#000", opacity=0.3))
b.append(circle(cx, cy, 17, "#3a2a22"))
b.append(circle(cx, cy, 14, "#fff0b8"))
for i in range(12):
    a = math.radians(i * 30)
    b.append(line(cx + math.sin(a) * 11, cy - math.cos(a) * 11, cx + math.sin(a) * 13, cy - math.cos(a) * 13, "#3a2a22", 1.2 if i % 3 == 0 else 0.7))
ah, am = math.radians((4 + 47 / 60) * 30), math.radians(47 * 6)
b.append(line(cx, cy, cx + math.sin(ah) * 7, cy - math.cos(ah) * 7, "#3a2a22", 1.8))
b.append(line(cx, cy, cx + math.sin(am) * 11, cy - math.cos(am) * 11, "#3a2a22", 1.1))
b.append(circle(cx, cy, 1.4, "#b02a2a"))
b.append(path(f"M{cx + 4},{cy - 13} l-3,6 l4,3 l-5,6", stroke="#bec2d1", stroke_width=0.6, opacity=0.9))  # crack
b.append(line(cx, cy - 17, cx, cy - 24, "#3a2a22", 1))

# hanging wooden menu plaques
menu = ["醤油", "味噌", "粥", "餃子", "茶"]
for i, m in enumerate(menu):
    mx = 292 + i * 17
    b.append(rect(mx, 46, 14, 42, "#c9b49a"))
    b.append(rect(mx, 46, 14, 2, "#fff0b8", opacity=0.5))
    b.append(rect(mx + 13, 46, 1, 42, "#7d6450"))
    b.append(text(mx + 7, 58, m[0], "#3a2a22", 8, family="IPAexGothic"))
    if len(m) > 1:
        b.append(text(mx + 7, 68, m[1], "#3a2a22", 8, family="IPAexGothic"))
    b.append(text(mx + 7, 83, str(6 + i * 2), "#b02a2a", 6))
    b.append(line(mx + 3, 46, mx + 3, 40, "#3a2a22", 0.6)); b.append(line(mx + 11, 46, mx + 11, 40, "#3a2a22", 0.6))
b.append(rect(290, 39, 88, 2, "#3a2a22"))

# photo of a young woman (Lu's daughter) on a little altar shelf
px, py = 300, 104
b.append(rect(px - 2, py - 2, 30, 38, "#3a2a22"))
b.append(rect(px, py, 26, 34, "#f6e7c8"))
b.append(rect(px + 2, py + 2, 22, 30, "#d2f0e2"))
b.append(rect(px + 2, py + 18, 22, 14, "#9bd6c4"))    # sea behind her
b.append(ellipse(px + 13, py + 13, 5, 6, "#e3b48f"))   # face
b.append(path(f"M{px + 7},{py + 14} q0,-10 6,-10 q7,0 7,10 l1,8 l-3,-2 l-1,-6 q-3,-5 -9,0 l-1,6 l-2,2 z", fill="#3a2a22"))  # hair
b.append(path(f"M{px + 5},{py + 32} q2,-10 8,-10 q6,0 8,10 z", fill="#e0458e"))  # pink jacket
b.append(path(f"M{px + 11},{py + 15} q2,1.5 4,0", stroke="#8a5236", stroke_width=0.7))  # smile
b.append(rect(px - 4, py + 37, 38, 3, "#3a2a22"))
b.append(circle(px + 3, py + 34, 2.6, "#e0802a")); b.append(circle(px + 3, py + 33, 1, "#ffd27a"))  # orange
b.append(line(px + 31, py + 37, px + 31, py + 24, "#7d6450", 0.8))                    # incense stick
b.append(path(f"M{px + 31},{py + 24} q-2,-4 1,-8 q2,-4 0,-8", stroke="#f6e7c8", stroke_width=0.7, opacity=0.5))
b.append(circle(px + 31, py + 24, 0.8, "#ff7a5a"))
# small radio on its own bracket
rx, ry = 340, 128
b.append(rect(rx - 4, ry + 14, 42, 3, "#3a2a22"))
b.append(rect(rx, ry, 34, 14, "#b02a2a"))
b.append(rect(rx, ry, 34, 2, "#ff7a5a"))
b.append(rect(rx + 2, ry + 3, 13, 9, "#3a2a22"))
for i in range(4):
    b.append(rect(rx + 3, ry + 4 + i * 2, 11, 0.8, "#7d6450"))
b.append(rect(rx + 18, ry + 4, 13, 4, "#fff0b8")); b.append(rect(rx + 24, ry + 4, 1, 4, "#e04a3a"))
b.append(circle(rx + 21, ry + 10.5, 1.5, "#c9b49a")); b.append(circle(rx + 28, ry + 10.5, 1.5, "#c9b49a"))
b.append(line(rx + 30, ry, rx + 40, ry - 16, "#bec2d1", 0.8))
b.append(text(rx + 44, ry - 2, "♪", "#ffd27a", 6, opacity=0.8))

# ticket rail at the pass, paper tickets clipped on
b.append(rect(196, 148, 130, 3, "#bec2d1"))
b.append(rect(196, 150, 130, 1, "#525a7a"))
b.append(line(200, 148, 200, 26, "#525a7a", 1)); b.append(line(322, 148, 322, 26, "#525a7a", 1))
for i, (tx, rot) in enumerate([(204, -3), (220, 2), (236, -1), (256, 4), (276, -2)]):
    tk = rect(tx, 151, 12, 18, "#fffaf0") + rect(tx, 151, 12, 2, "#c9b49a")
    for j in range(4):
        tk += rect(tx + 2, 155 + j * 3, 8 - (j * 3 + i) % 4, 0.9, "#3a2a22", opacity=0.7)
    if i == 0:
        tk += text(tx + 6, 167, "#12", "#b02a2a", 3.5)
    b.append(tr(tk, rot=rot, cx=tx + 6, cy=151))
b.append(rect(298, 151, 5, 3, "#525a7a"))  # empty clip

# drying noodles on a pole
b.append(rect(452, 36, 66, 3, "#a08870"))
b.append(line(456, 36, 456, 26, "#3a2a22", 1)); b.append(line(514, 36, 514, 26, "#3a2a22", 1))
import random
rnd = random.Random(9)
for i in range(30):
    nx = 455 + i * 2.1
    L = rnd.uniform(46, 64)
    b.append(path(f"M{nx},{39} q{rnd.uniform(-1.5, 1.5)},{L / 2} {rnd.uniform(-1, 1)},{L}", stroke="#fff0b8" if i % 3 else "#f6e7c8", stroke_width=1))
b.append(glow_pool(485, 70, 40, 30, "#ffd27a", 0.25))

# back-room door with a curtain (noren)
dx = 528
b.append(rect(dx, 104, 64, 170, "#3a1a10"))
b.append(rect(dx + 4, 108, 56, 166, "#1a1d2b"))
b.append(rect(dx + 4, 108, 56, 166, "#5e2a12", opacity=0.35))
b.append(rect(dx + 2, 108, 60, 3, "#a08870"))
for i in range(3):
    b.append(rect(dx + 4 + i * 19, 111, 18, 56, "#173a4a"))
    b.append(rect(dx + 4 + i * 19, 164, 18, 3, "#0f1f2b"))
b.append(circle(dx + 32, 132, 11, "#f6e7c8", opacity=0.9))
b.append(circle(dx + 36, 129, 9.5, "#173a4a"))              # half-moon crest on the noren
b.append(rect(dx + 22, 108, 0.8, 59, "#0f1f2b")); b.append(rect(dx + 41, 108, 0.8, 59, "#0f1f2b"))
b.append(rect(dx + 26, 230, 10, 2, "#ffb347", opacity=0.6))  # warm sliver under curtain
b.append(glow_pool(dx + 32, 220, 26, 40, "#ffb347", 0.25))

# right wall bits: calendar (unturned), hanging ladles
b.append(rect(600, 60, 30, 40, "#fffaf0"))
b.append(rect(600, 60, 30, 9, "#b02a2a"))
b.append(text(615, 67, "OCT", "#fffaf0", 5))
for r in range(4):
    for c in range(5):
        b.append(rect(603 + c * 5.4, 72 + r * 6, 3.5, 4, "#c9b49a" if (r * 5 + c) != 13 else "#e04a3a"))
b.append(rect(598, 130, 36, 2, "#525a7a"))
for i in range(4):
    lx = 602 + i * 9
    b.append(line(lx, 131, lx, 156 + i % 2 * 4, "#bec2d1", 1))
    b.append(ellipse(lx, 158 + i % 2 * 4, 3, 2, "#bec2d1"))

# ---- kitchen line behind the counter (stove + big broth pot)
b.append(rect(130, 236, 470, 40, "#4a1538"))
b.append(rect(130, 236, 470, 40, "#5e2a12", opacity=0.7))
b.append(rect(130, 236, 470, 3, "#bec2d1"))
b.append(rect(130, 239, 470, 2, "#000", opacity=0.35))
for x in range(136, 596, 46):
    b.append(rect(x, 244, 42, 28, "#3a1a10", opacity=0.6))
    b.append(rect(x + 1, 245, 40, 1, "#b85c1c", opacity=0.5))
    b.append(rect(x + 19, 252, 4, 1.5, "#c9b49a"))
# steam rising from the pot
b.append(ellipse(420, 150, 34, 70, "url(#steamv)", opacity=0.7, filter="url(#haze)"))
b.append(ellipse(408, 120, 18, 40, "#f6e7c8", opacity=0.22, filter="url(#soft)"))
b.append(ellipse(432, 170, 16, 30, "#fffaf0", opacity=0.25, filter="url(#soft)"))
# burner glow
b.append(glow_pool(420, 238, 40, 8, "#4fc0e8", 0.6))
b.append(rect(392, 232, 56, 4, "#1a1d2b"))
# the big pot
b.append(rect(390, 186, 60, 48, "#949bb3"))
b.append(rect(390, 186, 60, 48, "url(#counter)", opacity=0.2))
b.append(rect(392, 188, 8, 44, "#e6e8ef", opacity=0.5))
b.append(rect(436, 188, 12, 44, "#525a7a", opacity=0.5))
b.append(ellipse(420, 186, 31, 5, "#bec2d1"))
b.append(ellipse(420, 186, 27, 3.5, "#c9b49a"))
b.append(ellipse(420, 186, 27, 3.5, "#e0802a", opacity=0.6))   # broth
b.append(rect(384, 196, 7, 4, "#525a7a")); b.append(rect(449, 196, 7, 4, "#525a7a"))
b.append(line(432, 186, 452, 152, "#7d6450", 2.5))  # ladle handle
b.append(rect(452, 220, 30, 14, "#bec2d1"))         # small pot
b.append(ellipse(467, 220, 15, 3, "#949bb3"))
b.append(rect(482, 226, 18, 2, "#3a2a22"))
# condiment row on the back counter
for i, c in enumerate(["#b02a2a", "#3a2a22", "#e0802a", "#4f8f45", "#fffaf0"]):
    b.append(rect(160 + i * 9, 224, 6, 12, c)); b.append(rect(161 + i * 9, 221, 4, 3, "#3a2a22"))
b.append(rect(220, 228, 26, 8, "#f6e7c8")); b.append(rect(220, 228, 26, 2, "#fffaf0"))   # bowls
b.append(rect(510, 222, 22, 14, "#2f6a35")); b.append(text(521, 232, "米", "#fff0b8", 7, family="IPAexGothic"))
b.append(rect(560, 226, 30, 10, "#7d6450"))   # cutting board
b.append(rect(566, 224, 18, 3, "#e6e8ef"))    # cleaver

# ---- pendant lamps and their light
for lx in (230, 360, 490):
    b.append(line(lx, 26, lx, 60, "#1a1d2b", 1))
    b.append(light_cone(lx, 70, 20, 130, 210, "#ffd27a", 0.16))
    b.append(path(f"M{lx - 12},{70} q12,-16 24,0 z", fill="#b85c1c"))
    b.append(rect(lx - 12, 69, 24, 2, "#e0802a"))
    b.append(ellipse(lx, 72, 5, 2.5, "#fff0b8", filter="url(#glow)"))
    b.append(glow_pool(lx, 74, 30, 14, "#ffd27a", 0.5))
    b.append(glow_pool(lx, COUNTER_TOP, 70, 10, "#ffb347", 0.45))

# ---- front counter
b.append(rect(140, COUNTER_TOP + 8, 470, FLOOR - COUNTER_TOP - 8, "#173a4a"))
b.append(tiles(142, COUNTER_TOP + 10, 466, FLOOR - COUNTER_TOP - 18, 6, "#2b6e78", "#3f8f8f", "#173a4a", seed=12))
b.append(rect(142, COUNTER_TOP + 10, 466, FLOOR - COUNTER_TOP - 18, "#ffb347", opacity=0.12))
b.append(rect(142, COUNTER_TOP + 10, 466, 6, "#000", opacity=0.3))
b.append(rect(140, FLOOR - 8, 470, 8, "#3a2a22"))
b.append(rect(136, COUNTER_TOP, 478, 10, "url(#counter)"))
b.append(rect(136, COUNTER_TOP, 478, 2, "#fff0b8", opacity=0.8))
b.append(rect(136, COUNTER_TOP + 9, 478, 1, "#3a2a22"))
# chipped tile and a sticker on counter front
b.append(rect(330, 300, 5, 4, "#173a4a"))
b.append(circle(560, 300, 5, "#ffd27a")); b.append(circle(562, 298.5, 4, "#2b6e78"))   # moon sticker
# on the counter: register, lucky cat, chopsticks, a bowl, napkins, soy, menu card
b.append(rect(150, 252, 34, 20, "#525a7a"))       # register
b.append(rect(150, 252, 34, 3, "#949bb3"))
b.append(rect(154, 246, 18, 8, "#2a2f45")); b.append(rect(155, 247, 16, 5, "#9bd6c4"))
b.append(text(163, 251.5, "0.00", "#173a4a", 3.5, family="DejaVu Sans Mono"))
for r in range(2):
    for c in range(4):
        b.append(rect(155 + c * 7, 258 + r * 5, 5, 3, "#bec2d1"))
# maneki-neko with a cracked raised paw
mx, my = 200, 272
b.append(ellipse(mx, my, 11, 2.5, "#000", opacity=0.3))
b.append(rect(mx - 9, my - 16, 18, 16, "#fffaf0"))
b.append(ellipse(mx, my - 16, 9, 4, "#fffaf0"))
b.append(circle(mx, my - 23, 8.5, "#fffaf0"))
b.append(poly([(mx - 8, my - 27), (mx - 6, my - 35), (mx - 2, my - 30)], "#fffaf0"))
b.append(poly([(mx + 8, my - 27), (mx + 6, my - 35), (mx + 2, my - 30)], "#fffaf0"))
b.append(poly([(mx - 6.5, my - 28.5), (mx - 5.8, my - 32.5), (mx - 3.5, my - 30)], "#ff9cc6"))
b.append(path(f"M{mx - 5},{my - 24} q1.5,-1.5 3,0 M{mx + 2},{my - 24} q1.5,-1.5 3,0", stroke="#3a2a22", stroke_width=0.9))
b.append(circle(mx, my - 21, 0.9, "#e04a3a"))
b.append(rect(mx - 9, my - 15, 18, 2, "#e04a3a"))                       # collar
b.append(circle(mx, my - 12, 2.2, "#ffd27a"))                           # bell
b.append(ellipse(mx - 2, my - 6, 4, 3, "#ffd27a"))                      # koban coin
b.append(rect(mx + 8, my - 33, 6, 13, "#fffaf0"))                       # raised paw
b.append(ellipse(mx + 11, my - 33, 3.5, 3, "#fffaf0"))
b.append(path(f"M{mx + 9},{my - 30} l2,3 l-1,2 l2,3", stroke="#525a7a", stroke_width=0.7))  # crack
b.append(rect(mx + 9, my - 26, 4, 1, "#c9b49a"))                         # glue line
b.append(circle(mx - 6, my - 4, 1.5, "#e04a3a", opacity=0.6))
# napkin box, chopstick cup, soy bottles near guest stools
b.append(rect(452, 258, 18, 14, "#fffaf0")); b.append(rect(456, 255, 10, 3, "#f6e7c8"))
b.append(rect(476, 258, 9, 14, "#b85c1c"))
for i in range(5):
    b.append(line(477 + i * 1.6, 258, 476 + i * 2, 246, "#c9b49a", 0.8))
b.append(rect(490, 260, 5, 12, "#3a2a22")); b.append(rect(491, 257, 3, 3, "#b02a2a"))
b.append(rect(497, 262, 5, 10, "#e04a3a")); b.append(rect(498, 259, 3, 3, "#fffaf0"))
# a finished bowl someone left a coin under
b.append(ellipse(360, 268, 14, 3, "#000", opacity=0.25))
b.append(path("M346,262 q14,14 28,0 z", fill="#2f8fc0"))
b.append(ellipse(360, 262, 14, 2.5, "#f6e7c8"))
b.append(line(352, 260, 372, 254, "#c9b49a", 1)); b.append(line(353, 261, 373, 256, "#c9b49a", 1))
b.append(ellipse(378, 270, 3, 1.2, "#ffd27a"))
# a little bowl of cat food on the floor at the counter end
b.append(ellipse(594, FLOOR + 6, 8, 2.5, "#e04a3a")); b.append(ellipse(594, FLOOR + 5, 6, 1.5, "#8a3f16"))
b.append(text(594, FLOOR + 14, "DUMPLING", "#c9b49a", 3.5, opacity=0.8))

# ---- floor
b.append(rect(0, FLOOR, W, H - FLOOR, "url(#floor)"))
for i in range(0, W, 16):
    for j, yy in enumerate(range(FLOOR, H, 8)):
        if (i // 16 + j) % 2 == 0:
            b.append(rect(i, yy, 16, 8, "#3a2a22", opacity=0.55))
# reflections of counter light, door neon
b.append(ellipse(300, FLOOR + 14, 180, 8, "#ffb347", opacity=0.25, filter="url(#soft)"))
b.append(ellipse(65, FLOOR + 18, 50, 7, "#ff5fa2", opacity=0.25, filter="url(#soft)"))
b.append(ellipse(64, FLOOR + 6, 40, 3, "#bec2d1", opacity=0.2))  # wet footprint trail
for i, (fx, fy) in enumerate([(110, 336), (128, 344), (150, 338), (170, 348)]):
    b.append(ellipse(fx, fy, 4, 1.6, "#949bb3", opacity=0.3))

# door mat and a dropped paper ticket
b.append(poly([(20, 330), (104, 330), (112, 346), (12, 346)], "#1f5260"))
b.append(poly([(24, 332), (100, 332), (106, 344), (18, 344)], "none", stroke="#3f8f8f", stroke_width=0.8))
b.append(text(62, 342, "WELCOME", "#63b3a8", 5))
b.append(tr(rect(250, 350, 10, 6, "#fffaf0"), rot=18, cx=255, cy=353))
# ---- stools (front of house)
for sx, c in [(210, "#b02a2a"), (380, "#b02a2a"), (470, "#b02a2a"), (556, "#b02a2a")]:
    b.append(stool(sx, 346, c, h=36, seat_w=22))

# warm overall vignette
b.append(rect(0, 0, W, H, "#2a0f24", opacity=0.08))

out = svg(W, H, "".join(b), defs)
open(sys.argv[1], "w").write(out)
