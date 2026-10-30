# -*- coding: utf-8 -*-
"""AI agent, hub layout (own figure; no source figure).
The agent (the user's Claude Code mascot = LLM + Harness) sits in the middle; the human sends a request, may check
mid-way, and gets the result; the agent repeats Plan -> Act -> Verify and uses Memory, Skills and Tools.
Agent definition: Willison (2025-09-18), Anthropic (2025-09-29), OpenAI practical guide (2025);
harness: Claude Code docs, LangChain "Agent = Model + Harness" (2026-03-10).
Colours follow DESIGN_RULES.md: copper = input/active, grey = what the agent uses, cream lines/labels.
Writes fig-ai-agent.svg (animated with SMIL: steps light up in turn, mascot walks in place) and
fig-ai-agent-static.svg (for the PNG twin used in PPTX).
Domain variant (fig-domain-agent*.svg): same skeleton; row 2 switches from the general setup (grey, 2 s) to an
environmental-research setup (copper, 4 s) with an example line under each box, plus a Data store outside the
agent joined by a connector. Static twin shows the domain state.
"""
import math
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
COPPER = "#E4B592"; GREY = "#7E7E7E"; LINE = "#d6d0ca"; LABEL = "#e2dcd6"; MUTED = "#8C8681"; CREAM = "#fff3ea"
ORANGE = "#D97757"
W, H = 1100, 504

def t(x, y, s, size, fill, bold=False, anchor="middle", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" '
            f'font-size="{size}" fill="{fill}" text-anchor="{anchor}">{s}{extra}</text>')
def arrow(p1, p2, col=LINE, w=3, dash=None):
    """Straight arrow from p1 to p2 (any angle)."""
    (x1, y1), (x2, y2) = p1, p2
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    bx, by = x2 - 16 * ux, y2 - 16 * uy
    px, py = -uy * 9, ux * 9
    return (f'<path d="M{x1} {y1} L{bx:.1f} {by:.1f}" fill="none" stroke="{col}" stroke-width="{w}"'
            + (f' stroke-dasharray="{dash}"' if dash else "") + "/>"
            f'<polygon points="{bx + px:.1f},{by + py:.1f} {x2},{y2} {bx - px:.1f},{by - py:.1f}" fill="{col}"/>')
def path_arrow(pts, col=LINE, w=3):
    """Axis-aligned polyline with an arrowhead at the last point."""
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    dx, dy = (x2 > x1) - (x2 < x1), (y2 > y1) - (y2 < y1)
    bx, by = x2 - 14 * dx, y2 - 14 * dy
    px, py = -dy * 8, dx * 8
    return (f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"/>'
            f'<polygon points="{bx + px},{by + py} {x2},{y2} {bx - px},{by - py}" fill="{col}"/>')

