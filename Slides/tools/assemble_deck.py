# -*- coding: utf-8 -*-
"""Assemble a lecture deck from slides that live in the source decks, so each slide has one source.
usage: python tools/assemble_deck.py [deck name]   (default: every deck in DECKS)
Slides are picked by their <section aria-label="...">. Head (CSS) and script come from lecture_agents.html.
Re-run after editing a source slide; then: node bake.mjs <deck>.html && python make_pptx.py <deck>.pptx
"""
import re
import sys
from pathlib import Path
BASE = Path(__file__).resolve().parent.parent
SHELL = "lecture_agents.html"
A, C, X = "lecture_agents.html", "lecture_context.html", "slides_extra.html"

# (source file, aria-label[, note to prepend to the speaker notes])
DECKS = {
    "lecture_humanities": {
        "title": "AI 에이전트와 함께 연구하기 (전남대 대학원)",
        "slides": [
            # 도입
            (X, "표지"), (X, "오늘 다룰 것"), (X, "전제(강연판)"),
            # 1. 원리: AI는 어떻게 작동하나
            (X, "용어"), (X, "LLM"),
            (A, "AI 에이전트"), (A, "도메인 특화 에이전트"),
            (X, "컨텍스트(강연판)"), (C, "컨텍스트 창"), (X, "컨텍스트 엔지니어링(강연판)"),
            # 2. 주의: 어디서 틀리고, 어떻게 확인하나
            (A, "행동 특성"), (X, "획일화"), (X, "검증(강연판)"),
            # 3. 활용: 연구에 어떻게 쓰나
            (X, "논문 작성 단계별 활용"), (A, "사람 개입"), (A, "메타인지 부담"), (A, "역방향 학습"), (X, "연구윤리"),
            # 마무리
            (X, "정리"),
        ],
    },
}

SEC = re.compile(r'(?:<!--[^>]*-->\s*)?<section class="slide" aria-label="([^"]+)">.*?</section>', re.S)

def sections(name):
    text = (BASE / name).read_text(encoding="utf-8")
    return {m.group(1): m.group(0) for m in SEC.finditer(text)}

def build(deck):
    spec = DECKS[deck]
    shell = (BASE / SHELL).read_text(encoding="utf-8")
    head = shell[: shell.index("<body>") + len("<body>")]
    head = re.sub(r"<title>.*?</title>", f"<title>{spec['title']}</title>", head, count=1, flags=re.S)
    tail = shell[shell.rindex("</section>") + len("</section>"):]  # notes panel + script
    cache, out = {}, []
    for item in spec["slides"]:
        src, label = item[0], item[1]
        cache.setdefault(src, sections(src))
        if label not in cache[src]:
            sys.exit(f"missing slide: {label} in {src}")
        sec = cache[src][label]
        if len(item) > 2:  # demo marker etc. at the top of the notes
            sec = sec.replace('<aside class="notes"><ul>', f'<aside class="notes"><ul>\n    <li>{item[2]}</li>', 1)
        out.append(f"<!-- from {src} -->\n" + sec)
    html = (head + "\n<!-- Assembled by tools/assemble_deck.py; edit the source decks, not this file. -->\n\n"
            + "\n\n".join(out) + "\n\n" + tail)
    (BASE / f"{deck}.html").write_text(html, encoding="utf-8")
    print(f"{deck}.html: {len(out)} slides")

for d in (sys.argv[1:] or DECKS):
    build(d)
