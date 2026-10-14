"""Hand-drawn map of Halfmoon Street on dark paper. 640x360.

Iso-ish little buildings along the crescent street under the rail line,
the stairs climbing to the roofs, hill road leaving the edge, bay below.
Labels are painted; the engine adds pins at the hotspot centres.
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from svg import *
from props import *

INK = "#f6e7c8"
INK2 = "#c9b49a"
defs = (
    rad_grad("paper", [(0, "#332a57"), (0.7, "#262043"), (1, "#0d0b1a")]) +
    lin_grad("mbay", [(0, "#173a4a"), (1, "#0f1f2b")]) +
    '<filter id="wobble"><feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="3"/>'
    '<feDisplacementMap in="SourceGraphic" scale="2.2"/></filter>'
)

b = []
b.append(rect(0, 0, W, H, "#0d0b1a"))
# the paper sheet with ragged edges
rnd = random.Random(4)
pts = []
for x in range(8, 633, 12):
    pts.append((x, 8 + rnd.uniform(-2, 2)))
for y in range(8, 353, 12):
    pts.append((632 + rnd.uniform(-2, 2), y))
for x in range(632, 7, -12):
    pts.append((x, 352 + rnd.uniform(-2, 2)))
for y in range(352, 7, -12):
    pts.append((8 + rnd.uniform(-2, 2), y))
b.append(poly([(round(a, 1), round(c, 1)) for a, c in pts], "url(#paper)"))
# paper grain
for i in range(900):
    b.append(rect(rnd.randrange(10, 630), rnd.randrange(10, 350), 1, 1, rnd.choice(["#463a70", "#1b1630", "#5d4f8c"]), opacity=0.5))
# fold lines
b.append(line(320, 10, 320, 350, "#1b1630", 1, opacity=0.7)); b.append(line(321, 10, 321, 350, "#463a70", 0.6, opacity=0.5))
b.append(line(10, 180, 630, 180, "#1b1630", 1, opacity=0.6)); b.append(line(10, 181, 630, 181, "#463a70", 0.6, opacity=0.4))

art = []
labels = []
# ---- the bay (bottom-left), waves, a ferry, Kestrel across the water
art.append(path("M10,300 Q120,268 230,300 T460,352 L10,352 Z", "url(#mbay)"))
art.append(path("M10,300 Q120,268 230,300 T460,352", stroke=INK2, stroke_width=1))
for i in range(14):
    x, y = 30 + (i * 37) % 360, 312 + (i * 13) % 34
    if y > 300 + (x / 12):
        art.append(path(f"M{x},{y} q3,-3 6,0 q3,-3 6,0", stroke="#3f8f8f", stroke_width=0.8))
art.append(text(120, 336, "Lantern Bay", INK2, 9, family="DejaVu Serif", weight="normal", font_style="italic"))
art.append(poly([(52, 318), (55, 290), (58, 318)], "#4fc0e8"))
art.append(circle(55, 290, 2, "#a8fff6", filter="url(#glow)"))
art.append(text(55, 328, "Kestrel ↗", "#4fc0e8", 5, weight="normal"))

# ---- elevated rail line along the crescent (double line with sleepers)
STREET = "M30,262 Q300,150 600,250"
art.append(path(STREET, stroke="#2a2f45", stroke_width=22))
art.append(path(STREET, stroke=INK2, stroke_width=0.8, transform="translate(0,-11)"))
art.append(path(STREET, stroke=INK2, stroke_width=0.8, transform="translate(0,11)"))
art.append(path(STREET, stroke="#525a7a", stroke_width=1, stroke_dasharray="1 5"))
art.append(path("M30,282 Q300,170 600,270", stroke="#ffb347", stroke_width=1.2, stroke_dasharray="6 3", opacity=0.8))  # rail
art.append(path("M30,286 Q300,174 600,274", stroke="#ffb347", stroke_width=1.2, stroke_dasharray="6 3", opacity=0.8))
art.append('<path id="streetline" d="M30,266 Q300,154 600,254" fill="none"/>')
art.append('<text font-size="7" font-family="DejaVu Serif" font-weight="bold" fill="#f6e7c8" letter-spacing="3">'
           '<textPath href="#streetline" startOffset="9%">HALFMOON STREET</textPath></text>')
art.append(text(560, 286, "~ elevated line ~", INK2, 5, weight="normal", font_style="italic", transform="rotate(14,560,286)"))


def qpt(t, p0=(30, 262), p1=(300, 150), p2=(600, 250)):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
    return x, y


def iso(x, y, w, d, h, top, front, side, lit=0.4, seed=0, win="#ffb347"):
    """Little iso block whose front-bottom-left corner is (x, y)."""
    r = random.Random(seed)
    o = [poly([(x, y), (x + w, y), (x + w, y - h), (x, y - h)], front),
         poly([(x + w, y), (x + w + d * 0.6, y - d * 0.5), (x + w + d * 0.6, y - h - d * 0.5), (x + w, y - h)], side),
         poly([(x, y - h), (x + w, y - h), (x + w + d * 0.6, y - h - d * 0.5), (x + d * 0.6, y - h - d * 0.5)], top)]
    for wy in range(int(y - h + 3), int(y - 3), 5):
        for wx in range(int(x + 2), int(x + w - 2), 4):
            if r.random() < lit:
                o.append(rect(wx, wy, 2, 2, r.choice([win, "#ffd27a", "#4fc0e8"])))
    o.append(path(f"M{x},{y} L{x + w},{y} L{x + w + d * 0.6},{y - d * 0.5} L{x + w + d * 0.6},{y - h - d * 0.5} "
                  f"L{x + d * 0.6},{y - h - d * 0.5} L{x},{y - h} Z M{x + w},{y} L{x + w},{y - h} L{x},{y - h} "
                  f"M{x + w},{y - h} L{x + w + d * 0.6},{y - h - d * 0.5}", stroke=INK2, stroke_width=0.6, opacity=0.8))
    return "".join(o)


# filler buildings along the north side of the street
for i, t in enumerate([0.04, 0.3, 0.37, 0.62, 0.86, 0.95]):
    x, y = qpt(t)
    art.append(iso(x - 10, y - 14, 18, 14, 18 + (i * 7) % 12, "#463a70", "#262043", "#1b1630", seed=i + 10))
# south side: a few trees and lamp dots between the rail and the bay
for i, t in enumerate([0.08, 0.3, 0.5, 0.63, 0.8, 0.93]):
    x, y = qpt(t)
    art.append(circle(x + 8, y + 62, 5, "#1f4a2a")); art.append(circle(x + 8, y + 62, 5, "none", stroke=INK2, stroke_width=0.5))
    art.append(line(x + 8, y + 67, x + 8, y + 71, INK2, 0.6))


# ---- landmarks
# Suds & Stars laundromat
x, y = qpt(0.17)
art.append(iso(x - 16, y - 12, 30, 16, 26, "#2b6e78", "#173a4a", "#0f1f2b", seed=1, lit=0.2))
for k in range(3):
    art.append(circle(x - 9 + k * 8, y - 19, 2.6, "#d2f0e2")); art.append(circle(x - 9 + k * 8, y - 19, 1.4, "#3f8f8f"))
art.append(rect(x + 4, y - 34, 6, 5, "#4fc0e8"))   # Teo's window
# Halfmoon Noodle
x, y = qpt(0.43)
art.append(iso(x - 18, y - 12, 34, 18, 30, "#7a1f52", "#4a1538", "#2a0f24", seed=2, lit=0.5))
art.append(poly([(x - 20, y - 22), (x + 18, y - 22), (x + 20, y - 17), (x - 22, y - 17)], "#e04a3a"))
art.append(circle(x - 22, y - 16, 2.4, "#e04a3a", filter="url(#glow)")); art.append(circle(x + 20, y - 16, 2.4, "#e04a3a", filter="url(#glow)"))
art.append(path(f"M{x - 6},{y - 34} q-2,-6 1,-10 M{x + 2},{y - 34} q2,-6 -1,-10", stroke=INK, stroke_width=0.8, opacity=0.7))   # steam
art.append(text(x, y - 46, "★", "#ffd27a", 7))
# the alley — a dashed lane behind the shop
ax, ay = x + 4, y - 50
art.append(path(f"M{x + 22},{y - 18} q10,-20 -2,-46", stroke=INK2, stroke_width=4, stroke_linecap="round", opacity=0.35))
art.append(path(f"M{x + 22},{y - 18} q10,-20 -2,-46", stroke=INK2, stroke_width=0.8, stroke_dasharray="2 2"))
art.append(rect(x + 14, y - 68, 10, 8, "#6f7896")); art.append(text(x + 19, y - 62, "!", "#ffd27a", 6))   # junction box
art.append(path(f"M{x + 28},{y - 60} q2,-6 0,-12", stroke=INK, stroke_width=0.8, opacity=0.6))
# Hotline (above the pharmacy)
x, y = qpt(0.55)
art.append(iso(x - 14, y - 12, 28, 16, 34, "#1f5260", "#173a4a", "#0f1f2b", seed=3, lit=0.3, win="#ff9cc6"))
art.append(rect(x - 12, y - 40, 24, 6, "#ff5fa2", filter="url(#glow)"))
art.append(path(f"M{x - 3},{y - 50} q-4,0 -4,4 q0,4 4,4 l1,-2 l-2,-1 q0,-2 1,-3 l2,1 z", fill=INK))   # phone glyph
# mural (small star on the shutter)
art.append(path(f"M{x - 8},{y - 14} a6,6 0 0,1 12,0 z", fill="#ffb347"))
# Night Clinic
x, y = qpt(0.71)
art.append(iso(x - 14, y - 12, 28, 16, 28, "#e6e8ef", "#bec2d1", "#949bb3", seed=4, lit=0.6, win="#9bd6c4"))
art.append(rect(x - 3, y - 36, 6, 14, "#4ff0e6")); art.append(rect(x - 7, y - 32, 14, 6, "#4ff0e6"))
# the stairs climbing to the roofs
sx0, sy0 = qpt(0.83)
for k in range(16):
    xx, yy = sx0 + k * 4.2, sy0 - 14 - k * 6.5
    art.append(rect(xx, yy, 12, 2, INK2))
art.append(path(f"M{sx0 - 2},{sy0 - 14} L{sx0 + 64},{sy0 - 118}", stroke=INK2, stroke_width=0.6))
art.append(path(f"M{sx0 + 14},{sy0 - 14} L{sx0 + 80},{sy0 - 118}", stroke=INK2, stroke_width=0.6))
art.append(poly([(sx0 + 20, sy0 - 60), (sx0 + 26, sy0 - 66), (sx0 + 32, sy0 - 60)], "#e04a3a"))     # shrine
art.append(rect(sx0 + 22, sy0 - 60, 8, 6, "#b02a2a"))
art.append(rect(sx0 - 8, sy0 - 74, 8, 12, "#b02a2a"))                                              # vending
# the roofs and water tower (Mae) + June's tarp
rx, ry = 470, 72
art.append(iso(rx - 50, ry + 46, 70, 30, 14, "#463a70", "#262043", "#1b1630", seed=7, lit=0.3))
art.append(line(rx - 10, ry + 30, rx - 10, ry + 8, INK2, 1)); art.append(line(rx + 10, ry + 30, rx + 10, ry + 8, INK2, 1))
art.append(rect(rx - 14, ry - 10, 28, 18, "#5a4334")); art.append(poly([(rx - 16, ry - 10), (rx, ry - 20), (rx + 16, ry - 10)], "#3a2a22"))
art.append(path(f"M{rx - 14},{ry - 10} L{rx + 14},{ry - 10} L{rx + 14},{ry + 8} L{rx - 14},{ry + 8} Z", stroke=INK2, stroke_width=0.6))
art.append(line(rx + 6, ry - 18, rx + 6, ry - 34, INK2, 0.8)); art.append(circle(rx + 6, ry - 35, 1.6, "#ff5fa2", filter="url(#glow)"))
for k in range(3):
    art.append(path(f"M{rx + 12 + k * 4},{ry - 36 + k} a{4 + k * 3},{4 + k * 3} 0 0,1 0,{8 + k * 6}", stroke="#ff5fa2", stroke_width=0.6, opacity=0.7,
                    transform=f"translate({-k * 2},{-k * 3})"))
art.append(text(rx - 30, ry - 16, "87.9", "#ff5fa2", 6))
art.append(poly([(rx + 30, ry + 22), (rx + 52, ry + 12), (rx + 56, ry + 26), (rx + 34, ry + 34)], "#2f8fc0"))   # June's tarp
art.append(circle(rx + 46, ry + 28, 1.6, "#b8de7a", filter="url(#glow)"))
art.append(path(f"M{rx - 40},{ry + 20} Q{rx},{ry + 6} {rx + 34},{ry + 18}", stroke="#ffd27a", stroke_width=0.6, stroke_dasharray="1 2"))   # string lights
# hill road winding off the edge (top right)
art.append(path("M560,150 Q600,130 580,100 T612,40 T640,12", stroke="#2a2f45", stroke_width=10))
art.append(path("M560,150 Q600,130 580,100 T612,40 T640,12", stroke=INK2, stroke_width=0.6, stroke_dasharray="4 3"))
art.append(path("M548,160 Q560,152 566,150", stroke=INK2, stroke_width=0.8))
art.append(rect(600, 56, 14, 7, "#2b6e78")); art.append(circle(603, 63, 1.4, "#0d0b1a")); art.append(circle(611, 63, 1.4, "#0d0b1a"))   # Dolores
# hills contour hatching
for k in range(5):
    art.append(path(f"M{380 + k * 6},{150 - k * 14} q60,-30 120,-10", stroke="#463a70", stroke_width=0.8, opacity=0.8))

# ---- labels (hand-lettered), with leader dots
def label(x, y, s, sub=None, anchor="middle", col=INK):
    o = [text(x, y, s, col, 7.5, family="DejaVu Serif", anchor=anchor)]
    if sub:
        o.append(text(x, y + 7, sub, INK2, 4.6, family="DejaVu Serif", weight="normal", anchor=anchor, font_style="italic"))
    return "".join(o)

x, y = qpt(0.17); labels.append(label(x - 4, y + 42, "Suds &amp; Stars", "laundromat · Teo upstairs"))
x, y = qpt(0.43); labels.append(label(x - 8, y + 42, "Halfmoon Noodle", "Lu's · open all night", col="#ffd27a"))
x, y = qpt(0.43); labels.append(label(x - 30, y - 70, "The Alley", "out back", anchor="end"))
x, y = qpt(0.55); labels.append(label(x + 14, y + 42, "Hotline", "humans only"))
x, y = qpt(0.71); labels.append(label(x + 6, y + 42, "Night Clinic", "midwife on call"))
labels.append(label(sx0 + 76, sy0 - 50, "The Stairs", "shrine · vending", anchor="start"))
labels.append(label(rx - 60, ry + 2, "The Roofs", "water tower · 87.9 FM", anchor="end"))
labels.append(label(624, 82, "Hill Road", "to the overlook →", anchor="end"))

# ---- title cartouche, compass, doodles
art.append(rect(22, 22, 150, 44, "#1b1630")); art.append(rect(25, 25, 144, 38, "none", stroke=INK2, stroke_width=0.8))
art.append(path("M38,44 a8,8 0 1,0 8,-8 a6,6 0 1,1 -8,8", fill="#ffd27a"))
art.append(text(104, 43, "HALFMOON", INK, 12, family="DejaVu Serif"))
art.append(text(104, 55, "a map of the slow street", INK2, 5.5, family="DejaVu Serif", weight="normal", font_style="italic"))
cx, cy = 590, 312
art.append(circle(cx, cy, 16, "none", stroke=INK2, stroke_width=0.6))
art.append(poly([(cx, cy - 20), (cx + 4, cy), (cx, cy + 20), (cx - 4, cy)], INK2))
art.append(poly([(cx, cy - 20), (cx + 4, cy), (cx - 4, cy)], "#ff5fa2"))
art.append(poly([(cx - 20, cy), (cx, cy - 3), (cx + 20, cy), (cx, cy + 3)], INK2, opacity=0.6))
art.append(text(cx, cy - 23, "N", INK, 6))
# coffee ring and a doodled cat + note
art.append(circle(500, 316, 22, "none", stroke="#5e2a12", stroke_width=2.5, opacity=0.45))
art.append(circle(500, 316, 19, "none", stroke="#5e2a12", stroke_width=0.8, opacity=0.35))
art.append(tr("".join([ellipse(250, 120, 6, 4, "none", stroke=INK2, stroke_width=0.7), circle(256, 116, 3, "none", stroke=INK2, stroke_width=0.7),
path("M254,113 l1,-2 l1,2 M257,113 l1,-2 l1,2", stroke=INK2, stroke_width=0.6),
path("M244,121 q-5,-2 -3,-7", stroke=INK2, stroke_width=0.7),
text(250, 133, "cat (many names)", INK2, 4.2, weight="normal", font_style="italic"),
]), dx=40, dy=-24))
art.append(text(150, 100, "the swarm goes around us", "#4ff0e6", 4.5, weight="normal", font_style="italic", opacity=0.75))
art.append(path("M90,104 q30,-14 60,-10 q30,4 60,-6", stroke="#4ff0e6", stroke_width=0.5, stroke_dasharray="1 2", opacity=0.6))

b.append(g(*art, filter="url(#wobble)"))
b.append(g(*labels))

out = svg(W, H, "".join(b), defs)
open(sys.argv[1], "w").write(out)
