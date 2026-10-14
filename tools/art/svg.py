"""Tiny SVG authoring helpers shared by every scene/portrait script."""
import random

W, H = 640, 360


def attrs(**kw):
    out = []
    for k, v in kw.items():
        if v is None:
            continue
        out.append(f'{k.rstrip("_").replace("_", "-")}="{v}"')
    return " ".join(out)


def rect(x, y, w, h, fill, **kw):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" {attrs(**kw)}/>'


def poly(pts, fill, **kw):
    p = " ".join(f"{x},{y}" for x, y in pts)
    return f'<polygon points="{p}" fill="{fill}" {attrs(**kw)}/>'


def path(d, fill="none", **kw):
    return f'<path d="{d}" fill="{fill}" {attrs(**kw)}/>'


def circle(cx, cy, r, fill, **kw):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" {attrs(**kw)}/>'


def ellipse(cx, cy, rx, ry, fill, **kw):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" {attrs(**kw)}/>'


def line(x1, y1, x2, y2, stroke, width=1, **kw):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}" {attrs(**kw)}/>'


def text(x, y, s, fill, size=10, family="DejaVu Sans", weight="bold", anchor="middle", **kw):
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-family="{family}" '
            f'font-weight="{weight}" text-anchor="{anchor}" {attrs(**kw)}>{s}</text>')


def g(*children, **kw):
    return f'<g {attrs(**kw)}>' + "".join(children) + "</g>"


COMMON_DEFS = """
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
  <feGaussianBlur stdDeviation="2.2" result="b"/>
  <feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<filter id="bigglow" x="-100%" y="-100%" width="300%" height="300%">
  <feGaussianBlur stdDeviation="6"/>
</filter>
<filter id="soft" x="-50%" y="-50%" width="200%" height="200%">
  <feGaussianBlur stdDeviation="3"/>
</filter>
<filter id="haze" x="-50%" y="-50%" width="200%" height="200%">
  <feGaussianBlur stdDeviation="10"/>
</filter>
"""


def svg(w, h, body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f"<defs>{COMMON_DEFS}{defs}</defs>{body}</svg>")


def lin_grad(gid, stops, x1=0, y1=0, x2=0, y2=1):
    s = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op}"/>' for o, c, op in
                [(st + (1,))[:3] if len(st) == 2 else st for st in stops])
    return f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{s}</linearGradient>'


def rad_grad(gid, stops):
    s = "".join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{op}"/>' for o, c, op in
                [(st + (1,))[:3] if len(st) == 2 else st for st in stops])
    return f'<radialGradient id="{gid}">{s}</radialGradient>'


def glow_pool(cx, cy, rx, ry, color, opacity=0.5):
    """Soft additive light pool."""
    return ellipse(cx, cy, rx, ry, color, opacity=opacity, filter="url(#haze)", style="mix-blend-mode:screen")


def neon(x, y, s, color, size=12, family="DejaVu Sans", weight="bold", anchor="middle", **kw):
    return g(text(x, y, s, color, size, family, weight, anchor, filter="url(#glow)", **kw),
             text(x, y, s, "#fff0f8", size, family, weight, anchor, opacity=0.55, **kw))


def windows(x, y, cols, rows, ww, wh, gx, gy, seed, lit=0.45,
            colors=("#ffb347", "#ffd27a", "#4fc0e8", "#ff9cc6"), dark="#1b1630", frame=None):
    rnd = random.Random(seed)
    out = []
    for r in range(rows):
        for c in range(cols):
            wx, wy = x + c * (ww + gx), y + r * (wh + gy)
            if frame:
                out.append(rect(wx - 1, wy - 1, ww + 2, wh + 2, frame))
            if rnd.random() < lit:
                col = rnd.choice(colors)
                out.append(rect(wx, wy, ww, wh, col))
                out.append(rect(wx, wy + wh * 0.55, ww, wh * 0.45, "#000", opacity=0.18))
                if rnd.random() < 0.4:  # curtain
                    out.append(rect(wx, wy, ww * 0.35, wh, "#7a1f52", opacity=0.6))
            else:
                out.append(rect(wx, wy, ww, wh, dark))
                out.append(rect(wx + 1, wy + 1, ww * 0.3, wh * 0.4, "#525a7a", opacity=0.35))
    return "".join(out)


def lantern(cx, cy, r=7, color="#e04a3a"):
    return g(
        glow_pool(cx, cy, r * 3, r * 3, "#ff7a5a", 0.45),
        line(cx, cy - r - 6, cx, cy - r, "#3a2a22", 1),
        rect(cx - r * 0.5, cy - r - 2, r, 2, "#3a1a10"),
        ellipse(cx, cy, r * 0.85, r, color),
        ellipse(cx - r * 0.25, cy - r * 0.2, r * 0.3, r * 0.6, "#ff9a70", opacity=0.7),
        path(f"M{cx - r * 0.8},{cy - r * 0.3} Q{cx},{cy - r * 0.45} {cx + r * 0.8},{cy - r * 0.3}", stroke="#7a1a1e", stroke_width=0.8),
        path(f"M{cx - r * 0.8},{cy + r * 0.3} Q{cx},{cy + r * 0.45} {cx + r * 0.8},{cy + r * 0.3}", stroke="#7a1a1e", stroke_width=0.8),
        rect(cx - r * 0.5, cy + r, r, 2, "#3a1a10"),
        line(cx, cy + r + 2, cx, cy + r + 7, "#ffb347", 1),
    )


def reflect(content, axis_y, opacity=0.35, blur=True):
    """Mirror content below axis_y (wet-street reflection)."""
    f = 'filter="url(#soft)"' if blur else ""
    return (f'<g transform="translate(0,{2 * axis_y}) scale(1,-1)" opacity="{opacity}" {f}>{content}</g>')


def stars(n, seed, y_max, color="#a99ad0"):
    rnd = random.Random(seed)
    return "".join(rect(rnd.randrange(0, W), rnd.randrange(0, y_max), 1, 1, color, opacity=round(rnd.uniform(0.3, 0.9), 2))
                   for _ in range(n))
