# -*- coding: utf-8 -*-
"""Redraw of OpenAI GPT-6 Astra system card (2026-09-03) Figure 10 "Coding Deception", same format:
title + 'Lower is better', y axis 0-20% with gridlines, two bars with value labels (GPT-5.6 Sol navy,
GPT-6 Astra magenta). Dark, Paperlogy. Values as printed on the source chart."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
CREAM = "#fff3ea"; LABEL = "#e2dcd6"; MUTED = "#b8b2ac"
BARS = [("GPT-5.6 Sol", 14.29, "#5b7fd6"), ("GPT-6 Astra", 3.54, "#e05bbd")]
W, H = 620, 470
X0, X1, YT, YB = 110, 610, 130, 410          # plot area; YT = 20%
def y(v): return YB - v / 20 * (YB - YT)
def t(x, y_, s, size, fill, bold=False, anchor="middle", rot=None):
    tr = f' transform="rotate({rot} {x} {y_})"' if rot is not None else ""
    return (f'<text x="{x}" y="{y_}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}"{tr}>{s}</text>')
s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
s += t(X0, 42, "Coding Deception", 32, CREAM, True, "start") + t(X0, 78, "Lower is better", 22, MUTED, anchor="start")
for v in range(0, 21, 5):
    s += f'<line x1="{X0}" y1="{y(v)}" x2="{X1}" y2="{y(v)}" stroke="{"#8a847e" if v == 0 else "#3a3632"}" stroke-width="{2 if v == 0 else 1.4}"/>'
    s += t(X0 - 12, y(v) + 8, f"{v}%", 22, MUTED, anchor="end")
s += t(26, (YT + YB) / 2, "Failure rate (%)", 22, LABEL, rot=-90)
slot = (X1 - X0) / 2; bw = 170
for i, (name, v, col) in enumerate(BARS):
    cx = X0 + slot * (i + 0.5)
    s += f'<rect x="{cx - bw / 2}" y="{y(v)}" width="{bw}" height="{YB - y(v)}" fill="{col}"/>'
    s += t(cx, y(v) - 14, f"{v:.2f}%", 28, CREAM, True)
    s += t(cx, YB + 36, name, 24, LABEL)
s += "</svg>"
(OUT / "fig-coding-deception.svg").write_text(s, encoding="utf-8")
print("ok")
