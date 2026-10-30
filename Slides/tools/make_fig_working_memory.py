# -*- coding: utf-8 -*-
"""Working-memory slots: without AI all ~4 chunks (Cowan) go to the task; with AI part of them is taken by
metacognitive work — deciding what you want / what to delegate, and evaluating the output (Tankelevitch et al., CHI 2024).
Own figure, dark, Paperlogy."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
CREAM = "#fff3ea"; LABEL = "#e2dcd6"; MUTED = "#b8b2ac"
TASK = ("#2e2a27", "#bdb6b0", CREAM)
GOAL = ("#0f2340", "#5b95ff", "#a9c6ff")
EVAL = ("#2e1408", "#ff7a3d", "#ffab80")
W, H = 1040, 470
X0, SW, SH, GAP = 250, 180, 112, 16

def t(x, y, s, size, fill=LABEL, bold=False, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}">{s}</text>')
def slot(x, y, lines, pal):
    f, st, tx = pal
    out = f'<rect x="{x}" y="{y}" width="{SW}" height="{SH}" rx="10" fill="{f}" stroke="{st}" stroke-width="2.2"/>'
    for i, l in enumerate(lines):
        out += t(x + SW / 2, y + SH / 2 + 10 + (i - (len(lines) - 1) / 2) * 32, l, 26, tx, True)
    return out
def row(y, label, slots):
    out = t(0, y + SH / 2 + 10, label, 30, CREAM, True, "start")
    out += (f'<rect x="{X0 - 14}" y="{y - 14}" width="{4 * SW + 3 * GAP + 28}" height="{SH + 28}" rx="16" '
            f'fill="none" stroke="#6a645e" stroke-width="2" stroke-dasharray="9 7"/>')
    for i, (lines, pal) in enumerate(slots):
        out += slot(X0 + i * (SW + GAP), y, lines, pal)
    return out

s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
s += t(X0 - 14, 36, "Working memory  (about 4 chunks)", 26, MUTED, anchor="start")
s += row(80, "Without AI", [(["Task"], TASK)] * 4)
s += row(250, "With AI", [(["Task"], TASK), (["Task"], TASK), (["Goal", "Delegate"], GOAL), (["Evaluate"], EVAL)])
# brace under the two metacognitive slots
bx0 = X0 + 2 * (SW + GAP); bx1 = X0 + 4 * SW + 3 * GAP; by = 250 + SH + 28
s += (f'<path d="M{bx0} {by} Q{bx0} {by + 14} {bx0 + 14} {by + 14} L{(bx0 + bx1) / 2 - 14} {by + 14} '
      f'Q{(bx0 + bx1) / 2} {by + 14} {(bx0 + bx1) / 2} {by + 28} Q{(bx0 + bx1) / 2} {by + 14} {(bx0 + bx1) / 2 + 14} {by + 14} '
      f'L{bx1 - 14} {by + 14} Q{bx1} {by + 14} {bx1} {by}" fill="none" stroke="{MUTED}" stroke-width="2"/>')
s += t((bx0 + bx1) / 2, by + 30 + 28, "Metacognitive demands", 26, LABEL, True)
s += "</svg>"
(OUT / "fig-working-memory.svg").write_text(s, encoding="utf-8")
print("ok")
