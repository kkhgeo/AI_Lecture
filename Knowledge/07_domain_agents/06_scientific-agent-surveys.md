# 과학 에이전트 서베이 3편: 도메인 특화 에이전트의 정의·구성요소·자율성 단계 (Scientific agent surveys)

- **저자/기관**: 복수 출처
  - Shuo Ren, Can Xie, Pu Jian, Zhenjiang Ren, Chunlin Leng, Jiajun Zhang — 중국과학원 자동화연구소(CASIA) 등
  - Tianshi Zheng, Zheye Deng, Hong Ting Tsang, Weiqi Wang, Jiaxin Bai, Zihao Wang, Yangqiu Song — 홍콩과기대(HKUST) 컴퓨터공학과
  - Xinming Wang 외 15명 — 중국과학원(CAS)
- **발행일**: 출처별로 아래 표기 (2026-10-23 열람)
- **URL**:
  - Ren et al., "Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents", arXiv 2503.24047 (v1 2025-03-31, v2 2025-04-17, v3 2026-02-02; 본 노트는 v3 HTML 본문 기준): https://arxiv.org/abs/2503.24047 , https://arxiv.org/html/2503.24047v3
  - Zheng et al., "From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery", EMNLP 2025 Main (2025-11, pp. 17733–17750; arXiv 2505.13259, 2025-05 최초 공개, v3 2025-09-17): https://arxiv.org/html/2505.13259v3 , https://aclanthology.org/2025.emnlp-main.895/ , 저장소: https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery
  - Wang et al., "The Hitchhiker's Guide to Autonomous Research: A Survey of Scientific Agents", TechRxiv (2025-08, DOI 10.36227/techrxiv.175459840.02185500/v1): https://doi.org/10.36227/techrxiv.175459840.02185500/v1 (주의: TechRxiv 원문은 403으로 열리지 않음. infoDOCKET 소개 글(2025-08-18)의 초록 요약만 확인 — https://www.infodocket.com/2025/08/18/research-article-preprint-the-hitchhikers-guide-to-autonomous-research-a-survey-of-scientific-agents/)
- **자료 유형**: 논문(서베이)

## 핵심 요약
- **Ren et al. (2025, arXiv 2503.24047)**: 과학 에이전트(scientific agent)를 가설 생성, 실험 설계, 데이터 분석, 시뮬레이션 같은 연구 작업을 자동화하는 LLM 기반 에이전트로 본다. 초록과 서론에서 범용 LLM 에이전트와의 차이를 직접 대비한다. 범용 에이전트는 대화나 코딩 보조처럼 넓은 용도에 맞춰져 있고, 과학 에이전트는 (1) 도메인 지식을 통합하고, (2) 소프트웨어 API·시뮬레이터·분석 도구·실험 장비를 통해 행동하며, (3) 수치 데이터, 분자 구조, 생물 서열 같은 이질적 과학 데이터를 다루고, (4) 검증 메커니즘을 갖춘다는 것이다.
- **구조 4요소 (Ren et al.)**: Planner(계획기), Memory(기억), Action Space(행동 공간, 도구 집합), Verifier(검증기). Planner가 질의를 하위 작업으로 쪼개고, Memory에서 맥락을 불러오고, Action Space로 실행하면, Verifier가 결과를 확인하고 Memory에 저장한 뒤 검증될 때까지 다시 계획한다(Figure 1). 결론부에서 저자들은 이 네 요소의 통합된 관점이 과학 에이전트를 범용 시스템과 구분 짓는다고 정리한다.
- **세부 분류 (Ren et al.)**:
  - Planner — 프롬프트 기반(P1 지시·스키마형, P2 맥락 보강형, P3 숙고·성찰형, P4 탐색형(ToT, MCTS 등), P5 역할·다중에이전트형, P6 코드·DAG 합성형)과 학습 기반(L1 SFT·도메인 학습, L2 RL·선호 최적화).
  - Memory — M1 대화·세션 이력, M2 외부 지식베이스(RAG, 문헌 DB, 지식그래프, API), M3 모델 파라미터에 내재된 지식.
  - Action Space — T1 도구 사용·환경 제어, T2 검색·정보 검색, T3 코드 생성·실행, T4 LLM 추론 자체. 도구 중 하나로 단백질 구조 예측 같은 "도메인 AI 모델을 도구로(domain models as tools)" 호출하는 범주를 따로 둔다. 범용 LLM은 추론 엔진, 도메인 모델은 호출 대상이라는 역할 분담이다.
  - Verifier — V1 자기 교정·성찰, V2 다중 에이전트 비평, V3 사람 개입(전문가 감독), V4 도구·계산 기반 검증(시뮬레이터, 계산 결과로 확인).
