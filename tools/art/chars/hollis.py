"""Hollis Grey, 29 (they/them) — operator of the Humans Only Hotline. Teal-dyed buzz cut growing
out over dark roots, septum ring, a huge rust wool sweater, a call-centre headset, tired kind eyes."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from portrait import *

ROOT = "#1a1418"
TEAL = "#3f8f8f"
TEAL_L = "#63b3a8"
CX, TOP, W, H, JW = 100, 54, 76, 100, 60
KNIT = "#b85c1c"
KNIT_D = "#8a3f16"


def back_hair(s):
    return path("M62,104 Q55,46 100,44 Q145,46 138,104 Z", ROOT)


def clothes(s):
    rim = s["rim"]
    o = [
        # enormous sweater: wide dropped shoulders, chunky roll neck
        path("M8,240 L12,206 Q20,176 66,170 L134,170 Q180,176 188,206 L192,240 Z", KNIT),
        path("M8,240 L12,206 Q20,176 66,170 L74,240 Z", KNIT_D, opacity=0.6),
        path("M70,176 Q68,156 100,154 Q132,156 130,176 Q132,190 100,192 Q68,190 70,176 Z", shade(KNIT, 1.08)),
        path("M72,178 Q100,190 128,178", stroke=KNIT_D, stroke_width=2),
        path("M74,168 Q100,178 126,168", stroke=KNIT_D, stroke_width=1.4),
    ]
    # cable-knit columns
    for x0 in (36, 60, 140, 164):
        o.append("".join(path(f"M{x0},{196 + k * 12} q4,6 0,12", stroke=KNIT_D, stroke_width=1.6) +
                         path(f"M{x0 + 6},{196 + k * 12} q-4,6 0,12", stroke=KNIT_D, stroke_width=1.6) for k in range(4)))
    for x0 in (88, 112):
        o.append(line(x0, 196, x0, 240, KNIT_D, 1, opacity=0.6))
    # a loose thread and a darned patch
    o.append(path("M150,226 q4,4 2,10", stroke="#ffd27a", stroke_width=0.8))
    o.append(rect(44, 218, 10, 8, "#5e2a12", opacity=0.6))
    o.append(path("M132,171 Q178,176 186,204 L190,236", stroke=rim, stroke_width=2, opacity=0.55))
    return "".join(o)


def front_hair(s):
    rnd = random.Random(29)
    hairline = "M62,106 Q55,46 100,44 Q145,46 138,106 L135,94 Q133,82 124,78 Q112,74 100,75 Q88,74 76,78 Q67,82 65,94 Z"
    o = [path(hairline, ROOT)]
    # teal growing out: the dye sits on the outer part, dark roots show at the hairline
    o.append(path("M64,98 Q57,47 100,45 Q143,47 136,98 Q134,84 124,76 Q112,71 100,72 Q88,71 76,76 Q66,84 64,98 Z", TEAL))
    for _ in range(220):
        x, y = rnd.uniform(58, 142), rnd.uniform(44, 100)
        if (x - 100) ** 2 / 42 ** 2 + (y - 80) ** 2 / 36 ** 2 > 1 or (y > 72 and 76 < x < 124):
            continue
        edge = y > 90
        o.append(rect(round(x), round(y), 1, 1, ROOT if edge else (TEAL_L if rnd.random() < 0.6 else "#1f5260"), opacity=0.9))
    # headset band over the crown
    o.append(path("M61,108 Q58,54 100,52 Q142,54 139,108", stroke="#1a1d2b", stroke_width=3.5))
    o.append(path("M66,74 Q80,55 100,54", stroke="#525a7a", stroke_width=1))
    o.append(path("M134,58 Q142,72 141,92", stroke=s["rim"], stroke_width=1.6, opacity=0.6))
    return "".join(o)


def accessories(s):
    ey = TOP + H * 0.53 + 6
    rx = CX + W / 2
    return (
        # ear pad on their left (viewer's right), mic boom curving to the mouth
        rect(rx - 6, ey - 12, 12, 22, "#2a2f45", rx=5) + rect(rx - 4, ey - 9, 4, 16, "#3b4260", rx=2) +
        circle(rx + 2, ey - 6, 1.4, "#ff5fa2", filter="url(#glow)") +
        path(f"M{rx - 2},{ey + 6} Q{rx - 6},{ey + 28} {CX + 16},{ey + 30}", stroke="#1a1d2b", stroke_width=2.4, stroke_linecap="round") +
        ellipse(CX + 14, ey + 30, 4, 3, "#2a2f45") +
        # small pad on the other ear + two hoops
        rect(CX - W / 2 - 4, ey - 8, 6, 14, "#1a1d2b", rx=3) +
        circle(CX - W / 2 + 1, ey + 10, 2, "none", stroke="#bec2d1", stroke_width=1))


def extra_face(s, mood):
    d = shade(s["skin"], 0.62)
    ny = TOP + H * 0.7
    o = [
        # tired lower lids
        path("M79,118 Q86,122 93,118", stroke=d, stroke_width=1.1, opacity=0.55),
        path("M107,118 Q114,122 121,118", stroke=d, stroke_width=1.1, opacity=0.55),
        # septum ring
        path(f"M{CX - 2.2},{ny + 4.5} Q{CX},{ny + 8} {CX + 2.2},{ny + 4.5}", stroke="#bec2d1", stroke_width=1.1),
    ]
    return "".join(o)


SPEC = dict(skin="#7d4c36", hair=ROOT, iris="#2a120a", rim="#ff9cc6", brow_color="#1a1418", brow_thick=2.6, brow_len=10,
            eye_size=0.95, head=dict(cx=CX, top=TOP, w=W, h=H, jw=JW, chin=0.2), neck_w=24, lid="#140a08",
            nose="broad", nose_y=0.68, mouth_w=0.95, blush="#e0458e", smile_open=True,
            mouth_style={"smile": "closed"}, brow_mood={"neutral": "worried"},
            back_hair=back_hair, clothes=clothes, front_hair=front_hair, accessories=accessories,
            extra_face=extra_face)

if __name__ == "__main__":
    write_moods("hollis", SPEC, sys.argv[1], moods=("neutral", "smile", "sad"))
