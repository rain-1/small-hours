"""Maeve "Mae" Adair, 52 — DJ of Halfmoon FM 87.9. Shaved silver undercut with a long swept top,
big headphones round her neck, a denim jacket covered in band pins, warm crow's-feet."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from portrait import *

HAIR = "#d2d6e0"
HAIR_D = "#949bb3"
CX, TOP, W, H, JW = 100, 52, 80, 102, 68
DENIM = "#2f8fc0"
DENIM_D = "#1f5f8a"


def back_hair(s):
    # the long top falls past her left ear (viewer's right)
    return (path("M74,170 Q74,150 100,148 Q126,150 126,170", stroke="#1a1d2b", stroke_width=5) +
            path("M118,60 Q150,64 147,104 Q146,124 140,132 Q138,118 130,104 Z", HAIR_D))


def clothes(s):
    rim = s["rim"]
    tee = "#262043"
    pins = [(52, 202, "#ff5fa2", "o"), (66, 220, "#ffd27a", "star"), (44, 226, "#e6e8ef", "o"),
            (148, 204, "#4ff0e6", "bolt"), (160, 222, "#e04a3a", "o"), (140, 228, "#ffb347", "o")]
    o = [
        bust(100, 170, 78, DENIM, dark=DENIM_D),
        # black tee
        path("M80,166 L120,166 L114,240 L86,240 Z", tee),
        path("M82,166 Q100,180 118,166", stroke="#1b1630", stroke_width=3),
        # big denim collar, popped a little
        path("M72,162 L94,186 L80,206 L58,176 Z", shade(DENIM, 1.1)),
        path("M128,162 L106,186 L120,206 L142,176 Z", shade(DENIM, 1.15)),
        path("M72,162 L94,186 L80,206 L58,176 Z M128,162 L106,186 L120,206 L142,176 Z", stroke=DENIM_D, stroke_width=1.2),
        # front edges with orange top-stitching
        path("M86,206 L84,240 M114,206 L116,240", stroke=DENIM_D, stroke_width=3),
        path("M82,210 L80,240 M118,210 L120,240", stroke="#e0802a", stroke_width=0.8, stroke_dasharray="2,2"),
        # chest pocket flaps
        path("M44,212 L72,212 L70,220 L46,220 Z", DENIM_D, opacity=0.6),
        path("M128,212 L156,212 L154,220 L130,220 Z", DENIM_D, opacity=0.6),
    ]
    for x, y, c, kind in pins:
        if kind == "star":
            o.append(poly([(x, y - 5), (x + 1.5, y - 1.5), (x + 5, y - 1), (x + 2.5, y + 1.5), (x + 3, y + 5), (x, y + 3), (x - 3, y + 5),
                           (x - 2.5, y + 1.5), (x - 5, y - 1), (x - 1.5, y - 1.5)], c))
        elif kind == "bolt":
            o.append(circle(x, y, 5.5, "#1b1630"))
            o.append(poly([(x + 1, y - 4), (x - 2.5, y + 1), (x, y + 1), (x - 1, y + 4), (x + 2.5, y - 1), (x, y - 1)], c))
        else:
            o.append(circle(x, y, 4.5, c))
            o.append(circle(x, y, 1.8, "#1b1630"))
            o.append(circle(x - 1.5, y - 1.5, 1, "#ffffff", opacity=0.7))
    # headphones round her neck: band behind, two big cups on the collarbones
    o += [
          g(ellipse(72, 176, 11, 13, "#2a2f45", transform="rotate(-20 72 176)"), ellipse(73, 176, 6, 8, "#1a1d2b", transform="rotate(-20 73 176)"),
            ellipse(72, 176, 11, 13, "none", stroke="#6f7896", stroke_width=1, transform="rotate(-20 72 176)")),
          g(ellipse(128, 176, 11, 13, "#2a2f45", transform="rotate(20 128 176)"), ellipse(127, 176, 6, 8, "#1a1d2b", transform="rotate(20 127 176)"),
            path("M132,164 Q139,168 139,178", stroke=rim, stroke_width=1.6, opacity=0.8)),
          text(72, 179, "I", "#e04a3a", size=6), 
          path("M128,166 Q168,170 176,196 L178,236", stroke=rim, stroke_width=2, opacity=0.5)]
    return "".join(o)


def front_hair(s):
    sk = s["skin"]
    return (
        # buzzed right side (viewer's left): silver stubble over skin
        path("M61,106 Q54,50 100,46 L96,62 Q78,68 70,82 Q66,92 66,106 Z", HAIR_D, opacity=0.85) +
        "".join(rect(62 + (i * 7) % 22, 62 + (i * 11) % 38, 1, 1, "#e6e8ef", opacity=0.8) for i in range(30)) +
        # long silver top, swept over to her left in one big wave
        path("M74,64 Q86,38 118,42 Q150,50 147,90 Q146,112 140,128 Q134,106 124,94 Q114,82 98,82 Q84,82 72,88 Q68,74 74,64 Z", HAIR) +
        path("M80,62 Q100,50 124,56 Q142,68 142,94", stroke="#ffffff", stroke_width=1.6, opacity=0.8) +
        path("M88,74 Q112,68 128,84 Q136,96 139,116", stroke=HAIR_D, stroke_width=1.2) +
        path("M140,64 Q148,78 146,96", stroke=s["rim"], stroke_width=1.6, opacity=0.6))


def accessories(s):
    ex, ey = CX - W / 2 + 1, TOP + H * 0.53 + 6
    # a row of little hoops up the shaved-side ear
    return "".join(circle(ex - 5, ey - 7 + i * 6, 1.3, "#ffd27a") for i in range(3))


def extra_face(s, mood):
    d = shade(s["skin"], 0.62)
    # warm crow's-feet that deepen when she grins, a faint scatter of sun spots
    o = [path("M78,128 q-4,6 -1,12", stroke=d, stroke_width=1, opacity=0.5),
         path("M122,128 q4,6 1,12", stroke=d, stroke_width=1, opacity=0.5)]
    if mood == "smile":
        for sd in (-1, 1):
            x = CX + sd * W * 0.215 + sd * 9
            o.append(path(f"M{x},{108} l{sd * 4},-2 M{x},{110} l{sd * 4},1", stroke=d, stroke_width=0.8, opacity=0.6))
    return "".join(o)


SPEC = dict(skin="#f2cdb6", hair=HAIR, iris="#2b6e78", rim="#ff7a5a", brow_color="#7d6450", brow_thick=3, brow_len=11,
            age=2, eye_size=0.95, head=dict(cx=CX, top=TOP, w=W, h=H, jw=JW, chin=0.1), neck_w=24,
            mouth_w=1.05, blush="#e04a3a",
            back_hair=back_hair, clothes=clothes, front_hair=front_hair, accessories=accessories,
            extra_face=extra_face)

if __name__ == "__main__":
    write_moods("mae", SPEC, sys.argv[1], moods=("neutral", "smile", "sad"))
