"""Halfmoon Street — the hub. 640x360."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from svg import *

defs = (
    lin_grad("sky", [(0, "#0d0b1a"), (0.55, "#262043"), (1, "#7a1f52")]) +
    lin_grad("road", [(0, "#2a2f45"), (1, "#0d0b1a")]) +
    lin_grad("shopglow", [(0, "#ffd27a"), (1, "#e0802a")]) +
    lin_grad("beam", [(0, "#3b4260"), (1, "#1a1d2b")]) +
    lin_grad("headbeam", [(0, "#fff0b8", 0.9), (1, "#fff0b8", 0)], 0, 0, 1, 0) +
    '<filter id="beamblur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>' +
    lin_grad("steam", [(0, "#f6e7c8", 0), (0.5, "#f6e7c8", 0.5), (1, "#f6e7c8", 0)], 0, 0, 1, 0)
)

GROUND = 268  # base of building facades / sidewalk top

b = []
# --- sky & distant city
b.append(rect(0, 0, W, H, "url(#sky)"))
b.append(stars(70, 3, 120))
b.append(glow_pool(470, 200, 260, 70, "#b02d6f", 0.5))
# distant towers
for x, w_, h_ in [(160, 30, 140), (200, 22, 110), (240, 40, 170), (300, 26, 120), (350, 34, 150), (520, 38, 130), (600, 30, 115)]:
    b.append(rect(x, 230 - h_, w_, h_ + 40, "#262043"))
    b.append(windows(x + 4, 240 - h_, max(1, w_ // 9), h_ // 12, 3, 4, 5, 8, seed=x, lit=0.3, colors=("#5d4f8c", "#7d6fae", "#4fc0e8")))
# Kestrel tower — distant slim silhouette in the sky gap over the pharmacy,
# with a slow blue crown light (engine may pulse it; painted at mid-glow).
b.append(glow_pool(428, 52, 46, 34, "#2f8fc0", 0.45))
b.append(poly([(419, 230), (424, 58), (427, 46), (429, 46), (432, 58), (437, 230)], "#463a70"))
b.append(poly([(428, 46), (432, 58), (437, 230), (430, 230)], "#332a57"))   # shaded flank
b.append(line(424, 60, 419, 230, "#7d6fae", 0.8, opacity=0.8))              # rim light
b.append(line(428, 46, 428, 33, "#7d6fae", 0.8))                            # mast
b.append(rect(424, 52, 8, 3, "#a8fff6", filter="url(#glow)"))               # crown band
b.append(rect(423, 55, 10, 1, "#4fc0e8"))
b.append(circle(428, 33, 1.3, "#4ff0e6", filter="url(#glow)"))
for yy in range(64, 104, 7):
    b.append(rect(425, yy, 6, 1.4, "#2f8fc0", opacity=0.9))

# --- buildings (mid layer)
def facade(x, y, w_, color, trim):
    return rect(x, y, w_, GROUND - y, color) + rect(x, y, w_, 4, trim) + rect(x, y + 4, w_, 2, "#000", opacity=0.25)

# Laundromat (Teo upstairs)  x 0..122
b.append(facade(0, 92, 122, "#332a57", "#463a70"))
b.append(windows(10, 108, 4, 2, 18, 22, 10, 14, seed=11, lit=0.5, frame="#262043"))
# Teo's window (monitor glow) — upper right of laundromat
b.append(rect(88, 170, 26, 28, "#1f5f8a"))
b.append(rect(90, 172, 22, 24, "#4fc0e8", opacity=0.85))
b.append(rect(94, 182, 14, 9, "#1a3a5a"))
b.append(rect(90, 172, 6, 24, "#14301e", opacity=0.6))  # plant silhouette
b.append(glow_pool(100, 184, 30, 22, "#4fc0e8", 0.35))
# laundromat ground floor
b.append(rect(6, 214, 110, 54, "#1a3a5a"))
b.append(rect(8, 216, 106, 50, "#9bd6c4", opacity=0.55))
for i in range(4):
    cx = 22 + i * 26
    b.append(rect(cx - 10, 236, 20, 30, "#e6e8ef"))
    b.append(circle(cx, 250, 7, "#1f5260"))
    b.append(circle(cx, 250, 5, "#63b3a8"))
b.append(rect(6, 204, 110, 10, "#173a4a"))
b.append(neon(61, 212, "SUDS &amp; STARS", "#4ff0e6", 9))
b.append(glow_pool(60, 240, 70, 30, "#9bd6c4", 0.35))

# Alley gap x 122..152
b.append(rect(122, 120, 30, GROUND - 120, "#0d0b1a"))
b.append(rect(126, 200, 22, 68, "#1a1d2b"))
b.append(rect(122, 120, 3, GROUND - 120, "#262043"))
b.append(ellipse(137, 240, 14, 30, "url(#steam)", opacity=0.5, filter="url(#soft)"))
b.append(rect(130, 150, 14, 8, "#2a0f24"))
b.append(neon(137, 157, "↓", "#ff5fa2", 8))

# Halfmoon Noodle x 152..338
b.append(facade(152, 78, 186, "#4a1538", "#7a1f52"))
b.append(windows(166, 96, 6, 2, 18, 20, 11, 14, seed=21, lit=0.55, frame="#2a0f24"))
# sign board
b.append(rect(160, 160, 170, 26, "#2a0f24"))
b.append(rect(160, 160, 170, 26, "none", stroke="#ffb347", stroke_width=1.5, filter="url(#glow)"))
b.append(neon(256, 178, "HALFMOON NOODLE", "#ffb347", 12.5))
# half-moon logo, clear of the lettering
b.append(circle(175, 173, 7, "#ffd27a", filter="url(#glow)"))
b.append(circle(178.5, 170.5, 6, "#2a0f24"))
# awning
b.append(poly([(160, 190), (330, 190), (338, 202), (152, 202)], "#b02a2a"))
for i in range(9):
    b.append(rect(158 + i * 20, 190, 10, 12, "#e04a3a"))
# shop window + door
b.append(rect(160, 202, 170, 66, "#3a1a10"))
b.append(rect(164, 206, 104, 58, "url(#shopglow)"))
b.append(glow_pool(220, 236, 120, 50, "#ffb347", 0.6))
# interior silhouettes: counter, Lu, steam
b.append(rect(164, 244, 104, 20, "#8a3f16"))
b.append(rect(164, 242, 104, 3, "#b85c1c"))
b.append(ellipse(200, 232, 8, 10, "#5e2a12"))      # Lu's head
b.append(rect(192, 238, 16, 8, "#5e2a12"))
b.append(ellipse(240, 222, 20, 26, "#fff0b8", opacity=0.5, filter="url(#soft)"))  # steam
b.append(rect(222, 226, 24, 3, "#5e2a12", opacity=0.7))  # ticket rail
for i in range(4):
    b.append(rect(224 + i * 5, 229, 3, 6, "#fffaf0", opacity=0.85))
# OPEN ALL NIGHT — neon plaque hanging in the window
b.append(line(178, 206, 178, 209, "#3a1a10", 1)); b.append(line(254, 206, 254, 209, "#3a1a10", 1))
b.append(rect(170, 209, 92, 14, "#2a0f24"))
b.append(rect(170, 209, 92, 14, "none", stroke="#ff5fa2", stroke_width=1, filter="url(#glow)"))
b.append(neon(216, 220, "OPEN ALL NIGHT", "#ff5fa2", 9, textLength=84, lengthAdjust="spacingAndGlyphs"))
# noren door
b.append(rect(274, 206, 52, 62, "#1a1d2b"))
b.append(rect(276, 208, 48, 60, "#ffd27a", opacity=0.75))
for i in range(3):
    b.append(rect(276 + i * 16, 206, 15, 26, "#1f4a2a"))
    b.append(rect(276 + i * 16, 230, 15, 2, "#14301e"))
b.append(text(300, 223, "麺", "#f6e7c8", 12, family="IPAexGothic"))
# lanterns
b.append(lantern(166, 200))
b.append(lantern(332, 200))

# Pharmacy + Hotline x 338..470
b.append(facade(338, 104, 132, "#263b4a" if False else "#1f5260", "#2b6e78"))
b.append(windows(348, 122, 4, 1, 22, 20, 9, 14, seed=31, lit=0.3, frame="#173a4a"))
# hotline window (pink, warm)
b.append(rect(352, 160, 104, 34, "#2a0f24"))
b.append(rect(355, 163, 98, 28, "#ffb347", opacity=0.85))
b.append(rect(355, 163, 98, 28, "#ff9cc6", opacity=0.35))
for i, x in enumerate((368, 404, 440)):
    b.append(ellipse(x, 184, 6, 7, "#4a1538"))  # operators' heads
    b.append(rect(x - 8, 189, 16, 4, "#4a1538"))
b.append(glow_pool(404, 178, 70, 30, "#ff9cc6", 0.45))
b.append(rect(360, 144, 88, 13, "#2a0f24"))
b.append(neon(404, 154, "HUMANS ONLY HOTLINE", "#ff5fa2", 7.5))
# pharmacy ground floor, closed shutter
b.append(rect(344, 210, 120, 58, "#2a2f45"))
for yy in range(212, 266, 4):
    b.append(rect(344, yy, 120, 2, "#3b4260"))
# half-finished mural on the shutter: a big sun rising over the bay
mural = []
mural.append(f'<clipPath id="shut"><rect x="344" y="210" width="120" height="58"/></clipPath>')
mural.append('<g clip-path="url(#shut)">')
mural.append(rect(344, 210, 84, 58, "#7a1f52", opacity=0.75))          # painted dusk sky (left part done)
mural.append(rect(344, 232, 84, 14, "#e0802a", opacity=0.7))
for i, rr in enumerate((40, 32, 24)):                                    # sun rings, partly painted
    mural.append(circle(396, 254, rr, ["#e0802a", "#ffb347", "#ffd27a"][i], opacity=0.85))
mural.append(circle(396, 254, 16, "#fff0b8"))
for a in range(-80, 81, 20):                                             # rays
    import math
    x2, y2 = 396 + math.sin(math.radians(a)) * 58, 254 - math.cos(math.radians(a)) * 58
    mural.append(line(396 + math.sin(math.radians(a)) * 44, 254 - math.cos(math.radians(a)) * 44, x2, y2,
                      "#ffd27a", 2.5, opacity=0.8 if a < 30 else 0))
mural.append(path("M396,254 m-40,0 a40,40 0 0,1 68,-28", stroke="#ffd27a", stroke_width=0.8, opacity=0.8))
mural.append(path("M436,254 a40,40 0 0,0 -12,-28", stroke="#fffaf0", stroke_width=0.8, stroke_dasharray="2 2", opacity=0.7))  # chalk outline, unpainted
# bay waves (left painted, right just chalk)
mural.append(rect(344, 252, 70, 16, "#1f5f8a", opacity=0.9))
for i in range(4):
    mural.append(path(f"M{344 + (i % 2) * 6},{256 + i * 3.5} q6,-3 12,0 t12,0 t12,0 t12,0 t12,0", stroke="#4fc0e8", stroke_width=1))
mural.append(path("M414,258 q6,-3 12,0 t12,0 t12,0 t12,0", stroke="#fffaf0", stroke_width=0.7, stroke_dasharray="2 2", opacity=0.6))
mural.append(line(414, 252, 414, 268, "#fffaf0", 0.6, opacity=0.4))
mural.append(path("M372,246 l0,6 M381,246 l0,5 M352,240 l0,4", stroke="#e0802a", stroke_width=1))   # drips
mural.append(rect(428, 216, 30, 3, "#c9b49a", opacity=0.9))              # masking tape
mural.append(rect(441, 212, 3, 14, "#c9b49a", opacity=0.9))
mural.append('</g>')
for yy in range(212, 266, 4):
    mural.append(rect(344, yy + 1.5, 120, 0.8, "#1a1d2b", opacity=0.5))  # slats show through paint
b.append("".join(mural))
b.append(rect(390, 196, 28, 12, "#14301e"))
b.append(neon(404, 206, "+", "#4f8f45", 12))

# Night Clinic x 470..566
b.append(facade(470, 120, 96, "#e6e8ef", "#bec2d1"))
b.append(rect(470, 120, 96, GROUND - 120, "#262043", opacity=0.55))
b.append(windows(480, 136, 3, 2, 20, 18, 9, 12, seed=41, lit=0.7, colors=("#d2f0e2", "#9bd6c4")))
b.append(rect(482, 204, 72, 64, "#173a4a"))
b.append(rect(486, 208, 64, 60, "#d2f0e2", opacity=0.8))
b.append(rect(512, 216, 12, 52, "#63b3a8", opacity=0.6))  # door gap
b.append(glow_pool(518, 238, 60, 34, "#9bd6c4", 0.45))
b.append(rect(492, 190, 52, 12, "#0f1f2b"))
b.append(neon(518, 199, "NIGHT CLINIC", "#4ff0e6", 7))
b.append(neon(556, 186, "✚", "#4ff0e6", 14))

# Stairs going up the hill x 566..640
b.append(poly([(566, GROUND), (640, 150), (640, GROUND)], "#1a1d2b"))
for i in range(14):
    sx = 566 + i * 5.3
    sy = GROUND - i * 8.5
    b.append(rect(sx, sy - 3, 80, 3, "#3b4260"))
b.append(line(570, GROUND - 22, 640, 150 - 22, "#6f7896", 1.5))
b.append(line(576, GROUND, 576, GROUND - 26, "#6f7896", 1))
b.append(line(608, GROUND - 52, 608, GROUND - 76, "#6f7896", 1))
b.append(rect(626, 118, 3, 40, "#525a7a"))  # lamp post
b.append(circle(627, 116, 4, "#ffd27a", filter="url(#glow)"))
b.append(glow_pool(627, 130, 30, 40, "#ffd27a", 0.4))
# water tower on the hill roof (Mae)
b.append(rect(590, 52, 4, 40, "#1a1d2b"))
b.append(rect(620, 52, 4, 40, "#1a1d2b"))
b.append(poly([(584, 34), (630, 34), (634, 56), (580, 56)], "#3a2a22"))
b.append(poly([(584, 34), (607, 22), (630, 34)], "#2a2f45"))
b.append(circle(607, 18, 2, "#ff5fa2", filter="url(#glow)"))
b.append(line(607, 20, 607, 8, "#525a7a"))
b.append(neon(607, 48, "87.9", "#ff5fa2", 8))
b.append(rect(566, 92, 74, 60, "#262043"))

# --- elevated rail beam (foreground top)
b.append(rect(0, 0, W, 26, "url(#beam)"))
b.append(rect(0, 26, W, 4, "#0d0b1a"))
for xx in range(0, W, 40):
    b.append(rect(xx, 4, 2, 20, "#1a1d2b"))
b.append(rect(130, 30, 14, 90, "#2a2f45"))   # pillar into alley gap
b.append(rect(128, 30, 2, 90, "#3b4260"))
for xx in range(4, W, 22):
    b.append(rect(xx, 26, 8, 2, "#ffb347", opacity=0.5))  # under-beam lights
b.append(glow_pool(320, 30, 330, 14, "#ffb347", 0.15))

# --- sidewalk & road
b.append(rect(0, GROUND, W, 14, "#3b4260"))
b.append(rect(0, GROUND, W, 2, "#6f7896"))
b.append(rect(0, GROUND + 14, W, H - GROUND - 14, "url(#road)"))
b.append(rect(0, GROUND + 14, W, 2, "#1a1d2b"))
# reflections of the bright facades in the wet road
refl = "".join([
    rect(164, 206, 104, 58, "#ffb347"), rect(355, 163, 98, 28, "#ff9cc6"),
    rect(486, 208, 64, 60, "#9bd6c4"), rect(8, 216, 106, 50, "#9bd6c4"),
    rect(170, 160, 150, 26, "#ffb347"), rect(90, 172, 22, 24, "#4fc0e8"),
    path("M362,254 a34,34 0 0,1 68,0 Z", "#ffb347"), rect(460, 219, 11, 18, "#4ff0e6")])
b.append(f'<g transform="translate(0,{2 * (GROUND + 16)}) scale(1,-1)" opacity="0.28" filter="url(#soft)">{refl}</g>')
# lane markings broken by puddles
for xx in range(10, W, 70):
    b.append(rect(xx, 326, 34, 3, "#949bb3", opacity=0.4))
for cx, cy, rx in [(250, 304, 50), (470, 318, 40), (90, 340, 36), (590, 300, 30)]:
    b.append(ellipse(cx, cy, rx, 5, "#5d4f8c", opacity=0.35))
    b.append(ellipse(cx, cy, rx * 0.7, 2.5, "#a99ad0", opacity=0.25))

# --- foreground props
# Ozzie's car "Dolores": teal 2009 hatchback, headlights on, facing right, parked x 18..150
car = []
car.append(ellipse(84, 330, 70, 6, "#000", opacity=0.45))
car.append(path("M20,322 L22,300 Q28,292 44,290 L62,274 Q70,268 84,268 L118,268 Q130,268 136,280 L146,294 Q152,298 152,306 L152,322 Z", "#2b6e78"))
car.append(path("M22,306 L152,306 L152,322 L20,322 Z", "#1f5260"))
car.append(path("M66,277 Q72,272 84,272 L112,272 Q120,272 124,280 L130,290 L60,290 Z", "#1a3a5a"))
car.append(path("M68,278 L92,274 L92,288 L64,288 Z", "#63b3a8", opacity=0.5))
car.append(line(96, 272, 96, 290, "#1f5260", 2))
car.append(rect(40, 296, 14, 2, "#9bd6c4"))  # door handle
car.append(circle(50, 322, 10, "#0d0b1a")); car.append(circle(50, 322, 4, "#6f7896"))
car.append(circle(124, 322, 10, "#0d0b1a")); car.append(circle(124, 322, 4, "#6f7896"))
car.append(rect(144, 298, 8, 6, "#fff0b8", filter="url(#glow)"))   # headlight
car.append(f'<g filter="url(#beamblur)" style="mix-blend-mode:screen">' +
           poly([(150, 298), (250, 284), (262, 318), (150, 305)], "url(#headbeam)", opacity=0.85) + '</g>')
car.append(rect(20, 300, 4, 6, "#e04a3a", filter="url(#glow)"))    # tail light
car.append(ellipse(8, 316, 10, 4, "#bec2d1", opacity=0.35, filter="url(#soft)"))  # exhaust
car.append(ellipse(80, 283, 5, 6, "#4e2c1e"))                         # Ozzie silhouette
car.append(rect(74, 278, 12, 3, "#3a2a22"))                           # flat cap
b.append(g(*car))
# vending machine x 340..368 on sidewalk
b.append(rect(340, 222, 28, 48, "#1f5f8a"))
b.append(rect(343, 226, 22, 26, "#a8fff6", opacity=0.85))
for r_ in range(3):
    for c_ in range(3):
        b.append(rect(345 + c_ * 7, 228 + r_ * 8, 5, 6, ["#e04a3a", "#ffb347", "#4f8f45"][(r_ + c_) % 3]))
b.append(rect(345, 256, 18, 4, "#0d0b1a"))
b.append(glow_pool(354, 240, 26, 30, "#4ff0e6", 0.35))
# crate + cat by the shop
b.append(rect(130, 252, 22, 16, "#7d6450"))
b.append(line(130, 260, 152, 260, "#5a4334", 1))
b.append(ellipse(141, 247, 9, 6, "#6f7896"))   # cat body
b.append(circle(148, 243, 4.5, "#6f7896"))     # head
b.append(poly([(145, 240), (146, 236), (148, 239)], "#6f7896"))
b.append(poly([(149, 239), (151, 236), (152, 240)], "#6f7896"))
b.append(path("M132,248 Q126,244 130,238", stroke="#6f7896", stroke_width=2.5))
b.append(rect(146, 251, 3, 2, "#fffaf0"))     # white sock
b.append(circle(147, 243, 0.8, "#ffd27a")); b.append(circle(150, 243, 0.8, "#ffd27a"))
# trash bags tucked against the clinic wall by the stairs
b.append(ellipse(557, 262, 9, 7, "#1a1d2b")); b.append(ellipse(563, 264, 7, 5, "#262043"))
b.append(ellipse(555, 259, 3, 2, "#525a7a", opacity=0.6)); b.append(path("M557,255 l-2,-3 l3,1", fill="#1a1d2b"))
# paint cans, brush and a ladder below the mural
b.append(rect(372, 258, 6, 10, "#bec2d1")); b.append(rect(372, 258, 6, 2, "#ffb347")); b.append(rect(373, 262, 4, 3, "#e0802a"))
b.append(rect(380, 261, 7, 7, "#949bb3")); b.append(rect(380, 261, 7, 1.5, "#1f5f8a")); b.append(rect(381, 264, 5, 2, "#4fc0e8"))
b.append(rect(434, 262, 6, 6, "#bec2d1")); b.append(rect(434, 262, 6, 1.5, "#ff5fa2"))
b.append(line(390, 267, 400, 264, "#a08870", 1.2)); b.append(rect(399, 263, 3, 2, "#ffd27a"))
b.append(ellipse(382, 268, 14, 1.5, "#ffb347", opacity=0.5))
b.append(line(444, 268, 450, 228, "#a08870", 1.5)); b.append(line(456, 268, 452, 228, "#a08870", 1.5))
for yy in range(236, 268, 8):
    b.append(line(445 + (268 - yy) * 0.0, yy, 455, yy, "#a08870", 1))
# swarm kiosk — slim agent-errand terminal by the clinic, bidding ticker on screen
k = []
k.append(ellipse(465, 270, 9, 2, "#000", opacity=0.4))
k.append(rect(460, 214, 11, 56, "#2a2f45"))
k.append(rect(460, 214, 11, 2, "#6f7896"))
k.append(rect(470, 216, 1, 52, "#0d0b1a", opacity=0.6))
k.append(rect(461, 219, 9, 18, "#0f1f2b"))
for i, (wv, c) in enumerate([(7, "#4ff0e6"), (5, "#ffb347"), (6, "#4ff0e6"), (4, "#ff5fa2"), (7, "#4ff0e6"), (3, "#ffb347")]):
    k.append(rect(462, 221 + i * 2.6, wv, 1.2, c))
k.append(rect(462, 240, 7, 4, "#1f5f8a")); k.append(circle(465.5, 248, 1.5, "#4ff0e6"))
k.append(rect(462, 252, 7, 1, "#525a7a"))
k.append(text(465.5, 213, "BID", "#4ff0e6", 3.5))
k.append(glow_pool(465, 230, 18, 16, "#4ff0e6", 0.4))
b.append("".join(k))

# power lines
b.append(path("M0,96 Q160,120 338,104 T640,110", stroke="#0d0b1a", stroke_width=1))
b.append(path("M0,104 Q200,132 400,116 T640,124", stroke="#0d0b1a", stroke_width=0.8))
# hanging sign scraps


out = svg(W, H, "".join(b), defs)
open(sys.argv[1], "w").write(out)
