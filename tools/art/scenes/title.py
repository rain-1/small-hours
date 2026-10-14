"""Title key art: Halfmoon Street from slightly above at night. 640x360.

Upper centre (approx x 150-490, y 20-150) is kept clear for the logo.
Kestrel tower on the left skyline across the bay, the water tower with Mae's
antenna on the hill crest at right.
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from svg import *
from props import *

defs = (
    lin_grad("tsky", [(0, "#0d0b1a"), (0.4, "#1b1630"), (0.7, "#332a57"), (1, "#7a1f52")]) +
    lin_grad("tstreet", [(0, "#3b4260"), (1, "#1a1d2b")]) +
    lin_grad("tbay", [(0, "#463a70"), (1, "#173a4a")])
)

b = []
b.append(rect(0, 0, W, H, "url(#tsky)"))
b.append(stars(110, 91, 170))
b.append(stars(25, 92, 120, "#fffaf0"))
b.append(glow_pool(320, 200, 360, 60, "#b02d6f", 0.45))
# half moon, top right
b.append(glow_pool(516, 34, 28, 28, "#d2f0e2", 0.3))
b.append(circle(516, 34, 10, "#f6e7c8"))
b.append(path("M516,24 a10,10 0 0,0 0,20 z", fill="#262043", opacity=0.9))

# ---- far skyline across the bay
rnd = random.Random(12)
b.append(rect(0, 176, W, 30, "url(#tbay)"))
for i in range(40):
    b.append(rect(rnd.uniform(0, W), 180 + rnd.uniform(0, 20), rnd.uniform(3, 12), 1, rnd.choice(["#ffb347", "#ff9cc6", "#4fc0e8"]), opacity=0.5))
x = 0
while x < W:
    w_ = rnd.uniform(8, 22)
    h_ = rnd.uniform(8, 34) * (1.4 if x < 200 else 1)
    b.append(rect(x, 178 - h_, w_, h_, "#262043"))
    for wy in range(int(178 - h_ + 2), 176, 3):
        for wx in range(int(x + 1), int(x + w_ - 1), 3):
            if rnd.random() < 0.2:
                b.append(rect(wx, wy, 1, 1, rnd.choice(["#7d6fae", "#ffd27a", "#4fc0e8"]), opacity=0.8))
    x += w_ + rnd.uniform(0, 3)
# Kestrel tower (left)
KX = 92
b.append(glow_pool(KX, 44, 50, 40, "#2f8fc0", 0.55))
b.append(poly([(KX - 9, 178), (KX - 4, 50), (KX, 38), (KX + 4, 50), (KX + 9, 178)], "#463a70"))
b.append(poly([(KX, 38), (KX + 4, 50), (KX + 9, 178), (KX + 2, 178)], "#332a57"))
b.append(line(KX, 38, KX, 18, "#7d6fae", 0.8))
b.append(rect(KX - 4, 46, 8, 3, "#a8fff6", filter="url(#glow)"))
b.append(circle(KX, 18, 1.4, "#4ff0e6", filter="url(#glow)"))
for yy in range(56, 176, 7):
    b.append(rect(KX - 2, yy, 4, 1.3, "#2f8fc0", opacity=0.9))
b.append(rect(KX - 4, 180, 8, 26, "#4fc0e8", opacity=0.3, filter="url(#soft)"))

# ---- the hill rising on the right with the water tower on its crest
b.append(path("M380,206 Q470,150 560,140 Q610,136 660,150 L660,340 L380,340 Z", fill="#1b1630"))
b.append(windows(530, 214, 9, 6, 6, 7, 6, 8, seed=6, lit=0.4))
b.append(windows(470, 166, 8, 3, 6, 7, 8, 8, seed=5, lit=0.45))
TX, TY = 566, 140
for lx in (TX - 20, TX - 8, TX + 8, TX + 20):
    b.append(rect(lx - 1, TY - 30, 2, 30, "#0d0b1a"))
b.append(rect(TX - 26, TY - 60, 52, 32, "#3a2a22"))
for i in range(3):
    b.append(rect(TX - 26, TY - 54 + i * 9, 52, 1, "#1a1d2b"))
b.append(poly([(TX - 28, TY - 59), (TX, TY - 74), (TX + 28, TY - 59)], "#2a2f45"))
b.append(circle(TX - 10, TY - 44, 6, "#f6e7c8", opacity=0.7)); b.append(circle(TX - 7, TY - 46, 5, "#3a2a22"))
b.append(line(TX + 6, TY - 70, TX + 6, TY - 100, "#949bb3", 1.2))
for yy in range(TY - 98, TY - 70, 5):
    b.append(line(TX + 3, yy, TX + 9, yy, "#949bb3", 0.6))
b.append(circle(TX + 6, TY - 101, 2, "#ff5fa2", filter="url(#glow)"))
b.append(glow_pool(TX + 6, TY - 100, 14, 12, "#ff5fa2", 0.6))
for k in range(3):   # broadcast rings
    r = 8 + k * 7
    b.append(path(f"M{TX + 6 + r * 0.7},{TY - 101 - r * 0.7} a{r},{r} 0 0,1 0,{r * 1.4}", stroke="#ff5fa2", stroke_width=0.8, opacity=0.6 - k * 0.15))
b.append(rect(TX - 40, TY - 16, 22, 12, "#2a0f24")); b.append(neon(TX - 29, TY - 7, "87.9", "#ff5fa2", 7))
b.append(rect(TX + 26, TY - 8, 30, 10, "#1f5f8a"))                            # June's tarp
b.append(glow_pool(TX + 40, TY - 2, 18, 8, "#4ff0e6", 0.5))
b.append(string_lights(TX - 60, TY - 10, TX + 60, TY - 4, 8, 12, r=1.1, seed=2))
# the stairs climbing the hill
for k in range(22):
    xx, yy = 430 + k * 5.5, 250 - k * 4.6
    b.append(rect(xx, yy, 10, 1.6, "#6f7896"))
b.append(circle(474, 210, 1.6, "#ffd27a", filter="url(#glow)")); b.append(glow_pool(474, 214, 14, 10, "#ffd27a", 0.5))
b.append(rect(490, 196, 4, 7, "#e04a3a", filter="url(#glow)"))               # shrine light

# ---- the crescent street seen from above
def curve(t, p0=(-30, 318), p1=(300, 214), p2=(460, 250)):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
    return x, y

# far row of buildings (fronts face the street), drawn far-to-near
far = []
t = 0.0
specs = []
rr = random.Random(7)
while t < 1.0:
    specs.append(t)
    t += rr.uniform(0.07, 0.11)
signs = {2: ("SUDS &amp; STARS", "#4ff0e6"), 4: ("HALFMOON NOODLE", "#ffb347"), 6: ("HOTLINE", "#ff5fa2"), 8: ("✚ CLINIC", "#4ff0e6")}
for idx in range(len(specs) - 1, -1, -1):
    t0 = specs[idx]
    t1 = specs[idx + 1] if idx + 1 < len(specs) else 1.04
    x0, y0 = curve(t0)
    x1, y1 = curve(t1)
    base = min(y0, y1) - 6
    w_ = x1 - x0 + 2
    h_ = rr.uniform(46, 78) * (1.15 - t0 * 0.45)
    top = base - h_
    col = rr.choice(["#332a57", "#4a1538", "#1f5260", "#262043", "#463a70"])
    if idx == 4:
        col = "#4a1538"
    o = [rect(x0, top, w_, h_ + 8, col)]
    o.append(poly([(x0, top), (x0 + w_, top), (x0 + w_ + 6, top - 8), (x0 + 6, top - 8)], "#1b1630"))   # roof seen from above
    o.append(rect(x0, top, w_, 1.5, "#7d6fae", opacity=0.6))
    o.append(windows(x0 + 4, top + 5, max(1, int((w_ - 6) // 9)), max(1, int((h_ - 26) // 12)), 5, 6, 4, 6, seed=idx * 13 + 1, lit=0.55))
    # rooftop clutter
    if rr.random() < 0.6:
        o.append(rect(x0 + 6, top - 12, 8, 6, "#2a2f45"))
    if rr.random() < 0.25:
        o.append(potted_plant(x0 + w_ - 10, top - 3, 0.45, seed=idx))
    if idx in signs:
        s, c = signs[idx]
        sw = min(w_ - 4, 8 + len(s) * 3.6)
        o.append(rect(x0 + (w_ - sw) / 2, base - 20, sw, 9, "#1b1630"))
        o.append(neon(x0 + w_ / 2, base - 13, s, c, 5.6, textLength=sw - 4, lengthAdjust="spacingAndGlyphs"))
        o.append(glow_pool(x0 + w_ / 2, base - 8, w_ * 0.7, 14, c, 0.5))
    else:
        o.append(rect(x0 + 3, base - 14, w_ - 6, 12, rr.choice(["#ffb347", "#9bd6c4", "#ff9cc6", "#2a2f45"]), opacity=0.7))
    if idx == 4:   # the noodle shop: red awning + lanterns + steam from the roof
        o.append(ellipse(x0 + w_ / 2, top - 22, 10, 18, "#f6e7c8", opacity=0.3, filter="url(#soft)"))
        o.append(rect(x0 + 2, base - 9, w_ - 4, 3, "#e04a3a"))
        o.append(lantern(x0 + 4, base - 4, 3)); o.append(lantern(x0 + w_ - 4, base - 4, 3))
    far.append("".join(o))
b.append("".join(far))

# street surface (band) with neon reflections
P0, P1, P2 = (-30, 318), (300, 214), (460, 250)
def curve_off(t, d0, d1):
    x, y = curve(t)
    return x, y + d0 + (d1 - d0) * t
st = [curve_off(i / 40, 0, 0) for i in range(41)]
sb = [curve_off(i / 40, 24, 12) for i in range(40, -1, -1)]
b.append(poly([(round(x, 1), round(y, 1)) for x, y in st + sb], "url(#tstreet)"))
b.append(path("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in st), stroke="#6f7896", stroke_width=1))   # kerb
for t in [0.08, 0.2, 0.32, 0.44, 0.56, 0.68, 0.8, 0.92]:
    x, y = curve_off(t, 8, 4)
    b.append(ellipse(x + 4, y, 12 - t * 6, 2, rnd.choice(["#ffb347", "#ff5fa2", "#4ff0e6", "#ffd27a"]), opacity=0.5, filter="url(#soft)"))
for i in range(0, 40, 3):
    x, y = curve_off(i / 40, 13, 7)
    b.append(rect(x, y, 4, 1, "#949bb3", opacity=0.5))
# tiny car (Dolores) with headlights
cx, cy = curve_off(0.38, 6, 6)
b.append(rect(cx, cy + 4, 12, 5, "#2b6e78")); b.append(rect(cx + 2, cy + 2, 7, 3, "#1a3a5a"))
b.append(circle(cx + 12, cy + 7, 1, "#fff0b8", filter="url(#glow)"))
b.append(poly([(cx + 13, cy + 6), (cx + 30, cy + 2), (cx + 32, cy + 10), (cx + 13, cy + 8)], "#fff0b8", opacity=0.25, filter="url(#soft)"))
# near row: rooftops of the buildings on our side of the street
R0, R1, R2 = (-30, 380), (300, 262), (660, 284)
def railpt(t, dy=0):
    x = (1 - t) ** 2 * R0[0] + 2 * (1 - t) * t * R1[0] + t * t * R2[0]
    y = (1 - t) ** 2 * R0[1] + 2 * (1 - t) * t * R1[1] + t * t * R2[1]
    return x, y + dy
nr = [curve_off(i / 40, 24, 12) for i in range(41)]
rl = [railpt(i / 40 * 0.72) for i in range(40, -1, -1)]
b.append(poly([(round(x, 1), round(y, 1)) for x, y in nr + rl], "#1b1630"))
rr3 = random.Random(5)
for i in range(1, 16):
    t = i / 16
    xa, ya = curve_off(t, 24, 12)
    b.append(line(xa, ya, xa - 6, ya + 30, "#0d0b1a", 1.2))                              # party walls
    if rr3.random() < 0.6:
        b.append(rect(xa - 18, ya + 6, 10, 5, rr3.choice(["#ffb347", "#4fc0e8", "#ff9cc6"]), opacity=0.8))   # skylight
        b.append(glow_pool(xa - 13, ya + 8, 12, 6, "#ffb347", 0.3))
    if rr3.random() < 0.4:
        b.append(rect(xa - 8, ya + 12, 8, 6, "#262043"))
    if rr3.random() < 0.12:
        b.append(potted_plant(xa - 24, ya + 18, 0.5, seed=i + 40))
b.append(path("M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in nr), stroke="#463a70", stroke_width=1))
# cap the far end of the street where it meets the hill
b.append(poly([(440, 196), (520, 186), (520, 290), (440, 290)], "#1b1630"))
b.append(windows(448, 204, 3, 4, 6, 7, 10, 9, seed=71, lit=0.5))
b.append(rect(440, 196, 80, 1.5, "#463a70"))
# lantern strings across the street
for t in (0.16, 0.42, 0.66, 0.86):
    xa, ya = curve(t)
    b.append(string_lights(xa - 4, ya - 22, xa + 4, ya + 26, 4, 6, colors=("#ffb347", "#e04a3a", "#ffd27a"), r=1.1, seed=int(t * 10)))

# elevated rail beam along the near side, with a lit train
b.append(path(f"M{R0[0]},{R0[1]} Q{R1[0]},{R1[1]} {R2[0]},{R2[1]}", stroke="#1a1d2b", stroke_width=9))
b.append(path(f"M{R0[0]},{R0[1] - 4} Q{R1[0]},{R1[1] - 4} {R2[0]},{R2[1] - 4}", stroke="#6f7896", stroke_width=1.2))
b.append(path(f"M{R0[0]},{R0[1] + 4} Q{R1[0]},{R1[1] + 4} {R2[0]},{R2[1] + 4}", stroke="#ffb347", stroke_width=1, opacity=0.6, stroke_dasharray="3 4"))
for k in range(7):
    x, y = railpt(0.6 + k * 0.03, -9)
    b.append(rect(round(x, 1), round(y, 1), 11, 5, "#a8fff6" if k % 2 else "#4fc0e8"))
x, y = railpt(0.69)
b.append(glow_pool(x, y - 6, 80, 14, "#4fc0e8", 0.4))
for t in (0.15, 0.4, 0.65, 0.9):
    x, y = railpt(t, 4)
    b.append(rect(x - 3, y, 6, 40, "#1a1d2b"))

# fill beneath the rail (back walls far below, a few lit windows)
ub = [railpt(i / 40) for i in range(41)]
b.append(poly([(round(x, 1), round(y + 4, 1)) for x, y in ub] + [(660, H), (-30, H)], "#130f24"))
b.append(windows(20, 330, 30, 2, 4, 4, 16, 6, seed=99, lit=0.25))
# ---- near rooftops along the bottom (we're looking over them)
x = -10
rr2 = random.Random(31)
while x < W:
    w_ = rr2.uniform(50, 90)
    top = rr2.uniform(318, 334)
    b.append(rect(x, top, w_, H - top, "#0d0b1a"))
    b.append(rect(x, top, w_, 2, "#262043"))
    if rr2.random() < 0.6:   # glowing skylight
        sx_ = x + rr2.uniform(8, w_ - 24)
        b.append(rect(sx_, top + 8, 14, 6, rr2.choice(["#ffb347", "#4fc0e8", "#ff9cc6"]), opacity=0.8))
        b.append(glow_pool(sx_ + 7, top + 10, 16, 8, "#ffb347", 0.35))
    if rr2.random() < 0.5:
        b.append(rect(x + 6, top - 8, 10, 8, "#1a1d2b"))           # AC unit
        b.append(circle(x + 11, top - 4, 2.5, "#262043"))
    if rr2.random() < 0.2:
        b.append(potted_plant(x + w_ - 12, top, 0.6, seed=int(x + 300)))
    x += w_
# a cat on the near rooftop edge, watching the street
cx, cy = 380, 322
b.append(ellipse(cx, cy - 4, 6, 4, "#0d0b1a")); b.append(circle(cx + 5, cy - 9, 3.2, "#0d0b1a"))
b.append(poly([(cx + 3, cy - 11), (cx + 4, cy - 15), (cx + 6, cy - 12)], "#0d0b1a"))
b.append(poly([(cx + 6, cy - 12), (cx + 8, cy - 15), (cx + 8.5, cy - 11)], "#0d0b1a"))
b.append(path(f"M{cx - 6},{cy - 3} q-6,4 -2,10", stroke="#0d0b1a", stroke_width=1.6))
b.append(rect(cx - 12, cy, 30, 2, "#262043"))
# laundry line between near roofs
b.append(cable(120, 316, 240, 320, 8, "#262043", 0.7))
for i, c in enumerate(["#ff9cc6", "#fffaf0", "#ffd27a"]):
    b.append(rect(150 + i * 22, 320 + i * 0.8, 7, 9, c, opacity=0.7))

# soft vignette
b.append(rect(0, 0, W, 16, "#0d0b1a", opacity=0.4))

out = svg(W, H, "".join(b), defs)
open(sys.argv[1], "w").write(out)
