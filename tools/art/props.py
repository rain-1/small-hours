"""Reusable environment props for scene scripts (built on svg.py helpers).

All functions return SVG fragments (strings). Coordinates are 640x360 scene px.
"""
import random
from svg import *


def tr(content, dx=0, dy=0, rot=0, cx=0, cy=0, scale=1):
    t = f"translate({dx},{dy})"
    if rot:
        t += f" rotate({rot},{cx},{cy})"
    if scale != 1:
        t += f" scale({scale})"
    return f'<g transform="{t}">{content}</g>'


def mug(x, y, color="#e04a3a", steam=False, h=7, w=6):
    """Mug standing with its base at (x, y)."""
    out = [rect(x, y - h, w, h, color), rect(x, y - h, w, 1.2, "#fffaf0", opacity=0.35),
           path(f"M{x + w},{y - h + 1.5} q3,0 3,2.5 q0,2.5 -3,2.5", stroke=color, stroke_width=1.2),
           rect(x, y - 1, w, 1, "#000", opacity=0.25)]
    if steam:
        out.append(path(f"M{x + 2},{y - h - 2} q-2,-3 0,-6 q2,-3 0,-6", stroke="#f6e7c8",
                        stroke_width=1, opacity=0.45, filter="url(#soft)"))
    return "".join(out)


def sticky(x, y, color="#ffd27a", rot=0, s=7, lines=2):
    inner = rect(x, y, s, s, color) + rect(x, y, s, 1.5, "#000", opacity=0.12)
    for i in range(lines):
        inner += rect(x + 1, y + 2.5 + i * 1.8, s - 2 - (i % 2), 0.7, "#3a2a22", opacity=0.55)
    return tr(inner, rot=rot, cx=x + s / 2, cy=y + s / 2) if rot else inner


def potted_plant(x, y, s=1.0, pot="#b85c1c", leaf="#4f8f45", leaf2="#7fb85a", seed=1, kind="leafy"):
    """Plant in a pot, base centred at (x, y)."""
    rnd = random.Random(seed)
    pw, ph = 12 * s, 10 * s
    out = []
    if kind == "palm":
        for i in range(9):
            a = -80 + i * 20 + rnd.uniform(-6, 6)
            import math
            L = (26 + rnd.uniform(-4, 6)) * s
            ex = x + math.sin(math.radians(a)) * L
            ey = y - ph - 18 * s - math.cos(math.radians(a)) * L * 0.7
            mx = x + math.sin(math.radians(a)) * L * 0.4
            my = y - ph - 30 * s
            out.append(path(f"M{x},{y - ph - 4 * s} Q{mx},{my} {ex},{ey}", stroke=leaf if i % 2 else leaf2,
                            stroke_width=3.2 * s, stroke_linecap="round"))
        out.append(rect(x - 1.2 * s, y - ph - 16 * s, 2.4 * s, 16 * s, "#5a4334"))
    else:
        import math
        n = int(9 * max(1, s))
        for i in range(n):
            a = rnd.uniform(-70, 70)
            L = rnd.uniform(9, 17) * s
            ex = x + math.sin(math.radians(a)) * L
            ey = y - ph - math.cos(math.radians(a)) * L
            out.append(path(f"M{x},{y - ph} Q{(x + ex) / 2 + rnd.uniform(-3, 3)},{ey + 2} {ex},{ey}",
                            stroke="#2f6a35", stroke_width=0.8))
            out.append(ellipse(ex, ey, 3.2 * s, 1.8 * s, leaf if rnd.random() < 0.5 else leaf2,
                               transform=f"rotate({a + 90 + rnd.uniform(-20, 20)},{ex},{ey})"))
    out.append(poly([(x - pw / 2, y - ph), (x + pw / 2, y - ph), (x + pw * 0.38, y), (x - pw * 0.38, y)], pot))
    out.append(rect(x - pw / 2 - 1, y - ph, pw + 2, 2.5 * s, pot))
    out.append(rect(x - pw / 2 - 1, y - ph, pw + 2, 1, "#fff0b8", opacity=0.3))
    out.append(rect(x - pw * 0.38, y - ph * 0.45, pw * 0.76, ph * 0.45, "#000", opacity=0.18))
    return "".join(out)


