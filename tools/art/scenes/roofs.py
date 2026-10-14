"""The Roofs — water tower with Mae's radio shack, June's rig, the seed library.
640x360, figure scale. `--dawn` renders the 6:14am sunrise variant.

  python3 tools/art/scenes/roofs.py art_src/roofs.svg
  python3 tools/art/scenes/roofs.py art_src/roofs_dawn.svg --dawn
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from svg import *
from props import *

DAWN = "--dawn" in sys.argv


def P(night, dawn):
    return dawn if DAWN else night


def NEON(x, y, s, color, size=12, **kw):
    """Neon that is switched off (just painted tube) at dawn."""
    if DAWN:
        return text(x, y, s, "#a08870", size, **kw) + text(x, y, s, color, size, opacity=0.35, **kw)
    return neon(x, y, s, color, size, **kw)


def GLOW(cx, cy, rx, ry, color, op=0.5):
    return "" if DAWN else glow_pool(cx, cy, rx, ry, color, op)


defs = (
    lin_grad("rsky", P([(0, "#0d0b1a"), (0.45, "#262043"), (0.8, "#463a70"), (1, "#b02d6f")],
                       [(0, "#5d4f8c"), (0.3, "#b02d6f"), (0.55, "#ff7a5a"), (0.8, "#ffb347"), (1, "#ffd27a")])) +
    lin_grad("rbay", P([(0, "#1a3a5a"), (1, "#0d0b1a")], [(0, "#ffd27a"), (0.4, "#e0802a"), (1, "#7a1f52")])) +
    lin_grad("rfloor", P([(0, "#2a2f45"), (1, "#1a1d2b")], [(0, "#7d6450"), (1, "#4a1538")])) +
    lin_grad("tank", P([(0, "#3a2a22"), (0.5, "#5a4334"), (1, "#3a2a22")], [(0, "#5a4334"), (0.6, "#a08870"), (1, "#e0802a")]), 0, 0, 1, 0) +
    lin_grad("sunray", [(0, "#fff0b8", 0.7), (1, "#fff0b8", 0)], 0, 0, 0, 1)
)

HORIZON = 196
BACK = 262        # back parapet base / far edge of the roof floor
b = []

# ---- sky
b.append(rect(0, 0, W, H, "url(#rsky)"))
if not DAWN:
    b.append(stars(90, 23, 150))
    b.append(glow_pool(380, 190, 300, 50, "#b02d6f", 0.45))
else:
    b.append(stars(12, 23, 40, "#fff0b8"))
    # sun breaking over the bay, behind the far city
    b.append(glow_pool(436, 196, 220, 70, "#ffb347", 0.45))
    b.append(glow_pool(436, 190, 70, 40, "#fff0b8", 0.7))
    for a in range(-70, 71, 14):
        x2 = 436 + math.sin(math.radians(a)) * 420
        y2 = 188 - math.cos(math.radians(a)) * 300
        b.append(poly([(436, 188), (x2 - 14, y2), (x2 + 14, y2)], "#fff0b8", opacity=0.12, filter="url(#soft)"))
    b.append(circle(436, 186, 34, "#fff0b8", opacity=0.6, filter="url(#soft)"))
    b.append(circle(436, 186, 24, "#fff0b8"))
    b.append(circle(436, 186, 20, "#fffaf0"))
    # soft clouds lit from below
    for cx, cy, rx in [(120, 70, 70), (240, 46, 50), (540, 64, 80), (600, 110, 40), (300, 120, 60)]:
        b.append(ellipse(cx, cy, rx, 7, "#ff9cc6", opacity=0.7))
        b.append(ellipse(cx + 6, cy + 3, rx * 0.8, 3, "#fff0b8", opacity=0.8))
    for i, (bx_, by_, s_) in enumerate([(300, 90, 1.2), (318, 84, 1.0), (334, 94, 0.9), (350, 80, 1.1), (520, 120, 0.8), (534, 116, 0.7), (150, 130, 0.9)]):
        b.append(bird(bx_, by_, s_, "#4a1538"))

# ---- the bay & the far city with the Kestrel tower
b.append(rect(0, HORIZON, W, 80, "url(#rbay)"))
rnd = random.Random(3)
for i in range(60):
    x = rnd.uniform(0, W)
    y = HORIZON + 2 + rnd.uniform(0, 50)
    b.append(rect(x, y, rnd.uniform(4, 20), 1, P(rnd.choice(["#ffb347", "#ff5fa2", "#4fc0e8"]), "#fffaf0"),
                  opacity=round(P(0.45, 0.6) * rnd.uniform(0.5, 1), 2)))
if DAWN:   # sun glitter path on the water
    for i in range(60):
        t = rnd.random()
        y = HORIZON + 3 + t * 60
        spread = 8 + t * 50
        b.append(rect(round(436 + rnd.uniform(-spread, spread), 1), round(y, 1), rnd.uniform(3, 9), 1, "#fffaf0",
                      opacity=round(0.9 - t * 0.5, 2)))
x = 0
while x < W:
    w_ = rnd.uniform(10, 26)
    h_ = rnd.uniform(10, 46)
    if 360 < x < 400 or (DAWN and 405 < x < 470):
        h_ *= 0.35
    b.append(rect(x, HORIZON - h_, w_, h_, P("#262043", "#7a1f52")))
    if not DAWN:
        for wy in range(int(HORIZON - h_ + 3), HORIZON - 1, 4):
            for wx in range(int(x + 2), int(x + w_ - 2), 4):
                if rnd.random() < 0.3:
                    b.append(rect(wx, wy, 2, 1.5, rnd.choice(["#7d6fae", "#ffb347", "#4fc0e8"]), opacity=0.7))
    x += w_ + rnd.uniform(0, 2)
# Kestrel tower
KX = 382
b.append(poly([(KX - 9, HORIZON), (KX - 4, 52), (KX, 40), (KX + 4, 52), (KX + 9, HORIZON)], P("#332a57", "#7a1f52")))
b.append(poly([(KX, 40), (KX + 4, 52), (KX + 9, HORIZON), (KX + 2, HORIZON)], P("#262043", "#4a1538")))
b.append(line(KX, 40, KX, 22, P("#7d6fae", "#4a1538"), 0.8))
if not DAWN:
    b.append(glow_pool(KX, 50, 50, 40, "#2f8fc0", 0.55))
    b.append(rect(KX - 4, 48, 8, 3, "#a8fff6", filter="url(#glow)"))
    b.append(circle(KX, 22, 1.4, "#4ff0e6", filter="url(#glow)"))
    for yy in range(60, HORIZON, 8):
        b.append(rect(KX - 2, yy, 4, 1.4, "#2f8fc0", opacity=0.9))
    b.append(rect(KX - 30, HORIZON + 4, 60, 30, "#4fc0e8", opacity=0.15, filter="url(#soft)"))   # reflection
else:
    b.append(rect(KX - 4, 48, 8, 3, "#4fc0e8", opacity=0.6))
    b.append(line(KX + 5, 56, KX + 9, HORIZON, "#ffd27a", 1, opacity=0.8))   # sun rim

# ---- nearer rooftops just below our level (mid-ground)
for x0, w_, top in [(-10, 70, 236), (230, 60, 242), (440, 50, 238), (600, 60, 240)]:
    b.append(rect(x0, top, w_, 40, P("#1b1630", "#5e2a12")))
    if not DAWN:
        b.append(windows(x0 + 6, top + 6, int(w_ // 12), 2, 6, 6, 6, 6, seed=x0 + 900, lit=0.5))

# ---- back parapet of our roof
b.append(rect(0, BACK - 14, W, 14, P("#3b4260", "#a08870")))
b.append(rect(0, BACK - 14, W, 2, P("#6f7896", "#ffd27a")))
for xx in range(0, W, 22):
    b.append(rect(xx, BACK - 12, 1, 12, P("#2a2f45", "#7d6450")))
# roof floor
b.append(rect(0, BACK, W, H - BACK, "url(#rfloor)"))
for i in range(1, 9):
    yy = BACK + (H - BACK) * (i / 9) ** 1.5
    b.append(line(0, yy, W, yy, P("#1a1d2b", "#5e2a12"), 0.7, opacity=0.5))
# vents and a chimney on the parapet
b.append(rect(286, BACK - 34, 14, 22, P("#2a2f45", "#8a3f16")))
b.append(rect(284, BACK - 36, 18, 3, P("#3b4260", "#a08870")))
b.append(ellipse(293, BACK - 46, 8, 10, "#f6e7c8", opacity=P(0.25, 0.4), filter="url(#soft)"))

# ---- the water tower (left) with Mae's antenna
TX = 104
for lx in (TX - 54, TX - 20, TX + 20, TX + 54):
    b.append(rect(lx - 2, 128, 4, 168 if abs(lx - TX) > 30 else 150, P("#1a1d2b", "#3a2a22")))
b.append(line(TX - 52, 150, TX + 52, 230, P("#1a1d2b", "#3a2a22"), 1.2))
b.append(line(TX + 52, 150, TX - 52, 230, P("#1a1d2b", "#3a2a22"), 1.2))
b.append(rect(TX - 66, 126, 132, 5, P("#2a2f45", "#5a4334")))                  # catwalk
for xx in range(TX - 66, TX + 66, 6):
    b.append(line(xx, 118, xx, 126, P("#2a2f45", "#5a4334"), 0.6))
b.append(line(TX - 66, 118, TX + 66, 118, P("#3b4260", "#7d6450"), 0.8))
b.append(rect(TX - 58, 52, 116, 74, "url(#tank)"))
for i in range(5):
    b.append(rect(TX - 58, 60 + i * 14, 116, 1.5, P("#1a1d2b", "#5e2a12"), opacity=0.8))
for xx in range(TX - 50, TX + 58, 12):
    b.append(rect(xx, 52, 1, 74, P("#1a1d2b", "#5e2a12"), opacity=0.4))
b.append(poly([(TX - 62, 54), (TX, 26), (TX + 62, 54)], P("#2a2f45", "#5a4334")))
b.append(line(TX - 62, 54, TX, 26, P("#525a7a", "#ffd27a"), 0.8))
# painted moon & lettering on the tank
b.append(circle(TX - 26, 86, 13, P("#f6e7c8", "#fff0b8"), opacity=0.8))
b.append(circle(TX - 20, 82, 11, P("#4a3a33", "#7d6450")))
b.append(text(TX + 14, 92, "HALFMOON", P("#c9b49a", "#fff0b8"), 10, opacity=0.8))
# antenna mast from the tank roof
b.append(line(TX + 10, 36, TX + 10, 2, P("#949bb3", "#4a1538"), 1.6))
for yy in range(6, 36, 6):
    b.append(line(TX + 6, yy, TX + 14, yy, P("#949bb3", "#4a1538"), 0.8))
b.append(line(TX + 10, 4, TX - 60, 54, P("#525a7a", "#4a1538"), 0.5))
b.append(line(TX + 10, 4, TX + 80, 60, P("#525a7a", "#4a1538"), 0.5))
b.append(circle(TX + 10, 2, 2, "#ff5fa2", filter="url(#glow)", opacity=P(1, 0.5)))
b.append(GLOW(TX + 10, 4, 14, 12, "#ff5fa2", 0.6))

# ---- Mae's radio shack (at the tower's feet)
SX0, SX1, STOP, SBASE = 128, 252, 160, 302
b.append(rect(SX0, STOP, SX1 - SX0, SBASE - STOP, P("#1f5260", "#2b6e78")))
for xx in range(SX0, SX1, 8):
    b.append(rect(xx, STOP, 1, SBASE - STOP, P("#173a4a", "#1f5260")))         # corrugated
b.append(poly([(SX0 - 8, STOP + 2), (SX1 + 8, STOP - 8), (SX1 + 8, STOP - 2), (SX0 - 8, STOP + 8)], P("#3b4260", "#7d6450")))
# sign on the roof edge
b.append(rect(SX0 + 6, STOP - 26, 110, 20, P("#2a0f24", "#4a1538")))
b.append(rect(SX0 + 6, STOP - 26, 110, 20, "none", stroke=P("#ff5fa2", "#b02d6f"), stroke_width=1,
              filter=None if DAWN else "url(#glow)"))
b.append(NEON(SX0 + 61, STOP - 11, "87.9 HALFMOON FM", "#ff5fa2", 9, textLength=100, lengthAdjust="spacingAndGlyphs"))
b.append(line(SX0 + 20, STOP - 6, SX0 + 20, STOP + 4, "#1a1d2b", 1)); b.append(line(SX0 + 100, STOP - 6, SX0 + 100, STOP, "#1a1d2b", 1))
b.append(GLOW(SX0 + 61, STOP - 14, 70, 20, "#ff5fa2", 0.4))
# window with Mae's desk lamp, a mixing desk, a reel
b.append(rect(SX0 + 10, STOP + 22, 54, 34, "#0d0b1a"))
b.append(rect(SX0 + 12, STOP + 24, 50, 30, P("#ffb347", "#ffd27a"), opacity=P(0.9, 0.5)))
b.append(rect(SX0 + 14, STOP + 44, 46, 10, "#3a2a22"))
for i in range(7):
    b.append(rect(SX0 + 16 + i * 6, STOP + 45, 2, 4 + (i * 3) % 4, "#e6e8ef"))
b.append(circle(SX0 + 50, STOP + 34, 6, "#3a2a22")); b.append(circle(SX0 + 50, STOP + 34, 2, "#c9b49a"))
b.append(rect(SX0 + 12, STOP + 24, 50, 3, "#000", opacity=0.3))
b.append(text(SX0 + 26, STOP + 36, "ON AIR", P("#e04a3a", "#7a1a1e"), 5, filter=None if DAWN else "url(#glow)"))
b.append(GLOW(SX0 + 37, STOP + 40, 50, 30, "#ffb347", 0.45))
# door, ajar, warm light
b.append(rect(SX0 + 76, STOP + 28, 34, SBASE - STOP - 28, "#173a4a"))
b.append(rect(SX0 + 76, STOP + 28, 8, SBASE - STOP - 28, P("#ffd27a", "#ffd27a"), opacity=P(0.85, 0.5)))
b.append(rect(SX0 + 86, STOP + 30, 22, 30, "#fffaf0", opacity=0.08))
# stickers and band posters on the shack
for i, (x_, y_, c) in enumerate([(SX0 + 68, STOP + 70, "#ffd27a"), (SX0 + 70, STOP + 82, "#ff5fa2"), (SX0 + 16, STOP + 66, "#4ff0e6"),
                                 (SX0 + 30, STOP + 72, "#b8de7a"), (SX0 + 112, STOP + 50, "#ff9cc6")]):
    b.append(circle(x_, y_, 3, c))
b.append(rect(SX0 + 40, STOP + 62, 20, 26, P("#f6e7c8", "#fffaf0")))
b.append(circle(SX0 + 50, STOP + 72, 6, "#e04a3a")); b.append(text(SX0 + 50, STOP + 85, "IRIS LIVE", "#3a2a22", 3.4))
# a dish on the shack roof, cables down to the tank

# crates of records
for i, (cx_, cy_) in enumerate([(262, SBASE + 2), (290, SBASE + 4), (274, SBASE - 18)]):
    b.append(rect(cx_, cy_ - 20, 26, 20, P("#7d6450", "#a08870")))
    b.append(rect(cx_, cy_ - 20, 26, 2, P("#a08870", "#c9b49a")))
    b.append(rect(cx_ + 2, cy_ - 11, 22, 1, "#5a4334"))
    for j in range(7):
        b.append(rect(cx_ + 2 + j * 3.3, cy_ - 27 + (j % 3), 2.6, 9, ["#e04a3a", "#1b1630", "#ffd27a", "#2f8fc0", "#fffaf0", "#7a1f52", "#4f8f45"][(i + j) % 7]))
b.append(circle(318, SBASE - 6, 7, "#1b1630")); b.append(circle(318, SBASE - 6, 2.2, "#ffb347"))   # loose record
b.append(GLOW(285, SBASE - 10, 40, 14, "#ffb347", 0.2))

# ---- seed library against the back parapet
LX = 336
b.append(rect(LX, 188, 74, 82, P("#5a4334", "#8a3f16")))
b.append(rect(LX + 3, 191, 68, 76, P("#3a2a22", "#5a4334")))
b.append(poly([(LX - 4, 190), (LX + 37, 176), (LX + 78, 190)], P("#7a1f52", "#b02d6f")))
b.append(rect(LX + 14, 178, 46, 8, P("#fff0b8", "#fffaf0")))
b.append(text(LX + 37, 184.5, "SEED LIBRARY", "#3a2a22", 4.6))
for r, sy in enumerate((212, 236, 260)):
    b.append(rect(LX + 3, sy, 68, 3, P("#7d6450", "#a08870")))
    for j in range(7):
        jx = LX + 6 + j * 9.4
        jc = ["#e0802a", "#b8de7a", "#ffd27a", "#c9b49a", "#ff9cc6", "#7fb85a", "#e04a3a"][(r * 3 + j) % 7]
        b.append(rect(jx, sy - 12, 7, 12, "#d2f0e2", opacity=0.55))
        b.append(rect(jx + 1, sy - 7, 5, 7, jc))
        b.append(rect(jx, sy - 13, 7, 2, "#a08870"))
        b.append(rect(jx + 1, sy - 5, 5, 2, "#fffaf0", opacity=0.8))
# potted seedlings in front of it
for i, (x_, c) in enumerate([(330, "#e04a3a"), (346, "#b85c1c"), (414, "#2f8fc0"), (426, "#e0802a")]):
    b.append(potted_plant(x_, BACK + 10 + (i % 2) * 2, 0.8, pot=c, seed=60 + i))
b.append(rect(392, 262, 14, 10, "#2f8fc0")); b.append(path("M406,264 l8,-2", stroke="#2f8fc0", stroke_width=1.5))  # watering can
b.append(rect(LX + 50, 194, 16, 11, "#fffaf0"))
b.append(text(LX + 58, 199, "take one", "#3a2a22", 2.6, weight="normal"))
b.append(text(LX + 58, 203, "leave one", "#3a2a22", 2.6, weight="normal"))

# ---- divider wall to the next roof
# June's roof is the next building over: a slightly raised deck with a brick lip
JR = 300
b.append(rect(466, BACK, W - 466, JR - BACK, P("#262043", "#8a3f16")))
for i in range(1, 5):
    b.append(line(466, BACK + i * 9, W, BACK + i * 9, P("#1a1d2b", "#5e2a12"), 0.6, opacity=0.6))
b.append(rect(466, JR, W - 466, 12, P("#3b4260", "#a08870")))
for r in range(2):
    for xx in range(466 + r * 6, W, 12):
        b.append(rect(xx, JR + 1 + r * 6, 11, 5, P("#2a2f45", "#8a3f16"), opacity=0.8))
b.append(rect(466, JR, W - 466, 1.5, P("#6f7896", "#ffd27a")))
b.append(rect(462, BACK - 14, 6, JR - BACK + 26, P("#2a2f45", "#7d6450")))
b.append(rect(448, JR - 2, 18, 14, P("#7d6450", "#a08870")))   # crate step up
b.append(rect(448, JR - 2, 18, 2, P("#a08870", "#c9b49a")))
b.append(line(448, JR + 5, 466, JR + 5, "#5a4334", 0.8))

# ---- June's rig on the next roof
JX0, JX1, JTOP, JBASE = 486, 628, 196, 300
b.append(line(JX0 + 4, JBASE, JX0 + 4, JTOP + 10, "#525a7a", 2))
b.append(line(JX1 - 4, JBASE, JX1 - 4, JTOP, "#525a7a", 2))
b.append(poly([(JX0 - 6, JTOP + 14), (JX1 + 4, JTOP - 4), (JX1 + 10, JTOP + 60), (JX0 - 2, JTOP + 64)], P("#1f5f8a", "#2f8fc0")))   # tarp
b.append(poly([(JX0 - 6, JTOP + 14), (JX1 + 4, JTOP - 4), (JX1 + 4, JTOP + 2), (JX0 - 6, JTOP + 20)], P("#2f8fc0", "#4fc0e8"), opacity=0.6))
for k in range(4):
    b.append(line(JX0 + k * 38, JTOP + 14 - k * 5, JX0 + 4 + k * 38, JTOP + 62 - k * 1, P("#1a3a5a", "#1f5f8a"), 0.8))
b.append(line(JX0 - 6, JTOP + 14, JX0 - 20, JBASE, "#0d0b1a", 0.7))   # guy rope
b.append(line(JX1 + 10, JTOP + 60, JX1 + 12, JBASE, "#0d0b1a", 0.7))
# shade under the tarp
b.append(rect(JX0, JTOP + 62, JX1 - JX0, JBASE - JTOP - 62, P("#1a1d2b", "#5e2a12"), opacity=0.6))
# table (a crate) with laptop + monitor glow
b.append(rect(530, 270, 56, 30, P("#5a4334", "#8a3f16")))
b.append(rect(530, 270, 56, 3, P("#7d6450", "#a08870")))
b.append(GLOW(560, 258, 50, 26, "#4ff0e6", 0.55))
b.append(poly([(544, 270), (572, 270), (575, 250), (547, 250)], "#1a1d2b"))
b.append(poly([(546, 268), (570, 268), (573, 252), (549, 252)], P("#4ff0e6", "#63b3a8"), opacity=P(0.95, 0.7)))
for i in range(5):
    b.append(rect(550 + (i % 2), 255 + i * 2.6, 16 - (i * 3) % 7, 1, "#0f1f2b", opacity=0.7))
b.append(rect(540, 270, 36, 2, "#2a2f45"))
b.append(rect(578, 258, 6, 12, "#1a1d2b")); b.append(circle(581, 261, 1, "#b8de7a"))   # router
# battery packs and cables
for i in range(4):
    bx_ = 500 + i * 9
    b.append(rect(bx_, 288 - (i % 2) * 8, 8, 12, P("#262043", "#3b4260")))
    b.append(rect(bx_ + 1, 290 - (i % 2) * 8, 6, 1.5, ["#b8de7a", "#b8de7a", "#ffd27a", "#e04a3a"][i]))
b.append(path("M508,292 q20,10 34,-22", stroke="#0d0b1a", stroke_width=1.2))
b.append(path("M520,300 q30,8 60,-30", stroke="#0d0b1a", stroke_width=1))
b.append(path("M586,284 q20,20 40,10 q10,-4 14,6", stroke="#0d0b1a", stroke_width=1.2))
b.append(path("M590,276 q30,-40 38,-74", stroke="#0d0b1a", stroke_width=0.8))
# frog lantern hanging from the tarp pole
fx, fy = JX1 - 14, JTOP + 30
b.append(line(JX1 - 4, JTOP + 14, fx, fy - 8, "#1a1d2b", 0.8))
b.append(GLOW(fx, fy, 22, 20, "#b8de7a", 0.6))
b.append(ellipse(fx, fy, 8, 6.5, P("#7fb85a", "#4f8f45")))
b.append(circle(fx - 4, fy - 6, 3, P("#b8de7a", "#7fb85a"))); b.append(circle(fx + 4, fy - 6, 3, P("#b8de7a", "#7fb85a")))
b.append(circle(fx - 4, fy - 6, 1.2, "#1a1d2b")); b.append(circle(fx + 4, fy - 6, 1.2, "#1a1d2b"))
b.append(path(f"M{fx - 4},{fy + 1} q4,3 8,0", stroke="#2f6a35", stroke_width=0.8))
b.append(ellipse(fx - 2, fy - 1, 3, 2, "#fff0b8", opacity=P(0.6, 0.2)))
# a beanbag and June's backpack with patches
b.append(ellipse(608, 294, 16, 9, P("#7a1f52", "#b02d6f")))
b.append(rect(492, 270, 14, 16, "#463a70")); b.append(circle(497, 276, 2, "#ffd27a")); b.append(circle(502, 281, 2, "#b8de7a"))

# ---- string lights across the whole roof
b.append(string_lights(TX + 60, 120, 336, 186, 18, 12, seed=0) if not DAWN else cable(TX + 60, 120, 336, 186, 18, "#4a1538", 0.8))
b.append(string_lights(410, 186, JX1 + 4, JTOP - 2, 18, 10, seed=3) if not DAWN else cable(410, 186, JX1 + 4, JTOP - 2, 18, "#4a1538", 0.8))
b.append(string_lights(SX1 + 8, STOP - 6, 440, 228, 26, 12, seed=5) if not DAWN else cable(SX1 + 8, STOP - 6, 440, 228, 26, "#4a1538", 0.8))

# ---- roof hatch + ladder down (front left)
b.append(rect(10, 318, 60, 42, P("#1a1d2b", "#3a1a10")))
b.append(rect(10, 318, 60, 3, P("#525a7a", "#a08870")))
b.append(rect(14, 322, 52, 38, "#0d0b1a"))
b.append(rect(26, 296, 3, 64, P("#949bb3", "#c9b49a"))); b.append(rect(51, 296, 3, 64, P("#949bb3", "#c9b49a")))
b.append(path("M27,296 q0,-10 13,-10 q13,0 13,10", stroke=P("#949bb3", "#c9b49a"), stroke_width=3))
for yy in range(304, 360, 9):
    b.append(rect(29, yy, 22, 2, P("#6f7896", "#a08870")))

# ---- folding chairs set out for the broadcast, a thermos, puddles
def chair(x, y, c):
    return g(line(x - 10, y, x + 7, y - 30, "#525a7a", 1.6), line(x + 10, y, x - 7, y - 30, "#525a7a", 1.6),
             rect(x - 12, y - 30, 24, 4, c), rect(x - 10, y - 54, 20, 14, c), line(x + 9, y - 54, x + 9, y - 28, "#525a7a", 1.4),
             line(x - 9, y - 54, x - 9, y - 28, "#525a7a", 1.4))
b.append(chair(370, 306, P("#e04a3a", "#ff7a5a")))
b.append(chair(404, 310, P("#2f8fc0", "#4fc0e8")))
b.append(rect(420, 296, 6, 12, P("#b02a2a", "#e04a3a"))); b.append(rect(420, 294, 6, 2, "#bec2d1"))
for cx_, cy_, rx in [(220, 336, 44), (500, 344, 30), (340, 326, 26)]:
    b.append(ellipse(cx_, cy_, rx, 4, P("#5d4f8c", "#ffd27a"), opacity=P(0.45, 0.55)))
    b.append(ellipse(cx_, cy_, rx * 0.6, 1.5, P("#a99ad0", "#fffaf0"), opacity=0.4))
if not DAWN:   # neon reflected in puddles
    b.append(ellipse(200, 334, 20, 2, "#ff5fa2", opacity=0.4, filter="url(#soft)"))
    b.append(ellipse(560, 316, 30, 3, "#4ff0e6", opacity=0.3, filter="url(#soft)"))

if DAWN:
    # long warm light from the sun: rim highlights and long shadows toward the viewer
    b.append(rect(0, 0, W, H, "#ffb347", opacity=0.08, style="mix-blend-mode:screen"))
    for x0, x1 in [(TX - 54, TX - 40), (TX + 50, TX + 62), (SX0, SX1), (LX, LX + 74), (JX0, JX1)]:
        b.append(poly([(x0, BACK + 40), (x1, BACK + 40), (x1 - 80, H), (x0 - 80, H)], "#4a1538", opacity=0.22, filter="url(#soft)"))
    b.append(rect(SX1 - 2, STOP, 2, SBASE - STOP, "#ffd27a", opacity=0.8))
    b.append(rect(LX + 72, 188, 2, 82, "#ffd27a", opacity=0.8))
    b.append(rect(TX + 56, 52, 2, 74, "#ffd27a", opacity=0.9))
    b.append(glow_pool(420, 250, 300, 40, "#ffd27a", 0.25))

out = svg(W, H, "".join(b), defs)
open(sys.argv[1], "w").write(out)
