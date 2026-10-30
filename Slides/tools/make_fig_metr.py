# -*- coding: utf-8 -*-
"""Redraw of METR (2025-07-10) "forecasted vs observed" chart (CC-BY), same format:
dot + 95% CI whiskers, inverted y axis (-50% top .. +40% bottom), shaded forecast panel, separate
'Observed result' panel, Speedup/Slowdown arrows, green forecasts / red observed. Dark, Paperlogy.
Values read from the source image pixels (assets/source/metr_forecasted-vs-observed.png)."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
CREAM = "#fff3ea"; LABEL = "#e2dcd6"; MUTED = "#b8b2ac"; WHISK = "#d6d0ca"
GREEN = "#4fd18b"; RED = "#ff6b62"
# (labels, point, lo, hi) in % change of completion time (negative = faster)
DATA = [(["Economics", "expert", "forecasts"], -38.8, -48.5, -28.9),
        (["ML expert", "forecasts"], -38.1, -44.2, -32.0),
        (["Developer", "forecasts", "during study"], -23.8, -32.3, -14.1),
        (["Developer", "estimates", "after study"], -20.4, -30.9, -9.9)]
OBS = (["Observed", "result"], 18.8, 1.3, 39.5)
W, H = 1100, 650
YT, YB = 120, 540            # -50% .. +40%
def y(v): return YT + (v + 50) / 90 * (YB - YT)
AX = 220; P1 = (245, 885); P2 = (905, 1095); AR = 100  # AR: x of Speedup/Slowdown arrows

def t(x, y_, s, size, fill, bold=False, anchor="middle", rot=None):
    tr = f' transform="rotate({rot} {x} {y_})"' if rot is not None else ""
    return (f'<text x="{x}" y="{y_}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}"{tr}>{s}</text>')
def whisker(cx, lo, hi):
    return (f'<line x1="{cx}" y1="{y(lo)}" x2="{cx}" y2="{y(hi)}" stroke="{WHISK}" stroke-width="3"/>'
            f'<line x1="{cx - 12}" y1="{y(lo)}" x2="{cx + 12}" y2="{y(lo)}" stroke="{WHISK}" stroke-width="3"/>'
            f'<line x1="{cx - 12}" y1="{y(hi)}" x2="{cx + 12}" y2="{y(hi)}" stroke="{WHISK}" stroke-width="3"/>')

s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
     f'<defs><marker id="ag" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{GREEN}"/></marker>'
     f'<marker id="ar" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{RED}"/></marker></defs>')
s += t(0, 30, "Against Expert Forecasts and Developer Self-Reports, Early-2025", 26, CREAM, True, "start")
s += t(0, 64, "AI Slows Down Experienced Open-Source Developers", 26, CREAM, True, "start")
s += f'<rect x="{P1[0]}" y="{YT}" width="{P1[1] - P1[0]}" height="{YB - YT}" fill="#161616"/>'
for v in range(-50, 41, 10):
    yy = y(v)
    for a, b in (P1, P2):
        s += f'<line x1="{a}" y1="{yy}" x2="{b}" y2="{yy}" stroke="#3a3632" stroke-width="1.4" stroke-dasharray="6 5"/>'
    s += t(AX - 12, yy + 8, (f"+{v}%" if v > 0 else f"{v}%"), 22, LABEL, anchor="end")
for a, b in (P1, P2):
    s += f'<line x1="{a}" y1="{y(0)}" x2="{b}" y2="{y(0)}" stroke="#9a948e" stroke-width="2.4"/>'
s += f'<line x1="{AX}" y1="{YT}" x2="{AX}" y2="{YB}" stroke="{MUTED}" stroke-width="2"/>'
s += t(24, (YT + YB) / 2, "Change in time when AI allowed", 24, LABEL, rot=-90)
s += f'<line x1="{AR}" y1="{y(-8)}" x2="{AR}" y2="{y(-44)}" stroke="{GREEN}" stroke-width="3" marker-end="url(#ag)"/>'
s += t(AR - 14, y(-26), "Speedup", 20, GREEN, rot=-90)
s += f'<line x1="{AR}" y1="{y(6)}" x2="{AR}" y2="{y(34)}" stroke="{RED}" stroke-width="3" marker-end="url(#ar)"/>'
s += t(AR - 14, y(20), "Slowdown", 20, RED, rot=-90)
slot = (P1[1] - P1[0]) / len(DATA)
def labels(cx, ls):
    return "".join(t(cx, YB + 34 + k * 27, l, 22, LABEL) for k, l in enumerate(ls))
for i, (ls, p, lo, hi) in enumerate(DATA):
    cx = P1[0] + slot * (i + 0.5)
    s += whisker(cx, lo, hi) + f'<circle cx="{cx}" cy="{y(p)}" r="13" fill="{GREEN}"/>' + labels(cx, ls)
cx = (P2[0] + P2[1]) / 2
ls, p, lo, hi = OBS
s += whisker(cx, lo, hi) + f'<circle cx="{cx}" cy="{y(p)}" r="13" fill="{RED}"/>' + labels(cx, ls)
s += "</svg>"
(OUT / "fig-metr-forecast-vs-observed.svg").write_text(s, encoding="utf-8")
print("ok")
