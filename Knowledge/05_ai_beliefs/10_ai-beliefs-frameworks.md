# 인용 가능한 AI "믿음/입장" 프레임워크 모음: 실무자·낙관론·회의론 (AI 신념 프레임워크)

- **저자/기관**: 복수 출처 (아래 목록)
  - Ethan Mollick (Wharton), *Co-Intelligence* (2024-04) 및 One Useful Thing (2023–2026)
  - Simon Willison (개인 블로그 simonwillison.net): "Slop is the new name…"(2024-05-08), "Not all AI-assisted programming is vibe coding"(2025-03-19), "Things we learned about LLMs in 2024"(2024-12-31)
  - Andrej Karpathy: "Jagged Intelligence" X 게시물(2024-07, 정확한 날짜 미확인), "Software Is Changing (Again)" YC AI Startup School 기조연설(2025-06), "Sequoia Ascent 2026 summary"(2026-04-30)
  - Dario Amodei (Anthropic), "Machines of Loving Grace" (2024-10)
  - 회의론: Gary Marcus (Marcus on AI, Substack; "Deep Learning Is Hitting a Wall", Nautilus 2022-03), Emily M. Bender et al., "On the Dangers of Stochastic Parrots" (FAccT 2021-03), Bender & Hanna, *The AI Con* (Harper, 2025-05-13)
- **발행일**: 위 출처별 표기 (2026-09-30 열람)
- **URL**:
  - https://www.oneusefulthing.org/ (특히 /p/the-overhang, /p/management-as-ai-superpower, /p/choosing-to-stay-human)
  - https://simonwillison.net/2024/May/8/slop/ , https://simonwillison.net/2025/Mar/19/vibe-coding/ , https://simonwillison.net/2024/Dec/31/llms-in-2024/
  - https://www.youtube.com/watch?v=LCEmiRjPEtQ (Software 3.0), https://www.latent.space/p/s3 (슬라이드·요약), https://karpathy.bearblog.dev/sequoia-ascent-2026/
  - https://www.darioamodei.com/essay/machines-of-loving-grace
  - https://garymarcus.substack.com/ , https://dl.acm.org/doi/10.1145/3442188.3445922 , https://en.wikipedia.org/wiki/The_AI_Con
- **자료 유형**: 책 + 블로그 + 논문 + 강연

## 핵심 요약
- **Mollick — 실용적 협업론**: 4원칙(늘 초대 / 사람이 루프에 / 사람처럼 대하되 역할 부여 / 지금이 최악의 AI). 2026년에는 "좋은 것을 알아보고 설명하는 능력"(management), "언제 AI를 쓰지 않을지 고르기"(Choosing to Stay Human), "깊은 지식·넓은 지식·취향·주체성"(The Overhang)으로 확장. 강연자 믿음 슬라이드에 가장 직접 인용하기 좋은 틀.
- **Willison — 유용성과 과장을 동시에 인정**: LLM을 "no good use cases, 전부 표절 slop"으로 보는 것은 기술을 잘못 이해한 것이라고 보면서도, 검토 없이 AI 생성물을 게시하는 행위를 "slop"이라 명명해 비판했다. AI 도움 프로그래밍 전체를 vibe coding으로 부르는 것에 반대하고, **리뷰·테스트·이해했다면 그것은 그냥 소프트웨어 개발**이라고 구분. → "쓰되 책임지고 쓴다"는 실무자 입장의 대표.
- **Karpathy — 세 가지 개념**:
  - *Software 3.0* (2025-06): 1.0(손으로 쓴 코드) → 2.0(신경망 가중치) → 3.0(영어 프롬프트가 LLM을 프로그래밍). 완전 자율보다 사람이 조절하는 "autonomy slider"와 부분 자율 제품을 강조.
  - *People spirits*: LLM은 사람 데이터로 학습한 "사람의 확률적 시뮬레이션". 어떤 면에선 초인적, 다른 면에선 결함(환각, 자기 인식 부족, 맥락 밖 기억 없음 = 선행성 기억상실).
  - *Jagged intelligence* (2024): 어려운 수학은 풀면서 9.11과 9.9 중 큰 수를 틀리는 들쭉날쭉한 능력. 2026년 Sequoia 요약에서는 이 들쭉날쭉함이 "무엇을 학습시켰고 무엇이 검증 가능한지"에서 온다고 설명.
  - *Floor vs ceiling* (2026-04-30): vibe coding은 바닥을, agentic engineering은 천장을 올린다. 사람은 명세·설계·미적 판단·리뷰를 책임진다.
