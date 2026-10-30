# RL search agents and Deep Research (강화학습으로 검색을 배우는 에이전트와 딥 리서치 제품)

- **저자/기관**:
  - Search-R1: Bowen Jin, Zhenrui Yue, Dong Wang, Jiawei Han (UIUC 컴퓨터과학과) / Hansi Zeng, Hamed Zamani (UMass Amherst CIIR) / Jinsung Yoon, Sercan Ö. Arık (Google Cloud AI Research)
  - 관련 연구: R1-Searcher (Huatong Song 외, Wayne Xin Zhao, Ji-Rong Wen 등), DeepResearcher (Yuxiang Zheng 외, Pengfei Liu 등)
  - 제품: OpenAI (deep research), Google (Gemini Deep Research, 글쓴이 Dave Citron), Anthropic (Research, Jeremy Hadfield 외)
  - 주의 사항 근거: DeepTRACE (Pranav Narayanan Venkit, Philippe Laban 외), ReportBench (Minghao Li 외)
- **발행일**: (2026-10-23 열람)
  - Search-R1: arXiv v1 2025-03-12, v3 2025-04-08, v4 2025-07-21, v5 2025-08-05. v4 PDF 머리말에 "Published as a conference paper at COLM 2025" 표기 확인
  - R1-Searcher: arXiv v1 2025-03-07 / DeepResearcher: arXiv v1 2025-04-04
  - Google Gemini Deep Research: 2024-12-11 / OpenAI deep research: 2025-02-02 / OpenAI Deep Research System Card: 2025-02-25 / Anthropic 멀티에이전트 글: 2025-06-13
  - ReportBench: 2025-08-14 / DeepTRACE: 2025-09-02
- **URL**:
  - https://arxiv.org/abs/2503.09516 (HTML v5: https://arxiv.org/html/2503.09516v5 , 코드: https://github.com/PeterGriffinJin/Search-R1)
  - https://arxiv.org/abs/2503.05592 (R1-Searcher)
  - https://arxiv.org/abs/2504.03160 (DeepResearcher)
  - https://openai.com/index/introducing-deep-research/ (직접 접속은 403. OpenAI CDN에 있는 같은 글의 PDF 사본 https://cdn.openai.com/API/docs/deep_research_blog.pdf 로 확인)
  - https://cdn.openai.com/deep-research-system-card.pdf
  - https://blog.google/products/gemini/google-gemini-deep-research/
  - https://www.anthropic.com/engineering/multi-agent-research-system
  - https://arxiv.org/abs/2509.04499 (DeepTRACE), https://arxiv.org/abs/2508.15804 (ReportBench)
- **자료 유형**: 논문(arXiv, COLM 2025) / 공식 블로그 / 시스템 카드

## 핵심 요약
- **Search-R1의 문제의식**: 추론 모델에게 프롬프트만으로 검색엔진을 쓰게 하면 검색을 언제, 어떻게 할지 잘 모른다. 그래서 검색 호출 자체를 강화학습(RL)으로 가르친다. 검색엔진을 "환경(environment)"의 일부로 보고, 모델이 추론 도중 스스로 여러 번 검색 질의를 만들도록 학습한다.
- **상호작용 형식**: 모델은 `<think>…</think>`에서 추론하고, 필요하면 `<search>질의</search>`를 낸다. 시스템이 검색 결과를 `<information>…</information>`으로 끼워 넣으면 모델이 이어서 추론하고, 최종 답은 `<answer>…</answer>`로 낸다. 이 과정이 한 답변 안에서 여러 차례(multi-turn) 반복된다.
- **검색 토큰 마스킹(retrieved token masking)**: `<information>` 안의 검색 결과 토큰은 모델이 만든 것이 아니므로 손실(policy-gradient loss) 계산에서 뺀다. 모델이 직접 생성한 토큰만 최적화하며, 저자들은 이것이 RL 학습을 안정시킨다고 보고한다.
- **보상(reward)**: 정답과의 정확 일치(Exact Match)만으로 주는 규칙 기반 결과 보상(outcome-based reward). 형식 보상이나 신경망 보상모델, 과정 보상은 쓰지 않는다.
- **학습 설정**: RL 알고리즘은 PPO(기본)와 GRPO를 비교. 기반 모델은 Qwen2.5-3B, 7B(Base·Instruct). 검색기는 E5, 말뭉치는 2018 위키백과, 기본 top-3 문단. 학습 데이터는 NQ와 HotpotQA 학습셋을 합친 것.
- **평가**: 7개 QA 데이터셋(일반 QA: NQ, TriviaQA, PopQA / 다중 홉 QA: HotpotQA, 2WikiMultiHopQA, Musique, Bamboogle), 지표는 EM.
- **성능 수치는 버전마다 다르다(중요)**:
  - arXiv v3(2025-04-08) 초록: RAG 기준선 대비 **41%(Qwen2.5-7B), 20%(Qwen2.5-3B)** 향상.
  - arXiv v4(2025-07-21, COLM 판)와 v5(2025-08-05) 본문 초록: **24%(7B), 20%(3B)**. 그런데 같은 v4·v5의 서론(기여 요약)은 여전히 "41%와 20%"라고 쓴다. arXiv 초록 페이지의 메타데이터 초록도 41%로 남아 있다.
  - v5 표 2 평균 EM: 7B Search-R1-base(PPO) 0.431, RAG 0.304, rejection sampling 0.348. 41%는 RAG 대비, 24%는 rejection sampling 대비 상대 향상과 맞아떨어진다(강연자 계산이며, 논문이 이렇게 설명한 것은 확인하지 못함).
  - 이 노트는 v5(HTML)를 기준으로 하되 두 수치를 모두 적는다. 강연에서는 "v5 기준 평균 EM 0.304(RAG) → 0.431(7B)"처럼 절대값으로 인용하는 편이 안전하다.
