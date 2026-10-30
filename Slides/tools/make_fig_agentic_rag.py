# -*- coding: utf-8 -*-
"""Traditional RAG vs Agentic RAG (own figure; no source figure).
Top: fixed pipeline, retrieve once (Lewis et al. 2020; Gao et al. 2023 "Naive RAG").
Bottom: the LLM plans, retrieves with tools, evaluates the evidence and rewrites the query until it is enough
(Singh et al. 2025; Li et al. 2025: reasoning triggers new retrieval; ReAct, Self-RAG, CRAG as precursors).
Colours follow DESIGN_RULES.md: copper = input / active step, cream lines and labels.
Writes fig-agentic-rag.svg (SMIL: two loops Plan -> Retrieve -> Evaluate -> Rewrite, then Generate; mascot bobs)
and fig-agentic-rag-static.svg (PNG twin for PPTX).
"""
import math
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
COPPER = "#E4B592"; LINE = "#d6d0ca"; LABEL = "#e2dcd6"; MUTED = "#8C8681"; CREAM = "#fff3ea"; ORANGE = "#D97757"
W, H = 1100, 476

def t(x, y, s, size, fill, bold=False, anchor="middle", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" '
            f'font-size="{size}" fill="{fill}" text-anchor="{anchor}">{s}{extra}</text>')
def path_arrow(pts, col=LINE, w=3):
    """Axis-aligned polyline with an arrowhead at the last point."""
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    dx, dy = (x2 > x1) - (x2 < x1), (y2 > y1) - (y2 < y1)
    bx, by = x2 - 14 * dx, y2 - 14 * dy
    px, py = -dy * 8, dx * 8
    return (f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"/>'
            f'<polygon points="{bx + px},{by + py} {x2},{y2} {bx - px},{by - py}" fill="{col}"/>')

# Agentic loop schedule: 8 slots of 0.75 s = 6 s
SLOTS = ["Plan", "Retrieve", "Evaluate", "Rewrite", "Plan", "Retrieve", "Evaluate", "Generate"]
DUR = "6s"
KT = ";".join(f"{k / 8:.4f}" for k in range(9))

def step(x, y, w, h, lab, key, animated, size=28):
    """Outlined step box; lights copper in its slots."""
    on = [k for k, s in enumerate(SLOTS) if s == key]
    stroke = ";".join(COPPER if k in on else LINE for k in range(8)) + f";{LINE}"
    fill = ";".join(COPPER if k in on else CREAM for k in range(8)) + f";{CREAM}"
    a = lambda attr, v: (f'<animate attributeName="{attr}" values="{v}" keyTimes="{KT}" dur="{DUR}" '
                         f'repeatCount="indefinite" calcMode="discrete"/>') if animated and on else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#000" stroke="{LINE}" stroke-width="2.4">'
            f'{a("stroke", stroke)}</rect>' + t(x + w / 2, y + h / 2 + size * 0.36, lab, size, CREAM, True, extra=a("fill", fill)))
def query(x, y, w, h):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{COPPER}"/>'
            + t(x + w / 2, y + h / 2 + 10, "Query", 28, "#000", True))

def figure(animated):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
    C = [(200, 380), (450, 650), (720, 900)]  # three shared columns
    BH = 60

    # top: traditional RAG, one pass
    y0 = 52
    s += t(0, 30, "Traditional RAG", 26, LABEL, True, "start")
    s += query(0, y0, 140, BH)
    for (x1, x2), lab in zip(C, ["Retrieve", "Generate", "Answer"]):
        s += (f'<rect x="{x1}" y="{y0}" width="{x2 - x1}" height="{BH}" rx="8" fill="#000" stroke="{LINE}" stroke-width="2.4"/>'
              + t((x1 + x2) / 2, y0 + BH / 2 + 10, lab, 28, CREAM, True))
    cy0 = y0 + BH / 2
    s += path_arrow([(142, cy0), (198, cy0)])
    s += path_arrow([(382, cy0), (448, cy0)]) + path_arrow([(652, cy0), (718, cy0)])
    s += t(290, y0 + BH + 30, "top-k chunks, once", 24, MUTED)
    s += t(1094, cy0 + 9, "fixed path", 24, MUTED, False, "end")

    s += f'<line x1="0" y1="168" x2="1100" y2="168" stroke="{MUTED}" stroke-width="2" stroke-dasharray="10 7"/>'

    # bottom: agentic RAG, loop until the evidence is enough
    s += t(0, 214, "Agentic RAG", 26, LABEL, True, "start")
    U, MX, FEET = 4, 216, 222  # small mascot after the label
    body = [(2, 0, 13, 2), (2, 2, 2, 2), (5, 2, 7, 2), (13, 2, 2, 2), (0, 4, 17, 2), (2, 6, 13, 2), (2, 8, 1, 2),
            (4, 8, 1, 2), (12, 8, 1, 2), (14, 8, 1, 2)]
    bob = (f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -3;0 0" dur="0.5s" '
           f'repeatCount="indefinite"/>') if animated else ""
    s += (f'<g transform="translate({MX} {FEET})"><g fill="{ORANGE}" shape-rendering="crispEdges">{bob}'
          + "".join(f'<rect x="{c * U - 34}" y="{r * U - 40}" width="{w * U}" height="{h * U}"/>' for c, r, w, h in body)
          + "</g></g>")
    y1, y2 = 250, 382  # top and bottom rows of the loop
    cy1, cy2 = y1 + BH / 2, y2 + BH / 2
    s += query(0, y1, 140, BH)
    s += step(C[0][0], y1, 180, BH, "Plan", "Plan", animated)
    s += step(C[1][0], y1, 200, BH, "Retrieve", "Retrieve", animated)
    s += step(C[2][0], y1, 180, BH, "Evaluate", "Evaluate", animated)
    s += step(425, y2, 250, BH, "Rewrite query", "Rewrite", animated, 26)
    s += step(886, y2, 200, BH, "Generate", "Generate", animated)
    s += t(550, y1 + BH + 28, "vector DB, web, files", 24, MUTED)
    s += path_arrow([(142, cy1), (198, cy1)])
    s += path_arrow([(382, cy1), (448, cy1)]) + path_arrow([(652, cy1), (718, cy1)])
    # not enough -> rewrite -> plan
    s += path_arrow([(810, y1 + BH + 2), (810, cy2), (677, cy2)])
    s += t(818, y1 + BH + 52, "not enough", 24, LABEL, False, "start")
    s += path_arrow([(423, cy2), (290, cy2), (290, y1 + BH + 2)])
    # enough -> generate
    s += path_arrow([(902, cy1), (986, cy1), (986, y2 - 2)])
    s += t(994, cy1 + 60, "enough", 24, LABEL, False, "start")
    return s + "</svg>"

for name, animated in [("fig-agentic-rag.svg", True), ("fig-agentic-rag-static.svg", False)]:
    (OUT / name).write_text(figure(animated), encoding="utf-8")
    print("wrote", OUT / name)
