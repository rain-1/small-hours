"""Lu Meifang, 68 — Halfmoon Noodle. Silver bun with fish clip, glasses on a beaded chain,
apron over a faded cleanroom sweatshirt."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from portrait import *

HAIR = "#bec2d1"
HAIR_D = "#949bb3"


def back_hair(s):
    return (circle(100, 44, 22, HAIR_D) +                       # bun
            path("M84,40 Q100,30 116,40", stroke=HAIR, stroke_width=3) +
            path("M58,92 Q56,40 100,38 Q144,40 142,92 Q140,70 100,64 Q60,70 58,92 Z", HAIR_D))


def clothes(s):
    sweat = "#5d4f8c"
    apron = "#b02a2a"
    return (bust(100, 168, 74, sweat) +
            path("M70,178 Q100,192 130,178", stroke=shade(sweat, 0.7), stroke_width=4) +   # collar rib
            # apron bib & straps
            path("M74,240 L78,196 L122,196 L126,240 Z", apron) +
            path("M78,196 L70,172 M122,196 L130,172", stroke=apron, stroke_width=6) +
            rect(84, 208, 32, 18, shade(apron, 0.8)) +                           # pocket
            path("M84,208 L116,208", stroke="#f6e7c8", stroke_width=1, opacity=0.5) +
            # chopsticks + pen in pocket
            line(90, 196, 92, 214, "#c9b49a", 2) + line(94, 194, 95, 214, "#c9b49a", 2) +
            line(108, 200, 108, 214, "#1f5f8a", 2.5) +
            # faded cleanroom logo on sleeve
            circle(46, 214, 6, shade(sweat, 1.2), opacity=0.5) +
            # burn scars on forearm hint (shoulder area)
            path("M150,220 q4,2 8,0", stroke=shade(s["skin"], 0.7), stroke_width=1))


def front_hair(s):
    return (path("M60,98 Q56,44 100,42 Q146,44 141,100 Q138,76 124,70 Q108,76 92,68 Q74,74 66,84 Q62,90 60,98 Z", HAIR) +
            path("M66,84 Q80,60 104,56 Q124,58 132,74", stroke="#e6e8ef", stroke_width=1.5) +
            path("M92,68 Q100,56 120,54", stroke=HAIR_D, stroke_width=1.2) +
            path("M74,74 Q84,58 100,52", stroke=HAIR_D, stroke_width=1) +
            # fish hair clip (amber), at the bun
            g(path("M112,30 q10,-6 20,0 q-10,6 -20,0 Z", "#ffb347"),
              poly([(132, 30), (138, 25), (138, 35)], "#e0802a"),
              circle(116, 29, 1.2, "#3a1a10"), filter="url(#glow)"))


def accessories(s):
    # glasses on a beaded chain, resting low on the nose
    return (g(circle(84, 107, 10, "none", stroke="#8a5236", stroke_width=1.6),
              circle(116, 107, 10, "none", stroke="#8a5236", stroke_width=1.6),
              line(94, 106, 106, 106, "#8a5236", 1.4),
              ellipse(84, 107, 9, 9, "#d2f0e2", opacity=0.12),
              ellipse(116, 107, 9, 9, "#d2f0e2", opacity=0.12)) +
            "".join(circle(70 + i * 1.2 - (i // 12) * 0, 112 + i * 3.4, 1.2, ["#ffb347", "#e04a3a", "#4fc0e8"][i % 3]) for i in range(14)) +
            "".join(circle(130 - i * 1.2, 112 + i * 3.4, 1.2, ["#ffb347", "#e04a3a", "#4fc0e8"][i % 3]) for i in range(14)))


def extra_face(s, mood):
    # laugh lines
    return (path("M80,128 q-3,6 0,12", stroke=shade(s["skin"], 0.65), stroke_width=1, opacity=0.6) +
            path("M120,128 q3,6 0,12", stroke=shade(s["skin"], 0.65), stroke_width=1, opacity=0.6))


SPEC = dict(skin="#ecc39e", hair=HAIR, iris="#3a1a10", rim="#ffb347", brow_color="#949bb3", brow_thick=2.2,
            age=3, eye_size=0.92, head=dict(w=76, h=98, jw=58, top=50),
            back_hair=back_hair, clothes=clothes, front_hair=front_hair, accessories=accessories,
            extra_face=extra_face)

if __name__ == "__main__":
    write_moods("lu", SPEC, sys.argv[1], moods=("neutral", "smile", "sad", "surprised"))
