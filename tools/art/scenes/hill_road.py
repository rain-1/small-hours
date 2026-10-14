"""Hill Road overlook, pre-dawn. 640x360, figure scale.

Deep blue sky turning violet at the horizon, the city and bay below, Kestrel
tower across the water, Dolores parked by the guardrail. Ozzie ~x420, feet ~y336.
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from svg import *
from props import *

defs = (
    lin_grad("hsky", [(0, "#0d0b1a"), (0.35, "#1a3a5a"), (0.65, "#463a70"), (0.85, "#7d6fae"), (1, "#b02d6f")]) +
    lin_grad("hbay", [(0, "#463a70"), (0.3, "#1a3a5a"), (1, "#0d0b1a")]) +
    lin_grad("hroad", [(0, "#3b4260"), (1, "#1a1d2b")]) +
    lin_grad("headbeam2", [(0, "#fff0b8", 0.8), (1, "#fff0b8", 0)], 0, 0, 1, 0) +
    '<filter id="beamblur2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>'
)

HORIZON = 176
b = []
b.append(rect(0, 0, W, H, "url(#hsky)"))
b.append(stars(70, 61, 90))
b.append(stars(20, 62, 50, "#fffaf0"))
# the half moon, low and pale
b.append(glow_pool(120, 54, 30, 30, "#d2f0e2", 0.35))
b.append(circle(120, 54, 11, "#f6e7c8"))
b.append(path("M120,43 a11,11 0 0,0 0,22 z", fill="#463a70", opacity=0.85))
# horizon glow (dawn coming)
b.append(glow_pool(520, HORIZON, 260, 40, "#ff9cc6", 0.45))
b.append(glow_pool(520, HORIZON - 4, 120, 16, "#ffd27a", 0.3))
# a few wisps
for cx, cy, rx in [(300, 120, 80), (520, 140, 60), (80, 150, 50)]:
    b.append(ellipse(cx, cy, rx, 3, "#7d6fae", opacity=0.5))

# ---- far shore across the bay, with Kestrel tower
rnd = random.Random(9)
x = 0
while x < W:
    w_ = rnd.uniform(8, 22)
    h_ = rnd.uniform(4, 26)
    if 440 < x < 500:
        h_ = rnd.uniform(14, 34)
    b.append(rect(x, HORIZON - h_, w_, h_ + 2, "#332a57"))
    for wy in range(int(HORIZON - h_ + 2), HORIZON, 3):
        for wx in range(int(x + 1), int(x + w_ - 1), 3):
            if rnd.random() < 0.22:
                b.append(rect(wx, wy, 1, 1, rnd.choice(["#ffd27a", "#a99ad0", "#4fc0e8"]), opacity=0.8))
    x += w_ + rnd.uniform(0, 3)
KX = 470
b.append(glow_pool(KX, 64, 50, 40, "#2f8fc0", 0.55))
b.append(poly([(KX - 7, HORIZON), (KX - 3, 70), (KX, 60), (KX + 3, 70), (KX + 7, HORIZON)], "#463a70"))
b.append(poly([(KX, 60), (KX + 3, 70), (KX + 7, HORIZON), (KX + 1, HORIZON)], "#332a57"))
b.append(line(KX, 60, KX, 44, "#7d6fae", 0.8))
b.append(rect(KX - 3, 66, 6, 2.5, "#a8fff6", filter="url(#glow)"))
b.append(circle(KX, 44, 1.2, "#4ff0e6", filter="url(#glow)"))
for yy in range(76, HORIZON, 7):
    b.append(rect(KX - 1.5, yy, 3, 1.2, "#2f8fc0", opacity=0.9))
# the bay
b.append(rect(0, HORIZON, W, 50, "url(#hbay)"))
for i in range(50):
    b.append(rect(rnd.uniform(0, W), HORIZON + 2 + rnd.uniform(0, 40), rnd.uniform(3, 14), 1,
                  rnd.choice(["#ffb347", "#ff9cc6", "#4fc0e8", "#a99ad0"]), opacity=round(rnd.uniform(0.25, 0.6), 2)))
b.append(rect(KX - 3, HORIZON + 2, 6, 40, "#4fc0e8", opacity=0.25, filter="url(#soft)"))
# a ferry with lights
b.append(rect(220, HORIZON + 18, 26, 4, "#1b1630")); b.append(rect(226, HORIZON + 14, 12, 4, "#1b1630"))
for i in range(5):
    b.append(rect(222 + i * 5, HORIZON + 19, 2, 1.5, "#ffd27a"))

# ---- the city below the hill: dense lights, the rail line, Halfmoon's crescent
for layer, (y0, y1, dens, sz, col) in enumerate([(HORIZON + 30, HORIZON + 70, 0.5, 2, "#1b1630"),
                                                  (HORIZON + 50, 290, 0.45, 3, "#0d0b1a")]):
    x = -10
    while x < W:
        w_ = rnd.uniform(14, 36) * (1 + layer * 0.4)
        top = rnd.uniform(y0, y0 + 30)
        b.append(rect(x, top, w_, 300 - top, col))
        b.append(rect(x, top, w_, 1, "#332a57"))
        for wy in range(int(top + 2), 290, sz + 2):
            for wx in range(int(x + 1), int(x + w_ - 1), sz + 2):
                if rnd.random() < dens * 0.5:
                    b.append(rect(wx, wy, sz - 1 if sz > 2 else 1, sz - 1 if sz > 2 else 1,
                                  rnd.choice(["#ffb347", "#ffd27a", "#4fc0e8", "#ff9cc6", "#7d6fae", "#ffb347"]), opacity=0.85))
        x += w_ + rnd.uniform(0, 2)
# elevated rail curving through, a train of lights
b.append(path("M-10,236 Q200,218 360,232 T660,226", stroke="#1a1d2b", stroke_width=4))
b.append(path("M-10,234 Q200,216 360,230 T660,224", stroke="#ffb347", stroke_width=0.6, opacity=0.6, stroke_dasharray="2 3"))
for i in range(5):
    b.append(rect(300 + i * 11, 227, 9, 3.5, "#a8fff6", opacity=0.9))
b.append(glow_pool(328, 229, 40, 8, "#4fc0e8", 0.45))
# Halfmoon Street: a warm crescent of lanterns climbing the hill, its water tower
b.append(path("M90,268 Q150,236 230,250", stroke="#ffb347", stroke_width=2, opacity=0.8, stroke_dasharray="1.5 2.5", filter="url(#glow)"))
b.append(glow_pool(160, 252, 70, 14, "#ffb347", 0.35))
b.append(rect(214, 236, 8, 6, "#3a2a22")); b.append(line(215, 242, 215, 248, "#3a2a22", 1)); b.append(line(221, 242, 221, 248, "#3a2a22", 1))
b.append(circle(218, 233, 1, "#ff5fa2", filter="url(#glow)"))
# a murmuration of starling drones over the city
for i in range(26):
    a = i * 0.5
    b.append(rect(round(380 + math.cos(a) * (20 + i), 1), round(200 + math.sin(a * 1.3) * 8 + i * 0.3, 1), 1, 1, "#4ff0e6", opacity=0.8))

# ---- hillside scrub between road and city
b.append(path("M0,282 Q120,268 260,276 T640,272 L640,300 L0,300 Z", fill="#0f1f2b"))
for i in range(40):
    gx = rnd.uniform(0, W)
    b.append(path(f"M{gx:.1f},{290} q1,-6 {rnd.uniform(-3, 3):.1f},-10", stroke="#173a4a", stroke_width=1))

# ---- the guardrail (W-beam on posts)
RY = 262
for x in range(10, W, 46):
    b.append(rect(x, RY + 2, 5, 34, "#525a7a"))
    b.append(rect(x, RY + 2, 1.5, 34, "#949bb3", opacity=0.6))
b.append(rect(0, RY, W, 12, "#949bb3"))
b.append(rect(0, RY + 3, W, 2, "#bec2d1"))
b.append(rect(0, RY + 8, W, 2, "#6f7896"))
b.append(rect(0, RY + 11, W, 1, "#3b4260"))
for x in range(30, W, 92):
    b.append(rect(x, RY + 4, 6, 3, "#ffb347"))          # reflectors
# stickers / a ribbon tied on the rail, wildflowers
b.append(path("M520,262 l-4,14 M524,262 l4,13", stroke="#ff5fa2", stroke_width=1.5))
b.append(rect(518, 260, 8, 4, "#ff5fa2"))
for i in range(18):
    fx = rnd.uniform(330, 640)
    b.append(line(fx, 300, fx + rnd.uniform(-2, 2), 286, "#2f6a35", 0.8))
    b.append(circle(round(fx, 1), 286, 1.4, rnd.choice(["#ffd27a", "#fffaf0", "#ff9cc6"])))
# overlook sign
b.append(rect(600, 196, 3, 104, "#525a7a"))
b.append(rect(574, 196, 56, 22, "#1f4a2a")); b.append(rect(576, 198, 52, 18, "none", stroke="#fffaf0", stroke_width=0.8))
b.append(text(602, 206, "HILL RD", "#fffaf0", 6)); b.append(text(602, 213, "OVERLOOK", "#fffaf0", 4.5))

# ---- road
b.append(rect(0, 300, W, H - 300, "url(#hroad)"))
b.append(rect(0, 300, W, 2, "#525a7a"))
for x in range(0, W, 60):
    b.append(rect(x + 10, 346, 30, 2, "#ffd27a", opacity=0.5))
b.append(ellipse(470, 330, 60, 4, "#7d6fae", opacity=0.3))     # damp patch reflecting the sky
b.append(ellipse(470, 330, 30, 1.5, "#b02d6f", opacity=0.3))

# ---- Dolores — the same teal 2009 hatchback as on the street, at figure scale (x2)
car = []
car.append(ellipse(84, 330, 72, 6, "#000", opacity=0.5))
car.append(path("M20,322 L22,300 Q28,292 44,290 L62,274 Q70,268 84,268 L118,268 Q130,268 136,280 L146,294 Q152,298 152,306 L152,322 Z", "#2b6e78"))
car.append(path("M22,306 L152,306 L152,322 L20,322 Z", "#1f5260"))
car.append(path("M66,277 Q72,272 84,272 L112,272 Q120,272 124,280 L130,290 L60,290 Z", "#1a3a5a"))
car.append(path("M68,278 L92,274 L92,288 L64,288 Z", "#63b3a8", opacity=0.5))
car.append(path("M100,276 L114,275 Q119,276 122,282 L126,288 L100,288 Z", "#7d6fae", opacity=0.35))   # sky in the windscreen
car.append(line(96, 272, 96, 290, "#1f5260", 2))
car.append(path("M24,298 Q60,292 150,298", stroke="#9bd6c4", stroke_width=0.6, opacity=0.6))           # body crease highlight
car.append(rect(40, 296, 14, 2, "#9bd6c4"))  # door handle
car.append(circle(50, 322, 10, "#0d0b1a")); car.append(circle(50, 322, 4, "#6f7896"))
car.append(circle(124, 322, 10, "#0d0b1a")); car.append(circle(124, 322, 4, "#6f7896"))
car.append(rect(144, 298, 8, 6, "#fff0b8"))                         # headlight
car.append(rect(20, 300, 4, 6, "#e04a3a"))                           # tail light
car.append(rect(146, 308, 5, 2, "#ffb347"))                          # amber parking light
car.append(rect(98, 286, 22, 3, "#4fc0e8", opacity=0.5))             # dash glow
car.append(rect(60, 280, 3, 4, "#ffd27a"))                           # pine-tree air freshener
car.append(rect(30, 312, 18, 5, "#fffaf0")); car.append(text(39, 316, "DLRS", "#1a3a5a", 3.5))   # plate
car.append(rect(22, 304, 10, 3, "#ff5fa2", opacity=0.8))             # old bumper sticker
car.append(line(30, 292, 24, 276, "#525a7a", 0.6))                 # bent antenna
b.append(f'<g transform="translate(-6,-326) scale(2)">' + "".join(car) + "</g>")
b.append(glow_pool(294, 276, 20, 12, "#fff0b8", 0.6))
b.append(f'<g filter="url(#beamblur2)" style="mix-blend-mode:screen">' +
         poly([(298, 272), (430, 258), (446, 320), (298, 286)], "url(#headbeam2)", opacity=0.55) + "</g>")
b.append(ellipse(18, 304, 16, 6, "#bec2d1", opacity=0.3, filter="url(#soft)"))   # exhaust in the cold
b.append(ellipse(6, 296, 12, 8, "#bec2d1", opacity=0.2, filter="url(#soft)"))
# a thermos and a folded flat cap on the bonnet
b.append(rect(172, 196, 7, 14, "#b02a2a")); b.append(rect(172, 194, 7, 2, "#bec2d1"))
b.append(ellipse(204, 208, 10, 3, "#5a4334")); b.append(rect(196, 204, 14, 3, "#5a4334"))

out = svg(W, H, "".join(b), defs)
open(sys.argv[1], "w").write(out)
