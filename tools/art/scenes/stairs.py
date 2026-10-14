"""The Stairs — the long stairway climbing the hill. 640x360, figure scale.

Lower flight comes up from the bottom-left (down to the street), a landing with
the shrine, lamp and vending machine, then the upper flight climbs right toward
the roofs. Imogen sits on the first step of the upper flight.
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from svg import *
from props import *

defs = (
    lin_grad("ssky", [(0, "#0d0b1a"), (0.5, "#262043"), (0.85, "#5d4f8c"), (1, "#b02d6f")]) +
    lin_grad("bay", [(0, "#1a3a5a"), (1, "#0d0b1a")]) +
    lin_grad("stone", [(0, "#3b4260"), (1, "#1a1d2b")]) +
    lin_grad("bldg", [(0, "#262043"), (1, "#332a57")])
)

LAND = 262          # landing floor
LX0, LX1 = 226, 424  # landing extent
STEP_W, STEP_H = 16, 8

b = []
# ---- sky & view down over the city (left)
b.append(rect(0, 0, W, H, "url(#ssky)"))
b.append(stars(60, 17, 120))
b.append(glow_pool(120, 220, 200, 60, "#b02d6f", 0.4))
# distant bay and far shore
b.append(rect(0, 196, 300, 60, "url(#bay)"))
b.append(rect(0, 194, 300, 3, "#262043"))
for i in range(30):
    rnd = random.Random(i)
    b.append(rect(rnd.uniform(0, 290), 197 + rnd.uniform(0, 30), rnd.uniform(4, 14), 1, rnd.choice(["#ffb347", "#ff5fa2", "#4fc0e8"]), opacity=0.45))
# far shore skyline with Kestrel tower
for x, w_, h_ in [(10, 12, 18), (26, 8, 26), (36, 14, 14), (60, 10, 30), (78, 16, 20), (150, 10, 24), (166, 14, 16), (190, 8, 28), (206, 18, 12)]:
    b.append(rect(x, 194 - h_, w_, h_, "#262043"))
    for wy in range(194 - h_ + 2, 192, 4):
        b.append(rect(x + 2, wy, w_ - 4, 1, "#7d6fae", opacity=0.4))
b.append(poly([(112, 194), (116, 112), (118, 106), (120, 112), (124, 194)], "#332a57"))
b.append(rect(115, 116, 6, 2, "#a8fff6", filter="url(#glow)"))
b.append(glow_pool(118, 116, 20, 16, "#4fc0e8", 0.5))
# nearer rooftops below the stairs, lots of lit windows
rnd = random.Random(5)
x = -6
while x < 300:
    w_ = rnd.uniform(26, 48)
    top = rnd.uniform(212, 250)
    col = rnd.choice(["#1b1630", "#262043", "#1a1d2b"])
    b.append(rect(x, top, w_, H - top, col))
    b.append(rect(x, top, w_, 2, "#463a70"))
    b.append(windows(x + 4, top + 6, int(w_ // 9), 6, 5, 6, 4, 6, seed=int(x + 100), lit=0.45))
    if rnd.random() < 0.4:   # rooftop water tank / antenna
        b.append(rect(x + 6, top - 8, 8, 8, "#1a1d2b"))
        b.append(line(x + w_ - 6, top, x + w_ - 6, top - 14, "#1a1d2b", 1))
    x += w_ + rnd.uniform(0, 4)
# elevated rail sweeping through the view, with a lit train
b.append(path("M0,232 Q150,220 300,226", stroke="#1a1d2b", stroke_width=6))
for i in range(6):
    b.append(rect(40 + i * 15, 220, 13, 6, "#4fc0e8" if i % 2 else "#a8fff6", opacity=0.9))
b.append(glow_pool(85, 224, 60, 10, "#4fc0e8", 0.4))
for xx in range(20, 300, 50):
    b.append(rect(xx, 230, 4, 40, "#1a1d2b"))

# ---- apartment building behind the upper flight (right), with Pia's window
b.append(rect(412, 0, 228, 300, "url(#bldg)"))
b.append(rect(412, 0, 4, 300, "#463a70"))
for yy in range(0, 300, 12):
    b.append(rect(416, yy, 224, 1, "#1b1630", opacity=0.5))          # siding
b.append(windows(560, 18, 2, 2, 26, 30, 16, 26, seed=77, lit=0.6, frame="#1b1630"))
# Pia's window — dark room, glow-in-the-dark star stickers, nightlight
px, py, pw, ph = 452, 62, 60, 52
b.append(rect(px - 4, py - 4, pw + 8, ph + 8, "#1b1630"))
b.append(rect(px, py, pw, ph, "#173a4a"))
b.append(rect(px, py, pw, ph, "#1f5260", opacity=0.5))
b.append(glow_pool(px + 46, py + 42, 18, 12, "#ffb347", 0.6))   # nightlight
b.append(circle(px + 46, py + 44, 2, "#ffd27a"))
for sx, sy, s in [(8, 8, 3), (20, 14, 2.2), (34, 7, 3.4), (12, 24, 2), (44, 18, 2.6), (28, 30, 2.2), (6, 38, 2.6), (50, 6, 2)]:
    cx_, cy_ = px + sx, py + sy
    pts = []
    for k in range(10):
        r = s if k % 2 == 0 else s * 0.45
        a = math.radians(k * 36 - 90)
        pts.append((round(cx_ + math.cos(a) * r, 1), round(cy_ + math.sin(a) * r, 1)))
    b.append(poly(pts, "#b8de7a", filter="url(#glow)"))
b.append(path(f"M{px + 38},{py + 30} a5,5 0 1,0 5,-5 a3.8,3.8 0 1,1 -5,5", fill="#d2f0e2", filter="url(#glow)"))   # moon sticker
b.append(rect(px + pw / 2 - 1, py, 2, ph, "#1b1630"))
b.append(rect(px - 6, py + ph + 4, pw + 12, 4, "#463a70"))                # sill
b.append(potted_plant(px + 8, py + ph + 4, 0.6, pot="#e04a3a", seed=3))
b.append(rect(px + 40, py + ph - 2, 8, 6, "#ff9cc6"))                      # little toy rabbit
b.append(circle(px + 44, py + ph - 4, 3, "#ff9cc6"))
b.append(rect(px + 41, py + ph - 10, 1.5, 5, "#ff9cc6")); b.append(rect(px + 45, py + ph - 10, 1.5, 5, "#ff9cc6"))
# AC unit and a sitter's lit kitchen window next door
b.append(rect(530, 126, 28, 18, "#6f7896")); b.append(rect(532, 128, 24, 14, "#525a7a"))
for i in range(5):
    b.append(rect(534, 130 + i * 2.6, 20, 1, "#3b4260"))
b.append(path("M544,144 q2,8 -2,14", stroke="#4fc0e8", stroke_width=0.6, opacity=0.6))
b.append(rect(452, 150, 46, 34, "#1b1630")); b.append(rect(455, 153, 40, 28, "#ffd27a", opacity=0.85))
b.append(rect(455, 153, 14, 28, "#7a1f52", opacity=0.6))
b.append(glow_pool(475, 166, 40, 24, "#ffb347", 0.35))
# laundry line
b.append(cable(420, 136, 640, 128, 10, "#0d0b1a", 0.8))
for i, (lx, c) in enumerate([(586, "#ff9cc6"), (600, "#fffaf0"), (612, "#4fc0e8")]):
    b.append(rect(lx, 134 + i * 0.6, 9, 12 - i * 2, c, opacity=0.85))

# ---- upper flight (landing → up/right)
def flight(x0, y0, n, dirn, rise=1, w=STEP_W, h=STEP_H, base=H + 10):
    """n steps starting at x0 going in x-direction dirn; rise=+1 climbs, -1 descends."""
    out = []
    tops = []
    for i in range(n):
        xa = x0 + dirn * i * w
        ya = y0 - rise * i * h
        tops.append((xa, ya))
    pts = [(x0, base)]
    for i, (xa, ya) in enumerate(tops):
        pts += [(xa, ya), (xa + dirn * w, ya)]
    pts.append((x0 + dirn * n * w, base))
    out.append(poly(pts, "url(#stone)"))
    # stone coursing on the side mass
    for yy in range(int(min(t[1] for t in tops)) + 12, H, 13):
        out.append(line(min(x0, x0 + dirn * n * w), yy, max(x0, x0 + dirn * n * w), yy, "#1a1d2b", 0.8, opacity=0.5))
    for i, (xa, ya) in enumerate(tops):
        lo, hi = sorted((xa, xa + dirn * w))
        out.append(rect(lo, ya, hi - lo, 2, "#949bb3"))            # wet tread nosing
        out.append(rect(lo, ya + 2, hi - lo, h - 2, "#2a2f45"))      # riser
        out.append(rect(lo + 2, ya + 0.5, (hi - lo) * 0.5, 0.8, "#bec2d1", opacity=0.6))
        if rise == 1 and i < n - 1:                                   # vertical riser face between treads
            out.append(rect(hi - 1 if dirn > 0 else lo, ya - h, 1, h, "#1a1d2b", opacity=0.6))
        if rise == -1:
            out.append(rect(lo if dirn < 0 else hi - 1, ya, 1, h, "#1a1d2b", opacity=0.6))
    return "".join(out)

UP0 = LX1
b.append(flight(UP0, LAND - STEP_H, 15, +1))
# ---- landing
b.append(rect(LX0 - 4, LAND, LX1 - LX0 + 8, H - LAND, "url(#stone)"))
b.append(rect(LX0 - 4, LAND, LX1 - LX0 + 8, 3, "#949bb3"))
# stone blocks in the retaining wall below the landing
for r, yy in enumerate(range(LAND + 6, H, 14)):
    for xx in range(LX0 - 4 + (r % 2) * 14, LX1 + 4, 28):
        b.append(rect(xx, yy, 27, 13, "#2a2f45", opacity=0.6))
        b.append(rect(xx, yy, 27, 1, "#525a7a", opacity=0.6))
b.append(path(f"M{LX0 + 20},{LAND + 6} q4,20 -2,40 M{LX0 + 120},{LAND + 4} q-6,30 2,60", stroke="#2f6a35", stroke_width=2, opacity=0.7))  # moss/ivy
for i in range(14):
    b.append(ellipse(LX0 + 18 + (i % 3) * 3 + (i // 3) * 2, LAND + 10 + i * 3, 2, 1.4, "#4f8f45"))
# posters on the retaining wall
b.append(rect(LX0 + 40, LAND + 22, 26, 34, "#ff9cc6"))
b.append(text(LX0 + 53, LAND + 34, "LAST", "#4a1538", 5)); b.append(text(LX0 + 53, LAND + 41, "DANCE", "#4a1538", 5))
b.append(text(LX0 + 53, LAND + 50, "sat 2am", "#4a1538", 4, weight="normal"))
b.append(rect(LX0 + 72, LAND + 26, 22, 28, "#fff0b8"))
b.append(text(LX0 + 83, LAND + 34, "LOST", "#b02a2a", 5))
b.append(ellipse(LX0 + 83, LAND + 43, 6, 4, "#6f7896")); b.append(circle(LX0 + 88, LAND + 40, 2.5, "#6f7896"))
b.append(text(LX0 + 83, LAND + 52, "answers to anything", "#3a2a22", 2.6, weight="normal"))
# lower flight (landing → down/left)
b.append(flight(LX0, LAND + STEP_H, 15, -1, rise=-1))
b.append(rect(LX0 - 6, LAND, 6, H - LAND, "#1a1d2b", opacity=0.6))

# ---- handrails
b.append(line(0, 220 + LX0 * 0.5, LX0, 220, "#6f7896", 2))
b.append(line(LX1, 220, 640, 108, "#6f7896", 2))
b.append(line(LX0, 220, LX1, 220, "#6f7896", 2))
for x1 in (40, 100, 160):
    y1 = 220 + (LX0 - x1) * 0.5
    b.append(line(x1, y1, x1, y1 + 38, "#525a7a", 1.5))
for x1 in (LX0, LX1):
    b.append(line(x1, 220, x1, LAND, "#525a7a", 1.5))
for x1 in range(470, 640, 60):
    y1 = 220 - (x1 - LX1) * 0.5
    b.append(line(x1, y1, x1, y1 + 38, "#525a7a", 1.5))
b.append(line(LX0, 220, LX1, 220, "#bec2d1", 0.6, opacity=0.6))

# ---- shrine on the landing (left)
sx = 252
b.append(rect(sx - 26, 166, 4, 96, "#b02a2a"))                              # mini torii
b.append(rect(sx + 24, 166, 4, 96, "#b02a2a"))
b.append(rect(sx - 32, 160, 66, 5, "#e04a3a")); b.append(rect(sx - 28, 170, 58, 3, "#b02a2a"))
b.append(path(f"M{sx - 34},{160} q34,-6 70,0", stroke="#e04a3a", stroke_width=3))
# the little house
b.append(rect(sx - 16, 196, 34, 30, "#5a4334"))
b.append(poly([(sx - 22, 198), (sx + 1, 182), (sx + 24, 198)], "#3a2a22"))
b.append(rect(sx - 22, 197, 46, 2, "#7d6450"))
b.append(rect(sx - 10, 202, 22, 20, "#1a1d2b"))
b.append(circle(sx + 1, 210, 3, "#ffd27a", filter="url(#glow)"))             # mirror / candle
b.append(rect(sx - 14, 226, 30, 4, "#7d6450"))
b.append(rect(sx - 2, 230, 6, 32, "#3a2a22"))                                # post
# shide paper streamers + rope
b.append(path(f"M{sx - 22},176 q23,8 46,0", stroke="#c9b49a", stroke_width=1.5))
for i in range(3):
    b.append(path(f"M{sx - 12 + i * 12},180 l2,4 l-3,3 l3,4", stroke="#fffaf0", stroke_width=1.2))
# prayer box (saisen) in front
b.append(rect(sx - 14, 240, 30, 22, "#7d6450"))
b.append(rect(sx - 14, 240, 30, 3, "#a08870"))
for i in range(5):
    b.append(rect(sx - 12 + i * 6, 243, 3, 3, "#3a2a22"))
b.append(text(sx + 1, 256, "奉納", "#ffd27a", 6, family="IPAexGothic"))
# offerings: oranges, cup of sake, a paper crane, a little robot figurine, a usb stick, a folded note
b.append(circle(sx - 10, 224, 2.6, "#e0802a")); b.append(circle(sx - 5, 224, 2.6, "#e0802a"))
b.append(rect(sx + 6, 220, 4, 6, "#fffaf0"))
b.append(poly([(sx + 12, 225), (sx + 16, 219), (sx + 18, 223), (sx + 22, 220), (sx + 18, 226)], "#ff9cc6"))
b.append(rect(sx + 20, 252, 6, 10, "#bec2d1")); b.append(rect(sx + 21, 248, 4, 4, "#bec2d1"))  # robot
b.append(circle(sx + 22, 250, 0.6, "#4ff0e6")); b.append(circle(sx + 24, 250, 0.6, "#4ff0e6"))
b.append(rect(sx - 20, 258, 6, 3, "#2f8fc0"))                               # usb stick
b.append(tr(rect(sx - 26, 256, 6, 4, "#fff0b8"), rot=12, cx=sx - 23, cy=258))
b.append(lantern(sx - 32, 200, 5))
b.append(glow_pool(sx, 220, 50, 40, "#ffb347", 0.3))
# hydrangea bush beside the shrine
for i in range(10):
    rr = random.Random(i + 50)
    b.append(circle(LX0 - 2 + rr.uniform(-6, 10), 250 + rr.uniform(-8, 8), rr.uniform(3, 5), rr.choice(["#7d6fae", "#5d4f8c", "#a99ad0", "#2f6a35"])))

# ---- lamp post on the landing
lpx = 330
b.append(light_cone(lpx, 132, 10, 120, 130, "#ffd27a", 0.2))
b.append(rect(lpx - 2, 128, 4, LAND - 128, "#3b4260"))
b.append(rect(lpx - 4, LAND - 8, 8, 8, "#2a2f45"))
b.append(path(f"M{lpx},{130} q0,-12 12,-12", stroke="#3b4260", stroke_width=3))
b.append(rect(lpx + 6, 116, 14, 6, "#2a2f45"))
b.append(ellipse(lpx + 13, 123, 5, 2, "#fff0b8", filter="url(#glow)"))
b.append(glow_pool(lpx + 13, 126, 30, 16, "#ffd27a", 0.6))
b.append(glow_pool(lpx + 8, LAND + 2, 70, 8, "#ffb347", 0.5))
# taped-on lost-cat flyer on the post & a sticker
b.append(rect(lpx - 4, 190, 8, 10, "#fffaf0"))
b.append(circle(lpx, 176, 2.5, "#ff5fa2"))

# ---- vending machine on the landing (right) — full height (~1.8m)
vx, vt = 358, 150
b.append(rect(vx, vt, 46, LAND - vt, "#b02a2a"))
b.append(rect(vx, vt, 46, 5, "#e04a3a"))
b.append(rect(vx + 4, vt + 10, 38, 50, "#fff0b8"))
for r_ in range(4):
    for c_ in range(4):
        b.append(rect(vx + 7 + c_ * 9, vt + 13 + r_ * 12, 6, 9, ["#2f8fc0", "#e0802a", "#4f8f45", "#fffaf0", "#e04a3a"][(r_ * 4 + c_) % 5]))
        b.append(rect(vx + 8 + c_ * 9, vt + 22.5 + r_ * 12, 4, 1.5, "#4ff0e6"))
b.append(text(vx + 23, vt + 8.5, "COINS OK", "#fffaf0", 4))
b.append(rect(vx + 4, vt + 66, 24, 8, "#2a0f24")); b.append(rect(vx + 30, vt + 64, 12, 18, "#7a1f52"))
b.append(circle(vx + 36, vt + 69, 1.6, "#ffd27a")); b.append(rect(vx + 33, vt + 75, 6, 2, "#0d0b1a"))
b.append(rect(vx + 6, vt + 88, 26, 10, "#1a1d2b")); b.append(rect(vx + 8, vt + 90, 22, 3, "#3b4260"))
b.append(sticky(vx + 30, vt + 86, "#ffd27a", rot=8, s=8, lines=2))   # "out of tea"
b.append(circle(vx + 12, vt + 104, 3, "#4ff0e6")); b.append(circle(vx + 20, vt + 106, 2.4, "#ff9cc6"))  # stickers
b.append(glow_pool(vx + 23, vt + 40, 44, 50, "#fff0b8", 0.35))
# can left on the step + cat bowl
b.append(rect(vx - 8, 255, 4, 7, "#2f8fc0"))
b.append(ellipse(300, LAND + 1, 6, 2, "#e04a3a")); b.append(ellipse(300, LAND, 4.5, 1.2, "#8a3f16"))

# neighbours' potted plants climbing the upper steps
for i, (k, c) in enumerate([(3, "#e0802a"), (6, "#e04a3a"), (9, "#2f8fc0"), (12, "#b85c1c")]):
    xx = UP0 + k * STEP_W + 12
    yy = LAND - STEP_H - k * STEP_H
    b.append(potted_plant(xx, yy, 0.7, pot=c, seed=i + 20))
# a small paper lantern string across above the upper flight
b.append(string_lights(LX1, 120, 640, 40, 20, 9, colors=("#ffb347", "#ff5fa2", "#ffd27a"), r=1.6, seed=1))

# wet reflections on the landing
b.append(ellipse(vx + 23, LAND + 6, 24, 2, "#fff0b8", opacity=0.4, filter="url(#soft)"))
b.append(ellipse(sx, LAND + 6, 18, 2, "#ffb347", opacity=0.35, filter="url(#soft)"))
b.append(ellipse(380, LAND + 14, 30, 2, "#5d4f8c", opacity=0.6))   # puddle

out = svg(W, H, "".join(b), defs)
open(sys.argv[1], "w").write(out)
