# 생산에서 검증으로: 지식노동자의 인지 노력 이동 (Production → Verification)
- **저자/기관**: Hao-Ping (Hank) Lee (CMU), Advait Sarkar, Lev Tankelevitch, Ian Drosos, Sean Rintel, Richard Banks, Nicholas Wilson (Microsoft Research) — 주 논문. 보조: Microsoft Research New Future of Work 2024·2025 보고서; Tankelevitch et al. (CHI 2024 Best Paper); Mozannar et al. (CHI 2024); Fakhoury et al. TiCoder (IEEE TSE 2024); Mozannar et al. RealHumanEval (2024–2025)
- **발행일**: Lee et al. CHI 2025 (2025-04/05); NFW 2024 (2024-12), NFW 2025 (2025-12, MSR-TR-2025-58) (2026-10-01 열람)
- **URL**:
  - Lee et al. (2025) The Impact of Generative AI on Critical Thinking — https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf ; https://www.microsoft.com/en-us/research/?p=1135061
  - Tankelevitch et al. (2024) The Metacognitive Demands and Opportunities of Generative AI — https://arxiv.org/abs/2312.10893
  - NFW 2024 — https://www.microsoft.com/en-us/research/wp-content/uploads/2024/12/NFWReport2024_12.20.24.pdf
  - NFW 2025 — https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf
  - Mozannar et al. (2024) Reading Between the Lines (CUPS) — https://arxiv.org/abs/2210.14306
  - Fakhoury et al. (2024) LLM-based Test-driven Interactive Code Generation (TiCoder) — https://arxiv.org/abs/2404.10100
  - Mozannar et al. RealHumanEval — https://arxiv.org/abs/2404.02806
- **자료 유형**: 논문 / 보고서

## 핵심 요약
- **Lee et al. (CHI 2025) 표본**: 지식노동자 319명이 실제 업무 GenAI 사용 사례 957건을 제출, 정제 후 936건 분석 (Creation 39.96%, Information 32.37%, Advice 27.67%). 응답자는 이 중 555건(59.29%)에서 critical thinking을 했다고 자기보고.
- **"덜 힘들다"는 자기보고**: GenAI 사용 시 각 인지 활동이 "덜/훨씬 덜 노력"이라고 답한 비율 — Knowledge 72%, Comprehension 79%, Application 69%, Analysis 72%, Synthesis 76%, Evaluation 55% (Bloom 분류, 논문 Figure 2). 평가(Evaluation)에서 감소 체감이 가장 작다.
- **신뢰의 방향이 중요**: AI가 과제를 해낼 것이라는 confidence in AI가 높을수록 critical thinking 수행이 적었다 (β = −0.69, p < 0.001). 반대로 *내가* 그 일을 할 수 있다는 자신감(β = 0.26, p = 0.026), AI 응답을 평가할 수 있다는 자신감(β = 0.31, p = 0.046), 평소 성찰 성향(β = 0.52, p < 0.001)은 critical thinking과 양의 관계. 일반적인 AI trust는 유의하지 않음. (random-intercept 회귀, Benjamini–Hochberg 보정; 자기보고 설문이라 인과 아님)
- **세 가지 이동**: ① 지식·이해 — information gathering → **information verification**, ② 적용 — problem-solving → **AI response integration**, ③ 분석·종합·평가 — task execution → **task stewardship**(목표를 정하고 품질을 책임지는 관리자 역할).
- **Metacognitive demand (Tankelevitch et al., CHI 2024 Best Paper)**: GenAI는 프롬프트 작성, 출력 평가·의존 결정, workflow 최적화 단계마다 높은 metacognitive monitoring과 control을 요구한다. 이것이 새로 생긴 인지 부하의 정체라고 본다.
- **Microsoft NFW 2024**: AI가 성과는 높여도 자기 능력 과대평가를 부추길 수 있음(Fernandes et al. 2024 인용); 초보 프로그래머는 "illusion of competence"에 빠질 수 있음(Prather et al. 2024). 적절한 의존을 위한 UX 목표 중 하나로 *"검증의 cognitive load를 낮춰라"* 를 명시.
- **Microsoft NFW 2025**: AI pair programming에서 개발자는 처음부터 쓰기보다 검증·편집·조립하는 "critical editor·project coordinator"로 이동. Vibe coding은 반복적 목표 충족과 output verification으로 정의되며(Sarkar & Drosos 2025), 학생 vibe coding 연구에서 코드 관련 행동의 90.37%가 해석에 그쳤고, 맥락 없는 프롬프트 비율은 상급생 8.39% vs 입문생 28.89% (Geng et al. 2025).
- **실측 1 — 검증 시간 (Mozannar et al., CHI 2024)**: Copilot 사용 프로그래머 21명의 세션을 상태 분류(CUPS)한 결과, 'Thinking/Verifying Suggestion'이 세션 시간의 **22.4%**로 단일 최대. Copilot 상호작용 관련 상태를 합치면 **51.5%**. (2022년 8월 버전 Copilot 기준)
- **실측 2 — NASA-TLX (TiCoder, Fakhoury et al., IEEE TSE 2024)**: 15명 within-subject. 일반 코드 생성 보조(Assistant 1) 대비, 테스트로 의도를 확인하는 TiCoder에서 전체 NASA-TLX(0–100)가 **45.46 → 28.00 / 29.52**로 감소(p = 0.007 / 0.012). Mental Demand(0–20) 12.5 → 7.5. AI 코드의 정오를 올바로 판정한 비율 **40% → 84%**. 즉 *검증을 도와주는 인터페이스*가 부하를 낮추고 정확도를 올렸다.
- **실측 3 — 지각과 실제의 불일치 (RealHumanEval)**: 243명, 7개 조건. 무보조 대비 과제당 시간은 GPT-3.5에서 78초 단축(p = 0.04) 등 일부만 유의, 완수 과제 수 차이는 없음. 프로그래머의 선호는 실제 성과와 상관하지 않았다. NASA-TLX도 측정했으나 수치는 부록(D.6)에 있어 이 조사에서 확인하지 못함.

