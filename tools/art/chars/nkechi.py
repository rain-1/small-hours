"""Nkechi Adeyemi, 58 — midwife at Halfmoon Night Clinic. Close-cropped salt-and-pepper hair,
reading glasses pushed up on her head and another pair on a cord, a gold cross, plum scrubs
under a soft grey cardigan."""
import os, sys, random, math
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from portrait import *

HAIR = "#2a2430"
CX, TOP, W, H, JW = 100, 52, 80, 106, 62
SCRUB = "#7a1f52"
CARD = "#6f7896"
GOLD = "#ffd27a"


def crop_hair(extra=0):
    # short natural crop with a soft, slightly bumpy silhouette and a rounded hairline
    return (f"M{59 - extra},104 Q52,78 58,62 Q62,48 76,44 Q88,38 100,39 Q112,38 124,44 Q138,48 142,62 Q148,78 {141 + extra},104 "
            f"Q140,86 134,78 Q130,70 118,68 Q108,66 100,67 Q92,66 82,68 Q70,70 66,78 Q60,86 {59 - extra},104 Z")


def back_hair(s):
    return path("M60,108 Q52,44 100,39 Q148,44 140,108 Z", HAIR)


def clothes(s):
    rim = s["rim"]
    card_d = shade(CARD, 0.72)
    return (
        bust(100, 172, 76, CARD, dark=card_d) +
        # plum scrub top, deep V
        path("M72,170 L128,170 L122,240 L78,240 Z", SCRUB) +
        path("M80,170 L100,204 L120,170 Z", shade(s["skin"], 0.85)) +
        path("M80,170 L100,204 L120,170", stroke=shade(SCRUB, 0.65), stroke_width=3, stroke_linejoin="round") +
        # breast pocket with pens and a penlight
        rect(108, 214, 16, 14, shade(SCRUB, 0.85)) + line(112, 206, 112, 216, "#e6e8ef", 2) + line(117, 208, 117, 216, "#4fc0e8", 2) +
        # cardigan fronts
        path("M72,170 L84,240 L56,240 L52,190 Z", CARD) + path("M128,170 L116,240 L144,240 L148,190 Z", shade(CARD, 1.08)) +
        path("M72,170 L84,240 M128,170 L116,240", stroke=card_d, stroke_width=2.5) +
        # gold cross on a fine chain
        path("M86,172 Q100,200 114,172", stroke=GOLD, stroke_width=0.9) +
        g(rect(98.6, 194, 2.8, 11, GOLD), rect(95.5, 197, 9, 2.6, GOLD)) +
        # second pair of glasses hanging on a cord
        path("M76,170 Q84,210 90,216 M124,170 Q118,208 112,214", stroke="#e0802a", stroke_width=0.9) +
        g(ellipse(93, 219, 6, 4.5, "none", stroke="#3a2a22", stroke_width=1.4),
          ellipse(108, 217, 6, 4.5, "none", stroke="#3a2a22", stroke_width=1.4),
          line(99, 218, 102, 218, "#3a2a22", 1.2), ellipse(108, 217, 5, 3.5, "#d2f0e2", opacity=0.25)) +
        path("M130,171 Q168,176 176,198 L180,236", stroke=rim, stroke_width=2, opacity=0.55)
    )


def front_hair(s):
    rnd = random.Random(58)
    o = [path(crop_hair(), HAIR)]
    # soft coily texture along the outer edge
    for i in range(15):
        a = math.pi * (1.05 + i * 0.9 / 14)
        o.append(circle(round(100 + 44 * math.cos(a), 1), round(76 + 36 * math.sin(a), 1), 5, HAIR))
    # salt and pepper: grey flecks, thicker at the temples
    for _ in range(260):
        x, y = rnd.uniform(56, 144), rnd.uniform(40, 104)
        if (x - 100) ** 2 / 44 ** 2 + (y - 74) ** 2 / 36 ** 2 > 1:
            continue
        if y > 66 and 72 < x < 128:
            continue
        temple = abs(x - 100) > 30
        if temple or rnd.random() < 0.5:
            o.append(rect(round(x), round(y), 1, 1, "#bec2d1" if temple else "#6f7896"))
    # reading glasses pushed up onto her head
    o.append(g(ellipse(84, 62, 10, 6, "#d2f0e2", opacity=0.18), ellipse(116, 62, 10, 6, "#d2f0e2", opacity=0.18),
               ellipse(84, 62, 10, 6, "none", stroke="#b02d6f", stroke_width=2),
               ellipse(116, 62, 10, 6, "none", stroke="#b02d6f", stroke_width=2),
               path("M94,61 Q100,58 106,61", stroke="#b02d6f", stroke_width=1.8),
               line(74, 62, 62, 70, "#b02d6f", 1.8), line(126, 62, 138, 70, "#b02d6f", 1.8)))
    o.append(path("M132,58 Q142,72 141,96", stroke=s["rim"], stroke_width=1.6, opacity=0.6))
    return "".join(o)


def accessories(s):
    ey = TOP + H * 0.53 + 13
    return circle(CX - W / 2 + 0, ey, 2, GOLD) + circle(CX + W / 2 - 0, ey, 2, GOLD)


def extra_face(s, mood):
    d = shade(s["skin"], 0.7)
    hi = shade(s["skin"], 1.3)
    my = TOP + H * 0.83
    o = [path(f"M78,{my - 14} q-4,7 -1,15", stroke=d, stroke_width=1.2, opacity=0.4),
         path(f"M122,{my - 14} q4,7 1,15", stroke=d, stroke_width=1.2, opacity=0.4),
         # cheekbone highlights
         ellipse(78, 120, 7, 3, hi, opacity=0.25), ellipse(122, 120, 7, 3, hi, opacity=0.25)]
    if mood in ("neutral", "sad"):  # full lower lip
        o.append(ellipse(CX, my + 3.2, 6.5, 2.3, "#8a4038", opacity=0.9))
        o.append(ellipse(CX + 1, my + 2.8, 2.5, 0.8, "#c98d6a", opacity=0.6))
    return "".join(o)


SPEC = dict(skin="#6b3f2a", hair=HAIR, iris="#1a0d08", rim="#9bd6c4", brow_color="#1d1518", brow_thick=2.2, brow_len=10,
            age=1, eye_size=0.92, head=dict(cx=CX, top=TOP, w=W, h=H, jw=JW, chin=0.2), neck_w=24, lid="#140a08",
            nose="broad", nose_y=0.68, mouth_w=1.1, blush="#b85c1c", mouth_style={"neutral": None},
            back_hair=back_hair, clothes=clothes, front_hair=front_hair, accessories=accessories,
            extra_face=extra_face)

if __name__ == "__main__":
    write_moods("nkechi", SPEC, sys.argv[1], moods=("neutral", "smile", "sad"))
