# -*- coding: utf-8 -*-
"""Known task vs unknown task (speaker's own practice), drawn in one format so only the change stands out.
Both rows: four boxes left to right. Known task runs once (Plan -> Instruct -> Build -> Verify).
Unknown task starts from the artifact (Build -> Read back -> Understand -> Rebuild) and loops back,
with versions v1..v3 and 'my knowledge' growing on each loop. Own figure, dark, Paperlogy."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
CREAM = "#fff3ea"; LABEL = "#e2dcd6"; MUTED = "#b8b2ac"; LINE = "#d6d0ca"
C = {"blue": ("#0f2340", "#5b95ff", "#a9c6ff"), "green": ("#0c2a21", "#3fc59a", "#8fe6c6"),
     "orange": ("#2e1408", "#ff7a3d", "#ffab80")}
W, H = 1100, 600
BW, BH = 200, 70
XS = [0, 300, 600, 900]

def t(x, y, s, size, fill=LABEL, bold=False, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}">{s}</text>')
def box(x, y, label, col):
    f, st, tx = C[col]
    return (f'<rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="8" fill="{f}" stroke="{st}" stroke-width="2"/>'
            + t(x + BW / 2, y + BH / 2 + 9, label, 23 if len(label) > 10 else 25, tx, True))
def arrow(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{LINE}" stroke-width="2.6" marker-end="url(#a)"/>'
def row(y, title, sub, labels, cols):
    out = t(0, y - 22, title, 28, CREAM, True, "start") + t(232, y - 22, sub, 22, MUTED, anchor="start")
    for i, (lab, col) in enumerate(zip(labels, cols)):
        out += box(XS[i], y, lab, col)
        if i < 3:
            out += arrow(XS[i] + BW + 6, y + BH / 2, XS[i + 1] - 6, y + BH / 2)
    return out

s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
     '<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
     f'<path d="M0,0 L10,5 L0,10" fill="none" stroke="{LINE}" stroke-width="1.8"/></marker>'
     '<marker id="ao" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
     '<path d="M0,0 L10,5 L0,10" fill="none" stroke="#ff7a3d" stroke-width="1.8"/></marker></defs>')
# known task: plan first, one pass
y1 = 60
s += row(y1, "Known task", "plan first", ["Plan", "Instruct", "Build", "Verify"], ["blue", "blue", "green", "green"])
s += t(XS[3] + BW / 2, y1 + BH + 38, "done", 22, MUTED)
s += f'<line x1="0" y1="226" x2="{W}" y2="226" stroke="#3a3632" stroke-width="1.5" stroke-dasharray="8 8"/>'
# unknown task: artifact first, loop
y2 = 310
s += row(y2, "Unknown task", "artifact first", ["Build", "Walk through", "Understand", "Rebuild"], ["green", "orange", "orange", "green"])
ly = y2 + BH + 44
s += (f'<path d="M{XS[3] + BW / 2} {y2 + BH + 6} L{XS[3] + BW / 2} {ly} L{XS[1] + BW / 2} {ly} L{XS[1] + BW / 2} {y2 + BH + 10}" '
      f'fill="none" stroke="#ff7a3d" stroke-width="2.6" marker-end="url(#ao)"/>')
s += t((XS[1] + XS[3]) / 2 + BW / 2, ly - 12, "loop · v1 → v2 → v3", 22, "#ffab80")
# knowledge growth
ky = ly + 46; kx = XS[1] + 20
s += t(kx - 20, ky + 25, "my knowledge", 22, "#ffab80", anchor="end")
for i, (v, w) in enumerate([("v1", 150), ("v2", 330), ("v3", 560)]):
    s += f'<rect x="{kx}" y="{ky}" width="{w}" height="36" rx="6" fill="#ff7a3d" fill-opacity="{0.25 + 0.2 * i}"/>'
    s += t(kx + w - 24, ky + 25, v, 20, CREAM, True)
s += "</svg>"
(OUT / "fig-learning-backward.svg").write_text(s, encoding="utf-8")
print("ok")