def books(x, y, w, h, seed, colors=("#7a1f52", "#1f5260", "#b85c1c", "#463a70", "#4f8f45", "#c9b49a",
                                     "#b02a2a", "#2f8fc0", "#e0802a", "#5a4334")):
    """Row of book spines standing on shelf line y (books grow upward)."""
    rnd = random.Random(seed)
    out, cx = [], x
    while cx < x + w - 2:
        bw = rnd.choice([2, 3, 3, 4, 5])
        if cx + bw > x + w:
            break
        bh = h * rnd.uniform(0.7, 1.0)
        if rnd.random() < 0.08 and cx + bh < x + w:  # a book lying flat
            out.append(rect(cx, y - bw, bh, bw, rnd.choice(colors)))
            cx += bh + 1
            continue
        c = rnd.choice(colors)
        out.append(rect(cx, y - bh, bw, bh, c))
        out.append(rect(cx, y - bh + 2, bw, 0.8, "#ffd27a", opacity=0.45))
        if rnd.random() < 0.15:  # leaning
            pass
        cx += bw + (1 if rnd.random() < 0.2 else 0)
    return "".join(out)


def rain_glass(x, y, w, h, seed, n=None, color="#bec2d1"):
    """Static droplets/runnels on a window pane (not falling rain)."""
    rnd = random.Random(seed)
    out = []
    n = n or int(w * h / 90)
    for _ in range(n):
        dx, dy = x + rnd.uniform(1, w - 1), y + rnd.uniform(1, h - 2)
        r = rnd.choice([0.6, 0.8, 1.0, 1.3])
        out.append(circle(round(dx, 1), round(dy, 1), r, color, opacity=round(rnd.uniform(0.25, 0.6), 2)))
        if rnd.random() < 0.18:
            L = rnd.uniform(4, 14)
            out.append(line(dx, dy, dx + rnd.uniform(-0.6, 0.6), min(y + h, dy + L), color, 0.6, opacity=0.3))
    return "".join(out)


def night_view(x, y, w, h, seed, sky=("#0d0b1a", "#262043", "#7a1f52"), neon=True, horizon=0.62):
    """A little rainy city seen through a window; clipped to the rect."""
    rnd = random.Random(seed)
    cid = f"nv{seed}"
    out = [f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath>',
           f'<g clip-path="url(#{cid})">']
    gid = f"nvs{seed}"
    out.append(f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky[0]}"/>'
               f'<stop offset="0.6" stop-color="{sky[1]}"/><stop offset="1" stop-color="{sky[2]}"/></linearGradient>')
    out.append(rect(x, y, w, h, f"url(#{gid})"))
    hy = y + h * horizon
    cx = x - 4
    while cx < x + w:
        bw = rnd.uniform(8, 20)
        bh = rnd.uniform(h * 0.15, h * 0.7)
        col = rnd.choice(["#1b1630", "#262043", "#1a1d2b"])
        out.append(rect(cx, hy - bh, bw, bh + h, col))
        for wy in range(int(hy - bh + 3), int(y + h), 5):
            for wx in range(int(cx + 2), int(cx + bw - 2), 4):
                if rnd.random() < 0.28:
                    out.append(rect(wx, wy, 2, 2, rnd.choice(["#ffb347", "#ffd27a", "#4fc0e8", "#ff9cc6", "#7d6fae"]),
                                    opacity=0.85))
        cx += bw + rnd.uniform(0, 3)
    if neon:
        for _ in range(3):
            nx, ny = x + rnd.uniform(4, w - 10), y + rnd.uniform(h * 0.35, h * 0.85)
            c = rnd.choice(["#ff5fa2", "#4ff0e6", "#ffb347"])
            out.append(rect(nx, ny, rnd.uniform(5, 12), 2.5, c, filter="url(#glow)"))
            out.append(glow_pool(nx + 4, ny, 14, 10, c, 0.4))
    out.append("</g>")
    return "".join(out)