def figure(animated, domain=False):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'

    # agent frame: three equal boxed rows linked top to bottom
    #   row 1: mascot + "AI agent" (open), [LLM + Harness] boxed; rows share three columns / row 2: Memory, Skills, Tools / row 3: work loop
    FX, FY, FW, FH = 290, 6, 804, 492
    s += f'<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="18" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="10 7"/>'
    def box(x, y, w, h, lab, fill, txt="#000", size=30):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}"/>'
                + t(x + w / 2, y + h / 2 + size * 0.36, lab, size, txt, True))
    def group(x, y, w, h):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="none" stroke="{LINE}" stroke-width="2.4"/>'
    KT, DUR = "0;0.3333;0.6667;1", "6s"  # Plan, Act, Verify each lit for 2 s

    RX, RW, RH, RG = 314, 756, 128, 36
    ry = [24 + k * (RH + RG) for k in range(3)]
    MID = RX + RW / 2
    IW = 210                           # one column width, shared by all three rows
    IG = (RW - 40 - 3 * IW) / 2
    col = [RX + 20 + k * (IW + IG) for k in range(3)]
    G1 = col[1] - 20                   # row 1 box wraps LLM + Harness only; the mascot stands outside it
    s += group(G1, ry[0], RX + RW - G1, RH)
    s += group(RX, ry[1], RW, RH) + group(RX, ry[2], RW, RH)
    s += arrow(((G1 + RX + RW) / 2, ry[0] + RH + 3), ((G1 + RX + RW) / 2, ry[1] - 3))
    s += arrow((MID, ry[1] + RH + 3), (MID, ry[2] - 3))

    # row 1, column 1: "AI agent" over the mascot; it turns around once after Verify (scaleX 1 -> -1 -> 1)
    MX, U, FEET = (RX + G1) / 2, 8, ry[0] + 124
    body = [(2, 0, 13, 2), (2, 2, 2, 2), (5, 2, 7, 2), (13, 2, 2, 2), (0, 4, 17, 2), (2, 6, 13, 2)]
    def cells(rects):
        return "".join(f'<rect x="{c * U - 8.5 * U}" y="{r * U - 10 * U}" width="{w * U}" height="{h * U}"/>'
                       for c, r, w, h in rects)
    def legs(cols, vals):
        a = (f'<animate attributeName="opacity" values="{vals}" dur="0.5s" repeatCount="indefinite" calcMode="discrete"/>'
             if animated else "")
        return "<g>" + cells([(c, 8, 1, 2) for c in cols]) + a + "</g>"
    bob = (f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -4;0 0" dur="0.5s" '
           f'repeatCount="indefinite"/>') if animated else ""
    spin = (f'<animateTransform attributeName="transform" type="scale" dur="{DUR}" repeatCount="indefinite" '
            f'values="1 1;1 1;0.05 1;-1 1;0.05 1;1 1;1 1" keyTimes="0;0.70;0.74;0.78;0.82;0.86;1"/>') if animated else ""
    SW = "0;0.3333;1"  # domain swap: general for the first 2 s of the 6 s loop, then domain
    def swap(general, specific, y, x=None, anchor="middle", size=30, fill=LABEL, bold=True):
        """Two labels at one spot; in the domain figure the second replaces the first after 2 s."""
        x = MX if x is None else x
        if not domain:
            return t(x, y, general, size, fill, bold, anchor)
        if not animated:
            return t(x, y, specific, size, fill, bold, anchor)
        a = lambda v: (f'<animate attributeName="opacity" values="{v}" keyTimes="{SW}" dur="{DUR}" '
                       f'repeatCount="indefinite" calcMode="discrete"/>')
        return (t(x, y, general, size, fill, bold, anchor, extra=a("1;0;0"))
                + t(x, y, specific, size, fill, bold, anchor, extra=a("0;1;1")))
    s += swap("AI agent", "Domain agent", ry[0] + 28)
    s += (f'<g transform="translate({MX} {FEET})"><g>{bob}<g fill="{ORANGE}" shape-rendering="crispEdges">{spin}'
          + cells(body) + legs([2, 12], "1;0") + legs([4, 14], "0;1") + "</g></g></g>")
    # row 1, columns 2-3: LLM + Harness
    c1 = ry[0] + RH / 2
    s += box(col[1], c1 - 36, IW, 72, "LLM", COPPER)
    s += t((col[1] + IW + col[2]) / 2, c1 + 13, "+", 36, LABEL, True)
    s += box(col[2], c1 - 36, IW, 72, "Harness", GREY)

    # row 2: Memory, Skills, Tools
    c2 = ry[1] + RH / 2
    if not domain:
        for k, lab in enumerate(["Memory", "Skills", "Tools"]):
            s += box(col[k], c2 - 36, IW, 72, lab, GREY)
    else:
        gen = ["CLAUDE.md, notes", "general workflows", "files, shell, web"]
        env = ["SOPs, literature", "data QC, reporting", "GIS, DBs, models"]
        fill_anim = (f'<animate attributeName="fill" values="{GREY};{COPPER};{COPPER}" keyTimes="{SW}" dur="{DUR}" '
                     f'repeatCount="indefinite" calcMode="discrete"/>') if animated else ""
        for k, lab in enumerate(["Memory", "Skills", "Tools"]):
            s += (f'<rect x="{col[k]}" y="{c2 - 48}" width="{IW}" height="60" rx="8" fill="{COPPER}">{fill_anim}</rect>'
                  + t(col[k] + IW / 2, c2 - 7, lab, 30, "#000", True))
            s += swap(gen[k], env[k], c2 + 46, col[k] + IW / 2, size=24, bold=False)

    # row 3: Plan -> Act -> Verify, repeat until done
    R3 = ry[2] + 40
    BW, BH = IW, 56
    xs = col
    for k, lab in enumerate(["Plan", "Act", "Verify"]):
        on = [COPPER if j == k else LINE for j in range(3)] + [LINE]
        ont = [COPPER if j == k else CREAM for j in range(3)] + [CREAM]
        a_box = (f'<animate attributeName="stroke" values="{";".join(on)}" keyTimes="{KT}" dur="{DUR}" '
                 f'repeatCount="indefinite" calcMode="discrete"/>') if animated else ""
        a_txt = (f'<animate attributeName="fill" values="{";".join(ont)}" keyTimes="{KT}" dur="{DUR}" '
                 f'repeatCount="indefinite" calcMode="discrete"/>') if animated else ""
        s += (f'<rect x="{xs[k]}" y="{R3 - BH / 2}" width="{BW}" height="{BH}" rx="8" fill="#000" stroke="{LINE}" '
              f'stroke-width="2.4">{a_box}</rect>')
        s += t(xs[k] + BW / 2, R3 + 11, lab, 30, CREAM, True, extra=a_txt)
        if k < 2:
            s += arrow((xs[k] + BW + 2, R3), (xs[k + 1] - 2, R3))
    lx, rx = xs[0] + BW / 2, xs[2] + BW / 2
    s += path_arrow([(rx, R3 + BH / 2 + 2), (rx, R3 + 46), (lx, R3 + 46), (lx, R3 + BH / 2 + 2)])
    s += t((lx + rx) / 2, R3 + 76, "repeat until done", 24, LABEL)

    # human: request in, check (dashed, both ways), result out
    HY = 252
    s += (f'<rect x="0" y="{HY - 90}" width="150" height="180" rx="40" fill="none" stroke="{LINE}" stroke-width="2.4"/>'
          + t(75, HY + 11, "Human", 30, CREAM, True))
    s += arrow((152, HY - 50), (FX - 2, HY - 50), COPPER, 3.5) + t(220, HY - 64, "Request", 24, COPPER, True)
    s += arrow((152, HY), (FX - 2, HY), LINE, 2.4, "8 6") + arrow((FX - 2, HY), (152, HY), LINE, 2.4, "8 6")
    s += t(220, HY - 12, "check", 24, LABEL)
    s += arrow((FX - 2, HY + 50), (152, HY + 50)) + t(220, HY + 38, "Result", 24, LABEL, True)

    # domain figure only: data lives outside the agent, reached through a connector (e.g. MCP)
    if domain:
        yt, yb, rr = 384, 444, 13  # cylinder top / bottom centre lines, lid radius
        fill_anim = (f'<animate attributeName="fill" values="{GREY};{COPPER};{COPPER}" keyTimes="{SW}" dur="{DUR}" '
                     f'repeatCount="indefinite" calcMode="discrete"/>') if animated else ""
        s += (f'<path d="M0 {yt} A75 {rr} 0 0 1 150 {yt} V{yb} A75 {rr} 0 0 1 0 {yb} Z" fill="{COPPER}">{fill_anim}</path>'
              f'<ellipse cx="75" cy="{yt}" rx="73" ry="{rr - 1}" fill="none" stroke="#000" stroke-width="2.4"/>'
              + t(75, (yt + yb) / 2 + 17, "Data", 30, "#000", True))
        s += swap("local files", "domain knowledge", yb + 44, 2, "start", size=24, bold=False)
        s += arrow((152, 414), (FX - 2, 414)) + arrow((FX - 2, 414), (152, 414))
        s += t(220, 400, "connector", 24, LABEL)
    return s + "</svg>"

for name, animated, domain in [("fig-ai-agent.svg", True, False), ("fig-ai-agent-static.svg", False, False),
                               ("fig-domain-agent.svg", True, True), ("fig-domain-agent-static.svg", False, True)]:
    (OUT / name).write_text(figure(animated, domain), encoding="utf-8")
    print("wrote", OUT / name)
