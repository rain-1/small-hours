"""Dr Imogen Hale, 41 — alignment researcher at Kestrel, sitting on the stairs. Short dark bob
wet with rain, freckles, a soaked trench coat over a lab hoodie, a lanyard she keeps touching,
an unlit cigarette tucked behind her ear."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from portrait import *

HAIR = "#241a1e"
HAIR_L = "#5d4f8c"
CX, TOP, W, H, JW = 100, 54, 74, 100, 52
COAT = "#b09a78"
COAT_D = "#7d6450"


def back_hair(s):
    # the back of the bob, cut level just under the jaw
    return path("M58,96 Q54,52 100,50 Q146,52 142,96 L144,150 Q130,156 120,150 L120,120 L80,120 L80,150 Q70,156 56,150 Z", HAIR)


def clothes(s):
    rim = s["rim"]
    hood = "#3b4260"
    o = [
        # trench coat: wide lapels, epaulettes, darker where the rain soaked through
        bust(100, 170, 80, COAT, dark=COAT_D),
        # lab hoodie underneath, hood bunched at the collar
        path("M74,166 L126,166 L118,240 L82,240 Z", hood),
        path("M76,164 Q100,190 124,164 Q100,174 76,164 Z", shade(hood, 0.75)),
        path("M92,180 l-1,24 M108,180 l1,22", stroke="#bec2d1", stroke_width=1.6, stroke_linecap="round"),
        # lapels
        path("M70,164 L92,212 L78,240 L58,240 L50,186 Z", COAT),
        path("M130,164 L108,212 L122,240 L142,240 L150,186 Z", shade(COAT, 1.08)),
        path("M70,164 L92,212 L80,222 M130,164 L108,212 L120,222", stroke=COAT_D, stroke_width=1.6),
        path("M58,190 L68,196 M142,190 L132,196", stroke=COAT_D, stroke_width=1.2),
        # epaulettes
        path("M30,190 L58,180 L60,186 L32,196 Z", shade(COAT, 0.88)),
        path("M170,190 L142,180 L140,186 L168,196 Z", shade(COAT, 0.95)),
        circle(56, 183, 1.6, "#3a2a22"), circle(144, 183, 1.6, "#3a2a22"),
        # wet patches on the shoulders
        path("M34,200 Q46,190 60,192 Q52,204 38,210 Z", COAT_D, opacity=0.4),
        path("M150,196 Q160,198 166,208 Q156,208 148,204 Z", COAT_D, opacity=0.35),
        # Kestrel lanyard and badge
        path("M84,170 L96,222 M116,170 L104,222", stroke="#2f8fc0", stroke_width=3),
        rect(90, 220, 20, 20, "#e6e8ef", rx=2), rect(93, 223, 14, 6, "#2f8fc0"),
        circle(100, 234, 3, "#4fc0e8"),
        path("M130,165 Q170,170 178,196 L182,236", stroke=rim, stroke_width=2, opacity=0.55),
    ]
    # raindrops beaded on the coat
    rnd = random.Random(5)
    for _ in range(14):
        x, y = rnd.choice([(rnd.uniform(28, 70), rnd.uniform(196, 236)), (rnd.uniform(130, 172), rnd.uniform(196, 236))])
        o.append(rect(round(x), round(y), 1, 2, "#e6e8ef", opacity=0.8))
    return "".join(o)


def front_hair(s):
    return (
        # side-parted bob with a heavy fringe swept to her left, ends curling in at the jaw
        path("M60,104 Q54,56 96,52 Q144,52 142,112 L144,150 Q136,146 132,136 Q136,110 128,90 Q118,74 96,76 Q82,82 76,92 "
             "Q70,98 68,106 Q64,102 60,104 Z", HAIR) +
        # strand tucked behind the ear
        path("M62,100 Q60,92 68,96", stroke=HAIR, stroke_width=3, stroke_linecap="round") +
        path("M96,54 Q110,60 116,80", stroke=HAIR_L, stroke_width=1.2, opacity=0.8) +
        path("M70,70 Q86,58 98,56", stroke=HAIR_L, stroke_width=1.4, opacity=0.9) +
        path("M134,96 Q140,120 138,144", stroke=HAIR_L, stroke_width=1, opacity=0.7) +
        # wet strands stuck to her forehead
        path("M86,78 q-2,10 2,16", stroke=HAIR, stroke_width=2.2, stroke_linecap="round") +
        path("M120,80 q4,8 3,16", stroke=HAIR, stroke_width=2, stroke_linecap="round") +
        # raindrops in her hair
        "".join(circle(x, y, 1, "#d2f0e2", opacity=0.9) for x, y in [(80, 64), (112, 60), (130, 78), (138, 120)]) +
        path("M136,62 Q146,80 144,104", stroke=s["rim"], stroke_width=1.6, opacity=0.6))


def accessories(s):
    # unlit cigarette tucked behind her right ear (viewer's left)
    ex, ey = CX - W / 2, TOP + H * 0.53
    return g(line(ex - 11, ey - 1, ex + 5, ey + 3, "#fffaf0", 2.6, stroke_linecap="round"),
             line(ex - 11, ey - 1, ex - 6, ey + 0.25, "#e0802a", 2.6, stroke_linecap="round"))


def extra_face(s, mood):
    rnd = random.Random(41)
    d = shade(s["skin"], 0.62)
    o = []
    # freckles across the nose and cheeks
    for _ in range(20):
        sd = rnd.choice((-1, 1))
        x = CX + sd * rnd.uniform(3, 22)
        y = TOP + H * 0.62 + rnd.uniform(-3, 6) + abs(x - CX) * 0.1
        o.append(rect(round(x), round(y), 1, 1, "#4e2c1e"))
    # tired shadows under the eyes
    o.append(path("M80,118 Q87,121 94,118", stroke=d, stroke_width=1, opacity=0.45))
    o.append(path("M106,118 Q113,121 120,118", stroke=d, stroke_width=1, opacity=0.45))
    return "".join(o)


SPEC = dict(skin="#b77d58", hair=HAIR, iris="#5e2a12", rim="#a99ad0", brow_color="#241a1e", brow_thick=2.6, brow_len=10,
            eye_size=0.95, head=dict(cx=CX, top=TOP, w=W, h=H, jw=JW, chin=0.5), neck_w=22,
            mouth_w=0.85, mouth_style={"smile": "wry"}, smile_open=True, brow_mood={"smile": "neutral"},
            back_hair=back_hair, clothes=clothes, front_hair=front_hair, accessories=accessories,
            extra_face=extra_face)

if __name__ == "__main__":
    write_moods("imogen", SPEC, sys.argv[1], moods=("neutral", "smile", "sad", "surprised"))
