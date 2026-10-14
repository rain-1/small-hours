"""Small full-body FIGURE sprites for placing characters inside interior scenes.

  python3 tools/art/figures.py art_src/figures game/art/figures/figures.json
  then for each: <python-with-numpy> tools/art/render.py art_src/figures/<name>.svg game/art/figures/<name>.png

Scale: a standing adult is ~110px tall; feet (or the seat contact for floor-sitters) sit on the
bottom edge, horizontally centred. Simplified versions of the portrait designs: same clothing
colours, hair and accessories, light from the right with a 1px neon rim in each character's colour.
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from svg import *
from portrait import shade

FIGS = {}


def fig(name, w, h):
    def deco(fn):
        FIGS[name] = (w, h, fn)
        return fn
    return deco


def limb(pts, w, col, **kw):
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    return path(d, stroke=col, stroke_width=w, stroke_linecap="round", stroke_linejoin="round", **kw)


def rim(d, col, w=1.2, op=0.85):
    return path(d, stroke=col, stroke_width=w, opacity=op, stroke_linecap="round")


def face(cx, cy, rx, ry, skin, eyes=True, look=0, eye_dy=0, eye_col="#1a0f0c", gap=3.2):
    """Simple face: oval, left-side shade, two dot eyes."""
    o = [ellipse(cx, cy, rx, ry, skin),
         path(f"M{cx - rx},{cy} A{rx},{ry} 0 0 0 {cx - rx * 0.1},{cy + ry} Q{cx - rx * 0.55},{cy} {cx - rx * 0.1},{cy - ry} A{rx},{ry} 0 0 0 {cx - rx},{cy} Z",
              shade(skin, 0.8), opacity=0.5)]
    if eyes:
        ey = cy + eye_dy
        o.append(rect(round(cx - gap + look - 0.5), round(ey), 1.5, 2, eye_col))
        o.append(rect(round(cx + gap + look - 1), round(ey), 1.5, 2, eye_col))
    return "".join(o)


def shadow(cx, y, rx):
    return ellipse(cx, y, rx, 2, "#0d0b1a", opacity=0.35)


# ---------------------------------------------------------------------------------------------
@fig("lu_counter", 54, 104)
def lu_counter():
    skin, hair, hair_d = "#ecc39e", "#bec2d1", "#949bb3"
    sweat, apron, R = "#5d4f8c", "#b02a2a", "#ffb347"
    cx = 27
    o = [shadow(cx, 102, 14)]
    # legs + clogs
    o += [limb([(23, 70), (23, 98)], 7, "#2a2f45"), limb([(31, 70), (31, 98)], 7, "#262043"),
          ellipse(22, 101, 5, 2.6, "#5e2a12"), ellipse(32, 101, 5, 2.6, "#8a3f16")]
    # torso: sturdy sweatshirt
    o.append(path("M14,36 Q16,30 27,30 Q38,30 40,36 L42,72 L12,72 Z", sweat))
    o.append(path("M14,36 Q16,30 22,30 L20,72 L12,72 Z", shade(sweat, 0.75), opacity=0.7))
    # arms: one resting on the (scene) counter, one holding a ladle
    o.append(limb([(15, 36), (12, 50), (18, 58)], 6, sweat))
    o.append(limb([(39, 36), (42, 48), (36, 56)], 6, shade(sweat, 1.1)))
    o.append(circle(19, 58, 2.6, skin) + circle(35, 56, 2.6, skin))
    # burn-scarred forearm hint
    o.append(line(14, 52, 17, 55, shade(skin, 0.7), 1))
    # ladle
    o.append(line(36, 56, 44, 42, "#949bb3", 1.5) + ellipse(45, 41, 3, 2, "#bec2d1"))
    # apron with pocket
    o.append(path("M17,44 L37,44 L39,78 L15,78 Z", apron))
    o.append(path("M17,44 L14,32 M37,44 L40,32", stroke=apron, stroke_width=2.2))
    o.append(rect(21, 56, 12, 7, shade(apron, 0.8)))
    o.append(line(24, 52, 24, 57, "#c9b49a", 1) + line(26, 51, 26, 57, "#c9b49a", 1))
    # head: bun + fish clip, glasses
    o.append(circle(cx, 8, 6, hair_d))
    o.append(rect(cx - 3, 26, 6, 5, shade(skin, 0.78)))
    o.append(face(cx, 19, 8, 9, skin, eye_dy=1))
    o.append(path("M19,19 Q18,9 27,8 Q36,9 35,19 Q33,13 27,13 Q21,13 19,19 Z", hair))
    o.append(path("M31,4 q4,-2 7,0 q-3,2 -7,0 Z", R) + poly([(38, 4), (40, 2.5), (40, 5.5)], "#e0802a"))
    o.append(circle(23.3, 21, 2.4, "none", stroke="#8a5236", stroke_width=0.9) + circle(30.7, 21, 2.4, "none", stroke="#8a5236", stroke_width=0.9))
    o.append(rect(25, 26, 4, 1, "#7a1a1e", opacity=0.7))
    # rim light
    o.append(rim("M35,14 Q36,20 33,26", R) + rim("M40,34 L42,72", R) + rim("M33,4 Q34,8 32,12", R, 1))
    return "".join(o)


@fig("teo_desk", 62, 92)
def teo_desk():
    skin, hair, card, tee, R = "#d6a47c", "#2e1f1c", "#a08870", "#3b4260", "#4fc0e8"
    o = [shadow(30, 90, 20)]
    # office chair (side view): wheels, gas lift, seat, back
    o += [line(14, 86, 40, 86, "#1a1d2b", 2.5), circle(15, 88, 2, "#2a2f45"), circle(39, 88, 2, "#2a2f45"), circle(27, 88, 2, "#2a2f45"),
          rect(25, 66, 4, 20, "#3b4260"), rect(12, 60, 30, 6, "#2a2f45", rx=2),
          limb([(14, 62), (10, 44), (12, 28)], 4, "#3b4260"), rect(6, 24, 9, 28, "#2a2f45", rx=3)]
    # legs: thigh forward on the seat, shin down, slippers
    o.append(limb([(20, 58), (44, 58), (46, 84)], 8, "#2a2f45"))
    o.append(limb([(22, 56), (42, 56)], 3, shade("#2a2f45", 1.3), opacity=0.5))
    o.append(ellipse(49, 87, 6, 3, "#7a1f52"))
    # torso: hunched forward, cardigan
    o.append(path("M16,58 L26,58 Q34,44 40,30 Q36,24 28,26 Q18,34 16,44 Z", card))
    o.append(path("M16,58 L20,58 Q24,40 30,26 Q20,32 16,44 Z", shade(card, 0.72), opacity=0.7))
    o.append(path("M36,30 Q38,36 32,44", stroke=tee, stroke_width=2.5))
    # arms reaching forward to a keyboard
    o.append(limb([(32, 32), (34, 46), (50, 46)], 5.5, card))
    o.append(ellipse(34, 44, 2.6, 2, "#5a4334"))  # elbow patch
    o.append(circle(52, 46, 2.4, skin))
    # head pushed forward toward the screen (3/4 view, facing right)
    o.append(limb([(36, 28), (41, 24)], 4.5, shade(skin, 0.78)))
    o.append(ellipse(44, 17, 7, 8.5, skin))
    o.append(ellipse(41, 18, 4, 7, shade(skin, 0.8), opacity=0.5))
    for x, y, r in [(38, 10, 4.5), (43, 8, 4.5), (48, 9, 4), (36, 15, 4), (37, 21, 3.5), (51, 12, 2.5)]:
        o.append(circle(x, y, r, hair))
    o.append(path("M40,8 q2,-2 4,0 M45,7 q2,-2 3,1", stroke="#5a4334", stroke_width=0.8))
    # glasses (side) + eye, monitor-blue glint
    o.append(rect(47, 16, 4.5, 3.5, "none", stroke="#3a2a22", stroke_width=0.9) + line(42, 17, 47, 17, "#3a2a22", 0.8))
    o.append(rect(49, 17, 1.4, 1.6, "#1a0f0c") + rect(50.5, 16.5, 1, 1, R))
    o.append(rect(46, 23, 3, 1, "#3a2a22", opacity=0.4))
    # rim light: lit by the monitor on the right
    o.append(rim("M51,12 Q52,18 49,24", R) + rim("M40,30 Q36,40 30,50", R, 1) + rim("M50,44 L54,46", R, 1) + rim("M44,58 L47,82", R, 1))
    return "".join(o)


@fig("ozzie_stand", 56, 116)
def ozzie_stand():
    skin, cap, card, shirt, R = "#c48a63", "#7d6450", "#7a1a1e", "#1f5260", "#ff5fa2"
    o = [shadow(28, 114, 16)]
    # leaning back (against a car or wall on the left): body tilts, ankles crossed
    o += [limb([(26, 70), (24, 92), (30, 111)], 9, "#3a2a22"),
          limb([(32, 70), (34, 92), (22, 111)], 9, shade("#3a2a22", 1.15)),
          ellipse(20, 113, 6, 2.8, "#1a1d2b"), ellipse(32, 113, 6, 2.8, "#1a1d2b")]
    # barrel torso: cardigan open over the bowling shirt
    o.append(path("M14,38 Q16,32 28,31 Q42,31 44,40 Q47,58 42,74 L16,74 Q10,56 14,38 Z", card))
    o.append(path("M22,32 L36,32 L35,74 L23,74 Z", shirt))
    o.append(rect(30, 34, 3, 40, "#f6e7c8"))
    o.append(path("M14,38 Q16,32 22,32 L23,74 L16,74 Q10,56 14,38 Z", shade(card, 0.72), opacity=0.7))
    # arms straight down, hands in pockets
    o.append(limb([(15, 38), (12, 54), (16, 66)], 7, card))
    o.append(limb([(43, 38), (46, 54), (41, 66)], 7, shade(card, 1.12)))
    o.append(path("M14,66 L20,66 M38,66 L44,66", stroke="#2a1d18", stroke_width=1.6))
    # head: flat cap + white moustache, hearing aid
    o.append(rect(24, 27, 9, 6, shade(skin, 0.78)))
    o.append(face(28, 20, 8.5, 9, skin, eye_dy=0))
    o.append(path("M20,22 Q19,17 21,17 L22,25 Z M36,22 Q37,17 35,17 L34,25 Z", "#e6e8ef"))
    o.append(path("M19,15 Q19,6 28,6 Q38,6 38,14 Q30,12 19,15 Z", cap))
    o.append(path("M18,15 Q29,10 41,13 Q41,16 38,16 Q29,14 20,17 Z", shade(cap, 0.75)))
    o.append(path("M23,25 Q28,22 33,25 Q34,28 31,27 Q28,26 25,27 Q22,28 23,25 Z", "#e6e8ef"))
    o.append(path("M23,19 l3,0 M30,19 l3,0", stroke="#e6e8ef", stroke_width=1.2))
    o.append(circle(19.5, 22, 1, "#e3b48f"))
    o.append(rim("M37,15 Q38,22 35,28", R) + rim("M44,40 Q47,58 42,74", R) + rim("M38,14 L41,13", R, 1))
    return "".join(o)


@fig("june_sit", 56, 62)
def june_sit():
    skin, hair, hood, R = "#e8bb94", "#1d1520", "#6f5fa6", "#4ff0e6"
    o = [shadow(28, 60, 22)]
    # crossed legs (cargo pants) + sneakers
    o.append(path("M8,58 Q8,48 20,48 L36,48 Q48,48 48,58 Z", "#3b4260"))
    o.append(path("M10,58 Q12,51 24,52 L30,58 Z", "#2a2f45"))
    o.append(ellipse(14, 57, 5, 2.5, "#e6e8ef") + ellipse(42, 57, 5, 2.5, "#e6e8ef"))
    o.append(line(12, 56, 16, 56, "#ff5fa2", 0.8) + line(40, 56, 44, 56, "#ff5fa2", 0.8))
    # oversized hoodie
    o.append(path("M13,26 Q15,19 28,19 Q41,19 43,26 L46,50 L10,50 Z", hood))
    o.append(path("M13,26 Q15,19 22,19 L20,50 L10,50 Z", shade(hood, 0.72), opacity=0.7))
    o.append(circle(21, 34, 1.6, "#ffd27a") + circle(36, 30, 1.5, "#7fb85a", filter="url(#glow)"))
    # laptop on her lap, screen facing her (we see the lid back + glow)
    o.append(path("M14,47 L42,47 L44,50 L12,50 Z", "#949bb3"))
    o.append(path("M17,47 L39,47 L41,34 L19,34 Z", "#3b4260"))
    o.append(circle(29, 40, 2, "#e6e8ef", opacity=0.6))
    o.append(rect(26, 42, 6, 3, "#ffd27a", opacity=0.8))  # sticker
    o.append(ellipse(28, 30, 12, 6, R, opacity=0.18, filter="url(#soft)"))
    # arms to the keyboard, fingerless gloves
    o.append(limb([(15, 27), (12, 40), (18, 46)], 5, hood) + limb([(41, 27), (44, 40), (38, 46)], 5, shade(hood, 1.1)))
    o.append(circle(19, 46, 2, "#262043") + circle(37, 46, 2, "#262043"))
    # head: buns, fringe, AR monocle catching the screen light
    o.append(circle(20, 5, 4.5, hair) + circle(36, 5, 4.5, hair))
    o.append(rect(25, 16, 6, 4, shade(skin, 0.78)))
    o.append(face(28, 11, 7, 7.5, skin, eye_dy=1, look=0))
    o.append(path("M21,12 Q20,3 28,3 Q36,3 35,12 Q34,8 31,7 L28,9 L25,7 Q22,8 21,12 Z", hair))
    o.append(path("M21,12 L21,17 M35,12 L35,17", stroke=hair, stroke_width=2))
    o.append(circle(31.5, 12.5, 2.4, R, opacity=0.5) + circle(31.5, 12.5, 2.4, "none", stroke="#2a2f45", stroke_width=0.8))
    o.append(rim("M35,6 Q36,12 33,17", R) + rim("M43,26 L46,48", R) + rim("M40,5 Q41,7 39,9", R, 1))
    return "".join(o)


@fig("mae_stand", 52, 114)
def mae_stand():
    skin, hair, hair_d, den, R = "#f2cdb6", "#d2d6e0", "#949bb3", "#2f8fc0", "#ff7a5a"
    o = [shadow(26, 112, 15)]
    # legs: black jeans, boots; leg brace on her right leg (viewer's left)
    o += [limb([(21, 66), (20, 90), (20, 108)], 7.5, "#2a2f45"), limb([(31, 66), (33, 90), (34, 108)], 7.5, "#262043"),
          ellipse(19, 110, 5, 3, "#3a2a22"), ellipse(35, 110, 5, 3, "#3a2a22")]
    o += [rect(16, 82, 9, 16, "#949bb3", rx=1), rect(16, 84, 9, 2, "#1a1d2b"), rect(16, 94, 9, 2, "#1a1d2b"),
          circle(17.5, 90, 1.4, "#525a7a"), line(17, 78, 17, 102, "#bec2d1", 1)]
    # denim jacket over black tee
    o.append(path("M14,36 Q16,30 26,30 Q36,30 38,36 L40,68 L12,68 Z", den))
    o.append(path("M22,31 L30,31 L29,68 L23,68 Z", "#262043"))
    o.append(path("M14,36 Q16,30 22,30 L23,68 L12,68 Z", shade(den, 0.7), opacity=0.7))
    for x, y, c in [(17, 42, "#ff5fa2"), (19, 50, "#ffd27a"), (34, 44, "#4ff0e6"), (33, 52, "#e04a3a")]:
        o.append(circle(x, y, 1.3, c))
    # arms: left hangs, right hand on hip (elbow out)
    o.append(limb([(15, 36), (12, 52), (13, 64)], 5.5, den) + circle(13, 65, 2.4, skin))
    o.append(limb([(37, 36), (45, 48), (37, 58)], 5.5, shade(den, 1.12)) + circle(36, 58, 2.4, skin))
    # headphones round her neck
    o.append(ellipse(21, 31, 3.5, 3, "#2a2f45") + ellipse(31, 31, 3.5, 3, "#2a2f45") + path("M21,29 Q26,26 31,29", stroke="#1a1d2b", stroke_width=1.5))
    # head: buzzed side, long silver sweep
    o.append(rect(23, 25, 6, 5, shade(skin, 0.78)))
    o.append(face(26, 18, 7.5, 8.5, skin, eye_dy=1))
    o.append(path("M18.5,18 Q18,9 25,8 L23,13 Q20,14 19.5,18 Z", hair_d))
    o.append(path("M21,11 Q25,6 31,8 Q36,10 35,18 Q34,24 33,26 Q32,20 30,16 Q26,13 21,14 Z", hair))
    o.append(circle(18.5, 20, 0.8, "#ffd27a"))
    o.append(rim("M35,12 Q36,18 33,25", R) + rim("M38,36 L40,68", R) + rim("M45,48 L41,54", R, 1))
    return "".join(o)


@fig("imogen_sit", 46, 68)
def imogen_sit():
    skin, hair, coat, R = "#b77d58", "#241a1e", "#b09a78", "#a99ad0"
    o = [shadow(23, 66, 14)]
    # sitting on a step (seat ~20px above the feet): knees up, arms wrapped round them
    o.append(path("M10,48 Q8,40 14,38 L34,38 Q38,40 36,48 Z", shade(coat, 0.8)))   # coat tails on the step
    # shins + sneakers
    o += [limb([(17, 26), (16, 62)], 7, "#3b4260"), limb([(29, 26), (30, 62)], 7, "#2a2f45"),
          ellipse(15, 64, 4.5, 2.4, "#e6e8ef"), ellipse(31, 64, 4.5, 2.4, "#bec2d1")]
    # torso behind the knees: trench coat
    o.append(path("M11,22 Q13,16 23,16 Q33,16 35,22 L37,44 L9,44 Z", coat))
    o.append(path("M11,22 Q13,16 18,16 L18,44 L9,44 Z", shade(coat, 0.72), opacity=0.7))
    o.append(path("M19,17 L23,26 L27,17 Z", "#3b4260"))
    # knees (front) and arms wrapped round them
    o.append(ellipse(17, 26, 5, 4.5, "#3b4260") + ellipse(29, 26, 5, 4.5, "#2a2f45") + rect(14, 23, 5, 1.2, "#525a7a") + rect(26, 23, 5, 1.2, "#3b4260"))
    o.append(limb([(12, 22), (10, 31), (22, 33), (34, 31)], 5, coat))
    o.append(limb([(34, 22), (37, 28), (34, 31)], 5, shade(coat, 1.1)))
    o.append(circle(23, 32.5, 2.2, skin) + circle(27, 32, 2.2, skin))
    # unlit cigarette between two fingers
    o.append(line(27, 32, 32, 30, "#fffaf0", 1.2) + rect(32, 29.4, 1.2, 1.2, "#e0802a"))
    # lanyard
    o.append(path("M20,18 L23,28 L26,18", stroke="#2f8fc0", stroke_width=1))
    # head: bob, freckles too small to see; tilted down onto her knees a little
    o.append(rect(20, 12, 6, 5, shade(skin, 0.78)))
    o.append(path("M15,12 Q14,0 23,0 Q32,0 31,12 L31,15 L28,15 L28,6 L18,6 L18,15 L15,15 Z", hair))
    o.append(face(23, 8, 6.5, 7, skin, eye_dy=1.5))
    o.append(path("M16,8 Q16,0 23,0 Q30,0 30,8 Q27,3 21,4 Q18,5 16,8 Z", hair))
    o.append(path("M16.5,8 L16.5,14 M29.5,8 L29.5,14", stroke=hair, stroke_width=2))
    o.append(rim("M31,4 Q32,10 31,16", R) + rim("M35,22 L37,44", R) + rim("M37,27 L35,31", R, 1))
    return "".join(o)


@fig("nkechi_stand", 50, 120)
def nkechi_stand():
    skin, hair, scrub, card, R = "#6b3f2a", "#2a2430", "#7a1f52", "#6f7896", "#9bd6c4"
    o = [shadow(25, 118, 14)]
    # tall: scrub trousers, white sneakers with neon laces
    o += [limb([(20, 70), (20, 96), (20, 114)], 7.5, scrub), limb([(30, 70), (30, 96), (30, 114)], 7.5, shade(scrub, 1.12)),
          ellipse(19, 116, 5, 2.6, "#e6e8ef"), ellipse(31, 116, 5, 2.6, "#e6e8ef"),
          line(17, 115, 21, 115, "#4ff0e6", 1), line(29, 115, 33, 115, "#ff5fa2", 1)]
    # scrub top + long cardigan
    o.append(path("M13,38 Q15,32 25,32 Q35,32 37,38 L39,76 L11,76 Z", card))
    o.append(path("M20,33 L30,33 L29,70 L21,70 Z", scrub))
    o.append(path("M21,33 L25,40 L29,33 Z", shade(skin, 0.85)))
    o.append(path("M13,38 Q15,32 20,32 L20,76 L11,76 Z", shade(card, 0.72), opacity=0.7))
    o.append(rect(24.2, 40, 1.4, 4, "#ffd27a") + rect(23, 41, 3.8, 1.2, "#ffd27a"))
    # calm arms: folded, hands resting
    o.append(limb([(14, 38), (12, 52), (24, 56), (34, 52)], 6, card))
    o.append(limb([(36, 38), (38, 50), (32, 54)], 6, shade(card, 1.1)))
    o.append(circle(33, 52, 2.4, skin) + circle(17, 54, 2.2, skin))
    # glasses on a cord
    o.append(path("M21,34 Q25,46 29,34", stroke="#e0802a", stroke_width=0.7))
    # head: cropped salt-and-pepper hair, glasses pushed up
    o.append(rect(22, 26, 6, 7, shade(skin, 0.8)))
    o.append(face(25, 18, 7.5, 9, skin, eye_dy=1, eye_col="#0d0b1a"))
    o.append(path("M17.5,16 Q16,6 25,6 Q34,6 32.5,16 Q31,11 25,11 Q19,11 17.5,16 Z", hair))
    for x, y in [(19, 11), (22, 8), (28, 8), (31, 12), (25, 7), (18, 14), (32, 14)]:
        o.append(rect(x, y, 1, 1, "#bec2d1"))
    o.append(rect(19, 10, 5, 2.4, "none", stroke="#b02d6f", stroke_width=0.9, rx=1) + rect(26, 10, 5, 2.4, "none", stroke="#b02d6f", stroke_width=0.9, rx=1))
    o.append(circle(17.5, 21, 0.8, "#ffd27a") + circle(32.5, 21, 0.8, "#ffd27a"))
    o.append(rect(23, 23.5, 4, 1.2, "#8a4038"))
    o.append(rim("M32,11 Q33,18 31,25", R) + rim("M37,38 L39,76", R) + rim("M30,72 L30,112", R, 1, 0.6))
    return "".join(o)


@fig("hollis_sit", 52, 86)
def hollis_sit():
    skin, teal, root, knit, R = "#7d4c36", "#3f8f8f", "#1a1418", "#b85c1c", "#ff9cc6"
    o = [shadow(26, 84, 18)]
    # office chair, three-quarter front
    o += [line(12, 80, 40, 80, "#1a1d2b", 2.5), circle(12, 82, 2, "#2a2f45"), circle(40, 82, 2, "#2a2f45"), circle(26, 83, 2, "#2a2f45"),
          rect(24, 62, 4, 18, "#3b4260"), rect(4, 12, 44, 44, "#2a2f45", rx=6), rect(6, 14, 40, 4, "#3b4260", rx=2), rect(2, 54, 48, 8, "#3b4260", rx=3),
          rect(0, 44, 5, 3, "#1a1d2b"), rect(47, 44, 5, 3, "#1a1d2b")]
    # legs: knees toward us, feet on the floor
    o += [limb([(17, 60), (15, 76)], 7, "#2a2f45"), limb([(35, 60), (37, 76)], 7, "#262043"),
          ellipse(14, 78, 4.5, 2.4, "#3a2a22"), ellipse(38, 78, 4.5, 2.4, "#3a2a22"),
          ellipse(17, 59, 6, 5, "#3b4260"), ellipse(35, 59, 6, 5, "#2a2f45"),
          rect(13, 55, 7, 1.2, "#525a7a"), rect(31, 55, 7, 1.2, "#3b4260")]
    # huge sweater
    o.append(path("M9,30 Q11,22 26,22 Q41,22 43,30 L45,58 L7,58 Z", knit))
    o.append(path("M9,30 Q11,22 18,22 L17,58 L7,58 Z", shade(knit, 0.72), opacity=0.7))
    o.append(path("M19,22 Q26,26 33,22 Q33,19 26,19 Q19,19 19,22 Z", shade(knit, 1.1)))
    for x in (14, 38):
        o.append(path(f"M{x},34 q1.5,3 0,6 q-1.5,3 0,6 q1.5,3 0,6", stroke=shade(knit, 0.7), stroke_width=1))
    # both hands round a mug held at the chest (mug with a sticker), steam
    o.append(limb([(10, 30), (9, 44), (22, 44)], 6, knit) + limb([(42, 30), (43, 44), (30, 44)], 6, shade(knit, 1.1)))
    o.append(rect(22, 37, 8, 9, "#f6e7c8", rx=1) + path("M30,39 q3,0 3,3 q0,3 -3,3", stroke="#f6e7c8", stroke_width=1.2))
    o.append(rect(24, 40, 3, 3, "#ff5fa2"))
    o.append(circle(22, 44, 2.2, skin) + circle(30, 44, 2.2, skin))
    o.append(path("M25,35 q-2,-3 0,-6 M28,35 q2,-3 0,-6", stroke="#f6e7c8", stroke_width=0.8, opacity=0.6))
    # head: teal buzz cut, headset with mic
    o.append(rect(23, 15, 6, 5, shade(skin, 0.8)))
    o.append(face(26, 9, 7, 8, skin, eye_dy=1, eye_col="#0d0b1a"))
    o.append(path("M19,8 Q18,0 26,0 Q34,0 33,8 Q31,4 26,4 Q21,4 19,8 Z", teal))
    o.append(path("M19,8 Q19.5,6 20.5,5 M33,8 Q32.5,6 31.5,5", stroke=root, stroke_width=1))
    o.append(path("M18,10 Q18,-1 26,-1 Q34,-1 34,10", stroke="#1a1d2b", stroke_width=1.3))
    o.append(rect(32.5, 7, 3, 5, "#2a2f45", rx=1) + path("M33,12 Q32,16 28,15", stroke="#1a1d2b", stroke_width=0.9))
    o.append(rect(25, 13.5, 2, 0.8, "#bec2d1"))
    o.append(rim("M33,4 Q34,9 32,15", R) + rim("M43,30 L45,58", R) + rim("M36,58 L37,76", R, 1, 0.6))
    return "".join(o)


@fig("rafe_crouch", 74, 72)
def rafe_crouch():
    skin, hood, beard, R = "#d8b494", "#3b4260", "#4a3428", "#7fb85a"
    o = [shadow(34, 70, 30)]
    # the box / junction box he's working on (right), toolbag (left)
    o.append(rect(48, 42, 22, 26, "#a08870") + rect(48, 42, 22, 4, "#7d6450") + line(59, 42, 59, 68, "#7d6450", 1))
    o.append(rect(48, 42, 22, 26, "none", stroke="#5a4334", stroke_width=1))
    o.append(path("M2,68 L4,56 Q6,52 12,52 L22,52 Q28,52 28,56 L30,68 Z", "#5a4334"))
    o.append(path("M8,52 Q15,44 22,52", stroke="#3a2a22", stroke_width=2))
    o.append(rect(6, 58, 20, 2, "#949bb3") + line(10, 52, 12, 46, "#e04a3a", 2) + line(16, 52, 17, 47, "#bec2d1", 1.5))
    # crouched legs: one knee up, one down; boots
    o += [limb([(30, 52), (42, 44), (44, 66)], 8.5, "#2a2f45"),
          limb([(28, 54), (24, 66), (36, 66)], 8.5, "#262043"),
          ellipse(46, 67, 5.5, 2.8, "#3a2a22"), ellipse(36, 67, 5, 2.6, "#3a2a22")]
    # hunched torso, hood up
    o.append(path("M22,30 Q26,22 36,22 Q46,24 46,34 L42,54 L24,56 Q18,44 22,30 Z", hood))
    o.append(path("M22,30 Q26,22 32,22 L30,56 L24,56 Q18,44 22,30 Z", shade(hood, 0.72), opacity=0.7))
    # strap of the toolbag across the chest
    o.append(line(26, 26, 42, 50, "#5a4334", 2.5))
    # arms reaching into the box, careful hands, wire cutters
    o.append(limb([(42, 28), (48, 38), (54, 44)], 6, shade(hood, 1.12)))
    o.append(limb([(26, 30), (30, 42), (50, 48)], 6, hood))
    o.append(circle(55, 45, 2.4, skin) + circle(51, 48, 2.4, skin))
    o.append(line(55, 45, 60, 41, "#e04a3a", 1.4))
    # head in hood, beard, looking down-right
    o.append(path("M30,22 Q28,8 38,6 Q48,6 48,18 L47,26 L31,27 Z", hood))
    o.append(face(40, 17, 6.5, 7.5, skin, eye_dy=0, look=1.5))
    o.append(path("M34,18 Q34,26 40,26 Q46,26 46,18 Q44,22 40,22 Q36,22 34,18 Z", beard))
    o.append(rect(42, 20.5, 2, 0.8, skin))
    o.append(path("M32,24 Q30,10 38,8 Q46,8 47,16 Q44,10 38,11 Q33,13 34,24 Z", shade(hood, 1.15)))
    o.append(path("M35,12 Q40,10 45,12 L44,14 Q40,13 36,14 Z", "#3a2a22"))
    o.append(rim("M47,10 Q49,18 47,26", R) + rim("M46,34 L42,54", R) + rim("M70,44 L70,68", R, 1, 0.6) + rim("M44,46 L45,66", R, 1, 0.6))
    return "".join(o)


@fig("dev_sit", 50, 86)
def dev_sit():
    skin, hair, shirt, R = "#a8704c", "#171217", "#a9c4dc", "#9bd6c4"
    o = [shadow(25, 84, 17)]
    # moulded plastic waiting-room chair
    o += [rect(7, 54, 36, 6, "#2b6e78", rx=2), rect(9, 24, 32, 30, "#2b6e78", rx=4), rect(10, 26, 30, 4, "#3f8f8f", rx=2),
          limb([(10, 60), (9, 82)], 2, "#525a7a"), limb([(40, 60), (41, 82)], 2, "#525a7a")]
    # legs: knees apart, feet planted
    o += [limb([(17, 58), (15, 78)], 7.5, "#3b4260"), limb([(33, 58), (35, 78)], 7.5, "#3b4260"),
          ellipse(13, 80, 5, 2.6, "#3a2a22"), ellipse(37, 80, 5, 2.6, "#3a2a22"),
          ellipse(16, 56, 5.5, 4.5, "#3b4260"), ellipse(34, 56, 5.5, 4.5, shade("#3b4260", 1.15))]
    # torso leaning forward
    o.append(path("M12,34 Q14,28 25,28 Q36,28 38,34 L37,56 L13,56 Z", shirt))
    o.append(path("M12,34 Q14,28 19,28 L19,56 L13,56 Z", shade(shirt, 0.72), opacity=0.7))
    o.append(path("M22,28 L25,33 L28,28 Z", "#e6e8ef"))
    o.append(path("M20,29 L24,44 M30,29 L26,44", stroke="#e0802a", stroke_width=0.9) + rect(23, 44, 4, 4, "#fffaf0"))
    # elbows on knees, hands clasped in front
    o.append(limb([(13, 34), (14, 50), (22, 50)], 5.5, shirt) + limb([(37, 34), (36, 50), (28, 50)], 5.5, shade(shirt, 1.1)))
    o.append(circle(23, 50, 2.6, skin) + circle(27, 50, 2.6, skin))
    # head, slightly bowed, messy hair, stubble
    o.append(rect(22, 22, 6, 6, shade(skin, 0.8)))
    o.append(face(25, 16, 7, 8.5, skin, eye_dy=2))
    o.append(path("M18,22 Q19,24.5 25,25 Q31,24.5 32,22 L32,20 Q25,24 18,20 Z", "#171217", opacity=0.3))
    o.append(path("M18,15 Q17,6 25,5 Q33,6 32,15 Q30,10 25,10 Q20,10 18,15 Z", hair))
    o.append(path("M21,6 l-1,-3 l3,2 l1,-3 l2,3 l2,-2 l0,3", hair))
    o.append(rim("M32,10 Q33,16 31,23", R) + rim("M38,34 L37,56", R) + rim("M35,60 L36,76", R, 1, 0.6))
    return "".join(o)


@fig("cat_sit", 26, 28)
def cat_sit():
    grey, grey_d, grey_l = "#6f7896", "#525a7a", "#949bb3"
    o = [shadow(13, 26.5, 10)]
    # tail curled round the front
    o.append(path("M5,25 Q1,22 4,18", stroke=grey_d, stroke_width=3, stroke_linecap="round"))
    # fat body
    o.append(ellipse(13, 19, 9, 8, grey))
    o.append(ellipse(10, 19, 5, 7, grey_d, opacity=0.5))
    o.append(ellipse(14, 21, 4, 4, grey_l, opacity=0.6))
    # front paws: one white sock
    o.append(rect(9, 22, 3, 5, grey_d) + rect(14, 22, 3, 5, "#fffaf0"))
    # head with one notched ear
    o.append(ellipse(13, 9, 6.5, 5.5, grey))
    o.append(poly([(7.5, 7), (8, 1), (11.5, 5)], grey))
    o.append(poly([(14.5, 5), (18, 1), (18.5, 7)], grey))
    o.append(poly([(16.2, 2.6), (17.4, 1.6), (17.6, 3.8)], "#262043"))   # the notch (cut out of the right ear)
    o.append(poly([(8.6, 6), (9, 3), (10.6, 5)], "#ff9cc6", opacity=0.6))
    o.append(rect(10, 8, 1.5, 1.5, "#b8de7a") + rect(15, 8, 1.5, 1.5, "#b8de7a"))
    o.append(rect(12.5, 10.5, 1.2, 1, "#ff9cc6"))
    o.append(line(6, 11, 9, 10.5, "#e6e8ef", 0.5, opacity=0.7) + line(17, 10.5, 20, 11, "#e6e8ef", 0.5, opacity=0.7))
    o.append(rim("M19,7 Q20,10 18,13", "#ffb347", 1) + rim("M21,16 Q23,20 20,25", "#ffb347", 1))
    return "".join(o)


@fig("cat_sleep", 32, 18)
def cat_sleep():
    grey, grey_d, grey_l = "#6f7896", "#525a7a", "#949bb3"
    o = [shadow(16, 16.5, 14)]
    # loaf: body, head tucked at the right, tail wrapped along the front
    o.append(ellipse(15, 11, 12, 6, grey))
    o.append(ellipse(11, 11, 8, 5, grey_d, opacity=0.45))
    o.append(ellipse(23, 10, 5.5, 4.5, grey))
    o.append(poly([(20, 7), (21, 3), (23.5, 6)], grey))
    o.append(poly([(24, 6), (26.5, 3), (27, 7.5)], grey))
    o.append(poly([(25.3, 4.4), (26.3, 3.3), (26.6, 5)], "#262043"))
    o.append(path("M20.5,10.5 q1,1 2,0 M24.5,10.5 q1,1 2,0", stroke="#262043", stroke_width=0.8))
    o.append(path("M4,15 Q14,18 24,15", stroke=grey_d, stroke_width=2.5, stroke_linecap="round"))
    o.append(rect(25, 13, 3, 2, "#fffaf0"))   # the white sock peeking out
    o.append(ellipse(16, 8, 6, 1.5, grey_l, opacity=0.5))
    o.append(path("M28,6 q1,-2 3,-3 M29,8 q2,-1 3,-1", stroke="#e6e8ef", stroke_width=0.6, opacity=0.5))   # zz-ish breath
    o.append(rim("M27,8 Q29,11 27,14", "#ffb347", 1))
    return "".join(o)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "art_src/figures"
    jpath = sys.argv[2] if len(sys.argv) > 2 else "game/art/figures/figures.json"
    only = set(sys.argv[3:])
    os.makedirs(out, exist_ok=True)
    meta = {}
    for name, (w, h, fn) in FIGS.items():
        meta[name] = {"w": w, "h": h}
        if only and name not in only:
            continue
        open(os.path.join(out, f"{name}.svg"), "w").write(svg(w, h, fn()))
    os.makedirs(os.path.dirname(jpath), exist_ok=True)
    json.dump(meta, open(jpath, "w"), indent=1)
    print("wrote", len(meta), "figures")


if __name__ == "__main__":
    main()
