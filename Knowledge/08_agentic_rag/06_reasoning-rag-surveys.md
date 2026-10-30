# RAG와 추론을 묶는 2025년 서베이 두 편: Li 외(RAG-Reasoning) · Liang 외(System 1 / System 2) (Agentic RAG의 학술적 정의 정리)

- **저자/기관**:
  - Li 외: Yangning Li, Weizhi Zhang 외 18인(공동 1저자 Li·Zhang). 소속은 Tsinghua University, University of Illinois Chicago, The University of Tokyo, Peking University, UIUC, UCLA, HKUST. 교신 그룹에 Philip S. Yu 포함.
  - Liang 외: Jintao Liang(Beijing University of Posts and Telecommunications), Gang Su(University of Georgia; ACL Anthology에는 "Sugang"으로 표기), Huifeng Lin·You Wu(South China University of Technology), Rui Zhao(SenseTime Research), Ziyue Li(교신저자, Technical University of Munich / University of Cologne).
- **발행일**: (2026-10-23 열람)
  - Li 외: arXiv v1 2025-07-13, v2 2025-07-16. 게재: Findings of ACL: EMNLP 2025(2025년 11월, 중국 쑤저우), pp. 12120–12145. Anthology의 제목은 "A Survey of RAG-Reasoning Systems in Large Language Models"로 arXiv 제목과 다르다.
  - Liang 외: arXiv v1 2025-06-12. 게재: Findings of IJCNLP-AACL 2025(2025년 12월, 인도 뭄바이), pp. 1954–1966. ACL Anthology 페이지에서 직접 확인함.
- **URL**:
  - Li 외 arXiv: https://arxiv.org/abs/2507.09477 (PDF v2 전문 확인, arXiv HTML판 없음)
  - Li 외 ACL Anthology: https://aclanthology.org/2025.findings-emnlp.648/ (DOI 10.18653/v1/2025.findings-emnlp.648)
  - Li 외 논문 목록 저장소: https://github.com/DavidZWZ/Awesome-RAG-Reasoning
  - Liang 외 arXiv: https://arxiv.org/abs/2506.10408 (v1 HTML 전문 확인)
  - Liang 외 ACL Anthology: https://aclanthology.org/2025.findings-ijcnlp.122/ (DOI 10.18653/v1/2025.findings-ijcnlp.122)
- **자료 유형**: 논문(서베이) 2편. 둘 다 동료심사를 거친 ACL 계열 Findings 게재 논문. 이 노트는 arXiv판을 근거로 했다. Anthology 게재판 본문과의 차이는 확인하지 않았다.

## 핵심 요약
### Li 외, "Towards Agentic RAG with Deep Reasoning" (arXiv 2507.09477)
- **출발점**: LLM에는 두 한계가 얽혀 있다. 지식 환각(hallucination)과 복잡한 추론의 어려움이다. 지식이 없으면 추론이 막히고, 추론이 잘못되면 지식을 제대로 쓰지 못한다.
- **세 갈래 구도(Fig. 1, Fig. 2)**:
  1. **Reasoning-Enhanced RAG (Reasoning → RAG, §3)**: 추론으로 RAG 파이프라인의 각 단계를 개선한다. 검색 최적화(추론을 반영한 질의 재작성, 검색 전략·계획, 검색 모델 개선), 통합 개선(관련성 평가·필터링, 정보 종합), 생성 개선(맥락 인지 생성, 근거 기반 생성 통제)으로 나뉜다.
  2. **RAG-Enhanced Reasoning (RAG → Reasoning, §4)**: 검색한 지식으로 추론을 돕는다. 외부 지식 검색(지식베이스, 웹, 도구 사용)과 맥락 내 검색(과거 경험, 예시·학습 데이터)으로 나뉜다.
  3. **Synergized RAG-Reasoning (RAG ⇔ Reasoning, §5)**: 검색과 추론을 번갈아 반복하며 서로를 개선한다. 추론 워크플로(chain·tree·graph 기반)와 에이전트 조율(single-agent, multi-agent)의 두 관점으로 정리한다.
