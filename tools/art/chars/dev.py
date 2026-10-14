"""Dev Raman, 31 — anxious first-time father in the night clinic waiting room. Rumpled office
shirt with a crooked collar, a logistics-company lanyard, stubble, hair raked by worried hands, kind eyes."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from portrait import *

HAIR = "#171217"
HAIR_L = "#463a70"
CX, TOP, W, H, JW = 100, 54, 74, 104, 58
SHIRT = "#a9c4dc"
SHIRT_D = "#6f8fb0"


def back_hair(s):
    return path("M62,100 Q58,52 100,50 Q142,52 138,100 Z", HAIR)


def clothes(s):
    rim = s["rim"]
    return (
        bust(100, 172, 74, SHIRT, dark=SHIRT_D) +
        # rumple creases
        path("M40,206 q10,6 18,2 M52,226 q8,-4 14,2 M146,210 q-8,6 -16,0 M150,230 q-10,-2 -14,4", stroke=SHIRT_D, stroke_width=1.2, opacity=0.8) +
        # open collar, top button undone, one point flipped up
        path("M80,168 L100,196 L120,168 Z", shade(s["skin"], 0.8)) +
        path("M76,164 L100,192 L86,200 L70,174 Z", "#e6e8ef") +
        path("M124,164 L104,190 L122,186 L136,162 Z", "#e6e8ef") +
        path("M76,164 L100,192 L86,200 L70,174 Z M124,164 L104,190 L122,186 L136,162 Z", stroke=SHIRT_D, stroke_width=1) +
        # placket and buttons
        line(100, 196, 100, 240, SHIRT_D, 1.2) + circle(103, 210, 1.6, "#fffaf0") + circle(103, 228, 1.6, "#fffaf0") +
        # orange logistics lanyard + badge (a little parcel logo)
        path("M78,170 Q82,200 94,222 M122,168 Q118,200 106,222", stroke="#e0802a", stroke_width=3) +
        rect(88, 220, 24, 20, "#fffaf0", rx=2) + rect(88, 220, 24, 6, "#e0802a", rx=1) +
        rect(92, 229, 7, 7, "#b85c1c") + line(92, 232.5, 99, 232.5, "#ffd27a", 1) +
        rect(101, 230, 8, 1.4, "#525a7a") + rect(101, 233, 6, 1.4, "#525a7a") +
        # pen in the pocket
        rect(124, 208, 16, 14, shade(SHIRT, 0.92)) + line(128, 202, 128, 212, "#262043", 2) +
        path("M126,173 Q160,178 168,200 L172,236", stroke=rim, stroke_width=2, opacity=0.55)
    )


def front_hair(s):
    return (
        # short, thick, pushed up and sideways by nervous hands
        path("M63,100 Q58,60 76,52 Q72,42 86,46 Q92,36 102,44 Q112,36 118,46 Q130,42 128,54 Q144,62 137,100 "
             "Q134,82 124,76 Q112,72 100,74 Q86,72 76,78 Q66,84 63,100 Z", HAIR) +
        path("M80,58 Q92,50 104,54 M108,52 Q120,50 128,60", stroke=HAIR_L, stroke_width=1.4, opacity=0.9) +
        # a tuft sticking up
        path("M104,44 q2,-8 8,-10 q-2,6 -3,11 Z", HAIR) +
        path("M134,60 Q142,74 140,96", stroke=s["rim"], stroke_width=1.6, opacity=0.6))


def accessories(s):
    return ""


def extra_face(s, mood):
    d = shade(s["skin"], 0.62)
    return (stubble(CX, TOP, W, H, JW, "#171217", op=0.3, beard_line=0.7, seed=31) +
            path("M80,117 Q87,120 94,117", stroke=d, stroke_width=1, opacity=0.4) +
            path("M106,117 Q113,120 120,117", stroke=d, stroke_width=1, opacity=0.4))


SPEC = dict(skin="#a8704c", hair=HAIR, iris="#2a120a", rim="#9bd6c4", brow_color="#171217", brow_thick=3.2, brow_len=11,
            eye_size=1.05, head=dict(cx=CX, top=TOP, w=W, h=H, jw=JW, chin=0.1), neck_w=26, lid="#1a0f0c",
            nose="default", mouth_w=0.9, blush="#b85c1c", smile_open=True,
            brow_mood={"neutral": "worried", "smile": "worried"}, mouth_style={"smile": "closed"},
            back_hair=back_hair, clothes=clothes, front_hair=front_hair, accessories=accessories,
            extra_face=extra_face)

if __name__ == "__main__":
    write_moods("dev", SPEC, sys.argv[1], moods=("neutral", "smile", "sad"))
