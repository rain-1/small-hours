"""Rafe Castellan, 45 — former programmer, the saboteur in the alley. Gaunt, hood up, an old
company hoodie with the logo cut off, a greying beard, a toolbag strap across his chest."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from portrait import *

HAIR = "#3a2a22"
BEARD = "#4a3428"
GREY = "#a08870"
CX, TOP, W, H, JW = 100, 58, 68, 104, 54
HOOD = "#3b4260"
HOOD_D = "#262043"


def back_hair(s):
    # inside of the hood behind the head
    return (path("M46,180 Q36,90 56,62 Q76,34 100,34 Q124,34 144,62 Q164,90 154,180 Z", HOOD) +
            path("M54,170 Q48,96 64,70 Q80,48 100,48 Q120,48 136,70 Q152,96 146,170 Z", HOOD_D))


def clothes(s):
    rim = s["rim"]
    o = [
        bust(100, 170, 70, HOOD, dark=shade(HOOD, 0.7)),
        # hood fabric falling onto the shoulders
        path("M50,176 Q60,196 80,196 L100,206 L120,196 Q140,196 150,176 Q140,186 120,184 L100,190 L80,184 Q60,186 50,176 Z", shade(HOOD, 1.12)),
        # drawstring
        path("M86,194 q-2,16 0,30 M114,194 q2,14 0,26", stroke="#949bb3", stroke_width=1.6, stroke_linecap="round"),
        # the hole where the company logo used to be: rough cut, frayed edge, a lighter rectangle of unfaded cloth
        rect(110, 210, 30, 18, shade(HOOD, 1.25)),
        path("M110,210 L140,210 L140,228 L110,228 Z", stroke="#1b1630", stroke_width=1.2, stroke_dasharray="2,1.5"),
        rect(114, 214, 6, 1, "#949bb3", opacity=0.6), rect(126, 222, 8, 1, "#949bb3", opacity=0.5),
        # toolbag strap across the chest (webbing with a buckle)
        path("M44,186 L150,240", stroke="#5a4334", stroke_width=9),
        path("M44,186 L150,240", stroke="#7d6450", stroke_width=1.2, stroke_dasharray="3,3"),
        rect(74, 196, 12, 12, "#949bb3", transform="rotate(27 80 202)"),
        rect(77, 199, 6, 6, "#5a4334", transform="rotate(27 80 202)"),
        path("M128,171 Q160,176 166,198 L170,236", stroke=rim, stroke_width=2, opacity=0.55),
    ]
    return "".join(o)


def front_hair(s):
    return (
        # lank dark fringe escaping the hood
        path("M66,100 Q64,62 100,60 Q136,62 134,100 Q126,84 112,86 Q102,80 92,86 Q78,82 66,100 Z", HAIR) +
        path("M88,84 q-2,8 -6,12 M104,82 q0,8 -3,12", stroke=HAIR, stroke_width=2, stroke_linecap="round") +
        # hood rim framing the face
        path("M52,168 Q44,96 62,66 Q80,42 100,42 Q120,42 138,66 Q156,96 148,168 L140,168 Q146,104 134,80 Q120,64 100,64 "
             "Q80,64 66,80 Q54,104 60,168 Z", shade(HOOD, 1.1)) +
        path("M62,160 Q56,104 68,82 Q82,66 100,66", stroke=HOOD_D, stroke_width=1.2, opacity=0.8) +
        path("M140,72 Q154,100 148,166", stroke=s["rim"], stroke_width=1.8, opacity=0.65))


def accessories(s):
    return ""


def extra_face(s, mood):
    rnd = random.Random(45)
    sk = s["skin"]
    d = shade(sk, 0.6)
    my = TOP + H * 0.83
    ey = TOP + H * 0.53
    o = [
        # deep-set eyes, hollow cheeks
        ellipse(CX - 15, ey - 2, 10, 6, d, opacity=0.25), ellipse(CX + 15, ey - 2, 10, 6, d, opacity=0.25),
        path(f"M{CX - 26},{ey + 12} Q{CX - 20},{ey + 26} {CX - 22},{ey + 34}", stroke=d, stroke_width=4, opacity=0.25),
        path(f"M{CX + 26},{ey + 12} Q{CX + 20},{ey + 26} {CX + 22},{ey + 34}", stroke=d, stroke_width=4, opacity=0.25),
    ]
    # beard: jaw and chin, cut away around the mouth; moustache on top
    lift = {"smile": -1.5, "sad": 1.5, "angry": 1}.get(mood, 0)
    beard = (f"M{CX - W / 2 + 2},{TOP + H * 0.6} Q{CX - W / 2 + 4},{TOP + H + 4} {CX},{TOP + H + 10} "
             f"Q{CX + W / 2 - 4},{TOP + H + 4} {CX + W / 2 - 2},{TOP + H * 0.6} "
             f"Q{CX + 22},{my - 4} {CX + 14},{my - 4} Q{CX + 13},{my + 8} {CX},{my + 9} Q{CX - 13},{my + 8} {CX - 14},{my - 4} "
             f"Q{CX - 22},{my - 4} {CX - W / 2 + 2},{TOP + H * 0.6} Z")
    o.append(f'<defs><clipPath id="beardclip"><path d="{beard}"/></clipPath></defs>')
    o.append(path(beard, BEARD))
    o.append(path(f"M{CX - 13},{my - 1 + lift} Q{CX - 8},{my - 7} {CX},{my - 6} Q{CX + 8},{my - 7} {CX + 13},{my - 1 + lift} "
                  f"Q{CX + 8},{my - 3} {CX},{my - 3} Q{CX - 8},{my - 3} {CX - 13},{my - 1 + lift} Z", BEARD))
    # soul patch under the lip
    o.append(path(f"M{CX - 3},{my + 5} L{CX + 3},{my + 5} L{CX},{my + 9} Z", BEARD))
    # grey streaks + texture
    tex = []
    for _ in range(60):
        x = rnd.uniform(CX - 30, CX + 30)
        y = rnd.uniform(TOP + H * 0.66, TOP + H + 8)
        if abs(x - CX) < 13 and my - 6 < y < my + 6:
            continue
        tex.append(rect(round(x), round(y), 1, 2, GREY if rnd.random() < 0.45 else "#2a1d18", opacity=0.9))
    o.append(g(*tex, clip_path="url(#beardclip)"))
    o.append(path(f"M{CX + 6},{TOP + H + 2} q2,4 0,8", stroke=GREY, stroke_width=1.6))
    return "".join(o)


SPEC = dict(skin="#d8b494", hair=HAIR, iris="#4f6a45", rim="#7fb85a", brow_color="#2a1d18", brow_thick=3.4, brow_len=11,
            eye_size=0.82, age=2, brow_raise=-2, smile_open=True, head=dict(cx=CX, top=TOP, w=W, h=H, jw=JW, chin=0.3), neck_w=20, lid="#1a0f0c",
            nose="long", mouth_w=0.8, mouth_y=0.84, mouth_style={"smile": "wry"}, blush="#8a5236",
            back_hair=back_hair, clothes=clothes, front_hair=front_hair, accessories=accessories,
            extra_face=extra_face)

if __name__ == "__main__":
    write_moods("rafe", SPEC, sys.argv[1], moods=("neutral", "smile", "sad", "angry"))
