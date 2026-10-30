# -*- coding: utf-8 -*-
"""Doshi & Hauser (2024, Science Advances 10(28) eadn5290): GenAI ideas raise individual creativity but make stories
more alike. Own bar chart from the numbers in the text (PMC11244532, read 2026-10-23), changes vs Human-only:
  novelty  +5.4% (1 idea), +8.1% (5 ideas); usefulness +3.7%, +9.0%     (evaluator ratings, Results)
  similarity among stories in the same condition: +10.7%, +8.9% of the Human-only range (Results, 'Similarity of stories')
Colours: grey = 1 AI idea, copper = up to 5 AI ideas. Paperlogy."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
COPPER = "#E4B592"; GREY = "#7E7E7E"; LINE = "#d6d0ca"; LABEL = "#e2dcd6"; MUTED = "#8C8681"; CREAM = "#fff3ea"
W, H = 1100, 500
Y0, YT, VMAX = 400, 120, 12.0  # baseline, top, axis max (%)
def y(v): return Y0 - v / VMAX * (Y0 - YT)
def t(x, y_, s, size, fill=LABEL, bold=False, anchor="middle"):
    return (f'<text x="{x}" y="{y_}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}">{s}</text>')
def bars(cx, v1, v5, bw=74, gap=12):
    out = ""
    for x, v, col in [(cx - gap / 2 - bw, v1, GREY), (cx + gap / 2, v5, COPPER)]:
        out += f'<rect x="{x}" y="{y(v):.1f}" width="{bw}" height="{Y0 - y(v):.1f}" fill="{col}"/>'
        out += t(x + bw / 2, y(v) - 12, f"+{v:.1f}%", 26, CREAM, True)
    return out

s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
# panel A: each story rated higher
s += t(270, 36, "Each story: rated higher", 30, CREAM, True)
s += t(270, 72, "change vs. no AI (600 readers)", 24, MUTED)
s += bars(150, 5.4, 8.1) + bars(400, 3.7, 9.0)
s += t(150, Y0 + 40, "Novelty", 28, LABEL, True) + t(400, Y0 + 40, "Usefulness", 28, LABEL, True)
s += f'<line x1="20" y1="{Y0}" x2="520" y2="{Y0}" stroke="{LINE}" stroke-width="2"/>'
# panel B: stories more alike
s += f'<line x1="600" y1="20" x2="600" y2="{Y0 + 50}" stroke="{MUTED}" stroke-width="2" stroke-dasharray="8 6"/>'
s += t(860, 36, "All stories: more alike", 30, CREAM, True)
s += t(860, 72, "similarity among stories", 24, MUTED)
s += bars(860, 10.7, 8.9)
s += t(860, Y0 + 40, "Similarity", 28, LABEL, True)
s += t(860, Y0 + 74, "(share of no-AI spread)", 24, MUTED)
s += f'<line x1="680" y1="{Y0}" x2="1040" y2="{Y0}" stroke="{LINE}" stroke-width="2"/>'
# legend
s += (f'<rect x="20" y="{H - 34}" width="26" height="22" fill="{GREY}"/>' + t(56, H - 15, "1 AI idea", 24, LABEL, False, "start")
      + f'<rect x="200" y="{H - 34}" width="26" height="22" fill="{COPPER}"/>' + t(236, H - 15, "up to 5 AI ideas", 24, LABEL, False, "start"))
s += "</svg>"
(OUT / "fig-homogenization.svg").write_text(s, encoding="utf-8")
print("ok")
