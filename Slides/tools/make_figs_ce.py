# -*- coding: utf-8 -*-
"""Redraw of two source figures in one gothic face (Paperlogy), brighter lines, simple icons.
Structure, labels and colour roles follow the originals:
  fig-prompt-vs-context.svg   <- Anthropic (2025) "Prompt engineering vs. context engineering"
  fig-context-management.svg  <- Lance Martin (2025) "Context Engineering Overview"
"""
from pathlib import Path
import pathlib
OUT = Path(__file__).resolve().parent.parent / "assets"
F = "PLG,sans-serif"
FONTS = pathlib.Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
LINE = "#d6d0ca"; LABEL = "#e2dcd6"; CREAM = "#fff3ea"
C = {
 "blue": ("#0f2340", "#5b95ff", "#a9c6ff"), "green": ("#0c2a21", "#3fc59a", "#8fe6c6"),
 "orange": ("#2e1408", "#ff7a3d", "#ffab80"), "purple": ("#1b1540", "#8f83ff", "#c2baff"),
 "grey": ("#121212", "#bdb6b0", "#ece6e0"), "brown": ("#2a1e10", "#c9a36a", "#ecd3a8"),
}
def head(w, h):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10" fill="none" stroke="{LINE}" stroke-width="1.6"/></marker></defs>'
            f'<style>{FONTS}</style>')
def t(x, y, s, size=17, fill=LABEL, anchor="start", bold=False):
    return f'<text x="{x}" y="{y}" font-family="{F}" font-weight="{700 if bold else 500}" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{s}</text>'
def chip(x, y, w, s, col, h=32, lines=None):
    f, st, tx = C[col]
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{f}" stroke="{st}" stroke-width="1.6"/>'
    ls = lines or [s]
    for i, l in enumerate(ls):
        cy = y + h / 2 + 6 + (i - (len(ls) - 1) / 2) * 20
        out += t(x + w / 2, cy, l, 16, tx, "middle")
    return out
