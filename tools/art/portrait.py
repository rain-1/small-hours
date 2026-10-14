"""Portrait base: a parametric stylised head + mood-driven features.

Every character script builds a dict of parts and calls `portrait(spec, mood)`.
Canvas is 200x240, transparent; bust is cut off at the bottom edge.
Moods: neutral, smile, sad, plus 'surprised' and 'angry' (brows/mouth/eyes).
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from svg import *

PW, PH = 200, 240


def shade(hex_, k):
    """Darken (k<1) or lighten (k>1) a hex colour."""
    h = hex_.lstrip("#")
    r, g_, b_ = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    if k < 1:
        r, g_, b_ = r * k, g_ * k, b_ * k
    else:
        r, g_, b_ = r + (255 - r) * (k - 1), g_ + (255 - g_) * (k - 1), b_ + (255 - b_) * (k - 1)
    return "#%02x%02x%02x" % (int(r), int(g_), int(b_))


def head_path(cx, top, w, h, jw, chin=0.0):
    """Face outline. w = cheek width, jw = jaw width, chin>0 makes it pointier."""
    hw, jhw = w / 2, jw / 2
    return (f"M{cx},{top} "
            f"C{cx + hw * 1.1},{top} {cx + hw},{top + h * 0.22} {cx + hw},{top + h * 0.45} "
            f"C{cx + hw},{top + h * 0.66} {cx + jhw},{top + h * 0.8} {cx + jhw * 0.55},{top + h * (0.92 + chin * 0.02)} "
            f"Q{cx},{top + h + 2 + chin * 6} {cx - jhw * 0.55},{top + h * (0.92 + chin * 0.02)} "
            f"C{cx - jhw},{top + h * 0.8} {cx - hw},{top + h * 0.66} {cx - hw},{top + h * 0.45} "
            f"C{cx - hw},{top + h * 0.22} {cx - hw * 1.1},{top} {cx},{top} Z")


def eye(x, y, mood, iris, side, size=1.0, lid="#2a1a14", age=0, smile_open=False):
    s = size
    o = []
    if mood == "smile" and smile_open:
        # eyes stay open, lower lid pushed up by the cheek
        ry = 3.6 * s
        o.append(ellipse(x, y, 6.6 * s, ry, "#fffaf0"))
        o.append(ellipse(x + side * 0.6, y + 0.2, 3.9 * s, ry, iris))
        o.append(circle(x + side * 0.6, y + 0.2, 1.9 * s, "#0d0b1a"))
        o.append(circle(x + side * 0.6 + 1.4, y - 1.2, 1.1 * s, "#ffffff"))
        o.append(path(f"M{x - 7.4 * s},{y + 0.5} Q{x},{y - ry - 3.2} {x + 7.4 * s},{y + 0.5}",
                      stroke=lid, stroke_width=2.3 * s, stroke_linecap="round"))
        o.append(path(f"M{x - 6 * s},{y + 3.2 * s} Q{x},{y + 0.6 * s} {x + 6 * s},{y + 3.2 * s}", stroke=lid, stroke_width=1.1, opacity=0.6))
    elif mood == "smile":
        # happy closed-ish arcs
        o.append(path(f"M{x - 7 * s},{y + 1} Q{x},{y - 6 * s} {x + 7 * s},{y + 1}", stroke=lid, stroke_width=2.2 * s, stroke_linecap="round"))
        o.append(path(f"M{x - 5 * s},{y + 4} Q{x},{y + 1.5} {x + 5 * s},{y + 4}", stroke=lid, stroke_width=0.9, opacity=0.5))
    else:
        open_ = {"neutral": 1.0, "sad": 0.82, "surprised": 1.25, "angry": 0.75}.get(mood, 1)
        ry = 4.6 * s * open_
        o.append(ellipse(x, y, 6.6 * s, ry, "#fffaf0"))
        o.append(ellipse(x + side * 0.6, y + 0.4, 3.9 * s, min(ry, 4.2 * s), iris))
        o.append(circle(x + side * 0.6, y + 0.4, 1.9 * s, "#0d0b1a"))
        o.append(circle(x + side * 0.6 + 1.4, y - 1.4, 1.1 * s, "#ffffff"))
        # upper lid
        lift = {"sad": 1.5, "angry": -1.2}.get(mood, 0)
        o.append(path(f"M{x - 7.4 * s},{y + 0.5 - lift * side * 0} Q{x},{y - ry - 2.6} {x + 7.4 * s},{y + 0.5}",
                      stroke=lid, stroke_width=2.3 * s, stroke_linecap="round"))
        if mood == "angry":
            o.append(path(f"M{x - 7 * s},{y - 3.5} L{x + 7 * s},{y - 1.5 if side < 0 else y - 5}", stroke=lid, stroke_width=1.8))
        if mood == "sad":
            o.append(path(f"M{x - 5 * s},{y + ry + 1.5} Q{x},{y + ry + 3} {x + 5 * s},{y + ry + 1.5}", stroke=lid, stroke_width=0.8, opacity=0.5))
    for i in range(age):  # crow's feet / under-eye lines
        o.append(path(f"M{x + side * (8 + i * 1.5) * s},{y - 1 + i * 2.5} l{side * 3},{1 + i}", stroke=lid, stroke_width=0.7, opacity=0.45))
        o.append(path(f"M{x - 4 * s},{y + 6.5 * s + i * 1.6} Q{x},{y + 8 * s + i * 1.6} {x + 4 * s},{y + 6.5 * s + i * 1.6}", stroke=lid, stroke_width=0.6, opacity=0.3))
    return "".join(o)


def brow(x, y, mood, side, color, thick=2.6, length=9):
    if mood == "worried":  # inner ends up, outer level (anxious)
        xi, xo = x - side * length * 0.55, x + side * length * 0.55
        return path(f"M{xi},{y - 3.5} Q{x},{y - 4} {xo},{y + 0.5}", stroke=color, stroke_width=thick, stroke_linecap="round")
    # inner end is toward the face centre (x - side*length/2 ... )
    inner_dy = {"neutral": 0, "smile": -1.5, "sad": -4, "surprised": -5, "angry": 3.5}.get(mood, 0)
    outer_dy = {"neutral": -1, "smile": -2.5, "sad": 1.5, "surprised": -5, "angry": -2}.get(mood, 0)
    xi, xo = x - side * length * 0.55, x + side * length * 0.55
    return path(f"M{xi},{y + inner_dy} Q{x},{y - 2.5 + min(inner_dy, outer_dy)} {xo},{y + outer_dy}",
                stroke=color, stroke_width=thick, stroke_linecap="round")


def mouth(x, y, mood, lip="#a8505a", w=1.0, style=None):
    s = w
    if mood == "smile" and style == "closed":
        return (path(f"M{x - 8 * s},{y - 1} Q{x},{y + 5} {x + 8 * s},{y - 1}", stroke="#5a1e24", stroke_width=1.9, stroke_linecap="round") +
                path(f"M{x - 9.5 * s},{y - 2} Q{x - 10.5 * s},{y} {x - 8.5 * s},{y + 0.5}", stroke="#5a1e24", stroke_width=0.8) +
                path(f"M{x + 9.5 * s},{y - 2} Q{x + 10.5 * s},{y} {x + 8.5 * s},{y + 0.5}", stroke="#5a1e24", stroke_width=0.8))
    if mood == "smile" and style == "wry":
        return (path(f"M{x - 7 * s},{y + 0.5} Q{x + 1},{y + 3} {x + 8 * s},{y - 2.5}", stroke="#5a1e24", stroke_width=1.8, stroke_linecap="round") +
                path(f"M{x + 8.5 * s},{y - 4} q1.5,1.5 0.5,3", stroke="#5a1e24", stroke_width=0.8))
    if mood == "surprised" and style == "gasp":
        return (ellipse(x, y + 1.5, 5 * s, 5.5, "#5a1e24") + ellipse(x, y + 4.5, 3 * s, 1.6, "#c0505e", opacity=0.8))
    if mood == "smile":
        return (path(f"M{x - 9 * s},{y - 1} Q{x},{y + 8} {x + 9 * s},{y - 1} Q{x},{y + 3} {x - 9 * s},{y - 1} Z", "#5a1e24") +
                path(f"M{x - 6 * s},{y + 1.2} Q{x},{y + 3.6} {x + 6 * s},{y + 1.2}", fill="#fffaf0", opacity=0.9) +
                path(f"M{x - 10 * s},{y - 2} Q{x - 11 * s},{y} {x - 9.5 * s},{y + 1}", stroke="#5a1e24", stroke_width=0.8))
    if mood == "sad":
        return path(f"M{x - 6.5 * s},{y + 2.5} Q{x},{y - 2} {x + 6.5 * s},{y + 2.5}", stroke="#5a1e24", stroke_width=1.8, stroke_linecap="round")
    if mood == "surprised":
        return ellipse(x, y + 1, 3.5 * s, 4.5, "#5a1e24")
    if mood == "angry":
        return path(f"M{x - 7 * s},{y + 1.5} L{x + 7 * s},{y + 0.5}", stroke="#5a1e24", stroke_width=2, stroke_linecap="round")
    return path(f"M{x - 7 * s},{y} Q{x},{y + 2.5} {x + 7 * s},{y}", stroke="#5a1e24", stroke_width=1.8, stroke_linecap="round")


def nose(style, cx, eye_y, ny, skin):
    """Alternative nose shapes (optional; Lu uses the default inline one)."""
    d, hi = shade(skin, 0.62), shade(skin, 1.25)
    if style == "broad":
        return (path(f"M{cx + 1},{eye_y + 5} Q{cx + 3},{ny - 2} {cx + 4},{ny}", stroke=d, stroke_width=1.2, stroke_linecap="round", opacity=0.7) +
                path(f"M{cx - 7},{ny + 1} Q{cx - 8},{ny + 5} {cx - 4},{ny + 5} Q{cx},{ny + 7} {cx + 4},{ny + 5} Q{cx + 8},{ny + 5} {cx + 7},{ny + 1}",
                     stroke=d, stroke_width=1.4, stroke_linecap="round") +
                ellipse(cx, ny + 1, 3.2, 2.4, hi, opacity=0.35))
    if style == "big":  # bulbous, older
        return (path(f"M{cx + 1},{eye_y + 3} Q{cx + 5},{ny - 4} {cx + 6},{ny + 1}", stroke=d, stroke_width=1.3, stroke_linecap="round") +
                path(f"M{cx + 6},{ny + 1} Q{cx + 9},{ny + 6} {cx + 3},{ny + 7} Q{cx},{ny + 9} {cx - 3},{ny + 7} Q{cx - 9},{ny + 6} {cx - 6},{ny + 2}",
                     stroke=d, stroke_width=1.5, stroke_linecap="round") +
                circle(cx + 2, ny + 2, 3, hi, opacity=0.45) + ellipse(cx, ny + 3, 6, 4, "#e0458e", opacity=0.12))
    if style == "long":  # long straight bridge
        return (path(f"M{cx + 1},{eye_y + 2} L{cx + 4},{ny + 1} Q{cx + 5},{ny + 4} {cx + 2},{ny + 5} Q{cx},{ny + 6} {cx - 3},{ny + 4}",
                     stroke=d, stroke_width=1.3, stroke_linecap="round", stroke_linejoin="round") +
                line(cx + 2, eye_y + 6, cx + 3.5, ny - 1, hi, 1.2, opacity=0.5))
    if style == "button":  # small, young
        return (path(f"M{cx - 2.5},{ny + 2} Q{cx},{ny + 4} {cx + 2.5},{ny + 2}", stroke=d, stroke_width=1.3, stroke_linecap="round") +
                circle(cx + 1, ny, 1.5, hi, opacity=0.6))
    return ""


def glasses(cx, y, ex, rw, rh, color, shape="round", width=1.6, tint="#d2f0e2", tint_op=0.12, glint=None):
    """Glasses helper: lens centres at cx +/- ex, radius rw x rh."""
    o = []
    for sd in (-1, 1):
        x = cx + sd * ex
        if shape == "round":
            o.append(ellipse(x, y, rw, rh, tint, opacity=tint_op))
            o.append(ellipse(x, y, rw, rh, "none", stroke=color, stroke_width=width))
        else:  # rect / soft rectangle
            r = 2.5 if shape == "rect" else rh * 0.6
            o.append(rect(x - rw, y - rh, rw * 2, rh * 2, tint, opacity=tint_op, rx=r))
            o.append(rect(x - rw, y - rh, rw * 2, rh * 2, "none", stroke=color, stroke_width=width, rx=r))
        if glint:
            o.append(path(f"M{x + rw * 0.2},{y - rh * 0.7} l{rw * 0.5},{rh * 0.5}", stroke=glint, stroke_width=1.4, opacity=0.8, stroke_linecap="round"))
    o.append(path(f"M{cx - ex + rw},{y - 1} Q{cx},{y - 4} {cx + ex - rw},{y - 1}", stroke=color, stroke_width=width))
    return "".join(o)


def stubble(cx, top, w, h, jw, color, op=0.22, beard_line=0.62, seed=1):
    """Soft five o'clock shadow over the jaw and upper lip, clipped to the face."""
    import random as _r
    rnd = _r.Random(seed)
    y0 = top + h * beard_line
    my = top + h * 0.83
    shape = (f"M{cx - w / 2 - 4},{y0} Q{cx - w * 0.28},{y0 + h * 0.06} {cx - w * 0.2},{my - 9} Q{cx},{my - 12} {cx + w * 0.2},{my - 9} "
             f"Q{cx + w * 0.28},{y0 + h * 0.06} {cx + w / 2 + 4},{y0} L{cx + w / 2 + 4},{top + h + 14} L{cx - w / 2 - 4},{top + h + 14} Z")
    o = [path(shape, color, opacity=op, filter="url(#soft)")]
    dots = []
    for _ in range(int(w * 0.9)):
        x = rnd.uniform(cx - w / 2, cx + w / 2)
        y = rnd.uniform(y0 + h * 0.08, top + h + 4)
        if abs(x - cx) < w * 0.14 and y < my + 4 and y > my - 6:
            continue
        dots.append(rect(round(x), round(y), 1, 1, color, opacity=min(1, op * 1.5)))
    return '<g clip-path="url(#faceclip)">' + "".join(o) + "".join(dots) + "</g>"