- **관련 RL 검색 에이전트 2편(주의: 초록만 확인)**:
  - R1-Searcher(arXiv 2503.05592): 2단계 결과 기반 RL로 LLM이 추론 중 외부 검색을 호출하게 한다. 과정 보상이나 증류(distillation) 없이 RL만 쓴다. 초록에는 GPT-4o-mini를 포함한 기존 RAG 방법을 크게 앞선다고만 하고 수치는 없다.
  - DeepResearcher(arXiv 2504.03160): 통제된 RAG 환경이 아니라 실제 웹과 상호작용하며 end-to-end RL로 학습. 프롬프트 기반 기준선 대비 최대 28.9점, RAG 기반 RL 에이전트 대비 최대 7.2점 향상. 계획 수립, 출처 교차확인, 자기 성찰, 확실한 답이 없을 때 인정하기 같은 행동이 나타났다고 보고한다.
- **제품 사례 = 실전의 agentic RAG**:
  - **Google Gemini Deep Research(2024-12-11)**: 질문을 받으면 다단계 연구 계획을 먼저 보여주고 사용자가 수정·승인한다. 이후 몇 분간 웹을 검색하고, 찾은 내용을 보고 다음 검색을 다듬은 뒤, 원 출처 링크가 달린 보고서를 낸다(Google Docs로 내보내기 가능). 출시 당시 이름은 "Gemini 1.5 Pro with Deep Research", Gemini Advanced 구독자 대상.
  - **OpenAI deep research(2025-02-02)**: 수백 개의 온라인 출처를 찾아 분석·종합해 보고서를 쓰는 에이전트. o3의 초기 버전을 웹 브라우징·데이터 분석용으로 최적화한 모델 기반이며, 브라우저와 Python 도구를 쓰는 실제 과제에서 end-to-end RL로 학습했다고 밝힌다. 한 번에 5~30분 걸리고, 모든 출력에 인용(citation)과 사고 과정 요약이 붙는다. 출시 당시 Pro 사용자 대상. Humanity's Last Exam 26.6%(브라우징+Python 도구 사용), GAIA 평균 67.36(pass@1, 이전 SOTA 63.64).
  - OpenAI 글의 "Pass Rate vs Max Tool Calls" 그래프는 허용 도구 호출 수가 늘수록 통과율이 오른다는 것을 보여준다(약 80회에서 0.15 수준). 검색을 더 많이 할수록 잘한다는 메시지.
  - **Anthropic Research(2025-06-13 엔지니어링 글)**: 자세한 내용은 `01_context_engineering/10_anthropic-multi-agent-research-system.md` 참조. agentic RAG 관점의 요점만 적으면 다음과 같다(2026-10-23 원문 재확인). (1) 리드 에이전트가 계획을 세우고 하위 에이전트(subagent)들이 각자 검색 도구를 반복 사용하며 병렬로 탐색하는 orchestrator-worker 구조. (2) 글 스스로 이를 정적 RAG 검색과 대비시킨다. (3) Opus 4 리드 + Sonnet 4 하위 에이전트 구성이 단일 Opus 4보다 내부 연구 평가에서 90.2% 더 좋았다. (4) BrowseComp에서 토큰 사용량 하나가 성능 분산의 80%를 설명했고, 토큰 사용량·도구 호출 수·모델 선택 세 요인이 95%를 설명했다. (5) 에이전트는 채팅 대비 약 4배, 멀티에이전트는 약 15배 토큰을 쓴다. (6) 마지막에 CitationAgent가 주장마다 출처 위치를 찾아 붙인다.
