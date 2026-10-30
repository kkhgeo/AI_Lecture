# -*- coding: utf-8 -*-
"""Table of the four principles in the 'andrej-karpathy-skills' CLAUDE.md (Forrest Chang, 2026, from Karpathy's
2026-01-26 notes on LLM coding pitfalls). Headings and rules quoted verbatim from the file (selected lines). Dark, Paperlogy."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8") + Path(__file__).with_name("plgk_karpathy.css").read_text(encoding="utf-8")
F = "PLG,PLGK,sans-serif"
CREAM = "#fff3ea"; LABEL = "#e2dcd6"; MUTED = "#b8b2ac"; RULE = "#4a4540"
KO = ["(코딩 전에 생각하기)", "(단순함 우선)", "(필요한 곳만 고치기)", "(목표 기준 실행)"]
ROWS = [
    ("1", "Think Before Coding", ["Don't assume. Don't hide confusion.", "Surface tradeoffs."],
     ["State your assumptions explicitly. If uncertain, ask.", "If multiple interpretations exist, present them."]),
    ("2", "Simplicity First", ["Minimum code that solves the problem.", "Nothing speculative."],
     ["No features beyond what was asked.", "If you write 200 lines and it could be 50, rewrite it."]),
    ("3", "Surgical Changes", ["Touch only what you must.", "Clean up only your own mess."],
     ["Don't “improve” adjacent code, comments,", "or formatting. Every changed line should", "trace directly to the user's request."]),
    ("4", "Goal-Driven Execution", ["Define success criteria.", "Loop until verified."],
     ["“Fix the bug” → “Write a test that reproduces it,", "then make it pass.”"]),
]
COLS = [("Principle", 0), ("Rule", 410), ("Examples", 935)]
W, HH, RH = 1520, 56, 126
H = HH + RH * len(ROWS) + 4

def t(x, y, s, size, fill=LABEL, bold=False):
    s = s.replace("&", "&amp;")
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}">{s}</text>')

s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
for name, x in COLS:
    s += t(x, 36, name, 24, MUTED, True)
s += f'<line x1="0" y1="{HH}" x2="{W}" y2="{HH}" stroke="{LABEL}" stroke-width="2"/>'
for i, (num, name, rule, ex) in enumerate(ROWS):
    y0 = HH + i * RH
    s += t(0, y0 + 50, num, 30, "#ffab80", True) + t(36, y0 + 50, name, 28, CREAM, True)
    s += t(36, y0 + 88, KO[i], 22, MUTED)
    for k, l in enumerate(rule):
        s += t(COLS[1][1], y0 + 46 + k * 36, l, 24, CREAM)
    for k, l in enumerate(ex):
        s += t(COLS[2][1], y0 + 44 + k * 31, l, 21, MUTED)
    s += f'<line x1="0" y1="{y0 + RH}" x2="{W}" y2="{y0 + RH}" stroke="{RULE}" stroke-width="1.4"/>'
s += "</svg>"
(OUT / "fig-karpathy-guidelines.svg").write_text(s, encoding="utf-8")
print("ok", H)