- **응용 분류 (Ren et al.)**: 화학·재료, 생명·의생명, 물리·공학, 천문, 지구·환경·기후, ML·데이터과학, 문헌 리뷰·메타연구의 7개 영역. 지구·환경·기후 영역 예시로 GeoAgent(지리공간 코드 생성), GeoMap-Agent(지질도 해석), MineAgent(원격탐사 광물 탐사), LLM-Find(지리공간 데이터 검색), GeoSim.AI(지반역학 시뮬레이션 설정), PANGAEA GPT(지구과학 데이터 상호작용), Earth-Agent(지구관측 시공간 추론), ClimateGPT(검색 기반 기후 질의응답)를 든다. 서론은 40개 이상의 도메인 벤치마크를 다룬다고 밝힌다.
- **열린 과제 (Ren et al.)**: 분야 간 일반화가 약하고 새 데이터에 적응하지 못하는 정적 모델, 과학 벤치마크 대비 출력 검증 부족, 끝단 결과만 보는 정적 벤치마크가 단계별 실패를 가리는 문제, 분야마다 다른 평가지표, 도구 가용성·시뮬레이터 충실도·계산 비용이 도구 기반 검증을 제한하는 문제, 전문가 검증의 병목과 주관성. 윤리 절은 자율성(사람 감독 아래의 제한된 도구로 둘 것), 투명성(검색 로그·스크립트·중간 결과 등 전체 실행 기록 보존), 환각, 보안(프롬프트 인젝션, 지식그래프 오염, 다중 에이전트 통신의 데이터 유출), 편향, 책임(최종 책임은 사람), 지식재산·연구윤리(출처 메타데이터)를 다룬다. 재현성은 투명성·결론 절에서 반복해 강조된다.
- **Zheng et al. (EMNLP 2025)**: 과학적 방법을 6단계(관찰·문제 정의 → 가설 → 실험·데이터 수집 → 분석·해석 → 결론 → 반복·개선)로 보고, LLM의 역할을 자율성에 따라 3단계로 나눈다(Table 1).
  - Level 1 **Tool**: 사람이 과제를 명시적으로 배정하고, LLM은 한 단계 안의 정해진 작업(문헌 요약, 원고 초안, 코드 생성, 데이터 형식 변환)을 자동화한다. 흐름은 단순·정적.
  - Level 2 **Analyst**: 사람이 문제를 정의하고 결과를 검증하며, LLM은 데이터 모델링·분석 에이전트로 목표 지향적으로 여러 작업을 이어서 수행한다. 예: DS-Agent, LLM-SR(방정식 발견), MLAgentBench.
  - Level 3 **Scientist**: 사람 개입은 최소이고, LLM이 가설 수립부터 실험, 분석, 결론, 새 질문 제안까지 여러 단계를 가로지르며 개방형으로 탐색한다. 예: Agent Laboratory, The AI Scientist(v1, v2).
  - 향후 과제로 완전 자율 연구 주기, 실험실 로봇 자동화, 투명성·해석가능성, 지속적 자기개선, 윤리·사회적 정렬을 든다.
- **Wang et al. (TechRxiv 2025)** (주의: 초록 요약만 확인): AI와 자연과학 사이의 간극 때문에 도메인 특화 과학 에이전트를 설계·학습·검증하기 어렵다는 문제의식에서 출발한다. 표준 과학 워크플로를 축으로 구축 방법, 능력 강화, 평가를 정리하고, 기존 에이전트를 구축 전략과 능력 범위로 분류하며, "처음부터 구축하기 → 특정 능력 강화하기"의 2단 프레임을 제안한다. 범용 에이전트에서 목표 지향 과학 에이전트로의 진행을 그린다고 소개된다. **Assistant / Partner / Avatar 3단계는 원문에서 확인하지 못했다**(소개 글에는 없음, 다른 서베이의 인용이라는 검색 요약만 존재).

## 핵심 개념·용어 정의
- **과학 에이전트 (scientific agent, Ren et al.)**: 도메인 지식, 전문 도구 집합, 검증 메커니즘을 통합해 가설 생성·실험 설계·데이터 분석·시뮬레이션을 자동화하는 LLM 기반 에이전트.
- **범용 에이전트 (general-purpose LLM agent)**: 대화나 코딩 보조처럼 넓은 용도에 최적화된 에이전트(Ren et al.의 대비 표현).
- **Planner / Memory / Action Space / Verifier**: Ren et al.의 4요소. 이 노트에서 "도구 집합"이라 부르는 것은 논문의 Action Space에 해당한다.
- **Domain models as tools**: 단백질 구조 예측, 분자 물성 예측 같은 전문 모델을 에이전트가 함수처럼 호출하는 방식. LLM은 판단과 조율을 맡는다.
- **Tool / Analyst / Scientist (Zheng et al.)**: 사람이 과제를 배정하는 단계 → 사람이 문제를 정의하고 결과만 검증하는 단계 → 사람 개입이 최소인 단계.
- **도메인 특화 에이전트 — 강연용 한 문장 정의 (강연자 종합)**: "범용 에이전트의 루프(계획–도구 실행–관찰)에 특정 분야의 지식, 전문 도구, 데이터 형식, 검증 절차를 결합해, 그 분야의 결과를 그 분야의 기준으로 확인하며 작업하는 LLM 에이전트." 근거: Ren et al. 초록·서론(지식·도구·데이터·검증)과 Verifier 분류(V1–V4), 결론부의 4요소 통합 관점. "가드레일"은 Ren et al. 윤리 절(사람 감독, 실행 기록, 보안)에서 가져온 강연자 정리이며, 논문이 이 단어를 정의 요소로 쓰지는 않는다.