def line(pts, arrow=False, color=LINE, w=1.6):
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}"' + (' marker-end="url(#a)"' if arrow else "") + "/>"
def dbox(x, y, w, h):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="none" stroke="{LINE}" stroke-width="1.4" stroke-dasharray="6 5"/>'
def model(cx, cy):
    return "".join(f'<circle cx="{cx + i * 13}" cy="{cy + j * 13}" r="5" fill="none" stroke="{LINE}" stroke-width="1.5"/>' for i in (-1, 0, 1) for j in (-1, 0, 1))

# ---- figure 3 (1100 x 620)
s = head(1100, 620)
s += t(550, 40, "Prompt engineering vs. context engineering", 26, CREAM, "middle", True)
s += t(24, 92, "Prompt engineering", 18, CREAM, bold=True) + t(24, 116, "for single turn queries", 16)
s += t(30, 156, "Context window", 16) + dbox(30, 168, 160, 360)
s += chip(40, 182, 140, "System prompt", "blue") + chip(40, 224, 140, "User message", "blue")
s += line([(190, 330), (206, 330)], True) + model(226, 330) + line([(246, 330), (262, 330)], True)
s += chip(266, 306, 92, "", "grey", 48, ["Assistant", "message"])
s += t(386, 92, "Context engineering for agents", 18, CREAM, bold=True)
s += t(386, 156, "Possible context to give model", 16) + dbox(386, 168, 222, 360)
for i in range(3): s += chip(396 + i * 68, 182, 60, "Doc", "green")
for i in range(3): s += chip(396 + i * 68, 222, 60, "Tool", "orange")
s += chip(396, 262, 60, "Tool", "orange") + chip(464, 262, 128, "Memory file", "purple")
s += chip(396, 302, 196, "", "blue", 50, ["Comprehensive", "instructions"])
s += chip(396, 362, 170, "Domain knowledge", "blue")
s += chip(396, 402, 128, "Memory file", "purple") + chip(532, 402, 60, "Doc", "green")
s += chip(396, 442, 60, "Tool", "orange")
s += chip(396, 486, 150, "Message history", "grey")
s += t(648, 318, "Curation", 16, CREAM, "middle") + line([(612, 332), (686, 332)], True)
s += t(694, 156, "Context window", 16) + dbox(694, 168, 168, 360)
for y, w, lab, col in [(182, 148, "System prompt", "blue"), (262, 124, "Memory file", "purple"), (342, 136, "User message", "blue"), (382, 148, "Message history", "grey")]:
    s += chip(704, y, w, lab, col) + line([(704 + w, y + 16), (872, y + 16)])
s += chip(704, 222, 68, "Doc 1", "green") + chip(780, 222, 68, "Doc 2", "green") + line([(848, 238), (872, 238)])
s += chip(704, 302, 68, "Tool 1", "orange") + chip(780, 302, 68, "Tool 2", "orange") + line([(848, 318), (872, 318)])
s += line([(872, 198), (872, 398)]) + line([(872, 330), (892, 330)], True) + model(912, 330)
s += line([(932, 330), (944, 330), (944, 280), (958, 280)], True) + line([(944, 330), (944, 372), (958, 372)], True)
s += chip(962, 256, 118, "", "grey", 48, ["Assistant", "message"])
s += chip(962, 356, 100, "Tool call", "brown")
s += line([(1012, 388), (1012, 568), (964, 568)])
s += chip(852, 552, 110, "Tool result", "brown")
s += line([(852, 568), (650, 568), (650, 502), (550, 502)], True)
s += "</svg>"
(OUT / "fig-prompt-vs-context.svg").write_text(s, encoding="utf-8")

# ---- figure 4 (1300 x 470)
P = {"Write": ("#ff6b62", "#2a0d0c"), "Select": ("#5ea8ff", "#0d1d33"), "Compress": ("#4fd18b", "#0b2819"), "Isolate": ("#ffab45", "#2d1c07")}
def sq(x, y, n, col, fill):
    return f'<rect x="{x}" y="{y}" width="{n}" height="{n}" rx="4" fill="{fill}" stroke="{col}" stroke-width="1.8"/>'
def arrow(x1, y, x2, col):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{col}" stroke-width="1.8"/>'
            f'<path d="M{x2-7},{y-5} L{x2},{y} L{x2-7},{y+5}" fill="none" stroke="{col}" stroke-width="1.8"/>')
def ico(kind, x, y, col):
    st = f'fill="none" stroke="{col}" stroke-width="1.8"'
    if kind == "memory":
        return (f'<ellipse cx="{x+17}" cy="{y+6}" rx="15" ry="5" {st}/><path d="M{x+2},{y+6} V{y+28} A15,5 0 0 0 {x+32},{y+28} V{y+6}" {st}/>'
                f'<path d="M{x+2},{y+17} A15,5 0 0 0 {x+32},{y+17}" {st}/>')
    if kind == "note":
        return f'<path d="M{x+5},{y+1} H{x+23} L{x+30},{y+8} V{y+33} H{x+5} Z" {st}/>' + "".join(f'<line x1="{x+10}" y1="{y+13+k*6}" x2="{x+25}" y2="{y+13+k*6}" stroke="{col}" stroke-width="1.4"/>' for k in range(3))
    if kind == "folder":
        return f'<path d="M{x+1},{y+6} H{x+13} L{x+17},{y+10} H{x+33} V{y+31} H{x+1} Z" {st}/>'
    if kind == "cabinet":
        return (f'<rect x="{x+4}" y="{y+1}" width="26" height="32" rx="2" {st}/><line x1="{x+4}" y1="{y+17}" x2="{x+30}" y2="{y+17}" stroke="{col}" stroke-width="1.6"/>'
                f'<line x1="{x+13}" y1="{y+9}" x2="{x+21}" y2="{y+9}" stroke="{col}" stroke-width="1.6"/><line x1="{x+13}" y1="{y+25}" x2="{x+21}" y2="{y+25}" stroke="{col}" stroke-width="1.6"/>')
    if kind == "tool":
        return f'<circle cx="{x+10}" cy="{y+10}" r="7" {st}/><line x1="{x+15}" y1="{y+15}" x2="{x+31}" y2="{y+31}" stroke="{col}" stroke-width="3"/>'
    if kind == "llm":
        return f'<circle cx="{x+17}" cy="{y+17}" r="16" {st}/>' + t(x + 17, y + 22, "LLM", 12, col, "middle")
    if kind == "trim":
        return (f'<circle cx="{x+8}" cy="{y+27}" r="5" {st}/><circle cx="{x+26}" cy="{y+27}" r="5" {st}/>'
                f'<line x1="{x+11}" y1="{y+23}" x2="{x+27}" y2="{y+2}" stroke="{col}" stroke-width="1.8"/><line x1="{x+23}" y1="{y+23}" x2="{x+7}" y2="{y+2}" stroke="{col}" stroke-width="1.8"/>')
    if kind == "sandbox":
        return f'<rect x="{x+6}" y="{y+1}" width="22" height="6" rx="2" {st}/><rect x="{x+3}" y="{y+8}" width="28" height="25" rx="6" {st}/>'
