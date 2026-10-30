# -*- coding: utf-8 -*-
"""Table of Karpathy's AI-assisted coding rhythm (X post, 2025-04-25, text checked via api.fxtwitter.com).
Original lines quoted verbatim (selected); the original skips number 5, so steps are shown 1-6 here (noted on the slide notes).
Dark, Paperlogy; Korean labels use an embedded Paperlogy subset."""
import base64, io
from pathlib import Path
from fontTools import subset
from fontTools.ttLib import TTFont
OUT = Path(__file__).resolve().parent.parent / "assets"
ROWS = [
    ("Context", "맥락 넣기", ["Stuff everything relevant into context."]),
    ("Milestone", "중간 목표", ["Describe the next single, concrete incremental change.",
                               "Don't ask for code, ask for a few high-level approaches, pros/cons."]),
    ("Draft", "초안 받기", ["Pick one approach, ask for first draft code."]),
    ("Review / learn", "검토와 학습", ["Pull up all the API docs … ask for explanations, clarifications,",
                                   "changes, wind back and try a different approach."]),
    ("Test", "테스트", ["Test."]),
    ("Commit", "커밋", ["Git commit. Ask for suggestions on what we could implement next. Repeat."]),
]
KO_TEXT = "".join(r[1] for r in ROWS) + "()"
src = r"C:\Users\KEI\AppData\Local\Microsoft\Windows\Fonts\Paperlogy-5Medium.ttf"
opts = subset.Options(); opts.flavor = "woff2"
f = TTFont(src); sb = subset.Subsetter(opts); sb.populate(text=KO_TEXT); sb.subset(f)
buf = io.BytesIO(); f.flavor = "woff2"; f.save(buf)
KFONT = "@font-face{font-family:'PLGK2';font-weight:500;src:url(data:font/woff2;base64," + base64.b64encode(buf.getvalue()).decode() + ") format('woff2');}"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8") + KFONT
F = "PLG,PLGK2,sans-serif"
CREAM = "#fff3ea"; LABEL = "#e2dcd6"; MUTED = "#b8b2ac"; RULE = "#4a4540"
W, HH = 1520, 56
RHS = [70 if len(r[2]) == 1 else 100 for r in ROWS]
H = HH + sum(RHS) + 4
X1 = 480; XK = 305  # Korean label column

def t(x, y, s, size, fill=LABEL, bold=False):
    s = s.replace("&", "&amp;")
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}">{s}</text>')

s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
s += t(0, 36, "Step", 24, MUTED, True) + t(X1, 36, "Karpathy’s words (2025-04-25)", 24, MUTED, True)
s += f'<line x1="0" y1="{HH}" x2="{W}" y2="{HH}" stroke="{LABEL}" stroke-width="2"/>'
y0 = HH
for i, ((en, ko, lines), rh) in enumerate(zip(ROWS, RHS)):
    s += t(0, y0 + 44, str(i + 1), 28, "#ffab80", True) + t(34, y0 + 44, en, 27, CREAM, True)
    s += t(XK, y0 + 44, f"({ko})", 22, MUTED)
    for k, l in enumerate(lines):
        s += t(X1, y0 + 43 + k * 33, l, 23, LABEL if k == 0 else MUTED)
    y0 += rh
    s += f'<line x1="0" y1="{y0}" x2="{W}" y2="{y0}" stroke="{RULE}" stroke-width="1.4"/>'
s += "</svg>"
(OUT / "fig-karpathy-rhythm.svg").write_text(s, encoding="utf-8")
print("ok", H)