- **앞의 둘(1·2)의 한계**: 저자들은 1·2를 한 방향 개선으로 보고, 둘 다 정적인 "검색 후 추론(Retrieval-Then-Reasoning, RTR)" 틀에 묶여 있다고 본다. 이 틀에는 세 가지 문제가 있다. 미리 검색한 지식이 추론 중 생기는 필요와 어긋날 수 있다(검색의 적절성). 검색된 지식의 오류가 추론을 방해한다(추론 깊이). 추론 중 피드백이나 동적 검색 장치가 없다(적응성).
- **"agentic"이 들어오는 자리**: §5의 synergized 단계다. 초록은 이를 (agentic) LLM이 검색과 추론을 반복적으로 교차시키는 틀로 설명한다. §7은 synergized 시스템의 핵심 특징을 에이전트형 구조로 꼽는다. 추론 단계에서 어떤 에이전트가 어떤 역할을 맡고 어떤 도구나 검색 전략을 부를지 시스템이 스스로 정한다는 뜻이다. OpenAI·Gemini·Perplexity의 "Deep Research" 제품을 대표 사례로 든다.
- **경계 기준(각주 4)**: 추론이 이미 검색된 고정 지식을 한 방향으로 활용하기만 하면 §3(reasoning-enhanced)으로 분류한다. 추론이 새로운 검색을 동적으로 일으키면 §5(synergized)로 분류한다. Agentic RAG를 가르는 실용적 기준으로 쓸 만하다.
- **에이전트 조율(§5.2)**: Single-agent는 prompting(ReAct, Search-o1, Self-Ask, IRCoT), SFT(Toolformer, INTERS), 강화학습(Search-R1, R1-Searcher, DeepResearcher)으로 구현된다. Multi-agent는 분산형(역할별 전문 에이전트)과 중앙집중형(관리자-작업자, 계층형)으로 나뉜다.
- **과제(§7)**: 추론 효율(실제 deep research 질의 하나가 10분 넘게 걸리기도 한다), 검색 효율(예산을 고려한 질의 계획, 캐시), 사람-에이전트 협업, 에이전트 구조와 능력, 멀티모달 검색, 검색 신뢰성(오염된 지식원 공격).
- **과학 분야 언급**: 오픈도메인 QA와 과학적 발견(scientific discovery)을 반복적 검색-추론이 필요한 예로 든다. 도구 사용 사례에 과학 모델링용 SCIAGENT·TRICE(WolframAlpha 같은 기호 계산 도구)가 있다. 환경 분야 사례는 없다.

### Liang 외, "Reasoning RAG via System 1 or System 2" (arXiv 2506.10408)
- **용어**: 정적 파이프라인에서 추론 중심 구조로 옮겨 간 흐름을 묶어 "Reasoning Agentic RAG"라고 부른다. 검색 과정에 의사결정을 넣어 모델이 언제·무엇을·어떻게 검색할지 스스로 정하는 시스템이다(§2.2).
- **두 갈래**:
  - **Predefined reasoning (System 1)**: 사람이 설계한 고정 모듈 파이프라인을 LLM이 따른다(Fig. 1 상단). 세부 유형은 넷이다. Route-based(맥락이나 확신도에 따라 검색 여부 결정: RAGate, Self-Route), Loop-based(반복 피드백: Self-RAG, CRAG), Tree-based(계층 구조 탐색: RAPTOR, MCTS-RAG), Hybrid-modular(라우팅·루프·모듈 결합: Adaptive-RAG, Modular-RAG).
  - **Agentic reasoning (System 2)**: LLM이 능동적 의사결정자가 된다. 지식 공백을 찾고, 질의를 만들고, 검색 엔진·API 같은 도구로 정보를 가져와 풀이에 통합하는 과정을 스스로 반복한다(Fig. 1 하단). 구현은 둘로 나뉜다. Prompt-based(ReAct, Self-Ask, function calling, 대규모 추론 모델(LRM) 활용, Search-o1)와 Training-based(강화학습: Search-R1, R1-Searcher, ReZero, DeepRetrieval, DeepResearcher)다.
- **System 1/2 비유(Table 1)**: 인지과학의 이중 처리 이론에서 빌려 왔다. System 1은 빠르고 구조적이며 예측 가능하지만 설계 범위 밖에서는 유연하지 않다. System 2는 느리고 숙고하며 적응적이다. 저자들은 이를 효율과 적응성 사이의 trade-off로 정리한다.
- **산업 과제(industry challenges)**: 제목에 들어 있지만 별도 절은 없다. 서론에서 세 가지를 든다. 정보가 여러 문서에 흩어진 경우의 종합, 법률·생의학 QA에서 필요한 multi-hop 추론, 표·차트·이미지 같은 멀티모달 입력이다. 기업 인텔리전스·과학 보고서·기술 지원 같은 환경에서 이 문제가 두드러진다고 적었다. Table 2에는 산업용 오픈소스 구현(DeepSearcher, RAGFlow, Haystack, Langchain-Chatchat, LightRAG, R2R, FlashRAG)을 함께 정리했다.
- **향후 과제(§5)**: 도구의 고급 설정 활용(날짜·출처 필터, 구조화 DB 질의), 과정 지향의 세밀한 보상 함수, 검색 효율(불필요한 반복 검색 방지, 충분한 정보가 모였을 때 멈추기), 동적 환경에서의 일반화와 강건성.

