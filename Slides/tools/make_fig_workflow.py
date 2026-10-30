# -*- coding: utf-8 -*-
"""Research workflow with a coding agent (own figure; no source figure).
Explore -> Plan -> Implement -> Verify -> Commit (Claude Code best practices: explore, plan, code, commit)
plus the habits of Anthropic's long-running scientific-computing case (2026-03-23):
CLAUDE.md for plan/decisions, reference result as test oracle, CHANGELOG for progress/failed attempts, git commits."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
LINE = "#d6d0ca"; LABEL = "#e2dcd6"; MUTED = "#b8b2ac"; CREAM = "#fff3ea"
C = {"blue": ("#0f2340", "#5b95ff", "#a9c6ff"), "green": ("#0c2a21", "#3fc59a", "#8fe6c6"),
     "grey": ("#1c1a18", "#bdb6b0", "#ece6e0"), "brown": ("#2a1e10", "#c9a36a", "#ecd3a8")}
W, H = 1100, 440
BW, BH, GAP, Y0 = 188, 78, 40, 70
xs = [i * (BW + GAP) for i in range(5)]
cx = [x + BW / 2 for x in xs]
cy = Y0 + BH / 2

def t(x, y, s, size, fill, bold=False, anchor="middle"):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" '
            f'font-size="{size}" fill="{fill}" text-anchor="{anchor}">{s}</text>')
def box(x, y, w, h, col, lines, size=26, bold=True, dash=False):
    f, st, tx = C[col]
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{f}" stroke="{st}" stroke-width="2"'
           + (' stroke-dasharray="7 5"' if dash else "") + "/>")
    for i, l in enumerate(lines):
        yy = y + h / 2 + size * 0.36 + (i - (len(lines) - 1) / 2) * (size + 6)
        out += t(x + w / 2, yy, l, size if i == 0 else size - 4, tx if i == 0 else MUTED, bold and i == 0)
    return out
def arrow(x1, y1, x2, y2, col=LINE, w=3, dash=False):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"'
            + (' stroke-dasharray="7 5"' if dash else "") + ' marker-end="url(#a)"/>')

s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
     f'<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
     f'<path d="M0,0 L10,5 L0,10" fill="none" stroke="{LINE}" stroke-width="1.8"/></marker></defs><g transform="translate(0,12)">')
# plan-mode bracket over Explore + Plan
s += (f'<path d="M0 44 L0 30 L{xs[1] + BW} 30 L{xs[1] + BW} 44" fill="none" stroke="#5b95ff" stroke-width="2"/>'
      + t((xs[1] + BW) / 2, 20, "Plan mode (read only)", 22, "#a9c6ff"))
labels = [("Explore", "blue"), ("Plan", "blue"), ("Implement", "green"), ("Verify", "green"), ("Commit", "grey")]
SUB = {4: "git"}
for i, (lab, col) in enumerate(labels):
    s += box(xs[i], Y0, BW, BH, col, [lab] + ([SUB[i]] if i in SUB else []))
    if i < 4:
        s += arrow(xs[i] + BW + 4, cy, xs[i + 1] - 4, cy)
# fail -> fix loop (Verify back to Implement)
s += (f'<path d="M{cx[3]} {Y0 - 4} L{cx[3]} 52 L{cx[2]} 52 L{cx[2]} {Y0 - 6}" fill="none" stroke="#3fc59a" stroke-width="2.6" marker-end="url(#a)"/>'
      + t((cx[2] + cx[3]) / 2, 42, "fail → fix", 20, "#8fe6c6"))
# records row
DY = 244; DH = 108
docs = [(1, ["CLAUDE.md", "plan, decisions"]), (3, ["Reference", "known result"]), (4, ["CHANGELOG.md", "progress, failures"])]
for i, ls in docs:
    w = {1: 236, 3: 206, 4: 266}[i]
    x = {1: cx[1] - w / 2, 3: 596, 4: W - w - 2}[i]  # Reference shifted left so it clears CHANGELOG
    s += box(x, DY, w, DH, "brown", ls, size=27, dash=True)
    s += f'<line x1="{cx[i]}" y1="{Y0 + BH + 4}" x2="{cx[i]}" y2="{DY - 4}" stroke="#c9a36a" stroke-width="2" stroke-dasharray="6 5"/>'
# next task / next session loop back to Explore
ly = DY + DH + 54
s += (f'<path d="M{W - 127} {DY + DH + 4} L{W - 127} {ly} L{cx[0]} {ly} L{cx[0]} {Y0 + BH + 8}" fill="none" '
      f'stroke="{LINE}" stroke-width="2.4" stroke-dasharray="8 6" marker-end="url(#a)"/>'
      + t(W / 2 - 60, ly - 14, "next task · next session", 22, LABEL))
s += "</g></svg>"
(OUT / "fig-research-workflow.svg").write_text(s, encoding="utf-8")
print("ok")
