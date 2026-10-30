# 비슷한 주장: 70% 문제, 나인의 행진, 병렬 에이전트와 검토 병목 (시간 압축 슬라이드 근거)

- **저자/기관**: Addy Osmani(Google), Andrej Karpathy(Dwarkesh Podcast), Boris Cherny(Anthropic, Claude Code 책임자) 외
- **발행일**: Osmani "The 70% problem" 2024-12 / "The 80% Problem in Agentic Coding"(날짜 미확인) / Karpathy 인터뷰 2025-10 / Cherny 팁 2026-01~02, Fortune 인터뷰 2026-06-11 (2026-10-01 검색)
- **URL**:
  - https://addyo.substack.com/p/the-70-problem-hard-truths-about
  - https://addyo.substack.com/p/the-80-problem-in-agentic-coding
  - https://venturebeat.com/technology/karpathys-march-of-nines-shows-why-90-ai-reliability-isnt-even-close-to
  - https://x.com/bcherny/status/2017742743125299476
  - https://fortune.com/2026/06/11/anthropic-claude-boris-cherny-doesnt-write-code-by-hand-anymore/
  - https://en.wikipedia.org/wiki/Last_mile_(artificial_intelligence)
- **자료 유형**: 블로그, 인터뷰, 기사 (검색 결과 요약 기준, 본문 정독 전)

## 핵심 요약
- **70% 문제(Osmani, 2024-12)**: AI는 결과물의 70%까지는 놀랍게 빨리 데려가지만, 나머지 30%(예외 상황, 동시성 문제, 보안, 접근성, 다른 부분과의 연결)는 처음 70%보다 오래 걸리고 AI가 스스로 안정적으로 해내지 못하는 판단을 요구한다. 그 30%가 숙련자가 가치를 증명하는 구간이다. 후속 글에서 에이전트 시대에는 비율이 80%로 올라갔다고 봄(본문 미확인).
- **나인의 행진(Karpathy, 2025-10)**: 90% 작동하는 데모는 첫 번째 9일 뿐이고, 99%, 99.9%로 가는 각각의 9에 비슷한 양의 노력이 든다. 데모는 쉽고 제품은 어렵다. → 완성 기준(빨간 선)까지의 마지막 구간이 줄지 않는 이유를 설명.
- **마지막 1마일(last mile)**: 알고리즘은 선택지를 만들고, 사람은 그것이 무슨 뜻이며 무엇을 할지 정한다. "인상적으로 보이는 수준"과 "내보낼 수 있는 수준" 사이의 틈을 메우는 것이 사람의 일(여러 에세이, 위키백과 항목).
- **병렬 실행(Cherny, 2026)**: git worktree 3~5개에서 Claude 세션을 동시에 돌리는 것이 가장 큰 생산성 향상이라고 공개적으로 권장. 이후 병목은 코드 작성에서 **코드 검토**로 옮겨갔고, Anthropic은 검토도 여러 Claude로 나눠 맡기되 최종 승인은 사람이 한다(Fortune 2026-06-11 등 보도).

## 시간 압축 슬라이드와의 대응
| 그래프 요소 | 대응하는 기존 주장 |
|---|---|
| AI 한계선(초록 점선)까지 빠르게 | Osmani 70%(에이전트 80%) — 초안은 빠르다 |
| 흰 구간(사람이 채움) | Osmani 마지막 30%, 마지막 1마일, Karpathy 나인의 행진 |
| 빨간 선은 그대로 | 나인의 행진: 기준을 올릴수록 각 단계에 같은 노력 |
| 초록 곡선 여러 개(병렬) | Cherny의 3~5개 병렬 세션 |
| 병렬의 한계 | 병목이 검토로 이동(Cherny), 사람의 판단량이 상한 |

## 강연에 쓸 만한 포인트
- 표현 후보: "AI는 70%를 빨리, 마지막 30%는 사람이" / "데모는 쉽고, 완성은 어렵다" / "병목은 작성에서 검토로 옮겨간다"
- 주의: 70%·80%는 경험에서 나온 어림수이지 측정값이 아니다. 슬라이드에서는 "대부분"처럼 표현하거나 출처를 붙인다.