def portrait(spec, mood="neutral"):
    """spec keys:
    skin, hair, iris, rim (neon rim-light colour), lip (optional)
    head: dict(cx, top, w, h, jw, chin)
    back_hair, neck_clothes, front_hair, accessories: callables (spec)->svg, drawn in that order
    brow_color, brow_thick, eye_size, age (0-3), extra_face (callable(spec, mood))
    """
    hd = dict(cx=100, top=48, w=78, h=100, jw=56, chin=0)
    hd.update(spec.get("head", {}))
    cx, top, w, h = hd["cx"], hd["top"], hd["w"], hd["h"]
    skin = spec["skin"]
    sk_d = shade(skin, 0.78)
    sk_dd = shade(skin, 0.62)
    rim = spec.get("rim", "#ff5fa2")
    face = head_path(cx, top, w, h, hd["jw"], hd["chin"])
    eye_y = top + h * spec.get("eye_y", 0.53)
    ex = w * spec.get("eye_dx", 0.215)
    defs = f'<clipPath id="faceclip"><path d="{face}"/></clipPath>'
    o = []
    o.append(spec.get("back_hair", lambda s: "")(spec))
    # neck
    nw = spec.get("neck_w", 26)
    nh = nw // 2 if isinstance(nw, int) and nw % 2 == 0 else nw / 2
    o.append(rect(cx - nh, top + h - 18, nw, 40, sk_d))
    o.append(rect(cx - nh, top + h - 6, nw, 10, sk_dd, opacity=0.6))
    o.append(spec["clothes"](spec))
    # ears
    for sd in (-1, 1):
        ex_ = cx + sd * (w / 2 - 1)
        o.append(ellipse(ex_, eye_y + 6, 6, 10, skin if sd > 0 else sk_d))
        o.append(ellipse(ex_ + sd * 1, eye_y + 6, 2.5, 5.5, sk_dd, opacity=0.5))
    # face + shading (shadow side left, neon rim right)
    o.append(path(face, skin))
    o.append(f'<g clip-path="url(#faceclip)">'
             + path(f"M{cx - w},{top} L{cx - w * 0.22},{top} Q{cx - w * 0.36},{top + h * 0.5} {cx - w * 0.18},{top + h + 10} L{cx - w},{top + h + 10} Z", sk_d, opacity=0.4)
             + ellipse(cx + w * 0.62, top + h * 0.5, w * 0.2, h * 0.65, rim, opacity=0.35)
             + ellipse(cx, top + h + 4, w * 0.4, 10, sk_dd, opacity=0.35)
             + "</g>")
    # cheeks
    blush = spec.get("blush", "#e0458e")
    for sd in (-1, 1):
        o.append(ellipse(cx + sd * w * 0.27, eye_y + 14, 7, 3.5, blush, opacity=0.18 if mood != "smile" else 0.3))
    # eyes, brows
    lid = spec.get("lid", "#2a1a14")
    for sd in (-1, 1):
        o.append(eye(cx + sd * ex, eye_y, mood, spec.get("iris", "#4e2c1e"), sd, spec.get("eye_size", 1.0), lid, spec.get("age", 0),
                     spec.get("smile_open", False)))
        bmood = spec.get("brow_mood", {}).get(mood, mood)
        o.append(brow(cx + sd * ex, eye_y - 11 - spec.get("brow_raise", 0), bmood, sd,
                      spec.get("brow_color", shade(spec["hair"], 0.7)), spec.get("brow_thick", 2.6), spec.get("brow_len", 9)))
    # nose
    ny = top + h * spec.get("nose_y", 0.7)
    nose_style = spec.get("nose", "default")
    if callable(nose_style):
        o.append(nose_style(spec, cx, eye_y, ny))
    elif nose_style == "default":
        o.append(path(f"M{cx + 1},{eye_y + 4} Q{cx + 4},{ny} {cx + 3},{ny + 3} Q{cx},{ny + 5} {cx - 3},{ny + 3}",
                      stroke=sk_dd, stroke_width=1.3, stroke_linecap="round"))
        o.append(circle(cx + 2, ny + 1, 1.6, shade(skin, 1.25), opacity=0.6))
    else:
        o.append(nose(nose_style, cx, eye_y, ny, skin))
    # mouth
    o.append(mouth(cx, top + h * spec.get("mouth_y", 0.83), mood, w=spec.get("mouth_w", 1.0), style=spec.get("mouth_style", {}).get(mood)))
    if "extra_face" in spec:
        o.append(spec["extra_face"](spec, mood))
    o.append(spec.get("front_hair", lambda s: "")(spec))
    o.append(spec.get("accessories", lambda s: "")(spec))
    return svg(PW, PH, "".join(o), defs)


def bust(cx, y, wide, color, collar=None, dark=None):
    """Shoulders shape from y down to the bottom of the canvas."""
    d = dark or shade(color, 0.75)
    return (path(f"M{cx - wide},{PH} L{cx - wide + 6},{y + 22} Q{cx - wide + 14},{y} {cx - 26},{y - 4} "
                 f"L{cx + 26},{y - 4} Q{cx + wide - 14},{y} {cx + wide - 6},{y + 22} L{cx + wide},{PH} Z", color) +
            path(f"M{cx - wide},{PH} L{cx - wide + 6},{y + 22} Q{cx - wide + 14},{y} {cx - 26},{y - 4} L{cx - 20},{PH} Z", d, opacity=0.7))


def write_moods(name, spec, outdir, moods=("neutral", "smile", "sad")):
    os.makedirs(outdir, exist_ok=True)
    for m in moods:
        open(os.path.join(outdir, f"{name}_{m}.svg"), "w").write(portrait(spec, m))
