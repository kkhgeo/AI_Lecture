# -*- coding: utf-8 -*-
"""Redraw of Graphologue (Jiang et al., UIST 2023) teaser figure, same format:
GPT-4 response strip on top, the original text panel (original / outline / summary | highlight / hide)
on the left, and the node-link diagram built from it on the right (AI systems -> divided into -> narrow AI /
general AI -> ...), with the selected node 'narrow AI' highlighted. Dark, Paperlogy. Annotation tags and
the hand cursor are omitted."""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "assets"
FONTS = Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
F = "PLG,sans-serif"
CREAM = "#fff3ea"; LABEL = "#e2dcd6"; MUTED = "#9a948e"; LINE = "#8a847e"; HL = "#ffb347"
W, H = 1100, 500

def t(x, y, s, size, fill=LABEL, bold=False, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}" xml:space="preserve">{s}</text>')
def node(x, y, w, label, hl=False):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="9" fill="#24211e" stroke="{"#ff7a3d" if hl else "#5a5550"}" '
            f'stroke-width="{3 if hl else 1.6}"/>' + t(x + w / 2, y + 30, label, 20, CREAM, anchor="middle"))
def edge(pts, arrow=True):
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    return f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="2.2"' + (' marker-end="url(#a)"' if arrow else "") + "/>"

s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
     '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
     f'<path d="M0,0 L10,5 L0,10" fill="none" stroke="{LINE}" stroke-width="1.8"/></marker>'
     '<linearGradient id="fade" x1="0" x2="1"><stop offset="0.75" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="1"/></linearGradient></defs>')
# response strip
s += f'<rect x="0" y="4" width="168" height="38" rx="19" fill="#4a4540"/>' + t(84, 30, "GPT-4 Response", 19, LABEL, anchor="middle")
spans = [("AI systems", False), ("can be divided into", None), ("narrow AI", True), ("and", None), ("general AI", False),
         ("Narrow AI", True), ("is designed for …", None)]
x = 186
for txt, hl in spans:
    w = len(txt) * 11.2
    if hl is not None:
        s += f'<rect x="{x - 4}" y="8" width="{w + 8}" height="32" rx="4" fill="{HL if hl else "#6a645e"}" fill-opacity="{0.28 if hl else 0.35}"/>'
    s += t(x, 31, txt, 20, CREAM if hl is not None else LABEL)
    x += w + 16
s += f'<rect x="760" y="0" width="340" height="48" fill="url(#fade)"/>'
# text panel
s += f'<rect x="0" y="80" width="390" height="268" rx="10" fill="#1a1816" stroke="#3a3632" stroke-width="1.5"/>'
s += (f'<rect x="16" y="94" width="76" height="26" rx="6" fill="none" stroke="{MUTED}" stroke-width="1.4"/>'
      + t(54, 113, "original", 16, LABEL, anchor="middle") + t(106, 113, "outline · summary | highlight · hide", 15, MUTED))
para = ["AI systems can be divided into narrow", "AI and general AI. Narrow AI is", "designed for specific tasks, such as",
        "image recognition, and often excels", "in its designated task. General AI", "aims to mimic human intelligence."]
for i, l in enumerate(para):
    y = 156 + i * 31
    s += t(16, y, l, 18, LABEL)
    if i < 5:
        s += f'<line x1="16" y1="{y + 7}" x2="{16 + len(l) * 9.4}" y2="{y + 7}" stroke="{HL}" stroke-width="1.6" opacity="0.6"/>'
# diagram
s += node(240, 376, 160, "AI systems")
s += edge([(400, 399), (420, 399)], False) + t(428, 405, "divided into", 18, MUTED) + edge([(538, 399), (552, 399)], False)
s += edge([(552, 399), (552, 233), (576, 233)]) + edge([(552, 399), (552, 433), (576, 433)])
s += node(580, 210, 160, "narrow AI", True)
s += node(580, 410, 160, "general AI")
right = [(100, "specific tasks", "is designed for"), (210, "image recognition", "such as"), (320, "designated task", "often excels in")]
for y, lab, rel in right:
    s += node(895, y, 205, lab)
    s += edge([(740, 233), (760, 233), (760, y + 23), (891, y + 23)])
    s += t(768, y + 14, rel, 16, MUTED)
s += node(895, 410, 205, "mimic human")
s += edge([(740, 433), (891, 433)]) + t(768, 424, "aims to", 16, MUTED)
s += "</svg>"
(OUT / "fig-graphologue.svg").write_text(s, encoding="utf-8")
print("ok")