## 강연에 쓸 만한 포인트
- 비교표 슬라이드 (Ren et al. 기반, 강연자 재구성):
  | 항목 | 범용 에이전트 | 도메인 특화(과학) 에이전트 | Ren et al. 근거 |
  |---|---|---|---|
  | 지식 | 사전학습 지식 + 웹 검색 | 도메인 DB·지식그래프·문헌 RAG, 도메인 학습 모델 | M2, M3, 초록 |
  | 도구 | 파일·셸·브라우저 | 시뮬레이터, 과학 API, 도메인 모델, 실험 장비 | Action Space T1–T4 |
  | 데이터 | 텍스트·코드 | 수치 데이터, 분자 구조, 서열, 공간자료 | 서론 |
  | 검증 | 테스트 통과, 사람 리뷰 | 계산·시뮬레이션 검증, 전문가 검토, 다중 에이전트 비평 | Verifier V1–V4 |
  | 가드레일 | 권한·샌드박스 | 사람 감독, 실행 기록·재현성, 데이터 출처, 보안 | 윤리 절 |
- 자율성 사다리 슬라이드 (Zheng et al. Table 1): Tool → Analyst → Scientist. 각 칸에 "누가 문제를 정하나 / 누가 결과를 검증하나"를 적으면 청중이 바로 이해한다. 연구소 업무 대부분은 Level 1–2에 있다는 점을 짚는다(강연자 해석).
- 환경연구소 청중용 예시: Ren et al.의 지구·환경·기후 응용 목록(GeoAgent, Earth-Agent, ClimateGPT, PANGAEA GPT 등). 우리 분야에도 이미 별도 범주가 있다는 근거로 쓴다.
- 메시지: 도메인 에이전트를 만드는 일은 모델을 새로 학습하는 일보다 지식·도구·검증을 붙이는 일에 가깝다. Ren et al.의 Memory(M2)와 Action Space가 그 접점이다(강연자 해석).
- 인용(1개): "This integrated perspective distinguishes scientific agents from general-purpose systems." — Ren et al., 결론 (arXiv 2503.24047v3)

## 원본 그림
- Ren et al. Figure 1 (과학 에이전트 구조: Planner·Memory·Action Space·Verifier): https://arxiv.org/html/2503.24047v3/architecture.png (접속 확인)
- Ren et al. 세부 그림: https://arxiv.org/html/2503.24047v3/prompt_planner.png , https://arxiv.org/html/2503.24047v3/learned_planner.png , https://arxiv.org/html/2503.24047v3/memory.png , https://arxiv.org/html/2503.24047v3/action_space_v1.png , https://arxiv.org/html/2503.24047v3/verifier.png
- Zheng et al. Figure 1 (과학적 방법 단계별 LLM 응용): https://arxiv.org/html/2505.13259v3/scimethodv2.svg
- Zheng et al. Figure 2 (연구 분류 체계): https://arxiv.org/html/2505.13259v3/survey_new.svg
- Zheng et al. Table 1 (3단계 자율성 표)은 이미지가 아니라 HTML 표이므로 슬라이드용으로 다시 그려야 함.
- Wang et al.(TechRxiv): 원문 미열람, 그림 없음.

## Claude Code와의 연결점
- Claude Code는 Ren et al.의 4요소에 대응시켜 설명할 수 있다. Plan 모드·작업 분해는 Planner, CLAUDE.md·대화 이력·파일은 Memory(M1·M2), 셸·파일 편집·MCP 서버는 Action Space, 테스트 실행과 사람의 diff 리뷰는 Verifier(V4·V3)다(강연자 대응).
- 범용 코딩 에이전트를 도메인 에이전트로 바꾸는 손잡이도 같다. 도메인 지식은 CLAUDE.md·skill 문서로, 전문 도구는 MCP 서버나 스크립트(예: 기상·수질 데이터 API, 모델 실행기)로, 검증은 단위 검사·물리적 범위 검사·기준 데이터 비교를 hook이나 테스트로 넣는 식이다(강연자 해석).
- Zheng et al.의 사다리에서 Claude Code를 연구 분석에 쓰는 일반적 방식은 Level 2(Analyst)에 해당한다. 사람이 문제를 정의하고 결과를 검증한다는 점에서, 03_coding_agents의 agentic engineering 태도와 같은 이야기다(강연자 해석).
