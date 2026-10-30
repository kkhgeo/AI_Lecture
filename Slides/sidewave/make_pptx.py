# -*- coding: utf-8 -*-
"""Context lecture — PPTX builder (copied from Sidewave_Style/make_pptx.py; output name + speaker notes changed).

Pipeline:  node bake.mjs  →  python make_pptx.py
  bake.mjs writes assets/pptx_bg_slide*.png (Unity world plate + scrims only — no
  text, buttons, rails or tick marks) and pptx_layout.json (rects of every text, UI shape,
  icon, image, logo, table). This script rebuilds everything above the plate as
  separate PowerPoint objects at the HTML's rendered coordinates:
    [data-ui]   → native shapes (rails, tabs, dots, chips, field, buttons, frames; rotation kept)
    [data-icon] → assets/ui/icon-*.png pictures
    [data-tx]   → editable text boxes
  1 HTML px = 6350 EMU = 0.5 pt (960pt-wide slide).

문법(Sidewave): 색은 배경 세계(Unity 플레이트)가, 글자는 흰 UI가 맡는다.
  cyan #7DF9FF = 보내기/진행, violet #BC13FE = 단 하나의 '회사' 액션.
Fonts(무료 대체): Anton(표시) + JetBrains Mono(라벨), 한글은 전부 Paperlogy.
목차의 비활성 장은 외곽선 글자(채우기 없음 + 1.5px 흰 윤곽선).
강조 구절은 흰 바탕 반전(com_pass가 줄 단위 흰 사각형을 글자 뒤에 깔고, 글자는 검정).
KEI 로고는 assets/kei_logo.png 투명 PNG를 별도 그림 개체로 삽입.
"""
import json
import re
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn

BASE = Path(__file__).parent
ASSETS = BASE / "assets"
PX = 6350
PT_PER_PX = 0.5
LAYOUT = json.loads((BASE / "pptx_layout.json").read_text(encoding="utf-8"))

WHITE_BGR = 0xFFFFFF

ALIGN = {"left": PP_ALIGN.LEFT, "right": PP_ALIGN.RIGHT, "center": PP_ALIGN.CENTER}


def font_names(family, weight):
    """(latin, east-asian) typefaces for a computed family/weight."""
    ea = ("Paperlogy 8 ExtraBold" if weight >= 700 else "Paperlogy 6 SemiBold" if weight >= 600
          else "Paperlogy 5 Medium" if weight >= 500 else "Paperlogy 4 Regular")
    if family.startswith("Anton"):
        latin = "Anton"
    elif family.startswith("JetBrains Mono"):
        latin = "JetBrains Mono Medium" if weight >= 500 else "JetBrains Mono"
    else:  # Paperlogy carries Latin too in Korean body copy
        latin = ea
    return latin, ea


def hex_on_black(css):
    """CSS rgb()/rgba() → hex, alpha pre-blended over the void (#000)."""
    v = [float(x) for x in re.findall(r"[\d.]+", css)]
    a = v[3] if len(v) > 3 else 1.0
    return "%02X%02X%02X" % tuple(round(c * a) for c in v[:3])


def set_run(run, r):
    latin, ea = font_names(r["family"], r["weight"])
    run.text = r["text"]
    run.font.size = Pt(r["size"] * PT_PER_PX)
    run.font.bold = False
    run.font.color.rgb = RGBColor.from_string(hex_on_black(r["color"]))
    run.font.name = latin
    rPr = run._r.get_or_add_rPr()
    if r["ls"]:
        rPr.set("spc", str(int(round(r["ls"] * PT_PER_PX * 100))))
    for tag in ("a:ea", "a:cs"):
        el = rPr.makeelement(qn(tag), {})
        el.set("typeface", ea)
        rPr.append(el)
    if r.get("strokeW"):  # outlined display word: no fill + stroke (ln must precede the fill in rPr)
        for f in rPr.findall(qn("a:solidFill")):
            rPr.remove(f)
        hx, a = rgba(r["strokeColor"])
        ln = rPr.makeelement(qn("a:ln"), {"w": str(int(r["strokeW"] * PT_PER_PX * 12700))})
        sf = ln.makeelement(qn("a:solidFill"), {})
        clr = sf.makeelement(qn("a:srgbClr"), {"val": hx})
        sf.append(clr)
        ln.append(sf)
        rPr.insert(0, ln)
        rPr.insert(1, rPr.makeelement(qn("a:noFill"), {}))


