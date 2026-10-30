# AI 사용과 사고력 저하·탈숙련 증거 (비판론 측 근거 모음)
- **저자/기관**: Kosmyna 외 (MIT Media Lab); Lee 외 (Microsoft Research·CMU); Gerlich (SBS Swiss Business School); Bastani 외 (Univ. of Pennsylvania); Budzyń 외 (폴란드 ACCEPT 연구진); Liu, Christian 외 (2026); Shen & Tamkin (Anthropic, 2026)
- **발행일**: 2025-01 ~ 2026-08 (2026-09-30 열람)
- **URL**:
  - https://arxiv.org/abs/2506.08872 (Your Brain on ChatGPT, 프리프린트)
  - https://arxiv.org/abs/2601.00856 (위 논문에 대한 비판 코멘트)
  - https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/
  - https://papers.ssrn.com/abstract=5082524 (Gerlich, Societies 2025)
  - https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html (Bastani, PNAS 2025)
  - https://ascopost.com/news/august-2025/routine-ai-assistance-may-lead-to-loss-of-skills-in-endoscopists-study-shows/ (Lancet Gastroenterol Hepatol 2025 보도)
  - https://arxiv.org/abs/2604.04721 (AI Assistance Reduces Persistence, 2026)
  - https://www.anthropic.com/research/AI-assistance-coding-skills (2026-01)
- **자료 유형**: 논문(프리프린트·학회·학술지) + 기사

## 핵심 요약
- **MIT "Your Brain on ChatGPT" (Kosmyna 외, arXiv v1 2025-06-10, v2 2025-12-31)**: 대학생 54명을 LLM / 검색엔진 / 도구 없음(Brain-only) 세 집단으로 나눠 에세이 3회 작성, EEG 측정. 뇌 연결성은 Brain-only > 검색 > LLM 순. 4번째 세션(참여 18명)에서 LLM→Brain 전환자는 알파·베타 연결성이 낮았고, LLM 집단은 자기 글을 정확히 인용하지 못하고 글에 대한 소유감이 가장 낮았다. 저자들은 이를 "인지 부채(cognitive debt)"라 명명.
  - **한계**: 동료심사 전 프리프린트, 세션 4는 n=18, 과제는 에세이 한 종류. Stanković 외(arXiv 2601.00856, 2025-12)가 표본 크기·재현성·EEG 분석 방법·결과 보고의 불일치·투명성 부족을 지적.