- **연구자를 위한 주의점**:
  - **인용 정확도**: DeepTRACE(arXiv 2509.04499, 주의: 초록만 확인)는 GPT-4.5/5, You.com, Perplexity, Copilot/Bing, Gemini를 웹검색·딥리서치 설정으로 감사했다. 인용 정확도(citation accuracy)는 시스템에 따라 40~80%였고, 딥리서치 설정도 문장의 상당 부분이 자기가 제시한 출처로 뒷받침되지 않았다. 논쟁적 질문에는 한쪽으로 치우친 답을 자신 있게 내는 경향도 보고했다.
  - ReportBench(arXiv 2508.15804, 주의: 초록만 확인)는 arXiv 서베이 논문을 기준으로 딥리서치 보고서를 평가했다. OpenAI·Google의 상용 딥리서치가 검색 붙은 일반 LLM보다 낫지만, 사실 일관성(factual consistency)은 아직 개선 여지가 크다고 결론짓는다.
  - **비용**: Anthropic 글 기준 멀티에이전트 검색은 채팅보다 약 15배 토큰을 쓴다. OpenAI도 성능이 도구 호출 수와 함께 오른다고 보여준다. 성능의 상당 부분을 "검색과 토큰을 얼마나 쓰느냐"로 사는 셈이다.
  - **보안**: OpenAI 시스템 카드는 딥리서치가 웹에서 읽은 악성 지시문을 따를 수 있는 프롬프트 인젝션(prompt injection) 위험을 명시하고, 대응 중 하나로 모델이 임의 URL을 만들거나 그리로 이동하지 못하게 했다고 밝힌다.

## 핵심 개념·용어 정의
- **RL search agent**: 검색 호출 시점·질의 작성·반복 여부를 강화학습으로 익힌 LLM. 프롬프트로 검색을 시키는 방식(IRCoT, ReAct 등)과 대비된다.
- **Search engine as environment**: 검색엔진을 RL 환경으로 보고, 모델 생성과 검색 결과가 번갈아 끼워진 궤적(trajectory)을 롤아웃해 학습하는 설정.
- **Retrieved token masking**: 외부에서 들어온 검색 결과 토큰을 손실 계산에서 제외하는 기법. 모델이 "자기가 쓰지 않은 글"을 학습 대상으로 삼지 않게 한다.
- **Outcome-based reward**: 최종 답이 맞았는지만 보는 보상. 중간 검색 단계에는 점수를 주지 않는다(process reward와 대비).
- **PPO / GRPO**: PPO는 가치 함수(critic)를 함께 학습하는 RL 알고리즘. GRPO는 같은 질문에 여러 답을 뽑아 그룹 평균을 기준선으로 삼으므로 critic이 필요 없다. Search-R1은 둘 다 실험했고 PPO를 기본으로 썼다.
- **Deep research**: 하나의 질문에 대해 수 분~수십 분 동안 계획 → 반복 검색·열람 → 종합 → 인용 달린 보고서를 내는 에이전트형 제품군의 통칭.
- **Citation accuracy / faithfulness**: 인용한 출처가 실제로 해당 주장을 뒷받침하는 비율. 링크가 살아 있는지(existence)와는 다른 문제.

