"""The back alley behind Halfmoon Noodle. 640x360, figure scale.

Fibre junction box (left), graffiti, the noodle shop's back door with a warm
crack of light, milk crates, steam vent, starling drone roost, alley mouth to
the street (right). Rafe ~x172, feet ~y330.
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from svg import *
from props import *

defs = (
    lin_grad("asky", [(0, "#0d0b1a"), (1, "#332a57")]) +
    lin_grad("awall", [(0, "#1b1630"), (0.6, "#262043"), (1, "#1a1d2b")]) +
    lin_grad("aground", [(0, "#2a2f45"), (1, "#0d0b1a")]) +
    lin_grad("mouth", [(0, "#1b1630"), (0.5, "#4a1538"), (1, "#b02d6f")]) +
    lin_grad("crack", [(0, "#fff0b8"), (1, "#ffb347", 0)], 0, 0, 1, 0)
)

FLOOR = 296
b = []
b.append(rect(0, 0, W, H, "url(#asky)"))
b.append(stars(20, 41, 40))
# ---- back wall of the buildings
b.append(rect(0, 36, 560, FLOOR - 36, "url(#awall)"))
# bricks
rb = random.Random(1)
for r, y in enumerate(range(40, FLOOR, 8)):
    b.append(rect(0, y + 7, 560, 1, "#0d0b1a", opacity=0.45))
    for x in range((r % 2) * 10, 560, 20):
        b.append(rect(x + 19, y, 1, 7, "#0d0b1a", opacity=0.45))
        if rb.random() < 0.12:
            b.append(rect(x, y, 19, 7, rb.choice(["#332a57", "#463a70", "#1b1630"]), opacity=0.7))
b.append(rect(0, 36, 560, 3, "#463a70"))
# upper windows (dim, one lit), fire escape
b.append(windows(40, 52, 3, 1, 22, 26, 30, 0, seed=5, lit=0.3, frame="#1b1630"))
b.append(rect(260, 50, 30, 30, "#1b1630")); b.append(rect(262, 52, 26, 26, "#ffb347", opacity=0.8))
b.append(rect(262, 52, 10, 26, "#7a1f52", opacity=0.6))
b.append(glow_pool(275, 66, 30, 20, "#ffb347", 0.35))
b.append(rect(240, 86, 70, 3, "#1a1d2b"))
for x in range(240, 312, 6):
    b.append(line(x, 76, x, 86, "#1a1d2b", 0.8))
b.append(line(240, 76, 310, 76, "#1a1d2b", 1))
b.append(line(306, 89, 330, 140, "#1a1d2b", 1.5)); b.append(line(312, 89, 336, 140, "#1a1d2b", 1.5))
b.append(potted_plant(292, 86, 0.6, pot="#b85c1c", seed=9))

# ---- overhead cables criss-crossing
for (x1, y1, x2, y2, sag, wdt) in [(0, 20, 640, 40, 26, 1.2), (0, 44, 560, 10, 20, 1), (80, 0, 640, 70, 30, 0.8),
                                    (0, 70, 400, 0, 18, 0.8), (200, 0, 640, 20, 14, 1.4)]:
    b.append(cable(x1, y1, x2, y2, sag, "#0d0b1a", wdt))
b.append(rect(330, 28, 10, 6, "#1a1d2b")); b.append(circle(335, 34, 1, "#e04a3a", filter="url(#glow)"))   # junction on the wire
# a pair of sneakers thrown over the wire
b.append(line(452, 34, 450, 44, "#c9b49a", 0.5)); b.append(line(456, 34, 460, 46, "#c9b49a", 0.5))
b.append(rect(446, 44, 7, 4, "#ff5fa2")); b.append(rect(457, 46, 7, 4, "#ff5fa2"))

# ---- fibre junction box (big grey, warning stickers) with conduits
jx, jy, jw, jh = 34, 168, 106, 128
for i, cx_ in enumerate((54, 70, 86)):
    b.append(rect(cx_, 36, 6, jy - 36, "#525a7a")); b.append(rect(cx_, 36, 1.5, jy - 36, "#949bb3", opacity=0.6))
    for yy in range(60, jy, 34):
        b.append(rect(cx_ - 1, yy, 8, 3, "#3b4260"))
b.append(rect(jx - 2, jy - 2, jw + 4, jh + 2, "#1a1d2b"))
b.append(rect(jx, jy, jw, jh, "#6f7896"))
b.append(rect(jx, jy, jw, 4, "#949bb3"))
b.append(rect(jx + jw / 2 - 1, jy + 6, 2, jh - 6, "#3b4260"))
b.append(rect(jx + 4, jy + 8, jw / 2 - 7, jh - 12, "#949bb3", opacity=0.25))
for yy in (jy + 30, jy + 96):
    b.append(rect(jx + jw / 2 - 8, yy, 4, 10, "#3b4260")); b.append(rect(jx + jw / 2 + 4, yy, 4, 10, "#3b4260"))
b.append(rect(jx + jw / 2 + 6, jy + 58, 10, 6, "#2a2f45"))          # padlock hasp
b.append(path(f"M{jx + jw / 2 + 8},{jy + 58} q3,-6 6,0", stroke="#bec2d1", stroke_width=1.2))
b.append(rect(jx + jw / 2 + 7, jy + 60, 8, 7, "#ffb347"))
# warning stickers
b.append(poly([(jx + 18, jy + 30), (jx + 30, jy + 10), (jx + 42, jy + 30)], "#ffd27a"))
b.append(poly([(jx + 18, jy + 30), (jx + 30, jy + 10), (jx + 42, jy + 30)], "none", stroke="#1a1d2b", stroke_width=1.2))
b.append(path(f"M{jx + 31},{jy + 15} l-3,6 l3,0 l-2,6", stroke="#1a1d2b", stroke_width=1.2))
b.append(rect(jx + 62, jy + 12, 34, 16, "#e04a3a"))
b.append(text(jx + 79, jy + 19, "DANGER", "#fffaf0", 5)); b.append(text(jx + 79, jy + 25.5, "FIBRE TRUNK", "#fffaf0", 3.2))
b.append(rect(jx + 10, jy + 44, 36, 12, "#fffaf0"))
b.append(text(jx + 28, jy + 52, "HFM-07", "#1a1d2b", 5, family="DejaVu Sans Mono"))
b.append(rect(jx + 62, jy + 76, 30, 14, "#ffd27a"))
b.append(text(jx + 77, jy + 85, "NO CUT", "#1a1d2b", 4.6))
b.append(circle(jx + 18, jy + 100, 6, "#4ff0e6")); b.append(text(jx + 18, jy + 102, "↯", "#173a4a", 7))   # swarm-net sticker
b.append(rect(jx + 8, jy + 72, 30, 9, "#ff9cc6")); b.append(text(jx + 23, jy + 78.5, "slow zone", "#4a1538", 3.6))
b.append(circle(jx + 88, jy + 6, 1.6, "#7fb85a", filter="url(#glow)"))  # status LED
b.append(circle(jx + 94, jy + 6, 1.6, "#7fb85a", filter="url(#glow)"))
b.append(rect(jx + 14, jy + jh - 18, 24, 4, "#949bb3", opacity=0.4))   # scuffed paint
# Rafe's milk crate + thermos + toolbag beside the box
b.append(rect(144, 276, 26, 20, "#1f5f8a"))
for i in range(4):
    b.append(rect(146 + i * 6, 280, 3, 12, "#1a3a5a"))
b.append(rect(144, 276, 26, 2, "#2f8fc0"))
b.append(rect(150, 262, 7, 14, "#bec2d1")); b.append(rect(150, 262, 7, 2, "#525a7a"))
b.append(rect(112, 282, 28, 14, "#3a2a22")); b.append(path("M116,282 q10,-10 20,0", stroke="#1a1d2b", stroke_width=1.5))
b.append(line(132, 282, 136, 274, "#e04a3a", 1.5))   # bolt cutters poking out
b.append(line(134, 282, 140, 276, "#e04a3a", 1.5))

# ---- graffiti
gx = 180
# big bubble-letter piece: "SLOW" with a sunrise behind it, half-painted
b.append(circle(gx + 62, 236, 34, "#ffb347", opacity=0.55))
b.append(circle(gx + 62, 236, 24, "#ffd27a", opacity=0.55))
b.append(rect(gx + 20, 236, 90, 40, "url(#awall)"))
b.append(text(gx + 62, 262, "SLOW", "#ff5fa2", 34, family="DejaVu Sans", weight="bold",
              stroke="#1b1630", stroke_width=5, stroke_linejoin="round", paint_order="stroke",
              transform=f"rotate(-5,{gx + 62},262)"))
b.append(text(gx + 62, 262, "SLOW", "none", 34, family="DejaVu Sans", weight="bold",
              stroke="#ffd3e6", stroke_width=0.8, transform=f"rotate(-5,{gx + 62},262) translate(-1,-1)"))
b.append(text(gx + 30, 222, "stay", "#4ff0e6", 16, family="DejaVu Serif", weight="bold",
              stroke="#173a4a", stroke_width=2, paint_order="stroke", transform=f"rotate(-12,{gx + 30},222)"))
b.append(text(gx + 30, 286, "R + M 4EVER", "#a99ad0", 5, opacity=0.6, weight="normal"))
b.append(text(gx + 104, 182, "ned was here", "#bec2d1", 4, opacity=0.5, weight="normal"))
b.append(path(f"M{gx + 40},268 l0,10 M{gx + 92},262 l0,8 M{gx + 70},266 l0,6", stroke="#ff5fa2", stroke_width=1.2, opacity=0.8))   # drips
# a little bird stencil + heart + crossed-out drone
b.append(path(f"M{gx + 104},146 q6,-6 12,0 q6,-6 12,0", stroke="#fffaf0", stroke_width=2))
b.append(text(gx + 18, 160, "♥", "#ffd27a", 14, opacity=0.9))
b.append(circle(gx + 70, 150, 9, "none", stroke="#ffb347", stroke_width=1.5))
b.append(rect(gx + 64, 148, 12, 4, "#ffb347")); b.append(line(gx + 62, 158, gx + 78, 142, "#e04a3a", 2))
b.append(text(gx + 30, 286, "R + M 4EVER", "#a99ad0", 5, opacity=0.6, weight="normal"))
b.append(text(gx + 104, 182, "ned was here", "#bec2d1", 4, opacity=0.5, weight="normal"))
b.append(path(f"M{gx + 130},236 l0,10 M{gx + 40},250 l0,8", stroke="#ff5fa2", stroke_width=1, opacity=0.7))   # drips

# ---- noodle shop back door with warm crack of light
dx, dy, dw, dh = 352, 170, 46, FLOOR - 170
b.append(glow_pool(dx + dw / 2, dy + dh / 2, 50, 70, "#ffb347", 0.35))
b.append(rect(dx - 5, dy - 5, dw + 10, dh + 5, "#3a2a22"))
b.append(rect(dx, dy, dw, dh, "#7a1a1e"))
b.append(rect(dx + 4, dy + 6, dw - 8, 40, "#4a0f12", opacity=0.5)); b.append(rect(dx + 4, dy + 54, dw - 8, 64, "#4a0f12", opacity=0.5))
b.append(rect(dx + dw - 3, dy, 4, dh, "#fff0b8", filter="url(#glow)"))           # crack of light (door ajar)
b.append(poly([(dx + dw + 1, FLOOR), (dx + dw + 3, FLOOR), (dx + dw + 70, H), (dx + dw + 30, H)], "url(#crack)", opacity=0.55))
b.append(rect(dx + 6, dy + 60, 4, 10, "#c9b49a"))
b.append(rect(dx + 10, dy + 14, 26, 18, "#fffaf0"))
b.append(text(dx + 23, dy + 21, "STAFF", "#7a1a1e", 4.5)); b.append(text(dx + 23, dy + 28, "+ cat", "#3a2a22", 3.6, weight="normal"))
b.append(path(f"M{dx + 15},{dy + 44} a4,4 0 1,0 4,-4 a3,3 0 1,1 -4,4", fill="#ffd27a"))   # half-moon decal
# bulb above the door
b.append(rect(dx + dw / 2 - 6, dy - 16, 12, 4, "#3a2a22"))
b.append(circle(dx + dw / 2, dy - 9, 3.5, "#fff0b8", filter="url(#glow)"))
b.append(light_cone(dx + dw / 2, dy - 8, 10, 90, 130, "#ffd27a", 0.22))
# step + bin
b.append(rect(dx - 8, FLOOR - 4, dw + 16, 6, "#525a7a"))
b.append(rect(300, 250, 38, 46, "#2f6a35")); b.append(rect(298, 246, 42, 6, "#1f4a2a"))
b.append(rect(304, 256, 30, 2, "#1f4a2a")); b.append(text(319, 275, "♻", "#7fb85a", 10))
b.append(ellipse(330, 244, 6, 3, "#1a1d2b"))
# a bowl of water for the cat on the step
b.append(ellipse(344, FLOOR + 2, 6, 2, "#4fc0e8")); b.append(ellipse(344, FLOOR + 1.5, 4, 1, "#a8fff6"))

# ---- milk crates stacked
for i, (cx_, cy_, c) in enumerate([(412, FLOOR, "#e04a3a"), (440, FLOOR, "#2f8fc0"), (424, FLOOR - 22, "#ffd27a")]):
    b.append(rect(cx_, cy_ - 22, 26, 22, c))
    b.append(rect(cx_, cy_ - 22, 26, 2.5, "#fffaf0", opacity=0.3))
    for j in range(4):
        b.append(rect(cx_ + 2 + j * 6, cy_ - 17, 3, 13, "#0d0b1a", opacity=0.5))
b.append(rect(428, FLOOR - 52, 18, 8, "#f6e7c8"))   # empty broth tub on top

# ---- steam vent (low on the wall) with plume
vx, vy = 478, 252
b.append(rect(vx, vy, 44, 26, "#3b4260"))
for i in range(6):
    b.append(rect(vx + 3, vy + 3 + i * 4, 38, 2, "#1a1d2b"))
b.append(ellipse(vx + 22, vy - 30, 26, 40, "#f6e7c8", opacity=0.25, filter="url(#haze)"))
b.append(ellipse(vx + 18, vy - 10, 16, 18, "#fffaf0", opacity=0.3, filter="url(#soft)"))
b.append(ellipse(vx + 30, vy - 50, 14, 22, "#f6e7c8", opacity=0.2, filter="url(#soft)"))

# ---- starling drone roost (rack high on the wall, drones docked like birds)
rx0, ry0, rw = 420, 108, 132
b.append(rect(rx0, ry0, rw, 4, "#525a7a"))
b.append(rect(rx0, ry0 + 30, rw, 4, "#525a7a"))
for x in (rx0 + 4, rx0 + rw - 8):
    b.append(rect(x, ry0 - 4, 4, 44, "#3b4260"))
b.append(line(rx0 + 6, ry0 + 40, rx0 + 30, 160, "#3b4260", 1.5)); b.append(line(rx0 + rw - 6, ry0 + 40, rx0 + rw - 30, 160, "#3b4260", 1.5))
b.append(rect(rx0 + 2, ry0 - 16, 40, 10, "#1a3a5a"))
b.append(text(rx0 + 22, ry0 - 9, "STARLING", "#4ff0e6", 4.4))
def drone(x, y, lit, col="#949bb3"):
    o = [ellipse(x, y - 3, 5, 3, col), rect(x - 8, y - 5, 16, 1.5, "#3b4260"),
         ellipse(x - 8, y - 6, 3, 0.8, "#bec2d1", opacity=0.7), ellipse(x + 8, y - 6, 3, 0.8, "#bec2d1", opacity=0.7),
         line(x - 2, y - 1, x - 3, y, "#3b4260", 0.8), line(x + 2, y - 1, x + 3, y, "#3b4260", 0.8)]
    if lit:
        o.append(circle(x + 2, y - 3, 1, lit, filter="url(#glow)"))
    return "".join(o)
rnd = random.Random(2)
for row, yy in enumerate((ry0, ry0 + 30)):
    for k in range(7):
        x = rx0 + 12 + k * 18 + rnd.uniform(-2, 2)
        if rnd.random() < 0.85:
            b.append(drone(round(x, 1), yy, rnd.choice(["#4ff0e6", "#4ff0e6", "#7fb85a", "#e04a3a", None])))
b.append(drone(rx0 + rw + 20, ry0 - 14, "#4ff0e6"))   # one hovering in, late
b.append(glow_pool(rx0 + rw / 2, ry0 + 16, 80, 26, "#4ff0e6", 0.25))
# droppings of the mechanical kind: a fallen screw and a little nest of zip ties
b.append(path(f"M{rx0 + 30},{ry0 + 4} q3,-6 8,-2 q4,-4 6,2", stroke="#ffd27a", stroke_width=0.8))

# ---- alley mouth to the street (right) — exit
b.append(rect(560, 0, 80, FLOOR, "url(#mouth)"))
b.append(windows(578, 30, 2, 3, 12, 14, 12, 14, seed=88, lit=0.6, frame="#1b1630"))
b.append(rect(560, 236, 80, 60, "#3b4260", opacity=0.6))          # far sidewalk
b.append(rect(560, 236, 80, 2, "#949bb3", opacity=0.6))
b.append(rect(574, 120, 50, 22, "#2a0f24"))
b.append(neon(599, 136, "NOODLE", "#ffb347", 9))
b.append(glow_pool(600, 200, 70, 120, "#ff5fa2", 0.45))
b.append(rect(560, 0, 6, FLOOR, "#0d0b1a"))
b.append(rect(566, 0, 3, FLOOR, "#463a70"))
b.append(rect(600, 20, 10, 100, "#2a2f45"))           # rail pillar on the street

# ---- ground: wet asphalt, puddles reflecting the warm door and neon
b.append(rect(0, FLOOR, W, H - FLOOR, "url(#aground)"))
b.append(rect(0, FLOOR, W, 2, "#3b4260"))
b.append(line(0, 330, 560, 318, "#1a1d2b", 3))         # gutter channel
for cx_, cy_, rx, col in [(380, 322, 46, "#ffb347"), (600, 318, 40, "#ff5fa2"), (110, 340, 52, "#5d4f8c"), (500, 346, 34, "#4ff0e6")]:
    b.append(ellipse(cx_, cy_, rx, 5, "#3b4260", opacity=0.6))
    b.append(ellipse(cx_, cy_, rx * 0.8, 3, col, opacity=0.35, filter="url(#soft)"))
    b.append(ellipse(cx_ - rx * 0.3, cy_ - 1, rx * 0.3, 0.8, "#bec2d1", opacity=0.5))
b.append(rect(240, 310, 40, 4, "#1a1d2b")); b.append(rect(242, 311, 36, 2, "#3b4260"))   # drain grate
for i in range(6):
    b.append(rect(244 + i * 6, 311, 1, 2, "#0d0b1a"))
# cigarette butts & a crushed can
b.append(rect(200, 340, 3, 1, "#fffaf0")); b.append(rect(206, 344, 3, 1, "#fffaf0"))
b.append(rect(520, 310, 5, 3, "#e04a3a"))

out = svg(W, H, "".join(b), defs)
open(sys.argv[1], "w").write(out)
