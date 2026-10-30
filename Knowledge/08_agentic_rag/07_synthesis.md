# Agentic RAG 종합: 계보, 정의, 기존 RAG와의 차이, 주의점 (01~06 종합, 슬라이드용)

- **저자/기관**: 강연자 정리 (01~06번 노트 종합)
- **발행일**: 2026-10-23
- **URL**: 각 근거는 01~06번 노트의 URL 참조
- **자료 유형**: 종합 노트 (강연자 해석 포함, 해석은 따로 표시)

## 핵심 요약
- **계보 (연도 = 첫 공개)**:
  1. RAG 탄생 — Lewis 외, NeurIPS 2020: 검색기(DPR)가 위키피디아 약 2,100만 개 조각에서 찾고 생성기(BART)가 답한다. 모델 안의 지식(parametric)과 바깥 색인(non-parametric)을 결합(01).
  2. 고정 파이프라인의 정리 — Gao 외 서베이(2023-12): Naive(색인 → 검색 → 생성) → Advanced(검색 전·후 최적화) → Modular(모듈 교체·재배치)(01).
  3. 검색 시점을 모델이 정한다 — ReAct(ICLR 2023, 생각·행동·관찰 루프로 위키피디아 검색), IRCoT(ACL 2023), FLARE(EMNLP 2023, 확신이 낮을 때 검색), Self-RAG(ICLR 2024, 검색·평가 토큰 학습), CRAG(2024, 검색 결과를 평가해 웹 검색으로 교정), Adaptive-RAG(NAACL 2024, 질문 난이도로 경로 선택)(02, 03).
  4. Agentic RAG라는 이름 — Singh 외 서베이(2025-01, v4 2026-04): RAG 파이프라인 안에 자율 에이전트를 넣어 언제 검색할지, 질의를 어떻게 고칠지, 근거가 충분한지를 정하는 제어 층을 둔 것(04).
  5. 학습된 검색 에이전트와 딥리서치 — Search-R1(COLM 2025, 강화학습으로 추론 중 검색 학습), OpenAI deep research(2025-02-02), Gemini Deep Research(2024-12-11), Anthropic 다중 에이전트 리서치 시스템(2025-06-13)(05). 추론과 검색을 엮은 서베이 2편: Li 외(Findings of EMNLP 2025), Liang 외(Findings of IJCNLP-AACL 2025)(06).
- **정의 (강연용, 06번 종합)**: LLM이 추론 과정 안에서 언제·무엇을·어떻게 검색할지 스스로 정하고, 찾은 근거를 평가해 질의를 고치거나 다른 도구를 부르며, 근거가 충분할 때까지 검색과 추론을 반복하는 검색 증강 생성.
- **경계선 하나**: Li 외의 기준 — 추론이 새 검색을 동적으로 일으키면 agentic(상호작용형)이고, 검색을 한 번 하고 추론하면 정적이다(06).

## 핵심 개념·용어 정의
- **기존 RAG vs Agentic RAG (06번 표 요약)**:
  | 구분 | 기존 RAG | Agentic RAG |
  |---|---|---|
  | 검색 결정 | 파이프라인이 정함(항상 1회) | LLM이 언제·무엇을 검색할지 정함 |
  | 검색 횟수 | 1회 | 근거가 충분할 때까지 여러 번 |
  | 근거 평가 | 없음 또는 고정 규칙 | 에이전트가 평가 후 질의 수정·재검색 |
  | 도구 | 벡터 저장소 | 웹 검색, DB, 코드 실행 등 여러 도구 |
  | 비용·지연 | 낮음 | 높음(딥리서치 질의 하나에 10분 이상, 다중 에이전트는 대화의 약 15배 토큰) |
  - 주의: 질의 재작성·관련성 확인은 Li·Liang 외가 비(非)agentic 파이프라인에도 넣는다. 결정적 차이는 "누가 결정하고 몇 번 도느냐"(06).
