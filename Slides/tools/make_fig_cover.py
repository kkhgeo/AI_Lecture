# -*- coding: utf-8 -*-
"""Cover motion (own figure): the Claude Code mascot (user's pixel sprite) beside a document whose lines fill in
one by one; when the page is done a check appears and the mascot turns around once. 6 s loop (SMIL).
Writes fig-cover.svg (animated) and fig-cover-static.svg (finished page, for the PNG/PPTX twin)."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
COPPER = "#E4B592"; GREY = "#7E7E7E"; LINE = "#d6d0ca"; ORANGE = "#D97757"
W, H, DUR = 640, 480, 6.0

def figure(animated):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
    # document
    s += f'<rect x="300" y="50" width="300" height="390" rx="10" fill="none" stroke="{LINE}" stroke-width="3"/>'
    lines = [(330, 96, 170, COPPER, 14)] + [(330, 140 + 34 * k, w, GREY, 10)
                                           for k, w in enumerate([240, 220, 236, 200, 240, 228, 150])]
    n = len(lines)
    for k, (x, y, w, col, h) in enumerate(lines):
        t0 = 0.3 + k * 0.5  # line k appears at t0 and stays until the loop ends
        a = (f'<animate attributeName="width" values="0;0;{w};{w}" keyTimes="0;{t0 / DUR:.3f};{(t0 + 0.4) / DUR:.3f};1" '
             f'dur="{DUR}s" repeatCount="indefinite"/>') if animated else ""
        s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" fill="{col}">{a}</rect>'
    # check mark when the page is done
    tc = 0.3 + n * 0.5 + 0.2
    a = (f'<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{tc / DUR:.3f};{(tc + 0.2) / DUR:.3f};1" '
         f'dur="{DUR}s" repeatCount="indefinite"/>') if animated else ""
    s += (f'<g opacity="{0 if animated else 1}">{a}<circle cx="560" cy="400" r="34" fill="{COPPER}"/>'
          f'<path d="M543 400 L555 412 L578 388" fill="none" stroke="#000" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>')
    # mascot: walks in place, turns around once right after the check
    U, MX, FEET = 12, 150, 420
    body = [(2, 0, 13, 2), (2, 2, 2, 2), (5, 2, 7, 2), (13, 2, 2, 2), (0, 4, 17, 2), (2, 6, 13, 2)]
    cells = lambda rects: "".join(f'<rect x="{c * U - 8.5 * U}" y="{r * U - 10 * U}" width="{w * U}" height="{h * U}"/>'
                                  for c, r, w, h in rects)
    legs = lambda cols, v: ("<g>" + cells([(c, 8, 1, 2) for c in cols])
                            + (f'<animate attributeName="opacity" values="{v}" dur="0.5s" repeatCount="indefinite" calcMode="discrete"/>'
                               if animated else "") + "</g>")
    bob = (f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -8;0 0" dur="0.5s" '
           f'repeatCount="indefinite"/>') if animated else ""
    k0 = (tc + 0.2) / DUR
    spin = (f'<animateTransform attributeName="transform" type="scale" dur="{DUR}s" repeatCount="indefinite" '
            f'values="1 1;1 1;0.05 1;-1 1;0.05 1;1 1;1 1" '
            f'keyTimes="0;{k0:.3f};{k0 + .03:.3f};{k0 + .06:.3f};{k0 + .09:.3f};{k0 + .12:.3f};1"/>') if animated else ""
    s += (f'<g transform="translate({MX} {FEET})"><g>{bob}<g fill="{ORANGE}" shape-rendering="crispEdges">{spin}'
          + cells(body) + legs([2, 12], "1;0") + legs([4, 14], "0;1") + "</g></g></g>")
    return s + "</svg>"

for name, animated in [("fig-cover.svg", True), ("fig-cover-static.svg", False)]:
    (OUT / name).write_text(figure(animated), encoding="utf-8")
    print("wrote", OUT / name)