## 강연에 쓸 만한 포인트
- **흐름 도식**: Naive RAG(검색 1회 → 생성) → 프롬프트 기반 agentic RAG(ReAct처럼 모델이 검색을 도구로 호출) → RL로 검색을 배운 에이전트(Search-R1) → 제품화된 deep research(계획·병렬 검색·인용). 오른쪽으로 갈수록 검색 횟수와 비용이 늘고 모델의 자율성이 커진다.
- **Search-R1 한 장 요약**: `<think>` → `<search>` → `<information>` → … → `<answer>` 태그 흐름을 그대로 보여주면 "검색이 추론 루프 안의 도구"라는 점이 한눈에 보인다. 보상이 "정답이냐 아니냐" 하나뿐이라는 점도 청중에게 의외로 다가갈 만하다.
- **수치 인용 주의 슬라이드**: 같은 논문 안에 41%와 24%가 공존한다. 비교 기준선이 무엇인지 확인하지 않으면 "몇 % 향상"이 쉽게 오해된다는 방법론 사례로 쓸 수 있다.
- **제품 비교 표**: Gemini(계획을 사용자에게 먼저 보여주고 승인받음) / OpenAI(RL로 학습한 단일 에이전트, 5~30분) / Anthropic(리드 + 하위 에이전트 병렬). 셋 다 "계획 → 반복 검색 → 인용 보고서" 구조다.
- **연구자 메시지**: 딥리서치 결과는 1차 문헌 탐색의 출발점이지 인용 목록 그 자체가 아니다. 인용 정확도 40~80%라는 감사 결과(DeepTRACE)를 근거로, 보고서의 핵심 주장마다 원문을 열어 확인하라고 권한다.
- 요지(의역): 모델이 더 많이 검색하고 그 내용을 더 오래 생각할수록 성능이 오른다 — OpenAI, Introducing deep research(2025-02-02)의 그래프 설명문. 15단어 인용 제한 때문에 의역으로 둠.

## 원본 그림
- Search-R1 Figure 1: PPO와 GRPO 각각에서 검색엔진과 다중 턴 상호작용하는 롤아웃 구조 — https://arxiv.org/html/2503.09516v5 (개별 이미지 URL은 확인하지 않음)
- Search-R1 Figure 2: PPO vs GRPO, Base vs Instruct, 응답 길이, 유효 검색 횟수의 학습 곡선 — 같은 페이지
- OpenAI "Pass Rate vs Max Tool Calls" 그래프(도구 호출 수가 늘수록 통과율 상승) — https://cdn.openai.com/API/docs/deep_research_blog.pdf 12쪽(PDF 사본에서 확인)
- Anthropic 멀티에이전트 구조도(리드 에이전트가 하위 에이전트를 만들어 병렬 검색) — https://www-cdn.anthropic.com/images/4zrzovbb/website/1198befc0b33726c45692ac40f764022f4de1bf2-4584x2579.png
- Anthropic 전체 처리 흐름도(LeadResearcher → Memory → Subagents → CitationAgent) — https://www-cdn.anthropic.com/images/4zrzovbb/website/3bde53c9578d74f6e05c3e515e20b910c5a8c20a-4584x4584.png
- 참고: Anthropic 이미지 URL은 페이지의 `/_next/image?url=...` 래퍼를 풀어 얻은 것이며 개별 파일 접근 여부는 확인하지 않음.

## Claude Code와의 연결점
(강연자 해석)
- **에이전트 루프로 보기**: Search-R1의 `<think>` → `<search>` → `<information>` → `<answer>`는 강연에서 쓰는 plan → act → verify 루프와 같은 모양이다. think가 plan, search가 act, information을 읽고 다시 판단하는 것이 verify에 해당한다. Claude Code가 WebSearch·WebFetch·Grep을 도구로 부르고 결과를 보고 다음 행동을 고르는 것도 같은 구조다.
- **검색은 도구 중 하나**: Search-R1은 검색 결과를 "환경이 돌려주는 관찰"로 다룬다. Claude Code에서 검색 결과나 파일 내용이 도구 결과로 컨텍스트에 들어오는 방식과 같다. 차이는 Search-R1은 그 사용법을 RL로 모델 가중치에 새겼고, Claude Code는 범용 모델이 프롬프트와 도구 설명을 보고 판단한다는 점이다.
- **하위 에이전트 = 병렬 검색**: Anthropic Research의 orchestrator-worker 구조는 Claude Code의 subagent 위임과 대응된다. "세 주제를 각각 subagent로 조사하고 요약만 돌려줘"라고 시키면 딥리서치를 축소 재현할 수 있다(01_context_engineering/10번 노트 참조).
- **인용 검증을 verify 단계로**: DeepTRACE 결과를 고려하면, 연구용 문헌 조사를 시킬 때 "모든 수치는 실제로 연 페이지에서만 가져오고, 확인 못 한 것은 표시하라"는 규칙을 넣는 것이 verify 단계의 실전형이다. 이 노트도 각 항목에 원문 확인 범위를 표시하는 방식으로 작성했다.
- **비용 감각**: 성능이 토큰·도구 호출 수와 함께 오른다는 Anthropic·OpenAI의 관찰은, Claude Code에서 subagent를 많이 띄우면 결과는 좋아질 수 있으나 사용량도 함께 늘어난다는 점과 연결된다.