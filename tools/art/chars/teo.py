"""Teodor "Teo" Novak-Banerjee, 34 — data rater above the laundromat. Tall and stooped,
too-long dark curls, blue-light glasses, a cardigan with elbow patches over an old tee."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from portrait import *

HAIR = "#2e1f1c"
HAIR_D = "#1d1312"
HAIR_L = "#5a4334"
CX, TOP, W, H, JW = 100, 50, 70, 106, 50


def curls(pts, r_rng, col, seed, hl=True):
    rnd = random.Random(seed)
    o = []
    for (x, y) in pts:
        r = rnd.uniform(*r_rng)
        o.append(circle(x, y, r, col))
        if hl:
            o.append(path(f"M{x - r * 0.6},{y - r * 0.1} Q{x - r * 0.2},{y - r * 0.8} {x + r * 0.5},{y - r * 0.5}",
                          stroke=HAIR_L, stroke_width=1.2, opacity=0.8))
    return "".join(o)


def back_hair(s):
    # big soft mass of curls behind the head, falling past the ears to the nape
    pts = [(62, 64), (58, 82), (60, 100), (66, 114), (138, 64), (142, 82), (140, 100), (134, 114),
           (76, 42), (92, 36), (110, 36), (126, 44)]
    return (ellipse(100, 78, 44, 44, HAIR_D) +
            curls(pts, (10, 13), HAIR_D, 3, hl=False) +
            curls([(61, 96), (140, 98), (68, 118), (133, 118)], (6, 8), HAIR, 4))


def clothes(s):
    tee = "#3b4260"
    card = "#a08870"
    card_d = shade(card, 0.72)
    rim = s["rim"]
    return (
        # narrow, sloping, slightly stooped shoulders
        path("M30,240 L36,198 Q44,174 78,168 L122,168 Q156,174 164,198 L170,240 Z", card) +
        path("M30,240 L36,198 Q44,174 78,168 L84,240 Z", card_d, opacity=0.7) +
        # tee in the V
        path("M84,166 L116,166 L110,206 L100,222 L90,206 Z", tee) +
        path("M86,165 Q100,178 114,165", stroke=shade(tee, 0.7), stroke_width=3) +
        # tiny faded print on the tee (a little moon)
        circle(100, 206, 5, "#6f7896", opacity=0.7) + circle(102, 204, 4, tee) +
        # cardigan fronts, overlapping into a V
        path("M78,168 L100,226 L100,240 L68,240 L66,190 Z", card) +
        path("M122,168 L100,226 L100,240 L134,240 L136,190 Z", shade(card, 1.06)) +
        path("M78,168 L100,226 M122,168 L100,226", stroke=card_d, stroke_width=3) +
        path("M77,174 L99,227", stroke="#c9b49a", stroke_width=1, opacity=0.7) +
        # ribbing texture
        "".join(line(70 + i * 3, 200, 70 + i * 3, 240, card_d, 0.6, opacity=0.35) for i in range(4)) +
        # buttons
        circle(104, 232, 2.2, "#5a4334") + circle(103.4, 231.4, 0.8, "#c9b49a") +
        # pen + glasses-cloth in the breast pocket
        rect(122, 206, 16, 14, shade(card, 0.85), rx=1) +
        line(126, 198, 126, 210, "#e04a3a", 2.4) + line(131, 200, 131, 210, "#1f5f8a", 2) +
        # a stray leaf from the plant he talks to
        path("M150,200 q6,-6 10,0 q-6,4 -10,0 Z", "#4f8f45") + line(150, 200, 156, 200, "#2f6a35", 0.6) +
        # rim light on the right shoulder
        path("M124,169 Q156,174 164,198 L168,232", stroke=rim, stroke_width=2, opacity=0.55)
    )


def front_hair(s):
    # a tumbling fringe of curls, longer on his left, over the forehead and ears
    pts = [(68, 62), (80, 50), (95, 44), (110, 46), (124, 52), (133, 66), (64, 78), (76, 64), (90, 58), (104, 58),
           (118, 62), (136, 82), (63, 94)]
    return (path(f"M64,96 Q60,42 100,40 Q140,42 136,96 Q130,68 100,66 Q72,68 64,96 Z", HAIR) +
            curls(pts, (7, 10), HAIR, 7) +
            curls([(84, 68), (98, 70), (111, 67)], (5, 6.5), HAIR, 8) +
            # one loose ringlet dropping onto the brow
            path("M96,72 q-4,6 1,10 q4,3 1,6", stroke=HAIR, stroke_width=2.6, stroke_linecap="round"))


def accessories(s):
    ey = TOP + H * 0.53
    ex = W * 0.215
    # blue-light glasses: soft rectangles, faint blue sheen
    return (glasses(CX, ey + 1, ex, 10.5, 8, "#3a2a22", shape="soft", width=1.8, tint="#4fc0e8", tint_op=0.07,
                    glint="#a8fff6") +
            line(CX - ex - 10.5, ey - 1, CX - W / 2 + 1, ey - 3, "#3a2a22", 1.6) +
            line(CX + ex + 10.5, ey - 1, CX + W / 2 - 1, ey - 3, "#3a2a22", 1.6))


def extra_face(s, mood):
    d = shade(s["skin"], 0.62)
    return (stubble(CX, TOP, W, H, JW, "#2e1f1c", op=0.32, seed=11) +
            # tired under-eye shadows (nights of rating queues)
            path("M78,121 Q85,124 92,121", stroke=d, stroke_width=1, opacity=0.4) +
            path("M108,121 Q115,124 122,121", stroke=d, stroke_width=1, opacity=0.4))


SPEC = dict(skin="#d6a47c", hair=HAIR, iris="#3a2a22", rim="#4fc0e8", brow_color="#2e1f1c", brow_thick=2.4,
            brow_len=10, eye_size=0.95, head=dict(cx=CX, top=TOP, w=W, h=H, jw=JW, chin=0.6), neck_w=22,
            nose="long", mouth_w=0.85, mouth_style={"smile": "closed"}, brow_mood={"neutral": "worried"},
            back_hair=back_hair, clothes=clothes, front_hair=front_hair, accessories=accessories,
            extra_face=extra_face)

if __name__ == "__main__":
    write_moods("teo", SPEC, sys.argv[1], moods=("neutral", "smile", "sad", "surprised"))
