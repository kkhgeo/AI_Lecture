# -*- coding: utf-8 -*-
"""Coding-agent landscape table (own figure; no source figure). Rows = where it runs, columns = who builds it.
Representative examples as of 2026-09 (Knowledge/03_coding_agents/14_landscape-taxonomy.md, 05, 09-12)."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
CREAM = "#fff3ea"; LABEL = "#e2dcd6"; MUTED = "#b8b2ac"; RULE = "#6a645e"
COLS = [("Model labs", "#8fe6c6"), ("IDE / platform vendors", "#a9c6ff"), ("Open source", "#ffab80")]
ROWS = [
    ("Terminal (CLI)", [["Claude Code", "Codex CLI", "Antigravity CLI"], ["Copilot CLI"], ["OpenCode", "Aider", "Goose"]]),
    ("IDE", [["Claude Code (ext.)", "Codex (ext.)", "Antigravity"], ["Cursor", "GitHub Copilot", "Windsurf"], ["Cline", "Kilo Code"]]),
    ("Desktop app", [["Claude (Code tab)", "ChatGPT (Codex)"], ["Copilot app"], ["Goose", "OpenCode (beta)"]]),
    ("Cloud (async)", [["Claude Code (web)", "Codex cloud", "Jules"], ["Copilot cloud agent", "Devin"], ["OpenHands"]]),
]
W, HH, RH, LH = 1100, 66, 130, 33
CX = [205, 545, 875]  # column x (widths follow the longest entry)
H = HH + RH * len(ROWS) + 6

def t(x, y, s, size, fill, bold=False, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" '
            f'font-size="{size}" fill="{fill}" text-anchor="{anchor}">{s}</text>')

s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
for j, (name, col) in enumerate(COLS):
    s += t(CX[j], 40, name, 26, col, True)
s += f'<line x1="0" y1="{HH}" x2="{W}" y2="{HH}" stroke="{LABEL}" stroke-width="2"/>'
for i, (rname, cells) in enumerate(ROWS):
    y0 = HH + i * RH
    s += t(0, y0 + 42, rname, 26, CREAM, True)
    for j, items in enumerate(cells):
        for k, it in enumerate(items):
            s += t(CX[j], y0 + 42 + k * LH, it, 26, LABEL)
    s += f'<line x1="0" y1="{y0 + RH}" x2="{W}" y2="{y0 + RH}" stroke="{RULE}" stroke-width="1.4"/>'
s += "</svg>"
(OUT / "fig-landscape.svg").write_text(s, encoding="utf-8")
print("ok", W, H)