def split_lines(runs):
    paras, cur = [], []
    for r in runs:
        if r["text"] == "\v":
            paras.append(cur)
            cur = []
        else:
            cur.append(r)
    paras.append(cur)
    return paras


# CSS puts an Anton-strut baseline 0.4235em below the line centre ((ascent-descent)/2 of Anton);
# PowerPoint with exact spacing puts it ~0.28em below. Measured on the rendered previews (Δ ≈ 0.145 × size).
BASELINE_SHIFT = {"Anton": 0.145}


def add_text(slide, t):
    x, y, w, h = t["rect"]["x"], t["rect"]["y"], t["rect"]["w"], t["rect"]["h"]
    lead = t["runs"][0] if t["runs"] else None
    if lead and not lead.get("strokeW"):
        y += BASELINE_SHIFT.get(lead["family"], 0) * lead["size"]
    single = t["lines"] == 1 and not any(r["text"] == "\v" for r in t["runs"])
    if single and not t.get("rot"):  # no wrap: give room for metric drift, keep the aligned edge fixed
        pad = 60
        x = x - pad if t["align"] == "right" else x - pad / 2 if t["align"] == "center" else x
        w = w + pad
    else:
        w = w + (40 if any(r["text"] == "" for r in t["runs"]) else 6)  # explicit breaks: room for metric drift
    box = slide.shapes.add_textbox(Emu(round(x * PX)), Emu(round(y * PX)), Emu(round(w * PX)), Emu(round(h * PX)))
    if t.get("rot"):
        box.rotation = t["rot"] % 360
    tf = box.text_frame
    tf.word_wrap = not single
    tf.vertical_anchor = MSO_ANCHOR.TOP
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, 0)
    for i, para_runs in enumerate(split_lines(t["runs"])):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = ALIGN[t["align"]]
        p.line_spacing = Pt(t["lh"] * PT_PER_PX)
        p._p.get_or_add_pPr().set("eaLnBrk", "0")  # Korean wraps by word (HTML word-break: keep-all)
        for r in para_runs:
            set_run(p.add_run(), r)


def rgba(css):
    v = [float(x) for x in re.findall(r"[\d.]+", css)]
    return "%02X%02X%02X" % tuple(round(c) for c in v[:3]), (v[3] if len(v) > 3 else 1.0)


def _alpha(parent, a):
    """Attach <a:alpha> to the srgbClr under a solidFill (fill or line)."""
    if a >= 1:
        return
    clr = parent.find(qn("a:solidFill")).find(qn("a:srgbClr"))
    el = clr.makeelement(qn("a:alpha"), {"val": str(int(round(a * 100000)))})
    clr.append(el)


def box(slide, x, y, w, h, fill_css=None, radius=0, line=None, rot=0):
    """Rectangle/rounded rectangle in px. line = (width_px, css) drawn inside the box like a CSS border."""
    if line:
        lw = line[0]
        x, y, w, h = x + lw / 2, y + lw / 2, w - lw, h - lw
    oval = radius and radius >= min(w, h) / 2 and abs(w - h) < 1
    kind = MSO_SHAPE.OVAL if oval else MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shp = slide.shapes.add_shape(kind, Emu(round(x * PX)), Emu(round(y * PX)), Emu(round(w * PX)), Emu(round(h * PX)))
    if radius and not oval:
        shp.adjustments[0] = min(0.5, radius / min(w, h))
    if rot:
        shp.rotation = rot % 360
    shp.shadow.inherit = False
    if fill_css:
        hx, a = rgba(fill_css)
        shp.fill.solid()
        shp.fill.fore_color.rgb = RGBColor.from_string(hx)
        _alpha(shp.fill._xPr, a)
    else:
        shp.fill.background()
    if line:
        hx, a = rgba(line[1])
        shp.line.width = Pt(line[0] * PT_PER_PX)
        shp.line.color.rgb = RGBColor.from_string(hx)
        _alpha(shp.line._get_or_add_ln(), a)
    else:
        shp.line.fill.background()
    shp.text_frame.text = ""
    return shp


