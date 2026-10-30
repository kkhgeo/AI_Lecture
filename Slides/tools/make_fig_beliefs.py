# -*- coding: utf-8 -*-
"""Two redraws for the Beliefs slides, same format as the sources, dark + Paperlogy.
fig-brain-prediction.svg  <- Caucheteux, Gramfort & King (2023, Nature Human Behaviour) Fig. 1a
    'Architectures and objectives': language algorithm predicts the next word (IS) from its top layer;
    the human brain predicts several future words (IS NOT REJECTED) from different levels of its hierarchy.
fig-division-of-labor.svg <- Anthropic, 'How people use Claude Code' (2026), 'The division of labor':
    share of sessions by Claude's share of planning vs execution decisions (values read from the chart)."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
CREAM = "#fff3ea"; LABEL = "#e2dcd6"; MUTED = "#b8b2ac"; LINE = "#d6d0ca"
def t(x, y, s, size, fill=LABEL, bold=False, anchor="middle", rot=None):
    tr = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}"{tr}>{s}</text>')
def head(w, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><style>{FONTS}</style>'
            '<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{CREAM}"/></marker></defs>')

# ---------- brain prediction (Fig. 1a)
W, H = 830, 560
s = head(W, H)
SQ_W, SQ_H, GX, GY = 92, 34, 16, 14          # hierarchy cell size and gaps
def grid(x0, ybot, n_cols):
    out = ""
    for c in range(n_cols):
        for r in range(3):
            x = x0 + c * (SQ_W + GX); y = ybot - (r + 1) * SQ_H - r * GY
            out += f'<rect x="{x}" y="{y}" width="{SQ_W}" height="{SQ_H}" rx="4" fill="#4a4540" stroke="#8a847e" stroke-width="1.5"/>'
    return out
def cell(x, r, ybot):
    return x, ybot - (r + 1) * SQ_H - r * GY
def pbox(x, y, filled=True):
    return (f'<rect x="{x}" y="{y}" width="{SQ_W}" height="{SQ_H}" rx="4" fill="{"#8a847e" if filled else "none"}" '
            f'stroke="{CREAM}" stroke-width="1.8" stroke-dasharray="{"" if filled else "6 5"}"/>')
words = ["GREAT", "YOUR", "PAPER"]
X0 = 104; SEP = X0 + 3 * (SQ_W + GX) + 20; PX = SEP + 40
for row, (label, ybot, preds) in enumerate([("Language algorithm", 200, ["IS"]), ("Human brain", 470, ["IS", "NOT", "REJECTED"])]):
    s += t(X0, ybot - 150, label, 28, CREAM, True, "start")
    s += grid(X0, ybot, 3)
    for c, w_ in enumerate(words):
        s += t(X0 + c * (SQ_W + GX) + SQ_W / 2, ybot + 30, w_, 20, MUTED)
    s += t(X0 + 1.5 * (SQ_W + GX) - GX / 2, ybot + 58, "Input", 20, MUTED)
    s += f'<line x1="{SEP}" y1="{ybot - 3 * SQ_H - 2 * GY - 10}" x2="{SEP}" y2="{ybot + 40}" stroke="{MUTED}" stroke-width="1.6" stroke-dasharray="6 5"/>'
    lastx = X0 + 2 * (SQ_W + GX)
    for k, w_ in enumerate(preds):
        px = PX + k * (SQ_W + GX)
        s += t(px + SQ_W / 2, ybot + 30, w_, 20, CREAM, True)
        # predicted word represented at the level that predicts it: algorithm -> top only; brain -> level k
        r = 2 if row == 0 else k
        bx, by = cell(px, r, ybot)
        for rr in range(3):
            cx_, cy_ = cell(px, rr, ybot)
            s += pbox(cx_, cy_, rr == r)
        sx, sy = cell(lastx, r, ybot)
        sx += SQ_W; sy += SQ_H / 2
        ex, ey = bx, by + SQ_H / 2
        s += (f'<path d="M{sx} {sy} C {sx + 40} {sy - 34 - 18 * k}, {ex - 40} {ey - 34 - 18 * k}, {ex - 4} {ey}" '
              f'fill="none" stroke="{CREAM}" stroke-width="2.6" marker-end="url(#a)"/>')
    s += t(PX + (len(preds) * (SQ_W + GX) - GX) / 2, ybot + 58, "Predict", 20, MUTED)
s += t(26, 330, "Neural hierarchy", 22, MUTED, rot=-90)
s += f'<line x1="58" y1="470" x2="58" y2="60" stroke="{MUTED}" stroke-width="2" marker-end="url(#a)"/>'
s += "</svg>"
(OUT / "fig-brain-prediction.svg").write_text(s, encoding="utf-8")

# ---------- division of labor
W, H = 1100, 600
PLAN = [24.0, 16.5, 20.3, 13.4, 14.0, 9.3, 3.5, 1.5, 0.3, 0.0]
EXEC = [0.9, 1.7, 3.0, 4.1, 4.1, 7.1, 8.9, 10.4, 12.3, 50.0]
BINS = ["0-10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80-90", "90-100"]
X0, X1, YT, YB = 110, 1090, 150, 500
def y(v): return YB - v / 50 * (YB - YT)
s = head(W, H)
s += t(W / 2, 40, "The division of labor", 34, CREAM, True)
s += t(W / 2, 80, "People decide what to do, Claude decides how to do it", 24, MUTED)
for v in range(0, 51, 10):
    s += f'<line x1="{X0 - 6}" y1="{y(v)}" x2="{X0}" y2="{y(v)}" stroke="{MUTED}" stroke-width="2"/>' + t(X0 - 14, y(v) + 8, str(v), 22, MUTED, anchor="end")
s += f'<line x1="{X0}" y1="{YT}" x2="{X0}" y2="{YB}" stroke="{MUTED}" stroke-width="2"/><line x1="{X0}" y1="{YB}" x2="{X1}" y2="{YB}" stroke="{MUTED}" stroke-width="2"/>'
slot = (X1 - X0) / 10; bw = 36
for i in range(10):
    cx = X0 + slot * (i + 0.5)
    s += f'<rect x="{cx - bw}" y="{y(PLAN[i])}" width="{bw}" height="{YB - y(PLAN[i])}" fill="#4a8bdf"/>'
    s += f'<rect x="{cx}" y="{y(EXEC[i])}" width="{bw}" height="{YB - y(EXEC[i])}" fill="#ee7d50"/>'
    s += t(cx, YB + 30, BINS[i], 20, MUTED)
s += t(W / 2 + 40, YB + 76, "Claude’s share of the decisions (%)", 22, LABEL)
s += t(30, (YT + YB) / 2, "Share of sessions (%)", 22, LABEL, rot=-90)
s += (f'<rect x="{X0 + 30}" y="{YT + 10}" width="290" height="84" rx="8" fill="none" stroke="{MUTED}" stroke-width="1.6"/>'
      f'<rect x="{X0 + 48}" y="{YT + 32}" width="30" height="12" fill="#4a8bdf"/>' + t(X0 + 90, YT + 45, "Planning decisions", 21, LABEL, anchor="start")
      + f'<rect x="{X0 + 48}" y="{YT + 64}" width="30" height="12" fill="#ee7d50"/>' + t(X0 + 90, YT + 77, "Execution decisions", 21, LABEL, anchor="start"))
s += "</svg>"
(OUT / "fig-division-of-labor.svg").write_text(s, encoding="utf-8")
print("ok")
