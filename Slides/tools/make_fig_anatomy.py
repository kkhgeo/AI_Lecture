# -*- coding: utf-8 -*-
"""Common anatomy table (own figure): same four parts, different names in Claude Code and Codex.
As of 2026-09 (Knowledge/03_coding_agents 03, 05-07, 09, 13)."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
CREAM = "#fff3ea"; LABEL = "#e2dcd6"; MUTED = "#b8b2ac"; RULE = "#6a645e"
COLS = [("Claude Code", "#ffab80"), ("Codex", "#a9c6ff")]
ROWS = [
    ("Model", [["Claude", "(Opus, Sonnet, Haiku)"], ["GPT", "(GPT-6 Sol, Luna)"]]),
    ("Tools", [["Read, Edit, Bash, Web", "+ MCP"], ["Shell, Plan, Web search", "+ MCP"]]),
    ("Permissions", [["Permission modes + rules", "Sandbox (optional)"], ["Approval policy", "Sandbox (on by default)"]]),
    ("Instructions", [["CLAUDE.md", "(also reads AGENTS.md)"], ["AGENTS.md", ""]]),
]
W, HH, RH, LH = 1100, 66, 112, 35
CX = [250, 690]
H = HH + RH * len(ROWS) + 6

def t(x, y, s, size, fill, bold=False):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" '
            f'font-size="{size}" fill="{fill}">{s}</text>')

s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
for j, (name, col) in enumerate(COLS):
    s += t(CX[j], 40, name, 28, col, True)
s += f'<line x1="0" y1="{HH}" x2="{W}" y2="{HH}" stroke="{LABEL}" stroke-width="2"/>'
for i, (rname, cells) in enumerate(ROWS):
    y0 = HH + i * RH
    s += t(0, y0 + 46, rname, 26, CREAM, True)
    for j, items in enumerate(cells):
        for k, it in enumerate(items):
            if it:
                s += t(CX[j], y0 + 46 + k * LH, it, 26, LABEL if k == 0 else MUTED)
    s += f'<line x1="0" y1="{y0 + RH}" x2="{W}" y2="{y0 + RH}" stroke="{RULE}" stroke-width="1.4"/>'
s += "</svg>"
(OUT / "fig-anatomy.svg").write_text(s, encoding="utf-8")
print("ok", W, H)