s = head(1300, 470)
PW, GAP, FS = 305, 26, 19
for k, name in enumerate(P):
    col, fill = P[name]; x0 = k * (PW + GAP); cx = x0 + PW / 2
    s += t(cx, 26, f"{name} Context", 22, col, "middle", True)
    s += f'<rect x="{x0+1}" y="40" width="{PW-2}" height="392" rx="10" fill="none" stroke="{col}" stroke-width="2"/>'
    def row(y, lines, src, dst):
        out = "".join(t(cx, y + i * 23, l, FS, col, "middle") for i, l in enumerate(lines))
        iy = y + len(lines) * 23 - 6
        draw = lambda kind, x: sq(x + 3, iy + 3, 28, col, fill) if kind == "ctx" else ico(kind, x, iy, col)
        return out + draw(src, cx - 80) + arrow(cx - 34, iy + 17, cx + 30, col) + draw(dst, cx + 46)
    if name == "Write":
        s += row(86, ["Long-term memories", "(across agent sessions)"], "ctx", "memory")
        s += row(210, ["Scratchpad", "(within agent session)"], "ctx", "note")
        s += row(334, ["State", "(within agent session)"], "ctx", "folder")
    if name == "Select":
        s += row(74, ["Retrieve relevant tools"], "cabinet", "tool")
        s += row(168, ["Retrieve from scratchpad"], "note", "ctx")
        s += row(262, ["Retrieve long-term memory"], "memory", "ctx")
        s += row(356, ["Retrieve relevant knowledge"], "cabinet", "ctx")
    if name == "Compress":
        for y, lines, mid in [(110, ["Summarize context", "to retain relevant tokens"], "llm"), (272, ["Trim context to", "remove irrelevant tokens"], "trim")]:
            s += "".join(t(cx, y + i * 23, l, FS, col, "middle") for i, l in enumerate(lines))
            iy = y + 40
            s += sq(cx - 112, iy, 40, col, fill) + arrow(cx - 64, iy + 20, cx - 24, col) + ico(mid, cx - 17, iy + 3, col)
            s += arrow(cx + 24, iy + 20, cx + 64, col) + sq(cx + 76, iy + 12, 16, col, fill)
    if name == "Isolate":
        s += row(84, ["Partition context in state"], "ctx", "folder")
        s += row(190, ["Hold in environment/sandbox"], "ctx", "sandbox")
        s += t(cx, 300, "Partition across multi-agent", FS, col, "middle")
        s += sq(cx - 16, 318, 32, col, fill)
        s += f'<line x1="{cx-22}" y1="356" x2="{cx-70}" y2="386" stroke="{col}" stroke-width="1.8"/><line x1="{cx+22}" y1="356" x2="{cx+70}" y2="386" stroke="{col}" stroke-width="1.8"/>'
        s += ico("llm", cx - 104, 380, col) + ico("llm", cx + 70, 380, col)
s += sq(20, 444, 22, LINE, "#1a1a1a") + t(52, 462, "= LLM Context", 18, LABEL)
s += "</svg>"
(OUT / "fig-context-management.svg").write_text(s, encoding="utf-8")
print("ok")
