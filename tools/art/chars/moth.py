"""Moth — the scooter's small, old onboard AI. A chunky retro dash unit in scuffed pale-teal and
cream plastic, stickers, a tiny antenna, and a little screen with a glowing cyan pixel face.
Moods: neutral, happy, worried, glitch, thinking. Same 200x240 canvas as the portraits."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from portrait import *

CYAN = "#4ff0e6"
CYAN_L = "#a8fff6"
SCREEN = "#0f1f2b"
SX, SY, PX = 56, 86, 4          # screen origin + pixel size: 22 x 14 screen pixels
COLS, ROWS = 22, 14

FACES = {
    "neutral": [
        "......................",
        "......................",
        "......................",
        "......##......##......",
        "......##......##......",
        "......##......##......",
        "......................",
        "......................",
        "......................",
        ".........####.........",
        "......................",
        "......................",
        "......................",
        "......................",
    ],
    "happy": [
        "......................",
        "......................",
        "......................",
        ".....#..#....#..#.....",
        "....#....#..#....#....",
        "......................",
        "......................",
        "......................",
        ".......#......#.......",
        "........######........",
        "......................",
        "....++..........++....",
        "......................",
        "......................",
    ],
    "worried": [
        "......................",
        "......................",
        "........#....#........",
        ".......#......#.......",
        "......##......##......",
        "......##......##......",
        "......................",
        "......................",
        "......................",
        "........#.##.#........",
        ".......#.#..#.#.......",
        "......................",
        "......................",
        "......................",
    ],
    "thinking": [
        "......................",
        "......................",
        "........##......##....",
        "........##......##....",
        "......................",
        "......................",
        "......................",
        "......................",
        "......................",
        "......................",
        "......##..++..--......",
        "......##..++..--......",
        "......................",
        "......................",
    ],
    "glitch": [
        "......................",
        "......................",
        "......................",
        ".......##.......##....",
        "......##......##......",
        "......##.......##.....",
        "......................",
        "......................",
        "......................",
        "........##.##.........",
        "..........#..##.......",
        "......................",
        "......................",
        "......................",
    ],
}


def pix(c, r, color, op=1.0, w=1):
    return rect(SX + c * PX, SY + r * PX, PX * w - 0.6, PX - 0.6, color, opacity=op)


def screen_face(mood):
    o = []
    grid = FACES[mood]
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "#":
                o.append(pix(c, r, CYAN))
            elif ch == "+":
                o.append(pix(c, r, CYAN_L if mood == "thinking" else "#ff9cc6", 0.9 if mood == "thinking" else 0.5))
            elif ch == "-":
                o.append(pix(c, r, CYAN, 0.35))
    return "".join(o)


def glitch_layer():
    rnd = random.Random(9)
    o = []
    # chromatic ghost of the face, shifted
    for r, row in enumerate(FACES["glitch"]):
        for c, ch in enumerate(row):
            if ch == "#":
                o.append(rect(SX + c * PX - 3, SY + r * PX, PX - 0.6, PX - 0.6, "#ff5fa2", opacity=0.55))
    # torn scanlines: bright horizontal slices displaced sideways
    for r, dx in ((4, 10), (5, -8), (10, 6)):
        o.append(rect(SX + dx, SY + r * PX + 1, COLS * PX - abs(dx), 2, CYAN, opacity=0.45))
    o.append(rect(SX, SY + 7 * PX, COLS * PX, 3, CYAN_L, opacity=0.25))
    # static
    for _ in range(45):
        c, r = rnd.randrange(COLS), rnd.randrange(ROWS)
        o.append(rect(SX + c * PX + rnd.choice((0, 2)), SY + r * PX + rnd.choice((0, 2)), 1.5, 1.5,
                      rnd.choice((CYAN, "#ffffff", "#7d6fae")), opacity=rnd.choice((0.4, 0.7, 1))))
    return "".join(o)


def device(mood):
    teal, teal_d = "#9bd6c4", "#63b3a8"
    cream, cream_d = "#f6e7c8", "#c9b49a"
    rim = "#ff5fa2"
    o = []
    # glow behind the unit
    o.append(glow_pool(100, 110, 70, 50, CYAN, 0.25))
    # dash mount: a stubby arm and clamp at the bottom
    o.append(rect(88, 182, 24, 40, "#3b4260", rx=4))
    o.append(rect(92, 186, 4, 30, "#525a7a"))
    o.append(rect(70, 214, 60, 16, "#2a2f45", rx=5))
    o.append(rect(74, 216, 52, 3, "#525a7a"))
    o.append(path("M128,224 Q150,232 160,240", stroke="#1a1d2b", stroke_width=4))
    # antenna (bent a little) with a bead
    o.append(path("M138,52 L142,30 L150,22", stroke="#525a7a", stroke_width=2.4, stroke_linecap="round", stroke_linejoin="round"))
    o.append(circle(150, 22, 4, "#e04a3a"))
    o.append(circle(149, 21, 1.4, "#ff9cc6"))
    o.append(rect(132, 50, 12, 6, "#3b4260", rx=2))
    # chunky body: teal shell with a cream face plate
    o.append(rect(28, 54, 144, 136, teal_d, rx=22))
    o.append(rect(28, 50, 144, 134, teal, rx=22))
    o.append(rect(36, 58, 128, 118, cream, rx=16))
    o.append(rect(36, 150, 128, 26, cream_d, rx=12, opacity=0.35))
    # shell shading + neon rim on the right edge
    o.append(path("M38,58 Q30,60 30,80 L30,160 Q30,180 44,182", stroke=teal_d, stroke_width=3, opacity=0.6))
    o.append(path("M160,52 Q170,54 170,72 L170,164 Q170,180 156,183", stroke=rim, stroke_width=2, opacity=0.6))
    # scuffs and scratches
    for (x, y, l, a) in [(44, 64, 8, 0.6), (150, 140, 10, 0.5), (60, 170, 6, 0.5), (152, 70, 5, 0.6), (34, 120, 6, 0.4)]:
        o.append(line(x, y, x + l, y + 2, "#a08870", 1, opacity=a))
    o.append(ellipse(46, 170, 6, 3, "#a08870", opacity=0.25))
    # screen bezel + screen
    o.append(rect(SX - 8, SY - 10, COLS * PX + 16, ROWS * PX + 18, "#2a2f45", rx=8))
    o.append(rect(SX - 2, SY - 3, COLS * PX + 4, ROWS * PX + 5, SCREEN, rx=4))
    o.append(rect(SX - 2, SY - 3, COLS * PX + 4, ROWS * PX + 5, CYAN, rx=4, opacity=0.06))
    # faint pixel grid
    o.append("".join(rect(SX, SY + r * PX + PX - 1, COLS * PX, 0.6, "#173a4a", opacity=0.8) for r in range(ROWS)))
    face = screen_face(mood)
    o.append(g(face, filter="url(#glow)"))
    o.append(face)
    if mood == "glitch":
        o.append(glitch_layer())
    # glass glare
    o.append(path(f"M{SX + 2},{SY + 10} L{SX + 14},{SY - 1} L{SX + 22},{SY - 1} L{SX + 4},{SY + 18} Z", "#ffffff", opacity=0.08))
    # power LED + tiny label
    o.append(circle(SX - 2, SY + ROWS * PX + 14, 2, CYAN if mood != "glitch" else "#ff5fa2", filter="url(#glow)"))
    o.append(text(SX + 30, SY + ROWS * PX + 17, "MOTH-5", "#7d6450", size=6, family="DejaVu Sans Mono"))
    # controls: d-pad, two buttons, speaker grille
    o.append(rect(46, 160, 18, 6, "#525a7a", rx=1.5))
    o.append(rect(52, 154, 6, 18, "#525a7a", rx=1.5))
    o.append(circle(132, 166, 6, "#e0802a"))
    o.append(circle(131, 165, 2, "#ffd27a", opacity=0.7))
    o.append(circle(148, 158, 6, "#b02d6f"))
    o.append(circle(147, 157, 2, "#ff9cc6", opacity=0.7))
    o.append("".join(rect(82 + i * 6, 162 + j * 5, 3, 2, "#a08870") for i in range(6) for j in range(2)))
    # stickers: a peeling star, a Halfmoon Noodle bowl, a little frog (June's)
    o.append(g(poly([(156, 92), (159, 100), (167, 100), (161, 105), (163, 113), (156, 108), (149, 113), (151, 105), (145, 100), (153, 100)], "#ffd27a"),
               poly([(163, 113), (156, 108), (160, 114)], "#c9b49a"), transform="rotate(14 156 102)"))
    o.append(g(rect(31, 104, 22, 18, "#fffaf0", rx=3, transform="rotate(-10 42 113)"),
               path("M34,112 Q42,122 50,110 Z", "#e04a3a", transform="rotate(-10 42 113)"),
               path("M38,108 q1,-3 0,-5 M43,107 q1,-3 0,-5", stroke="#949bb3", stroke_width=1, transform="rotate(-10 42 113)")))
    o.append(g(ellipse(160, 136, 7, 5.5, "#7fb85a"), circle(156, 132, 2.4, "#b8de7a"), circle(164, 132, 2.4, "#b8de7a"),
               circle(156, 132, 0.9, "#14301e"), circle(164, 132, 0.9, "#14301e"),
               path("M156,138 Q160,140 164,138", stroke="#14301e", stroke_width=0.7)))
    # a strip of tape holding one corner together
    o.append(rect(30, 56, 20, 7, "#fff0b8", opacity=0.6, transform="rotate(-38 40 59)"))
    return svg(PW, PH, "".join(o))


if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for m in ("neutral", "happy", "worried", "glitch", "thinking"):
        open(os.path.join(out, f"moth_{m}.svg"), "w").write(device(m))