## 핵심 개념·용어 정의
- **Retrieval-Then-Reasoning (RTR, Li 외)**: 먼저 검색하고 그 결과로 추론하는 정적 틀. 추론 도중 새로 검색하지 않는다.
- **Synergized RAG-Reasoning (Li 외)**: 추론이 검색을 이끌고, 새로 검색한 지식이 다시 추론을 다듬는 반복적 상호작용. Li 외 서베이에서 Agentic RAG에 해당하는 부분.
- **Reasoning Agentic RAG (Liang 외)**: 검색 과정에 의사결정과 적응적 도구 사용을 넣은 RAG 계열 전체. predefined reasoning과 agentic reasoning을 모두 포함한다.
- **Predefined reasoning / System 1 (Liang 외)**: 검색·추론 단계가 미리 설계되어 있다. 질의 재작성, 문서 검색, 재순위화, 답변 종합이 고정된 제어 논리로 이어진다.
- **Agentic reasoning / System 2 (Liang 외)**: 모델이 추론 상태에 따라 언제·어떻게 도구를 쓸지 결정한다. 프롬프트로 유도하거나 강화학습으로 훈련한다.
- **주의(분류가 서베이마다 다르다)**: 같은 방법이 서베이마다 다른 칸에 들어간다. Adaptive-RAG는 Singh 외에서는 "Adaptive Agentic RAG"이고, Liang 외에서는 predefined(System 1)의 hybrid-modular이며, Li 외에서는 reasoning-enhanced RAG의 검색 전략(한 번의 예측으로 검색 여부를 정하는 방식)이다. CRAG도 Singh 외에서는 agentic 아키텍처(Corrective RAG)이고 Liang 외에서는 predefined loop-based다. "agentic"의 경계가 아직 합의되지 않았다는 증거로 쓸 수 있다.

## 강연에 쓸 만한 포인트
- **System 1 vs System 2 슬라이드**: Liang 외 Fig. 1이 가장 직관적이다. 위쪽은 사람이 그린 순서도를 LLM이 따라가고, 아래쪽은 LLM이 추론하며 도구를 부르고 결과를 받아 다시 추론하는 루프다. "누가 순서도를 그리는가"라는 질문 하나로 전통 RAG와 Agentic RAG의 차이를 설명할 수 있다.
- **Li 외의 화살표 세 개**: Reasoning → RAG, RAG → Reasoning, RAG ⇔ Reasoning. 화살표가 양방향이 되는 지점이 agentic이다.
- **"agentic"을 가르는 시험 질문(강연자 정리, Li 외 각주 4 근거)**: 추론 도중 새 검색이 일어나는가? 그렇다면 agentic 쪽이고, 검색이 한 번 앞에서 끝나면 아무리 정교해도 전통 RAG 쪽이다.
- **비용 감각**: Li 외는 deep research 질의 하나가 10분 넘게 걸릴 수 있다고 적었다. Liang 외의 System 1/2 비유도 결국 속도와 적응성의 trade-off다. 연구소 업무에서 매번 System 2가 필요하지 않다는 메시지로 연결할 수 있다.
- **인용(1개)**: "the model autonomously orchestrates tool interaction during inference" — Liang 외 (arXiv 2506.10408, 초록, agentic reasoning 정의)

### 제안 정의(세 서베이를 종합한 한 문장)
> **Agentic RAG**는 LLM이 추론 과정 안에서 언제·무엇을·어떻게 검색할지 스스로 결정하고, 검색된 증거를 평가하여 질의를 고치거나 다른 도구를 호출하며, 충분한 근거가 모일 때까지 검색과 추론을 반복하는 검색 증강 생성 방식이다.

- 근거: "자율 에이전트가 검색 시점·질의 재작성·증거 충분성을 판단하는 제어 계층"(Singh 외, 서론), "모델이 언제·무엇을·어떻게 검색할지 결정"(Liang 외 §2.2), "추론이 새로운 검색을 동적으로 일으키는 반복적 상호작용"(Li 외 §1·§5, 각주 4).
- 이 문장은 강연자가 세 출처를 종합해 만든 것이며 어느 서베이에도 그대로 나오지 않는다.

