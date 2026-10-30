# -*- coding: utf-8 -*-
"""References written by AI: share fabricated / real-but-wrong / correct (own stacked bars, full texts read 2026-10-29).
GPT-3.5 & GPT-4: Walters & Wilder 2023, Sci Rep 13:14045 (PMC10484980), April 2023, 84 papers, 636 citations:
  GPT-3.5 222 cites, 101 real (121 fabricated), 43% of real with substantive errors; GPT-4 414 cites, 340 real, 24% errors.
GPT-4o: Linardon et al. 2025, JMIR Mental Health 12:e80371 (PMC12658395), June 2025: 176 cites, 35 fabricated,
  64 of 141 real with errors (mostly wrong DOIs).
Colours: copper = fabricated, light copper = real but wrong details, grey = correct. Paperlogy."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
COPPER = "#E4B592"; LIGHT = "#8a6e58"; GREY = "#7E7E7E"; LABEL = "#e2dcd6"; MUTED = "#8C8681"; CREAM = "#fff3ea"
ROWS = [  # label, total, fabricated, real-with-errors
    ("GPT-3.5 (2023)", 222, 121, round(101 * .43)),
    ("GPT-4 (2023)", 414, 74, round(340 * .24)),
    ("GPT-4o (2025)", 176, 35, 64),
]
W, H = 1100, 470
X0, BW, BH = 250, 820, 70
def t(x, y, s, size, fill=LABEL, bold=False, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}">{s}</text>')
s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
s += t(0, 34, "References in AI-written papers", 30, CREAM, True, "start")
s += t(0, 70, "share of all citations", 24, MUTED, False, "start")
for i, (lab, n, fab, err) in enumerate(ROWS):
    y = 110 + i * 100
    s += t(X0 - 20, y + BH / 2 + 10, lab, 28, LABEL, True, "end")
    x = X0
    for cnt, col, txt in [(fab, COPPER, "#000"), (err, LIGHT, CREAM), (n - fab - err, GREY, "#000")]:
        w = BW * cnt / n
        s += f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{BH}" fill="{col}"/>'
        if w > 70:
            s += t(x + w / 2, y + BH / 2 + 10, f"{100 * cnt / n:.0f}%", 28, txt, True)
        x += w
# legend
ly = H - 40
for k, (col, lab) in enumerate([(COPPER, "fabricated"), (LIGHT, "real, but wrong details"), (GREY, "correct")]):
    lx = X0 + [0, 220, 590][k]
    s += f'<rect x="{lx}" y="{ly - 20}" width="26" height="24" fill="{col}"/>' + t(lx + 36, ly, lab, 24, LABEL, False, "start")
s += "</svg>"
(OUT / "fig-fake-refs.svg").write_text(s, encoding="utf-8")
print("ok", [(r[0], round(100 * r[2] / r[1]), round(100 * r[3] / r[1])) for r in ROWS])
