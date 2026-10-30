# -*- coding: utf-8 -*-
"""Redraw of the competency-distribution figure in Eero Alvar, "Bodybuilding for the Mind" (YouTube, 2026-09-27).
Same format: dark ground, red block 'not "the competition"' (left), green block '"the competition"' (right),
narrow grey dashed distribution (before) widening into a red->orange->green distribution (after), outward arrows,
double-headed 'competency' axis. Paperlogy."""
import math
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
CREAM = "#fff3ea"; LINE = "#d6d0ca"
W, H = 1260, 600
AX_Y, C = 520, 626
def gauss(sig, peak_y, x0=60, x1=1200):
    pts = []
    for i in range(0, 241):
        x = x0 + (x1 - x0) * i / 240
        y = AX_Y - (AX_Y - peak_y) * math.exp(-((x - C) ** 2) / (2 * sig ** 2))
        pts.append(f"{x:.1f},{y:.1f}")
    return "M" + " L".join(pts)
def t(x, y, s_, size, fill=CREAM, bold=False):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}" text-anchor="middle">{s_}</text>')
s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
     '<defs><linearGradient id="g" x1="60" y1="0" x2="1200" y2="0" gradientUnits="userSpaceOnUse">'
     '<stop offset="0" stop-color="#ff2a2a"/><stop offset="0.5" stop-color="#ffb020"/><stop offset="1" stop-color="#3fe03f"/></linearGradient>'
     '<marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
     f'<path d="M0,0 L10,5 L0,10" fill="none" stroke="{CREAM}" stroke-width="1.6"/></marker></defs>')
s += f'<rect x="66" y="98" width="560" height="{AX_Y - 98}" fill="#b01c1c" fill-opacity="0.55"/>'
s += f'<rect x="850" y="98" width="326" height="{AX_Y - 98}" fill="#1f9e2a" fill-opacity="0.6"/>'
s += t(346, 64, 'not "the competition"', 44) + t(1010, 64, '"the competition"', 44)
s += f'<path d="{gauss(72, 148)}" fill="none" stroke="#bdb6b0" stroke-width="3.5" stroke-dasharray="12 9" opacity="0.85"/>'
s += f'<path d="{gauss(230, 365)}" fill="none" stroke="url(#g)" stroke-width="4.5"/>'
s += f'<line x1="515" y1="355" x2="440" y2="355" stroke="{CREAM}" stroke-width="3" marker-end="url(#a)"/>'
s += f'<line x1="737" y1="355" x2="812" y2="355" stroke="{CREAM}" stroke-width="3" marker-end="url(#a)"/>'
s += f'<line x1="50" y1="{AX_Y}" x2="1210" y2="{AX_Y}" stroke="{CREAM}" stroke-width="2.5" marker-start="url(#a)" marker-end="url(#a)"/>'
s += t(626, 568, "competency", 40)
s += "</svg>"
(OUT / "fig-competency-bifurcation.svg").write_text(s, encoding="utf-8")
# variant without the two "competition" labels (talk deck premises slide), top trimmed
LABELS = t(346, 64, 'not "the competition"', 44) + t(1010, 64, '"the competition"', 44)
s2 = (s.replace(LABELS, "")
      .replace(f'viewBox="0 0 {W} {H}" width="{W}" height="{H}"', f'viewBox="0 0 {W} {H - 88}" width="{W}" height="{H - 88}"')
      .replace("</defs>", '</defs><g transform="translate(0 -88)">').replace("</svg>", "</g></svg>"))
(OUT / "fig-competency-bifurcation-plain.svg").write_text(s2, encoding="utf-8")
print("ok")