def add_ui(slide, u):
    r, b = u["rect"], u["border"]
    has_fill = rgba(u["bg"])[1] > 0
    sides = {k: v for k, v in b.items() if v["w"] > 0}
    uniform = len(sides) == 4 and len({(v["w"], v["color"]) for v in sides.values()}) == 1
    if has_fill or uniform:
        box(slide, r["x"], r["y"], r["w"], r["h"], u["bg"] if has_fill else None, u["radius"],
            (b["top"]["w"], b["top"]["color"]) if uniform else None, u.get("rot", 0))
    if not uniform:  # single-side borders → hairline bars
        for k, v in sides.items():
            x, y, w, h = r["x"], r["y"], r["w"], r["h"]
            if k == "top":
                h = v["w"]
            elif k == "bottom":
                y, h = y + h - v["w"], v["w"]
            elif k == "left":
                w = v["w"]
            else:
                x, w = x + w - v["w"], v["w"]
            box(slide, x, y, w, h, v["color"])


def contain(slide, img_path, rect):
    iw, ih = Image.open(img_path).size
    fx, fy, fw, fh = rect["x"], rect["y"], rect["w"], rect["h"]
    s = min(fw / iw, fh / ih)
    dw, dh = iw * s, ih * s
    slide.shapes.add_picture(str(img_path), Emu(round((fx + (fw - dw) / 2) * PX)), Emu(round((fy + (fh - dh) / 2) * PX)),
                             Emu(round(dw * PX)), Emu(round(dh * PX)))


def _edge(cell, edge, width_px, color_hex=None):
    tcPr = cell._tc.get_or_add_tcPr()
    order = ["a:lnL", "a:lnR", "a:lnT", "a:lnB"]
    ln = tcPr.makeelement(qn(edge), {"w": str(int(width_px * PT_PER_PX * 12700)) if color_hex else "0", "cap": "flat"})
    if color_hex:
        fill = tcPr.makeelement(qn("a:solidFill"), {})
        fill.append(tcPr.makeelement(qn("a:srgbClr"), {"val": color_hex}))
        ln.append(fill)
    else:
        ln.append(tcPr.makeelement(qn("a:noFill"), {}))
    pos = sum(1 for tag in order[:order.index(edge)] if tcPr.find(qn(tag)) is not None)
    tcPr.insert(pos, ln)


def add_table(slide, T):
    rows, cols = len(T["cells"]), len(T["colW"])
    r0 = T["rect"]
    gf = slide.shapes.add_table(rows, cols, Emu(round(r0["x"] * PX)), Emu(round(r0["y"] * PX)),
                                Emu(round(r0["w"] * PX)), Emu(round(r0["h"] * PX)))
    tbl = gf.table
    tbl.first_row = False
    tbl.horz_banding = False
    for c, w in enumerate(T["colW"]):
        tbl.columns[c].width = Emu(round(w * PX))
    for r, h in enumerate(T["rowH"]):
        tbl.rows[r].height = Emu(round(h * PX))
    top, row = hex_on_black(T["border"]["top"]), hex_on_black(T["border"]["row"])
    for r in range(rows):
        for c in range(cols):
            cell, spec = tbl.cell(r, c), T["cells"][r][c]
            cell.fill.background()
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.margin_left = Emu(round(spec["padL"] * PX))
            cell.margin_right = Emu(round(spec["padR"] * PX))
            cell.margin_top = cell.margin_bottom = Emu(4 * PX)
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT
            for run in spec["runs"]:
                set_run(p.add_run(), run)
            _edge(cell, "a:lnL", 0)
            _edge(cell, "a:lnR", 0)
            if r == 0:
                _edge(cell, "a:lnT", 1, top)
            _edge(cell, "a:lnB", 1, row)


