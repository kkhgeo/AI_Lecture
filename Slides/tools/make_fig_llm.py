# -*- coding: utf-8 -*-
"""How an LLM writes (own figure; illustrative numbers): the input tokens go into the LLM (labels Input / Output), which scores the
candidates for the next token; the top one is appended and the loop repeats (autoregressive generation).
Korean example sentence (allowed exception to the English-in-figures rule, 2026-10-23); Paperlogy Korean subset
embedded. 3 steps x 2 s = 6 s loop (SMIL). Writes fig-llm.svg and fig-llm-static.svg (step-1 state, PNG twin)."""
import base64, io
from pathlib import Path
from fontTools import subset
from fontTools.ttLib import TTFont
OUT = Path(__file__).resolve().parent.parent / "assets"
CTX = ["논문의", "결론은", "연구", "질문에"]
STEPS = [  # (candidates with illustrative probabilities, chosen = first)
    [("답해야", .48), ("맞춰야", .21), ("따라야", .12), ("기초해야", .07)],
    [("한다", .83), ("합니다", .09), ("하며", .04)],
    [(".", .91), (",", .05)],
]
KO = "".join(CTX) + "".join(c for st in STEPS for c, _ in st)

def ko_font(weight_file, family):
    f = TTFont(rf"C:\Users\KEI\AppData\Local\Microsoft\Windows\Fonts\{weight_file}")
    opts = subset.Options(); opts.flavor = "woff2"
    sb = subset.Subsetter(opts); sb.populate(text=KO + "0123456789."); sb.subset(f)
    buf = io.BytesIO(); f.flavor = "woff2"; f.save(buf)
    return (f"@font-face{{font-family:'{family}';src:url(data:font/woff2;base64,"
            + base64.b64encode(buf.getvalue()).decode() + ") format('woff2');}")
FONTS = (Path(__file__).with_name("plg_fonts.css").read_text(encoding="utf-8")
         + ko_font("Paperlogy-5Medium.ttf", "PLGK5") + ko_font("Paperlogy-7Bold.ttf", "PLGK7"))
COPPER = "#E4B592"; GREY = "#7E7E7E"; LINE = "#d6d0ca"; LABEL = "#e2dcd6"; MUTED = "#8C8681"
W, H, DUR = 1100, 520, 6.0

def t(x, y, s, size, fill, bold=False, anchor="start", extra=""):
    fam = "PLG,PLGK7" if bold else "PLG,PLGK5"
    return (f'<text x="{x}" y="{y}" font-family="{fam},sans-serif" font-weight="{700 if bold else 500}" '
            f'font-size="{size}" fill="{fill}" text-anchor="{anchor}">{s}{extra}</text>')
def arrow(pts, col=LINE, w=3):
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    dx, dy = (x2 > x1) - (x2 < x1), (y2 > y1) - (y2 < y1)
    bx, by = x2 - 14 * dx, y2 - 14 * dy
    px, py = -dy * 8, dx * 8
    return (f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"/>'
            f'<polygon points="{bx + px},{by + py} {x2},{y2} {bx - px},{by - py}" fill="{col}"/>')
def window(k, animated, show_from=None):
    """Opacity animation: visible during step k (or from step `show_from` to the end)."""
    if not animated:
        return ""
    a, b = (k * 2 / DUR, (k + 1) * 2 / DUR) if show_from is None else (show_from, 1.0)
    vals = "0;1;0" if b < 1 else "0;1"
    kt = f"0;{a:.4f};{b:.4f}" if b < 1 else f"0;{a:.4f}"
    if a == 0:
        vals, kt = ("1;0", f"0;{b:.4f}") if b < 1 else ("1", "0")
    return (f'<animate attributeName="opacity" values="{vals}" keyTimes="{kt}" dur="{DUR}s" '
            f'repeatCount="indefinite" calcMode="discrete"/>')

def chip(x, y, word, fill, txt="#000"):
    w = 30 * len(word) + 34 if word not in ".," else 44
    return w, (f'<rect x="{x}" y="{y}" width="{w}" height="58" rx="10" fill="{fill}"/>'
               + t(x + w / 2, y + 40, word, 30, txt, True, "middle"))

def figure(animated):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><style>{FONTS}</style>'
    # row 1: tokens so far (grey = given, copper = generated, appears when chosen)
    s += t(0, 26, "Input", 24, MUTED, True)
    x, y0 = 0, 44
    for wd in CTX:
        w, g = chip(x, y0, wd, GREY); s += g; x += w + 14
    out_lab = t(x, 26, "Output", 24, COPPER, True)
    s += (f'<g opacity="0">{window(0, True, 1.2 / DUR)}{out_lab}</g>' if animated else out_lab)
    for k, st in enumerate(STEPS):
        w, g = chip(x, y0, st[0][0], COPPER)
        appear = (k * 2 + 1.2) / DUR  # chosen token joins the sentence 1.2 s into its step
        if animated:
            s += f'<g opacity="0">{window(0, True, appear).replace("0;1", "0;1")}{g}</g>'
        elif k == 0:
            s += g
        x += w + 14
        if k == 0:
            x_first = x  # end of the sentence in the static (step-1) state
    # LLM box
    s += arrow([(100, y0 + 60), (100, 186)])
    s += f'<rect x="0" y="190" width="200" height="84" rx="10" fill="{COPPER}"/>' + t(100, 245, "LLM", 36, "#000", True, "middle")
    s += arrow([(202, 232), (290, 232), (290, 300)])
    # candidates for the next token
    s += t(310, 300, "next-token probabilities", 24, MUTED)
    for k, st in enumerate(STEPS):
        if not animated and k:
            continue
        g = ""
        for i, (word, p) in enumerate(st):
            yy = 330 + i * 46
            col = COPPER if i == 0 else GREY
            g += (t(290, yy + 28, word, 30, LABEL, i == 0, "end")
                  + f'<rect x="310" y="{yy + 6}" width="{p * 560:.0f}" height="30" rx="4" fill="{col}"/>'
                  + t(310 + p * 560 + 12, yy + 30, f"{p:.2f}", 24, LABEL))
        s += f'<g>{window(k, animated)}{g}</g>'
    # pick the top one and append, then repeat
    s += arrow([(900, 351), (1040, 351), (1040, 74), ((x if animated else x_first) + 8, 74)])
    s += (t(1028, 216, "pick one,", 24, LABEL, False, "end") + t(1028, 246, "add to input", 24, LABEL, False, "end")
          + t(1028, 284, "autoregressive", 24, COPPER, True, "end"))
    return s + "</svg>"

for name, animated in [("fig-llm.svg", True), ("fig-llm-static.svg", False)]:
    (OUT / name).write_text(figure(animated), encoding="utf-8")
    print("wrote", OUT / name)