- **Amodei — 낙관론이지만 "지능만으로는 부족"**: "Machines of Loving Grace"(2024-10)는 강력한 AI가 생물학·의학 발전을 크게 압축할 수 있다는 낙관론. 동시에 물리 세계의 속도, 데이터, 사람·제도 같은 **지능 외의 병목**("marginal returns to intelligence")을 명시한다. 이번 주제(완성은 사람 몫)와는 간접 관련 → 필요할 때만 한 줄 인용. (세부 표현은 원문 재확인 권장)
- **Marcus — 스케일링 회의론**: 2022년 "Deep learning is hitting a wall"의 요지는 순수 LLM 스케일링만으로는 AGI에 이르지 못하며 신경-기호(neurosymbolic) 결합이 필요하다는 것. 환각·신뢰성 문제를 지속적으로 지적. 2026년에도 같은 기조(보도 기반, 개별 글은 미열람).
- **Bender — 의미 없는 형태의 조합**: "Stochastic Parrots"(2021, Gebru·McMillan-Major·Mitchell 공저)는 LM이 의미에 대한 참조 없이 언어 형태를 확률적으로 이어 붙인다고 보고, 환경 비용·데이터 편향·과장 위험을 경고. *The AI Con*(2025, Hanna 공저)은 AI 능력이 홍보보다 작고, "AI" 과장이 노동·권력 문제를 가린다고 비판.
- **공정한 요약**: 회의론자들도 "LLM이 아무것도 못 한다"기보다 **신뢰성·의미·과장·사회적 비용**을 문제 삼는다. 실무자(Mollick, Willison, Karpathy)도 이 한계를 인정하며, 차이는 "그래서 쓰지 말자"냐 "그래서 사람이 책임지고 쓰자"냐에 있다.

## 핵심 개념·용어 정의
- **Co-intelligence**: 사람과 AI가 서로의 약점을 보완하는 협업 지능(Mollick).
- **Software 3.0**: 자연어 프롬프트가 곧 프로그램이 되는 패러다임(Karpathy).
- **People spirits**: 사람 데이터로 학습해 사람을 확률적으로 흉내 내는 존재로서의 LLM(Karpathy).
- **Jagged intelligence**: 과제별로 들쭉날쭉한 LLM 능력(Karpathy).
- **Autonomy slider**: 과제에 따라 AI 자율성의 정도를 사람이 조절하는 설계 원칙(Karpathy).
- **Slop**: 요청하지 않은·검토되지 않은 AI 생성물(Willison 확산).
- **Stochastic parrot**: 의미 이해 없이 통계적으로 언어 형태를 이어 붙이는 모델이라는 비판적 은유(Bender et al.).
- **Neurosymbolic AI**: 신경망과 기호 추론을 결합하자는 입장(Marcus).

## 비판론(skeptic)과 반론의 대응
| 쟁점 | 회의론 (Marcus, Bender) | 실무자 입장 (Mollick, Willison, Karpathy) |
|---|---|---|
| LLM은 이해하는가 | 형태만 조합, 의미 없음 | 사람의 확률적 시뮬레이션; 능력은 들쭉날쭉하지만 실재 |
| 신뢰성 | 환각은 구조적 결함 | 사람이 루프에서 검증하면 쓸 만함 |
| 품질 | slop 대량 생산 | 검토·리뷰하면 그냥 "개발/작업"; 검토 안 하면 slop |
| 미래 | 스케일링 한계 | 지금이 최악의 AI(Mollick), 자율성 슬라이더를 점차 올림(Karpathy) |
- 강연 슬라이드에서는 회의론을 허수아비로 만들지 말 것: Bender·Marcus의 핵심 우려(신뢰성, 과장, 책임)는 강연자 믿음 ③("완성은 사람 몫")과 오히려 **같은 방향**이라고 짚으면 설득력이 커진다.

## 강연에 쓸 만한 포인트
- **믿음 슬라이드 구성 틀**: "나는 [회의론의 핵심 우려]에 동의한다. 그래서 [사람의 역할]을 지킨다. 그 위에서 [AI의 역할]을 믿는다." — Mollick·Willison의 공통 문법.
- **스펙트럼 그림 아이디어**: 가로축 "회의 ↔ 낙관"에 Bender·Marcus / Willison·Mollick·Karpathy / Amodei를 배치하고, 강연자의 위치를 가운데 약간 오른쪽에 점으로 표시. 세로축은 "사람 책임 강조 정도".
- **Karpathy 3종 세트 한 장**: Software 3.0(무엇이 바뀌었나), people spirits + jagged(무엇을 조심하나), floor/ceiling(누가 어디까지 가나).
- 인용(1개): "Assume this is the worst AI you will ever use." — Ethan Mollick, *Co-Intelligence* (2024) 4원칙 중 하나

## 원본 그림
- Karpathy "Software Is Changing (Again)" 슬라이드(1.0/2.0/3.0, autonomy slider) — Latent Space 요약 페이지 https://www.latent.space/p/s3 에 슬라이드 이미지 포함, 개별 이미지 URL 미확인
- Mollick 4원칙 스케치노트(제3자 제작) — https://alyssafuward.substack.com/p/sketchnote-a-summary-of-ethan-mollicks (저작권 제3자, 참고용)
- 그 외: 없음