def string_lights(x1, y1, x2, y2, sag, n, colors=("#ffd27a", "#ffb347", "#ff9cc6", "#4ff0e6"), r=1.4, seed=0):
    import math
    rnd = random.Random(seed)
    mx, my = (x1 + x2) / 2, max(y1, y2) + sag
    out = [path(f"M{x1},{y1} Q{mx},{my + sag * 0.0} {x2},{y2}", stroke="#0d0b1a", stroke_width=0.8)]
    for i in range(1, n):
        t = i / n
        bx = (1 - t) ** 2 * x1 + 2 * (1 - t) * t * mx + t * t * x2
        by = (1 - t) ** 2 * y1 + 2 * (1 - t) * t * my + t * t * y2
        c = colors[(i + seed) % len(colors)]
        out.append(circle(round(bx, 1), round(by + 1.5, 1), r, c, filter="url(#glow)"))
    return "".join(out)


def cable(x1, y1, x2, y2, sag=10, color="#0d0b1a", width=1.2):
    mx, my = (x1 + x2) / 2, max(y1, y2) + sag
    return path(f"M{x1},{y1} Q{mx},{my} {x2},{y2}", stroke=color, stroke_width=width)


def stool(cx, y, color="#b02a2a", h=34, seat_w=20):
    """Bar stool, feet at y."""
    return g(
        ellipse(cx, y, seat_w * 0.55, 2.5, "#000", opacity=0.35),
        line(cx - seat_w * 0.35, y, cx - 3, y - h + 4, "#525a7a", 1.6),
        line(cx + seat_w * 0.35, y, cx + 3, y - h + 4, "#525a7a", 1.6),
        line(cx - seat_w * 0.25, y - h * 0.35, cx + seat_w * 0.25, y - h * 0.35, "#6f7896", 1.2),
        rect(cx - 1.5, y - h + 2, 3, h * 0.5, "#6f7896"),
        ellipse(cx, y - h + 2, seat_w / 2, 4, color),
        ellipse(cx, y - h + 1, seat_w / 2 - 1, 2.5, "#ff7a5a", opacity=0.45),
    )


def light_cone(x, y, top_w, bot_w, h, color, opacity=0.18):
    return poly([(x - top_w / 2, y), (x + top_w / 2, y), (x + bot_w / 2, y + h), (x - bot_w / 2, y + h)],
                color, opacity=opacity, filter="url(#soft)", style="mix-blend-mode:screen")


def bird(x, y, s=1.0, color="#3a2a22"):
    return path(f"M{x - 4 * s},{y} q{2 * s},{-2.5 * s} {4 * s},0 q{2 * s},{-2.5 * s} {4 * s},0",
                stroke=color, stroke_width=1.1 * s)


def floor_planks(x, y, w, h, color="#5a4334", line_c="#3a2a22", n=8):
    out = [rect(x, y, w, h, color)]
    for i in range(1, n):
        yy = y + h * (i / n) ** 1.6
        out.append(line(x, yy, x + w, yy, line_c, 0.8, opacity=0.6))
    return "".join(out)


def tiles(x, y, w, h, size, c1, c2, grout, seed=0):
    rnd = random.Random(seed)
    out = [rect(x, y, w, h, grout)]
    yy, row = y, 0
    while yy < y + h:
        xx = x + (size / 2 if row % 2 else 0) - size
        while xx < x + w:
            c = c1 if rnd.random() < 0.8 else c2
            x0, x1_ = max(x, xx + 0.5), min(x + w, xx + size - 0.5)
            if x1_ > x0:
                out.append(rect(round(x0, 1), round(yy + 0.5, 1), round(x1_ - x0, 1),
                                round(min(size - 1, y + h - yy - 0.5), 1), c))
            xx += size
        yy += size
        row += 1
    return "".join(out)
