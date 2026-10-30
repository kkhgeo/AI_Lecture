# -*- coding: utf-8 -*-
"""Redraw of Anthropic (2024) "Building effective agents" — Autonomous agent figure.
Structure, labels and colour roles follow the original (Human/Environment = orange pills,
LLM Call = green box, Stop = purple box, grey Action/Feedback arcs); dark, Paperlogy (PLG), larger text.
"""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
LINE = "#d6d0ca"; LABEL = "#e2dcd6"
C = {"orange": ("#2e1408", "#ff7a3d", "#ffab80"), "green": ("#0c2a21", "#3fc59a", "#8fe6c6"),
     "purple": ("#1b1540", "#8f83ff", "#c2baff")}
W, H = 1100, 470

def t(x, y, s, size, fill, bold=False):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" '
            f'font-size="{size}" fill="{fill}" text-anchor="middle">{s}</text>')
def node(x, y, w, h, s, col, pill=False):
    f, st, tx = C[col]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2 if pill else 4}" fill="{f}" stroke="{st}" stroke-width="2"/>'
            + t(x + w / 2, y + h / 2 + 11, s, 32, tx, True))

s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
     f'<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
     f'<path d="M0,0 L10,5 L0,10" fill="none" stroke="{LINE}" stroke-width="1.8"/></marker></defs><style>{FONTS}</style>')
cy = 200
s += node(10, cy - 40, 190, 80, "Human", "orange", True)
s += f'<line x1="218" y1="{cy}" x2="332" y2="{cy}" stroke="{LINE}" stroke-width="2.4" stroke-dasharray="7 6" marker-start="url(#a)" marker-end="url(#a)"/>'
s += node(350, cy - 40, 220, 80, "LLM Call", "green")
s += node(810, cy - 40, 280, 80, "Environment", "orange", True)
s += f'<path d="M592,{cy - 55} Q690,{cy - 175} 790,{cy - 55}" fill="none" stroke="{LINE}" stroke-width="3" marker-end="url(#a)"/>'
s += t(690, cy - 138, "Action", 30, LABEL)
s += f'<path d="M790,{cy + 55} Q690,{cy + 175} 592,{cy + 55}" fill="none" stroke="{LINE}" stroke-width="3" marker-end="url(#a)"/>'
s += t(690, cy + 162, "Feedback", 30, LABEL)
s += f'<line x1="460" y1="{cy + 56}" x2="460" y2="{cy + 150}" stroke="{LINE}" stroke-width="2.4" stroke-dasharray="7 6" marker-end="url(#a)"/>'
s += node(385, cy + 170, 150, 80, "Stop", "purple")
s += "</svg>"
(OUT / "fig-autonomous-agent.svg").write_text(s, encoding="utf-8")
print("wrote", OUT / "fig-autonomous-agent.svg")