- **같은 방법, 다른 이름**: Adaptive-RAG는 Singh에서 agentic, Liang에서 System 1(미리 정한 추론), Li에서 추론 강화 RAG. CRAG도 Singh은 agentic, Liang은 System 1 반복형. 용어 경계가 아직 합의되지 않았다(06).
- **Liang 외의 두 갈래**: 미리 정한 추론(System 1: 경로·반복·트리·혼합 모듈) vs 에이전트 추론(System 2: 프롬프트 기반 ReAct·Search-o1, 학습 기반 Search-R1 등)(06).

## 강연에 쓸 만한 포인트
- **숫자 (원문 확인)**:
  - ReAct 오류 분석(HotpotQA 200건): CoT 실패의 56%가 환각, ReAct는 0%. 다만 ReAct 단독 EM은 CoT보다 낮고(27.4 vs 29.4), 둘을 결합할 때 가장 높다(35.1)(02).
  - Adaptive-RAG: 질문당 시간 무검색 0.35초, 1회 검색 3.08초, 다단계 27.18초 — 반복 검색은 비싸다(03).
  - CRAG: PopQA 50.5 → 54.9, Self-RAG 54.9 → Self-CRAG 61.8(03).
  - Search-R1(7B, 7개 QA 평균 EM): 0.431 vs RAG 0.304. 초록의 향상률은 판본마다 41%/24%로 다르므로 인용 시 판본 명시(05).
  - Anthropic: 다중 에이전트가 단일 에이전트보다 내부 평가 90.2% 높음, BrowseComp 성능 분산의 80%를 토큰 사용량이 설명(05).
- **주의점**:
  - 인용 정확도: 딥리서치류의 인용 정확도는 40~80%이고, 제시한 출처가 뒷받침하지 않는 문장이 상당하다(DeepTRACE, 초록만 확인)(05). 연구에 쓸 때 원문 대조는 사람 몫.
  - Singh 서베이 스스로 "agentic RAG가 늘 기본값은 아니다", "검색 품질이 여전히 병목"이라고 정리(04).
  - 비용·지연: 단순 질문엔 기존 RAG나 무검색이 낫다(Adaptive-RAG 결과)(03).
- **슬라이드 구성안 (강연자 제안, 한 장)**: 정의 + 그림 하나. 그림 후보:
  1. 기존 RAG(질문 → 검색 1회 → 생성)와 Agentic RAG(계획 → 검색 → 근거 평가 → 질의 수정 → 재검색 … → 답) 비교 도식. 8번 AI 에이전트 그림의 Plan → Act → Verify와 같은 색·형식으로.
  2. 계보 타임라인(2020 RAG → 2023 Naive/Advanced/Modular → 2023~24 적응형 검색 → 2025 Agentic RAG·Search-R1·딥리서치).
  학술적 접근이라면 1번 도식 + 노트에 계보, 또는 1번 그림 아래 한 줄 타임라인.

## 원본 그림
- Gao 외 Fig. 3 (Naive·Advanced·Modular 비교): https://arxiv.org/html/2312.10997v5/images/RAG_FrameCompre_eng.png (01)
- Gao 외 Fig. 5 (반복·재귀·적응형 검색): https://arxiv.org/html/2312.10997v5/images/aug_process.png (01)
- Singh 외 분류 지도: https://arxiv.org/html/2501.09136v4/images/taxonomy.png (04)
- Liang 외 Fig. 1 (System 1 vs System 2): https://arxiv.org/html/2506.10408v1/high_level_description.png (06)
- Lewis 외 Fig. 1 (RAG 구조): https://arxiv.org/html/2005.11401v4/RAG-Architecture.svg (01)

## Claude Code와의 연결점
- Claude Code의 탐색은 벡터 색인이 아니라 패턴 검색(Grep·Glob, 또는 Bash의 grep·find)을 루프 안에서 반복하는 방식이다(공식 도구 문서 확인). "벡터 DB 대신 agentic search를 택했다"는 Boris Cherny 발언은 2차 보도로만 확인(01).
- 강연자 해석: Claude Code가 파일을 찾고, 읽고, 부족하면 다시 찾는 것이 곧 agentic RAG의 실천 형태다. 8번 그림으로 보면 검색은 Tools 중 하나이고, Plan → Act → Verify 루프가 검색 횟수와 질의를 정한다. 9번 도메인 그림의 Data(모니터링 DB)를 connector로 반복 조회하는 것도 같은 구조.
