# -*- coding: utf-8 -*-
"""Redraw of Claude Code Docs "How Claude Code works" — agentic loop figure (official dark variant).
Structure, labels and colours follow the original dark SVG (green loop boxes #2E5A3C, grey prompt/done #383838,
green repeat arrow #4A8C5C, brown 'You' box #4A372B/#D4A27F); Paperlogy (PLG), larger text, no background plate.
"""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
LINE = "#d6d0ca"; TXT = "#f5f5f5"; MUTED = "#b8b2ac"
W, H = 1100, 440

def t(x, y, s, size, fill=TXT, bold=False):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" '
            f'font-size="{size}" fill="{fill}" text-anchor="middle">{s}</text>')
def box(x, y, w, h, fill, s=None, stroke=None, bold=True, size=26):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}"' + (f' stroke="{stroke}" stroke-width="2"' if stroke else "") + "/>"
    return out + (t(x + w / 2, y + h / 2 + 9, s, size, TXT, bold) if s else "")
def arrow(x1, x2, y, col=LINE):
    return (f'<path d="M{x1} {y} L{x2 - 12} {y}" stroke="{col}" stroke-width="3"/>'
            f'<polygon points="{x2 - 14},{y - 8} {x2},{y} {x2 - 14},{y + 8}" fill="{col}"/>')

s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
cy = 168
BW, GAP, X1 = 214, 30, 212
xs = [X1 + i * (BW + GAP) for i in range(3)]
cx = [x + BW / 2 for x in xs]
s += box(0, cy - 38, 160, 76, "#383838", "Your prompt", bold=False, size=22)
s += f'<rect x="196" y="60" width="{xs[2] + BW + 16 - 196}" height="240" rx="14" fill="none" stroke="#6a6a6a" stroke-width="2" stroke-dasharray="9 6"/>'
s += t(cx[1], 98, "agentic loop", 22, MUTED)
s += arrow(160, X1, cy)
for i, lab in enumerate(["Gather context", "Take action", "Verify results"]):
    s += box(xs[i], cy - 38, BW, 76, "#2E5A3C", lab, size=23)
    if i < 2:
        s += arrow(xs[i] + BW, xs[i + 1], cy)
s += (f'<path d="M{cx[2]} {cy + 38} L{cx[2]} 252 Q{cx[2]} 264 {cx[2] - 12} 264 L{cx[0] + 12} 264 Q{cx[0]} 264 {cx[0]} 252 L{cx[0]} {cy + 56}" '
      f'fill="none" stroke="#4A8C5C" stroke-width="3.5"/>'
      f'<polygon points="{cx[0] - 8},{cy + 58} {cx[0]},{cy + 40} {cx[0] + 8},{cy + 58}" fill="#4A8C5C"/>')
s += t(cx[1], 252, "repeat", 22, TXT)
s += arrow(xs[2] + BW, 990, cy)
s += box(990, cy - 38, 110, 76, "#383838", "Done", bold=False, size=22)
s += box(0, 340, 300, 90, "#4A372B", None, "#D4A27F")
s += t(150, 378, "You: interrupt, steer,", 22) + t(150, 410, "or add context", 22)
s += (f'<path d="M300 385 L{cx[1]} 385 L{cx[1]} 318" fill="none" stroke="#D4A27F" stroke-width="2.4" stroke-dasharray="8 5"/>'
      f'<polygon points="{cx[1] - 8},320 {cx[1]},302 {cx[1] + 8},320" fill="#D4A27F"/>')
s += "</svg>"
(OUT / "fig-agentic-loop.svg").write_text(s, encoding="utf-8")
print("ok")