## 핵심 개념·용어 정의
- **Critical thinking (Lee et al. 운영적 정의)**: Bloom 분류의 knowledge, comprehension, application, analysis, synthesis, evaluation 활동.
- **Information verification**: AI 출력을 외부 출처·자기 지식과 교차확인하는 일.
- **Response integration**: AI 출력을 자기 맥락에 맞게 고치고 붙이는 일.
- **Task stewardship**: 직접 수행 대신 목표 설정, 방향 조정, 품질 책임을 지는 관리자 역할.
- **Metacognition**: 자기 사고를 감시(monitoring)하고 조절(control)하는 능력. "이 출력을 믿어도 되나, 내가 판단할 수 있나"를 묻는 층위.
- **NASA-TLX**: Hart & Staveland(1988)의 주관적 작업부하 척도. Mental/Physical/Temporal Demand, Performance, Effort, Frustration 6개 하위척도(연구에 따라 변형 사용, TiCoder는 stress·pace·confidence 등으로 변형).
- **CUPS (Mozannar)**: Copilot 사용 중 프로그래머 상태 분류 체계(검증, 프롬프트 작성, 문서 찾기 등).

## 코딩 에이전트 사용과의 연결점
- **줄어드는 곳**: 정보 수집과 초안 생산. Lee의 응답자 대다수가 "덜 힘들다"고 느낀 영역이며, 코딩에선 API 찾기·초안 코드 작성에 해당.
- **옮겨 가는 곳**: 검증(테스트·diff 읽기), 통합(내 코드베이스·연구 맥락에 맞추기), stewardship(CLAUDE.md, 작업 분할, 완료 기준 정의). Copilot 시대에 이미 세션의 약 절반이 AI 상호작용 관련 상태였고, 에이전트는 생산 단위가 더 커져 검증 몫이 더 커질 가능성이 높다(추론, 직접 측정 아님).
- **늘어나는 곳**: metacognitive 판단 — "이걸 믿을지, 내가 판단할 수 있는지." Evaluation에서 노력 감소 체감이 55%로 가장 낮다는 것은 판정 단계가 여전히(또는 더) 무겁다는 신호.
- **관리 전략**:
  - 검증 비용을 낮추는 설계를 먼저: TiCoder처럼 *테스트로 의도를 고정*하고 에이전트에게 테스트를 통과하게 시키기 → 부하 ↓, 판정 정확도 ↑.
  - AI에 대한 confidence가 아니라 *자기 평가 능력*을 키워야 critical thinking이 유지된다(β 부호가 반대).
  - "AI가 해 줬다"는 느낌과 실제 생산성은 다를 수 있다(RealHumanEval) — 체감 대신 측정(시간, 통과 테스트 수)을 볼 것.

## 강연에 쓸 만한 포인트
- **비유**: 작가에서 편집장으로. 원고는 AI가 쓰지만 교정·사실확인·지면 배치와 최종 책임은 편집장의 몫 — 일이 사라진 게 아니라 종류가 바뀌었다.
- **그림 아이디어**: 세 개의 화살표(수집→검증, 문제해결→통합, 실행→stewardship)를 Lee 논문 구조 그대로.
- **그림 아이디어 2**: 시소 그림 — 왼쪽 "AI를 믿는 마음(β −0.69)", 오른쪽 "내 실력에 대한 자신감(β +0.26, +0.31)". 어느 쪽이 무거운지가 critical thinking을 결정.
- **그림 아이디어 3**: TiCoder 막대 — NASA-TLX 45 → 28, 판정 정확도 40% → 84%. "검증을 쉽게 만들면 부하는 줄고 정확도는 오른다."
- **인용 후보(1개)**: Lee et al. — 생성형 AI는 critical thinking의 성격을 "verification, response integration, and task stewardship" 쪽으로 옮긴다 (Lee et al., CHI 2025)

## 원본 그림
- Lee et al. Figure 2: Bloom 활동별 인지 노력 체감 분포(%) — PDF 내 그림 (https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf), 별도 이미지 URL 없음
- Mozannar et al. Figure 1: CUPS 상태 타임라인 — https://arxiv.org/html/2210.14306v5/figure1.png
- TiCoder workflow 도식 — https://arxiv.org/html/2404.10100v2/figures/ticoder-flow.png
- NFW 2024 p.18 Dunning-Kruger(AI 사용 집단 메타인지) 그래프 — PDF 내 그림 (https://www.microsoft.com/en-us/research/wp-content/uploads/2024/12/NFWReport2024_12.20.24.pdf)
