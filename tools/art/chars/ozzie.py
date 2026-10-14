"""Osvaldo "Ozzie" Ferreira, 71 — retired cab driver. Barrel chest, big white moustache,
tweed flat cap, cardigan over a two-tone bowling shirt, hearing aid."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from portrait import *

WHITE = "#e6e8ef"
WHITE_D = "#bec2d1"
CX, TOP, W, H, JW = 100, 52, 84, 104, 76
CAP = "#7d6450"
CAP_D = "#5a4334"


def back_hair(s):
    # short white hair at the back/sides, under the cap
    return path("M58,96 Q56,60 100,58 Q144,60 142,96 L144,124 Q140,132 134,128 L132,100 Q100,86 68,100 L66,128 Q60,132 56,124 Z", WHITE_D)


def clothes(s):
    card = "#7a1a1e"
    card_d = shade(card, 0.7)
    shirt = "#1f5260"
    panel = "#f6e7c8"
    rim = s["rim"]
    return (
        # very broad, rounded barrel chest
        path("M10,240 L14,200 Q22,164 70,158 L130,158 Q178,164 186,200 L190,240 Z", card) +
        path("M10,240 L14,200 Q22,164 70,158 L76,240 Z", card_d, opacity=0.7) +
        # bowling shirt: teal with a cream panel, camp collar
        path("M74,158 L126,158 L120,240 L80,240 Z", shirt) +
        path("M106,170 L118,170 L114,240 L104,240 Z", panel) +
        path("M106,170 L118,170", stroke=shade(panel, 0.8), stroke_width=1) +
        # camp collar flaps
        path("M74,154 L100,174 L84,190 Z", shirt) + path("M126,154 L100,174 L116,190 Z", shade(shirt, 1.1)) +
        path("M74,154 L100,174 L84,190 Z M126,154 L100,174 L116,190 Z", stroke=shade(shirt, 0.6), stroke_width=1.2) +
        circle(100, 198, 1.8, panel) + circle(100, 216, 1.8, panel) +
        # embroidered name over the pocket: "OZ"
        text(88, 214, "Oz", "#ffb347", size=8, family="DejaVu Serif", weight="bold") +
        # cardigan fronts, open
        path("M70,158 L80,240 L56,240 L52,186 Z", card) + path("M130,158 L120,240 L144,240 L148,186 Z", shade(card, 1.08)) +
        path("M70,158 L80,240 M130,158 L120,240", stroke=card_d, stroke_width=3) +
        "".join(circle(126 - i * 1.3, 184 + i * 16, 2, "#c9b49a") for i in range(4)) +
        # cable-knit hint
        "".join(path(f"M{34 + i * 12},200 q3,8 0,16 q-3,8 0,16 q3,8 0,16", stroke=card_d, stroke_width=1, opacity=0.5) for i in range(2)) +
        "".join(path(f"M{156 + i * 12},200 q3,8 0,16 q-3,8 0,16 q3,8 0,16", stroke=card_d, stroke_width=1, opacity=0.5) for i in range(2)) +
        path("M132,159 Q178,164 186,200 L189,236", stroke=rim, stroke_width=2, opacity=0.55)
    )


def front_hair(s):
    # tweed flat cap: crown sits low, brim juts over the forehead
    crown = "M54,94 Q50,52 100,46 Q152,50 148,90 Q140,80 100,80 Q62,80 54,94 Z"
    return g(path(crown, CAP) +
            path("M54,94 Q50,52 100,46 L92,80 Q62,80 54,94 Z", CAP_D, opacity=0.5) +
            # tweed flecks
            "".join(rect(60 + (i * 37) % 84, 54 + (i * 23) % 26, 2, 1, "#a08870" if i % 2 else "#3a2a22", opacity=0.8)
                    for i in range(30)) +
            # seam + button
            path("M100,48 Q104,64 100,80", stroke=CAP_D, stroke_width=1.2) + circle(100, 49, 2.2, CAP_D) +
            # brim
            path("M56,92 Q100,74 146,90 Q146,98 140,98 Q100,88 60,100 Q54,98 56,92 Z", CAP_D) +
            path("M60,98 Q100,88 140,96", stroke="#3a2a22", stroke_width=2) +
            path("M70,90 Q100,80 130,88", stroke="#a08870", stroke_width=1, opacity=0.6) +
            # shadow cast by the brim on the brow
            path("M64,100 Q100,92 136,100 Q100,98 64,104 Z", shade(s["skin"], 0.6), opacity=0.35) +
            # rim light on the cap edge
            path("M140,62 Q150,74 148,90", stroke=s["rim"], stroke_width=1.6, opacity=0.6), transform="translate(0,-7)")


def accessories(s):
    # hearing aid tucked behind his right ear (viewer's left)
    ex, ey = CX - W / 2 + 1, TOP + H * 0.53 + 6
    return (path(f"M{ex - 3},{ey - 10} q-6,4 -4,14 q2,4 5,2", "#e3b48f", stroke="#a86a4a", stroke_width=0.8) +
            line(ex - 2, ey - 2, ex + 2, ey, "#8a5236", 1))


def extra_face(s, mood):
    sk = s["skin"]
    d = shade(sk, 0.6)
    my = TOP + H * 0.80
    lift = {"smile": -3, "sad": 3, "angry": 2}.get(mood, 0)
    # deep nasolabial folds + forehead lines + ruddy cheeks
    o = [path(f"M76,{my - 12} q-5,8 -1,18", stroke=d, stroke_width=1.2, opacity=0.6),
         path(f"M124,{my - 12} q5,8 1,18", stroke=d, stroke_width=1.2, opacity=0.6),
         ellipse(76, my - 6, 9, 5, "#e04a3a", opacity=0.18), ellipse(124, my - 6, 9, 5, "#e04a3a", opacity=0.18),
         path(f"M84,{TOP + H} q16,4 32,0", stroke=d, stroke_width=1, opacity=0.4)]
    # big white walrus moustache, ends follow the mood
    m = (f"M{CX},{my - 6} Q{CX + 10},{my - 9} {CX + 18},{my - 4} Q{CX + 25},{my + 1 + lift} {CX + 24},{my + 8 + lift} "
         f"Q{CX + 18},{my + 4 + lift} {CX + 12},{my + 4} Q{CX + 5},{my + 6} {CX},{my + 3} "
         f"Q{CX - 5},{my + 6} {CX - 12},{my + 4} Q{CX - 18},{my + 4 + lift} {CX - 24},{my + 8 + lift} "
         f"Q{CX - 25},{my + 1 + lift} {CX - 18},{my - 4} Q{CX - 10},{my - 9} {CX},{my - 6} Z")
    o.append(path(m, WHITE))
    o.append(path(f"M{CX - 20},{my + 4 + lift} Q{CX - 10},{my} {CX - 2},{my + 2}", stroke=WHITE_D, stroke_width=1.2))
    o.append(path(f"M{CX + 20},{my + 4 + lift} Q{CX + 10},{my} {CX + 2},{my + 2}", stroke=WHITE_D, stroke_width=1.2))
    o.append(path(f"M{CX + 6},{my - 5} Q{CX + 14},{my - 6} {CX + 18},{my - 2}", stroke="#ffffff", stroke_width=1.2, opacity=0.8))
    return "".join(o)


SPEC = dict(skin="#c48a63", hair=WHITE, iris="#4e2c1e", rim="#ff5fa2", brow_color=WHITE, brow_thick=4.2, brow_len=12,
            age=3, eye_size=0.82, eye_dx=0.2, head=dict(cx=CX, top=TOP, w=W, h=H, jw=JW, chin=-0.6), neck_w=40,
            nose="big", nose_y=0.66, mouth_y=0.87, mouth_w=1.1, smile_open=False, blush="#e04a3a",
            back_hair=back_hair, clothes=clothes, front_hair=front_hair, accessories=accessories,
            extra_face=extra_face)

if __name__ == "__main__":
    write_moods("ozzie", SPEC, sys.argv[1], moods=("neutral", "smile", "sad", "angry"))
