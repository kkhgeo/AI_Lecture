# 08_agentic_rag 자료 색인

- 수집일: 2026-10-23
- 주제: Agentic RAG — 학술적 계보(RAG 2020 → 적응형 검색 → Agentic RAG → 학습된 검색 에이전트·딥리서치), 정의, 기존 RAG와의 차이 (슬라이드 1장용)
- 수록: 8개 파일
- 저작권: 요약·재서술 중심, 직접 인용은 파일당 1개(15단어 미만)

## 1. 자료 목록

### A. 출발점
| 파일 | 한 줄 설명 |
|---|---|
| 01_rag-origin-and-paradigms.md | Lewis 외 NeurIPS 2020(DPR + BART, 위키 약 2,100만 조각, RAG-Sequence/Token), Gao 외 서베이(Naive·Advanced·Modular, 반복·재귀·적응형 검색, "agentic RAG" 용어는 없음) |

### B. 모델이 검색 시점을 정하는 방법들
| 파일 | 한 줄 설명 |
|---|---|
| 02_react-and-active-retrieval.md | ReAct(ICLR 2023, 생각·행동·관찰, 환각 실패 56% → 0%), FLARE(EMNLP 2023, 낮은 확신에서 검색), IRCoT(ACL 2023, 초록만) |
| 03_self-rag-crag-adaptive-rag.md | Self-RAG(ICLR 2024, 반성 토큰), CRAG(검색 평가기 + 웹 검색 교정), Adaptive-RAG(NAACL 2024, 난이도별 3경로, 질문당 0.35/3.08/27.18초), 비교표 |

### C. Agentic RAG와 그 이후
| 파일 | 한 줄 설명 |
|---|---|
| 04_agentic-rag-survey-singh.md | Singh 외 서베이(2025-01, v4 2026-04): 제어 층으로서의 에이전트, 4가지 에이전트 패턴, 워크플로 5종(Anthropic 인용), 아키텍처 분류, "늘 기본값은 아님" |
| 05_rl-search-agents-and-deep-research.md | Search-R1(COLM 2025, 강화학습, 판본별 수치 차이), OpenAI·Gemini 딥리서치, Anthropic 다중 에이전트 리서치, 인용 정확도 40~80%(초록만) |
| 06_reasoning-rag-surveys.md | Li 외(Findings of EMNLP 2025) 추론⇔검색 3분류, Liang 외(Findings of IJCNLP-AACL 2025) System 1 vs 2, 종합 정의와 기존 RAG 대비표, 같은 방법·다른 이름 |
| 07_synthesis.md | 계보, 강연용 정의, 비교표, 원문 확인 숫자, 주의점, 슬라이드 구성안, Claude Code와의 연결 |

## 2. 슬라이드 연결
- 뼈대: 07번. 정의 한 문장 + 기존 RAG vs Agentic RAG 비교 도식(8번 그림의 Plan → Act → Verify 형식과 통일).
- 9번 도메인 특화 에이전트 그림의 Data·connector와 이어진다: 같은 자료를 한 번 꺼내 쓰는가, 루프 안에서 반복해 찾는가.

## 3. 확인하지 못한 것
- IRCoT 본문(초록만), CRAG의 학회 게재 여부(프리프린트로 처리), ReAct·Self-RAG 학회는 공식 저장소·arXiv 주석으로 확인(OpenReview 접근 불가).
- DeepTRACE·ReportBench(인용 정확도) 본문, R1-Searcher·DeepResearcher 본문.
- Claude Code가 벡터 DB 대신 agentic search를 택했다는 발언의 1차 출처(2차 보도로만 확인).
- Li·Liang의 ACL Anthology 게재본과 arXiv본의 본문 차이.
