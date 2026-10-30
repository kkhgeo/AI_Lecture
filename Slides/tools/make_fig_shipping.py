# -*- coding: utf-8 -*-
"""'Pain of imperfection vs pain of not shipping' — redrawn in the format of the user-provided figure
(red horizontal line, rising green curve, glowing white dot where they cross, solid before / dashed after),
extended with the speaker's theory:
  - the imperfection line stays where it is with AI (a human in the loop still has to reach it),
  - AI steepens the not-shipping curve, so the crossing comes earlier on the time axis,
  - several such processes run in parallel.
Dark, Paperlogy."""
import math
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
CREAM = "#fff3ea"; LABEL = "#e2dcd6"; MUTED = "#b8b2ac"
W, H = 1100, 690
X0, Y0 = 80, 560          # origin
YR = 190                  # imperfection threshold
YS = 510                  # start height of not-shipping pain

def t(x, y, s, size, fill=LABEL, anchor="start", bold=False, rot=None):
    tr = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}"{tr}>{s}</text>')

YA = 292                  # AI-alone ceiling: AI gets the work this far, a human closes the rest

def curve(xs, xc, k, color, width, human=None, x_end_extra=110):
    """exponential rise from (xs, YS) crossing YR at xc; solid up to xc, dashed afterwards.
    If human is a colour, the stretch above the AI ceiling (YA -> YR) is drawn in that colour."""
    A = (YS - YR) / (math.exp(k * (xc - xs)) - 1)
    def y(x): return YS - A * (math.exp(k * (x - xs)) - 1)
    xsamp = [xs + (xc - xs) * i / 160 for i in range(161)]
    style = lambda c, w: f'fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round"'
    if human:
        lo = [p_ for p_ in xsamp if y(p_) >= YA]; hi = [p_ for p_ in xsamp if y(p_) <= YA + 2]
        out = f'<path d="M{" L".join(f"{x:.1f},{y(x):.1f}" for x in lo)}" {style(color, width)}/>'
        out += f'<path d="M{" L".join(f"{x:.1f},{y(x):.1f}" for x in hi)}" {style(human, width + 1)}/>'
    else:
        out = f'<path d="M{" L".join(f"{x:.1f},{y(x):.1f}" for x in xsamp)}" {style(color, width)}/>'
    post = []
    x = xc
    while x < xc + x_end_extra and y(x) > 50:
        post.append(f"{x:.1f},{y(x):.1f}"); x += 3
    if len(post) > 1:
        out += f'<path d="M{" L".join(post)}" {style(color if not human else human, width)} stroke-dasharray="10 8" opacity="0.7"/>'
    return out

def dot(x, r=9):
    return f'<circle cx="{x}" cy="{YR}" r="{r}" fill="#ffffff"/>'

s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
     '<defs>'
     '<marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
     f'<path d="M0,0 L10,5 L0,10" fill="none" stroke="{CREAM}" stroke-width="1.6"/></marker></defs>')
# axes
s += f'<line x1="{X0}" y1="{Y0}" x2="{X0}" y2="30" stroke="{CREAM}" stroke-width="3" marker-end="url(#a)"/>'
s += f'<line x1="{X0}" y1="{Y0}" x2="{W - 20}" y2="{Y0}" stroke="{CREAM}" stroke-width="3" marker-end="url(#a)"/>'
s += t(W - 30, Y0 + 40, "time", 26, LABEL, "end")
s += t(40, 300, "pain", 26, LABEL, "middle", rot=-90)
# imperfection line (unchanged with AI)
s += f'<line x1="{X0}" y1="{YR}" x2="{W - 60}" y2="{YR}" stroke="#ff3b3b" stroke-width="4"/>'
s += t(X0 + 14, YR - 18, "perfection", 30, "#ff4a4a", bold=True)
# AI-alone ceiling
s += f'<line x1="{X0}" y1="{YA}" x2="{W - 60}" y2="{YA}" stroke="#3fe03f" stroke-width="2" stroke-dasharray="8 8" opacity="0.7"/>'
# without AI (grey, solid)
XC_OLD = 930
s += curve(X0, XC_OLD, 0.0042, "#b8b2ac", 5.5, x_end_extra=60)
s += dot(XC_OLD, 8)
s += t(705, 438, "without AI", 28, LABEL, bold=True)
# with AI: three parallel processes, steeper; AI carries them to the ceiling, the human closes the gap
greens = [(X0, 420, "#3fe03f"), (X0 + 50, 490, "#34c935"), (X0 + 100, 560, "#2aa82c")]
for xs, xc, col in greens:
    s += curve(xs, xc, 0.0095, col, 4.5, human=CREAM)
for xs, xc, col in greens:
    s += dot(xc)
s += t(474, 422, "with AI", 28, "#8ff08f", bold=True)
# time saved bracket
yb = Y0 + 44
s += f'<line x1="{greens[0][1]}" y1="{yb}" x2="{XC_OLD}" y2="{yb}" stroke="{MUTED}" stroke-width="2.4" marker-start="url(#a)" marker-end="url(#a)"/>'
for xx in (greens[0][1], XC_OLD):
    s += f'<line x1="{xx}" y1="{YR + 12}" x2="{xx}" y2="{yb + 10}" stroke="{MUTED}" stroke-width="1.4" stroke-dasharray="4 6" opacity="0.6"/>'
s += t((greens[0][1] + XC_OLD) / 2, yb + 34, "time saved", 24, LABEL, "middle")
s += "</svg>"
(OUT / "fig-shipping-pain.svg").write_text(s, encoding="utf-8")
print("ok")