- **Microsoft Research·CMU (Lee 외, CHI 2025)**: 지식노동자 319명, 실제 업무 사례 936건 설문. **AI에 대한 신뢰가 높을수록 비판적 사고를 덜 수행**하고, **자기 과업 자신감이 높을수록 비판적 사고를 더 수행**. 비판적 사고의 내용이 "문제 해결"에서 "정보 검증·응답 통합·과업 관리(stewardship)"로 이동. 자기보고 기반이라 인과 추론은 불가.
- **Gerlich (Societies, 2025-01 게재, 2025-09-10 정정)**: 666명 설문+인터뷰. AI 사용 빈도와 비판적 사고 점수 사이에 유의한 음의 상관, 인지적 오프로딩이 매개. 젊은 층(17–25세)이 의존도 높고 점수 낮음. **학력이 높을수록 AI 사용과 무관하게 비판적 사고 점수가 높음**. 횡단 상관연구, 정정본 존재.
- **Bastani 외 (PNAS 2025, 튀르키예 고교 수학 현장실험, 약 1,000명)**: 연습 중에는 GPT Base 48%, GPT Tutor 127% 성적 향상. 그러나 AI를 뺀 시험에서 **GPT Base 집단은 대조군보다 17% 낮은 성적**. 교육적 안전장치(힌트 위주·정답 비공개)를 둔 GPT Tutor는 이 손실을 대체로 상쇄. 학생들이 AI를 "목발(crutch)"로 사용한 것이 원인으로 제시됨.
- **의학의 탈숙련 (Budzyń 외, Lancet Gastroenterology & Hepatology, 2025-08 온라인)**: 폴란드 4개 센터, 대장내시경 2,000건 이상 경험한 숙련의 19명. AI 도입 이후 **AI 없이 시행한 내시경의 선종 발견율(ADR)이 28.4% → 22.4%**(절대 6%p, 상대 약 20% 감소). 후향적 관찰연구이므로 업무량 변화 등 교란 가능성이 있으나, **숙련자도 탈숙련될 수 있다**는 실제 임상 증거로 평가됨.
- **Liu, Christian, Dumbalska, Bakker, Dubey (arXiv 2604.04721, 2026-04, 개정 2026-08)**: RCT 총 1,222명, 수학 추론·독해. AI 보조는 즉시 성과를 높이지만, **약 10분 사용 후 AI 없이 풀 때 성과가 낮고 더 빨리 포기**. 프리프린트.
- **Anthropic (Shen & Tamkin, 2026-01-29)**: 새 파이썬 라이브러리(Trio)를 배우는 주니어 개발자 52명 RCT. 퀴즈 점수 AI 집단 약 50% vs 수작업 집단 약 67%(Cohen's d=0.738, p=0.01), 디버깅 문항에서 격차가 가장 큼. 작업 시간 단축은 통계적으로 유의하지 않음. 단, 사용 방식에 따라 결과가 갈림(06 파일 참조).

## 핵심 개념·용어 정의
- **인지적 오프로딩(cognitive offloading)**: 외부 도구로 과업의 인지 부하를 줄이는 행동 (Risko & Gilbert, 2016).
- **인지 부채(cognitive debt)**: Kosmyna 외의 비유. 당장의 노력을 AI로 미루면 나중에 기억·이해·소유감 결손으로 돌아온다는 가설.
- **자동화 안주(automation complacency)**: 자동화를 믿고 스스로의 감시·판단을 줄이는 현상. 항공·의료에서 오래 연구됨.
- **탈숙련(deskilling)**: 도구에 기대는 동안 도구 없이 수행하는 능력이 퇴화하는 현상.
- **목발 효과**: Bastani 외가 말한 "AI를 연습의 대체물로 사용"하는 패턴.

## 비판론(skeptic)과 반론의 대응
- **비판론을 지지하는 부분**: 인과 설계(Bastani RCT, Liu 외 RCT, Anthropic RCT)와 관찰연구(내시경)가 같은 방향을 가리킨다. **도구 없이 해야 할 때의 성과**, 즉 독립 역량은 무방비한 AI 사용으로 떨어질 수 있다. "평균적으로 저하될 수 있다"는 강연자 믿음의 전반부는 상당히 지지된다.
- **과장된 부분**: "AI가 뇌를 망가뜨린다"는 대중 보도는 MIT 프리프린트(n 작음, 비판 코멘트 존재)를 과대 해석한 것이다. Gerlich·Lee는 상관·자기보고라 인과가 아니다.
- **강연자 믿음의 후반부("상위 집단은 오히려 증가")에 대한 제약**: 내시경 연구는 **숙련자도 탈숙련**될 수 있음을 보여준다. 즉, 숙련 자체가 면역이 아니다. 반면 Lee 외(자기 자신감↑ → 비판적 사고↑), Gerlich(고학력층은 AI 사용과 무관하게 점수 높음), Bastani(안전장치가 손실 상쇄), Anthropic(개념 질문형 사용자는 점수 유지)은 **"누가"보다 "어떻게 쓰느냐"가 결정적**임을 시사한다.

## 강연에 쓸 만한 포인트
- 인용: 내시경 연구 보도 요지 — 숙련 전문의 19명 모두 경험 2,000건 이상이었는데도 ADR이 떨어졌다(수치 인용: "28.4% → 22.4%").
- 그림 아이디어: 막대 2쌍 — "AI 있을 때 성과"(GPT Base +48%, GPT Tutor +127%) vs "AI 뺐을 때 성과"(GPT Base −17%, GPT Tutor ≈0). 제목: "AI가 올려준 점수는 AI를 빼면 사라진다 — 설계에 따라".
- 두 번째 그림: 내시경 ADR 전후 두 점 연결 그래프(28.4 → 22.4).
- 주의 문구: MIT EEG 연구는 "프리프린트·소표본"임을 슬라이드 노트에 명시.

## 원본 그림
- Bastani 외 PNAS 2025 Figure(집단별 연습/시험 성적) — 이미지 URL 없음(원문 PNAS 참조)
- Kosmyna 외 EEG 연결성 비교 그림 — 이미지 URL 없음(arXiv 원문 PDF 참조)
- Budzyń 외 ADR 전후 비교 — 없음
