# AI가 사고를 대체하지 않고 확장하는 조건 (Conditions for learning with AI)
- **저자/기관**: Bastani 외 (UPenn, PNAS 2025); Kestin 외 (Harvard, Scientific Reports 2025); Lehmann·Cornelius·Sting (Cologne·Erasmus, arXiv 2024); Shen & Tamkin (Anthropic, 2026); Anthropic Education Report (2025-04); OpenAI (study mode, 2025-07); Risko & Gilbert (2016); Bjork (1994)
- **발행일**: 1994 ~ 2026-01 (2026-09-30 열람)
- **URL**:
  - https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html
  - https://www.nature.com/articles/s41598-025-97652-6 (Kestin 외)
  - https://arxiv.org/abs/2409.09047 (AI Meets the Classroom)
  - https://www.anthropic.com/research/AI-assistance-coding-skills
  - https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude
  - https://www.anthropic.com/news/introducing-claude-for-education
  - https://openai.com/index/chatgpt-study-mode/
  - https://doi.org/10.1016/j.tics.2016.07.002 (Risko & Gilbert)
- **자료 유형**: 논문 + 보고서 + 기사

## 핵심 요약
- **Bastani 외 (PNAS 2025)**: 같은 GPT-4라도 **정답을 바로 주지 않고 힌트를 주도록 설계한 GPT Tutor**는 AI 제거 후 성적 손실(GPT Base −17%)을 대체로 상쇄. 차이는 모델이 아니라 **안전장치(guardrail) 설계**.
- **Kestin 외 (Scientific Reports, 2025-06; 하버드 PS2, 2023년 가을, 194명 교차 RCT)**: 소크라테스식 질문·인지부하 조절·정답 직접 제공 금지로 설계한 AI 튜터가 교실 능동학습보다 **학습 이득이 2배 이상**, 소요 시간은 더 짧음. 효과의 원천은 교수설계(scaffolding).
- **Lehmann 외 (arXiv 2409.09047)**: 사전등록 실험 2건에서 LLM의 전체 학습 효과는 0. 탐색적 분석에서 **개념 설명을 묻는 "튜터형" 사용은 이득, 연습문제 풀이를 맡기는 사용은 손해**. 흥미롭게도 **사전 지식이 없는 학생이 LLM 접근으로 더 이득**.
- **Anthropic 코딩 RCT (2026-01, n=52)**: AI 집단 평균 퀴즈 50% vs 67%. 그러나 하위 패턴(전면 위임 n=4, 점진적 의존 n=4, AI에 디버깅 맡기기 n=4)은 40% 미만, 상위 패턴(생성 후 이해 질문 n=2, 코드+설명 동시 요청 n=3, **개념 질문만 하고 오류는 스스로 해결 n=7**)은 65% 이상. 개념 질문형은 속도도 두 번째로 빠름. 하위 집단 n이 매우 작아 탐색적 결과.
- **Anthropic Education Report (2025-04-08, 학생 대화 100만 건)**: 대화의 **47%가 최소 노력의 "직접형"** 상호작용. 블룸 분류상 "창작(39.8%)"·"분석(30.2%)" 같은 고차 인지 과업을 AI에 맡기는 비중이 큼 → 고차 사고의 외주화 우려.
- **제품 차원의 대응**: Anthropic **Claude for Education·학습 모드(2025-04-02)**, OpenAI **ChatGPT study mode(2025-07-29)** — 둘 다 정답 대신 소크라테스식 질문·단계적 힌트를 제공. 효과에 대한 독립 RCT는 아직 제한적.
- **Risko & Gilbert (Trends in Cognitive Sciences, 2016)**: 인지적 오프로딩은 자연스럽고 종종 합리적이지만, 오프로딩한 정보는 내부 기억에 덜 남는다. 오프로딩 여부는 **메타인지적 판단**(내 기억·능력에 대한 믿음)에 좌우.
- **Bjork (1994) "바람직한 어려움"**: 인출 연습, 간격 두기, 교차 연습처럼 **당장은 힘들게 느껴지는 조건이 장기 학습을 강화**. AI가 모든 마찰을 제거하면 이 어려움도 사라진다.

## 핵심 개념·용어 정의
- **안전장치(guardrail) 설계**: 정답 비공개, 힌트 단계화, 학생의 시도를 먼저 요구하는 프롬프트·인터페이스 설계.
- **스캐폴딩(scaffolding)**: 학습자가 혼자 못하는 단계만 일시적으로 지원하고 점차 거두는 교수법.
- **확장(extend) vs 대체(offload/replace)**: 확장은 AI로 더 어려운 문제·더 넓은 탐색을 하되 핵심 추론은 자신이 수행, 대체는 추론 자체를 AI에 넘기는 것.
- **바람직한 어려움(desirable difficulties)**: 학습 중 수행을 늦추지만 장기 파지·전이를 높이는 난이도.

## 비판론(skeptic)과 반론의 대응
- **강연자 믿음을 지지**: 여러 연구가 **같은 도구라도 사용 방식에 따라 학습이 늘거나 줄어든다**는 점에서 일치한다(Bastani, Kestin, Lehmann, Anthropic). 동기가 높고 이해를 목표로 하는 사용자는 "개념 질문 → 스스로 해결" 패턴을 택할 가능성이 높고, 이 패턴은 손실이 없거나 이득이다.
- **강연자 믿음을 제약**: (1) Lehmann 외는 **사전 지식이 없는 학생이 더 이득**을 봤다고 보고 — "상위 집단만 이득"과 반대. (2) 좋은 결과는 **사용자 특성보다 도구 설계(가드레일)**에서 나온 경우가 많다(Bastani, Kestin). 즉 "상위 집단이라서"가 아니라 "사고를 유지하도록 쓰였기 때문". (3) Anthropic 패턴 분석은 소표본·탐색적이며, 동기 높은 사람이 원래 개념 질문을 선택했을 가능성(선택 편향)을 배제 못한다.
- **함의**: "숙련·동기 → 확장적 사용 → 역량 증가"라는 경로는 그럴듯하고 일부 증거가 있지만, **확장적 사용은 가르칠 수 있는 기술**이라는 쪽이 더 방어 가능한 주장이다.

## 강연에 쓸 만한 포인트
- 인용(Bastani 외 논문 제목): "Generative AI without guardrails can harm learning" — 가드레일 없는 AI는 학습을 해칠 수 있다.
- 그림 아이디어: Anthropic 6가지 사용 패턴을 가로 막대로 — 왼쪽(위임·점진적 의존·AI 디버깅: <40%), 오른쪽(생성 후 이해·코드+설명·개념 질문: ≥65%). 제목: "같은 AI, 다른 결과: 차이는 질문 방식".
- 실천 규칙 슬라이드: ① 먼저 스스로 시도 ② AI에는 "답"보다 "왜"를 묻기 ③ 생성된 코드는 설명할 수 있을 때만 채택 ④ 오류는 먼저 직접 추적 ⑤ 주기적으로 AI 없이 풀어보기(바람직한 어려움).

## 원본 그림
- Anthropic "How AI assistance impacts the formation of coding skills" 사용 패턴별 점수 그림 — 이미지 URL 없음(https://www.anthropic.com/research/AI-assistance-coding-skills 참조)
- Kestin 외 학습 이득 비교 그림 — 이미지 URL 없음(Scientific Reports 원문 참조)
