"""June Takahashi-Reyes, 16 — swarm wrangler on the roof. Two buns, blunt fringe, an oversized
hoodie with hand-drawn patches, a glowing frog LED pin, a cheap AR monocle."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from portrait import *

HAIR = "#1d1520"
HAIR_L = "#463a70"
CX, TOP, W, H, JW = 100, 66, 74, 88, 54
HOOD = "#6f5fa6"
HOOD_D = shade(HOOD, 0.72)


def back_hair(s):
    return (
        # two buns, slightly lopsided, with a few escaping strands
        circle(68, 56, 17, HAIR) + circle(133, 54, 16, HAIR) +
        path("M58,48 Q66,40 76,46", stroke=HAIR_L, stroke_width=1.4) +
        path("M124,44 Q132,38 142,46", stroke=HAIR_L, stroke_width=1.4) +
        path("M54,62 q-6,6 -3,12", stroke=HAIR, stroke_width=1.4) +
        path("M146,58 q6,4 5,12", stroke=HAIR, stroke_width=1.4) +
        # scrunchies
        path("M74,68 q8,-2 12,-8", stroke="#4ff0e6", stroke_width=3.5, stroke_linecap="round") +
        path("M126,66 q-8,-2 -12,-8", stroke="#ff5fa2", stroke_width=3.5, stroke_linecap="round") +
        # side hair down to the jaw
        path("M62,100 Q58,62 100,60 Q142,62 138,100 L140,140 Q132,146 126,138 L126,108 L74,108 L74,138 Q68,146 60,140 Z", HAIR))


def clothes(s):
    rim = s["rim"]
    return (
        # hood bunched up behind the neck
        path("M56,184 Q60,152 100,150 Q140,152 144,184 Z", HOOD_D) +
        # oversized, drooping shoulders
        path("M14,240 L20,204 Q28,176 72,168 L128,168 Q172,176 180,204 L186,240 Z", HOOD) +
        path("M14,240 L20,204 Q28,176 72,168 L80,240 Z", HOOD_D, opacity=0.6) +
        # neck opening + drawstrings
        path("M78,166 Q100,186 122,166 Q100,176 78,166 Z", HOOD_D) +
        path("M90,178 q-2,18 1,32", stroke="#f6e7c8", stroke_width=2, stroke_linecap="round") +
        path("M110,178 q2,16 -1,28", stroke="#f6e7c8", stroke_width=2, stroke_linecap="round") +
        rect(89, 208, 4, 5, "#c9b49a") + rect(107, 204, 4, 5, "#c9b49a") +
        # hand-drawn patches: wonky star, mushroom, "404"
        g(poly([(40, 206), (44, 214), (53, 214), (46, 219), (49, 228), (40, 222), (31, 228), (34, 219), (27, 214), (36, 214)], "#ffd27a"),
          path("M40,206 L44,214 L53,214 L46,219 L49,228 L40,222 L31,228 L34,219 L27,214 L36,214 Z", stroke="#e0802a", stroke_width=1)) +
        g(rect(136, 214, 22, 16, "#173a4a", rx=2), text(147, 226, "404", "#4ff0e6", size=8, family="DejaVu Sans Mono"),
          rect(136, 214, 22, 16, "none", stroke="#f6e7c8", stroke_width=1, rx=2, stroke_dasharray="2,2")) +
        g(path("M60,232 Q66,222 72,232 Z", "#e04a3a"), rect(64, 232, 4, 6, "#f6e7c8"), circle(64, 228, 1.2, "#fffaf0"), circle(69, 229, 1, "#fffaf0")) +
        # LED frog pin, glowing
        g(ellipse(126, 190, 7, 5.5, "#7fb85a"), circle(122, 186, 2.6, "#b8de7a"), circle(130, 186, 2.6, "#b8de7a"),
          circle(122, 186, 1, "#14301e"), circle(130, 186, 1, "#14301e"),
          path("M122,192 Q126,194 130,192", stroke="#14301e", stroke_width=0.8), filter="url(#glow)") +
        # rim light along the right shoulder
        path("M130,169 Q172,176 180,204 L185,236", stroke=rim, stroke_width=2, opacity=0.6)
    )


def front_hair(s):
    return (path("M64,108 Q58,62 100,62 Q142,62 136,108 Q135,94 130,86 Q126,91 121,88 Q115,93 108,86 Q101,92 94,87 Q88,92 83,86 Q77,90 72,88 Q66,94 64,108 Z", HAIR) +
            path("M76,72 Q96,64 120,70", stroke=HAIR_L, stroke_width=1.6, opacity=0.9) +
            # a couple of flyaway strands
            path("M104,62 q6,-8 14,-8", stroke=HAIR, stroke_width=1.3) +
            path("M86,64 q-4,-8 -2,-14", stroke=HAIR, stroke_width=1.2))


def accessories(s):
    ey = TOP + H * 0.53
    ex = W * 0.215
    x = CX + ex
    # cheap AR monocle over her left eye, with a strap to the ear and a little HUD glint
    return (path(f"M{x + 10},{ey - 2} L{CX + W / 2 + 2},{ey - 6}", stroke="#2a2f45", stroke_width=2.2) +
            rect(CX + W / 2 - 2, ey - 10, 7, 9, "#3b4260", rx=2) + rect(CX + W / 2, ey - 8, 2, 2, "#ff5fa2") +
            circle(x, ey, 10, "#4ff0e6", opacity=0.22) +
            circle(x, ey, 10, "none", stroke="#2a2f45", stroke_width=2.2) +
            circle(x, ey, 10, "none", stroke="#4ff0e6", stroke_width=0.8, opacity=0.8, filter="url(#glow)") +
            rect(x - 6, ey - 6, 5, 1, "#a8fff6", opacity=0.9) + rect(x - 6, ey - 4, 3, 1, "#a8fff6", opacity=0.7) +
            # gold stud earring on the left ear
            circle(CX - W / 2 + 1, ey + 12, 1.6, "#ffd27a"))


def extra_face(s, mood):
    return ""


SPEC = dict(skin="#e8bb94", hair=HAIR, iris="#3a1a10", rim="#4ff0e6", brow_color="#1d1520", brow_thick=2.2, brow_len=8,
            eye_size=1.15, eye_y=0.55, head=dict(cx=CX, top=TOP, w=W, h=H, jw=JW, chin=0.4), neck_w=20,
            nose="button", nose_y=0.71, mouth_w=0.8, blush="#ff5fa2",
            mouth_style={"surprised": "gasp"},
            back_hair=back_hair, clothes=clothes, front_hair=front_hair, accessories=accessories,
            extra_face=extra_face)

if __name__ == "__main__":
    write_moods("june", SPEC, sys.argv[1], moods=("neutral", "smile", "sad", "surprised"))