prs = Presentation()
prs.slide_width = Emu(1920 * PX)
prs.slide_height = Emu(1080 * PX)
blank = prs.slide_layouts[6]
PEN_SPECS = []

for n, L in enumerate(LAYOUT, start=1):
    s = prs.slides.add_slide(blank)
    s.shapes.add_picture(str(ASSETS / f"pptx_bg_slide{n}.png"), 0, 0, Emu(1920 * PX), Emu(1080 * PX))
    for u in L["ui"]:
        add_ui(s, u)
    for ic in L["icons"]:
        r = ic["rect"]
        s.shapes.add_picture(str(ASSETS / "ui" / f"icon-{ic['name']}.png"), Emu(round(r["x"] * PX)), Emu(round(r["y"] * PX)),
                             Emu(round(r["w"] * PX)), Emu(round(r["h"] * PX)))
    for lg in L["logos"]:
        r = lg["rect"]
        s.shapes.add_picture(str(ASSETS / "kei_logo.png"), Emu(round(r["x"] * PX)), Emu(round(r["y"] * PX)),
                             Emu(round(r["w"] * PX)), Emu(round(r["h"] * PX)))
    for im in L["imgs"]:
        src = im["src"]
        if src.endswith(".svg"):  # PowerPoint gets the raster twin
            src = src[:-4] + ".png"
        contain(s, BASE / src, im["rect"])
    for T in L["tables"]:
        add_table(s, T)
    for t in L["texts"]:
        add_text(s, t)
        PEN_SPECS += [(n, r["text"]) for r in t["runs"] if r.get("mark")]
    if L.get("notes"):
        s.notes_slide.notes_text_frame.text = L["notes"]

out = BASE / "lecture_context.pptx"
prs.save(out)
print("saved", out)


def com_pass(path, specs, preview_dir):
    """PowerPoint COM: white inverse block behind each flagged phrase (per rendered line) + PNG previews."""
    try:
        import win32com.client
    except ImportError:
        print("pywin32 not available - skipped pen-mark pass")
        return
    pp = win32com.client.Dispatch("PowerPoint.Application")
    pres = pp.Presentations.Open(str(path), WithWindow=False)
    try:
        for slide_no, phrase in specs:
            sl = pres.Slides(slide_no)
            for sh in list(sl.Shapes):
                if not (sh.HasTextFrame and sh.TextFrame.HasText):
                    continue
                found = sh.TextFrame.TextRange.Find(phrase)
                if found is None:
                    continue
                n = found.Lines().Count
                pieces = [found.Lines(j) for j in range(1, n + 1)] if n > 1 else [found]
                for piece in pieces:
                    rect = sl.Shapes.AddShape(1, piece.BoundLeft - 2, piece.BoundTop + 1,
                                              piece.BoundWidth + 4, piece.BoundHeight - 2)
                    rect.Fill.Solid()
                    rect.Fill.ForeColor.RGB = WHITE_BGR
                    rect.Line.Visible = 0
                    rect.ZOrder(1)  # msoSendToBack …
                    rect.ZOrder(2)  # … then msoBringForward: directly above the baked world, below all text
                break
        pres.Save()
        preview_dir.mkdir(exist_ok=True)
        for i in range(1, pres.Slides.Count + 1):
            pres.Slides(i).Export(str(preview_dir / f"pptx-slide-{i}.png"), "PNG", 1920, 1080)
    finally:
        pres.Close()
        pp.Quit()


com_pass(out, PEN_SPECS, BASE / "previews")