### 전통 RAG vs Agentic RAG 비교표
| 항목 | 전통 RAG | Agentic RAG | 근거 |
|---|---|---|---|
| 검색 여부·시점은 누가 정하나 | 설계자가 정한 고정 파이프라인(항상 검색) | LLM(에이전트)이 추론 상태를 보고 결정 | Singh(서론), Liang(§1, §2.2, §4), Li(§7) |
| 검색 횟수 | 보통 1회, 생성 전에 끝남 | 여러 차례, 추론과 교차 | Li(§1 RTR 한계, §5), Singh(§2.3.5, §5.5), Liang(§4) |
| 질의 재작성 | 없거나 고정 모듈로만 존재 | 중간 결과를 보고 에이전트가 다시 씀 | Singh(서론, §5.4), Liang(§4.2 DeepRetrieval) / 주의: Li §3.1.1과 Liang §1은 질의 재작성이 비-agentic 파이프라인에도 있다고 정리 |
| 검색 증거 평가 | 거의 없음(받은 대로 생성에 사용) | 관련성·충분성을 판단해 재검색하거나 멈춤 | Singh(서론, §5.4), Liang(§2.1: 기존 RAG는 충분성 평가 불가) / 주의: Li §3.2는 관련성 평가를 reasoning-enhanced RAG에도 포함 |
| 벡터 저장소 밖의 도구 | 주로 문서·벡터 검색 | SQL, 웹 검색, API, 계산 도구 등 | Singh(§5.1·5.2), Liang(§4.1 function calling, 검색 엔진·API), Li(§4.1.3) |
| 비용·지연시간 | 낮음, 예측 가능 | 높음(반복 검색·다중 에이전트) | Singh(Table 3, §10.1, §12.4), Li(§7, 10분 이상 사례), Liang(Table 1 System 1 빠름 / System 2 느림, §5 검색 효율) |

- 표의 "전통 RAG"·"Agentic RAG" 칸은 강연자가 세 서베이 서술을 요약한 것이다. 근거 칸에 적은 절을 슬라이드 노트에 남겨 둔다.

## 원본 그림
- **Liang 외 (arXiv v1 HTML, 모두 HTTP 200 확인)**:
  - Fig. 1 Predefined vs Agentic Reasoning 개념도(강연용으로 가장 적합): https://arxiv.org/html/2506.10408v1/high_level_description.png
  - Fig. 2 Reasoning Agentic RAG 연구 분포: https://arxiv.org/html/2506.10408v1/reasoning.png
  - Fig. 5 Predefined reasoning 예시: https://arxiv.org/html/2506.10408v1/predefined_reasoning.png
  - Fig. 6 Agentic reasoning 예시: https://arxiv.org/html/2506.10408v1/agentic_reasoning.png
  - Fig. 3 분류 트리는 HTML에서 이미지가 아니라 LaTeX forest로 되어 있어 단독 이미지 URL이 없다. PDF에서 잘라 써야 한다.
- **Li 외 (arXiv HTML판 없음, 저자 GitHub 저장소 이미지)**:
  - 전체 구도(논문 Fig. 1과 같은 그림, 세 갈래와 §5.1·§5.2 하위 구조): https://raw.githubusercontent.com/DavidZWZ/Awesome-RAG-Reasoning/main/Assets/Framework.png
  - 분류 트리(논문 Fig. 2와 같은 그림): https://raw.githubusercontent.com/DavidZWZ/Awesome-RAG-Reasoning/main/Assets/Taxonomy.png
  - 같은 저장소의 RAG_Reasoning.png는 장식용 일러스트이므로 학술 슬라이드에는 쓰지 않는다.
- 두 논문 모두 슬라이드에 쓸 때 출처 표기가 필요하다. 저장소 이미지의 라이선스(저장소는 MIT 배지 표시)가 그림에도 적용되는지는 확인하지 않았다.

## Claude Code와의 연결점 (또는 다른 도구와의 비교점)
이 절은 모두 강연자 해석이다.
- Liang 외의 System 2 루프(추론 → 도구 호출 → 검색 결과 → 다시 추론)는 강연 프레임의 plan → act → verify 루프와 같은 모양이다. 차이는 도구가 "검색"에 집중되어 있다는 점뿐이다.
- 강연의 "AI agent = LLM + harness" 관점에서 보면, predefined reasoning(System 1)은 사람이 harness 안에 순서도를 미리 박아 둔 것이고, agentic reasoning(System 2)은 harness가 도구만 주고 순서는 LLM에 맡긴 것이다. Anthropic "Building effective agents"의 workflow vs agent 구분과도 같은 축이다(03_coding_agents 폴더 참조).
- Claude Code가 Grep·Read로 코드를 찾다가 결과를 보고 검색어를 바꾸거나 다른 파일을 여는 행동은 Li 외 각주 4 기준으로 보면 "추론이 새로운 검색을 일으키는" synergized 유형에 해당한다.
- Li 외가 든 "Deep Research" 제품군과 Liang 외의 DeepResearcher는 강연에서 연구자에게 가장 익숙한 Agentic RAG 사례다. 문헌 조사 자동화를 보여 줄 때 이 계보를 짚어 줄 수 있다.
- 두 서베이 모두 비용·지연시간과 "언제 멈출지"를 미해결 과제로 꼽는다. 이는 코딩 에이전트에서 사람이 정지 기준과 검증 책임을 쥐어야 한다는 강연 메시지와 연결된다.