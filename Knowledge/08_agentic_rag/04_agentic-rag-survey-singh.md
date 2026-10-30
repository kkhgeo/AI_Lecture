# Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG (Singh 외 서베이: 정의·에이전트 패턴·아키텍처 분류)

- **저자/기관**: Aditi Singh(Cleveland State University), Abul Ehtesham(Kent State University), Saket Kumar(Northeastern University, Khoury College), Tala Talaei Khoei(Northeastern University, Roux Institute), Athanasios V. Vasilakos(University of Agder, Center for AI Research). Vasilakos는 v4에서 추가됨(v1~v3은 앞의 4인).
- **발행일**: arXiv v1 2025-01-15, v2 2025-02-03, v3 2025-02-04, v4 2026-04-01 (2026-10-23 열람, v4 HTML 전문 확인)
- **URL**:
  - arXiv 초록: https://arxiv.org/abs/2501.09136
  - v4 HTML(이 노트의 근거): https://arxiv.org/html/2501.09136v4
  - 저자 GitHub: https://github.com/asinghcsu/AgenticRAG-Survey
- **자료 유형**: 논문(서베이). arXiv 프리프린트. 학회·저널 게재 정보는 확인되지 않음(arXiv 페이지에 journal-ref·comments 없음, 웹 검색에서도 게재처를 찾지 못함).

## 핵심 요약
- **문제 설정**: LLM은 정적 학습 데이터에 묶여 있고, RAG가 추론 시점에 외부 지식을 붙여 이를 보완한다. 그러나 전통적 RAG(traditional RAG)는 정적이고 선형적인 파이프라인이라 다단계 추론(multi-step reasoning)과 반복적 답변 개선에 약하다고 본다.
- **Agentic RAG의 정의(서론)**: 자율 에이전트(autonomous agents)를 RAG 파이프라인 안에 넣어, 검색을 동적으로 하고 맥락을 반복해서 다듬고 워크플로를 상황에 맞게 조율하는 방식. 저자들은 이를 "명시적인 제어 계층(control layer)"으로 설명한다. 이 계층이 언제 검색할지, 질의를 어떻게 고쳐 쓸지, 증거가 충분히 모였는지를 결정한다.
- **RAG 패러다임의 진화**: Naïve RAG(키워드 검색, TF-IDF·BM25) → Advanced RAG(dense 검색, 재순위화, multi-hop) → Modular RAG(교체 가능한 모듈, 하이브리드 검색, 도구·API 통합) → Graph RAG(그래프 구조로 관계 추론) → Agentic RAG(자율 의사결정, 반복 개선, 워크플로 최적화). 앞의 세 단계 구분은 Gao 외(2023, arXiv 2312.10997) 서베이를 따른다.
- **에이전트 구성요소(Fig. 7)**: LLM(역할·과업 부여), 메모리(단기·장기), 계획(reflection·self-critique 포함), 도구(벡터 검색, 웹 검색, API 등).
- **4가지 에이전트 패턴(agentic patterns)**: Reflection, Planning, Tool Use, Multi-Agent collaboration. 출처는 저자들의 2024년 IEEE AIIoT 논문과 DeepLearning.AI(The Batch) 글이다.
- **5가지 워크플로 패턴(agentic workflow patterns)**: Prompt chaining, Routing, Parallelization(sectioning·voting), Orchestrator-workers, Evaluator-optimizer. **Anthropic "Building effective agents"(2024)를 [13]으로, LangGraph workflows 튜토리얼을 [31]로 명시적으로 인용한다**(§4 전체와 §4.1~4.5 각각). v3에서도 같은 Anthropic 글을 참고문헌에 올려 두었다.
- **아키텍처 분류(taxonomy, §5)**: 단일 에이전트 라우터, 다중 에이전트, 계층형, 교정형(Corrective), 적응형(Adaptive), 그래프 기반(Agent-G, GeAR), 에이전트형 문서 워크플로(ADW). v4에서는 이 분류를 네 가지 설계 축으로 정리했다고 밝힌다: 에이전트 수(agent cardinality), 제어 구조(control structure), 자율성(autonomy), 지식 표현(knowledge representation). Table 3이 이를 지연시간·공학적 복잡도 같은 trade-off와 함께 정리한다.
- **v4에서 새로 보강된 부분(§10 교훈)**: Agentic RAG가 항상 기본값은 아니다(단순 질의는 modular RAG로 충분). 검색 품질이 여전히 주된 병목이다. 자율성에는 명시적 제약(계획 범위, 도구 접근 정책, 정지 기준)이 필요하다. 평가는 결과만이 아니라 과정(process)을 봐야 한다.
- **응용(§7)**: 고객지원(Twitch 광고 영업, Amazon Bedrock), 의료(환자 사례 요약), 법률(계약 검토), 금융(자동차 보험 청구), 교육(연구 논문 보고서 생성), 그래프 기반 멀티모달(시장 조사). 대부분의 사례 출처가 LlamaIndex·AWS 블로그와 데모 노트북이며 동료심사 연구가 아니다.
- **과학·환경 분야**: 독립된 응용 절은 없다. 환경 관련 내용은 예시 질의로만 나온다. §2.4에는 건조 지역 소규모 농업의 지속가능한 관행, 유럽 재생에너지 정책이 개발도상국에 주는 교훈 같은 질의가 있고, §5.2 다중 에이전트 사례는 유럽 재생에너지 도입의 경제·환경 영향을 묻는다. 주의: 이 사례들의 "Integrated Response"에 나오는 수치(온실가스 20% 감소, 일자리 120만 개 등)는 인용 출처가 없는 설명용 예시 답변이다. 사실로 인용하면 안 된다.
- **과제(§12)**: 에이전트 조율과 창발 행동, 출력 품질을 넘어서는 평가 방법론, 메모리 관리와 장기 적응, 계산 비용·효율·지속가능성, 안전·신뢰·거버넌스, 도메인 간 일반화.

## 핵심 개념·용어 정의
- **Traditional RAG (Singh 외 용법)**: 검색 → 증강 → 생성이 고정된 순서로 한 번 지나가는 파이프라인. 맥락 통합, 다단계 추론, 확장성·지연시간이 한계로 꼽힌다(§2.4). Table 2는 워크플로 조율이 "없음(Absent)"이라고 적는다.
- **Agentic RAG (Singh 외)**: RAG 파이프라인에 자율 에이전트를 넣어 검색 전략을 동적으로 관리하고, 맥락을 반복해서 다듬고, 워크플로를 적응시키는 시스템. 핵심 특징은 자율적 의사결정, 반복 개선(feedback loop), 워크플로 최적화 세 가지(§2.3.5).
- **Reflection**: 에이전트가 자기 출력을 비평하고 그 피드백을 다음 반복에 반영한다. 단위 테스트나 웹 검색 같은 외부 도구로 검증할 수도 있다(Self-Refine, Reflexion, CRITIC 인용).
- **Planning**: 복잡한 과업을 하위 과업으로 스스로 쪼갠다. 저자들은 Reflection보다 결과 예측이 어렵다고 적었다.
- **Tool Use**: 외부 도구·API·계산 자원을 호출한다. 도구가 많을 때 어떤 도구를 고르느냐가 남은 과제다.
- **Multi-Agent**: 전문화된 에이전트들이 각자의 메모리와 워크플로를 가지고 중간 결과를 공유한다. 저자들은 이 패턴이 Reflection·Tool Use보다 예측 가능성이 낮다고 평가한다.
- **Single-Agent Agentic RAG (Router)**: 한 에이전트가 질의를 분석해 Text-to-SQL, 의미 검색, 웹 검색, 추천 시스템 중 알맞은 지식원을 고른다. 단순하고 지연시간이 낮지만 다영역 추론에 약하다.
- **Multi-Agent Agentic RAG**: 조정 에이전트가 SQL·의미 검색·웹·추천 등 전문 검색 에이전트에 질의를 나눠 주고 병렬로 검색한 뒤 LLM이 종합한다.
- **Hierarchical Agentic RAG**: 상위 에이전트가 질의를 평가해 하위 에이전트에 위임하고, 결과를 모아 종합한다. 신뢰도가 높은 출처를 우선시하는 전략적 판단이 가능하다. 근거 문헌으로 Ravuru 외 "Agentic RAG for time series analysis"(arXiv 2408.14484)를 든다.
- **Agentic Corrective RAG**: 문맥 검색, 관련성 평가, 질의 재작성, 외부 지식 검색(웹), 답변 종합의 5개 에이전트로 구성된다. 관련성 기준을 넘지 못한 문서가 나오면 교정 단계가 작동한다. CRAG(Yan 외 2024)와 LangGraph 튜토리얼에 근거한다.
- **Adaptive Agentic RAG**: 작은 언어모델 분류기가 질의 복잡도를 예측해 검색 생략, 1회 검색, 다단계 검색 중 하나를 고른다. Adaptive-RAG(Jeong 외 2024)에 근거한다.
- **Graph-Based Agentic RAG**: Agent-G는 그래프 지식베이스와 비정형 문서를 함께 쓰고, critic 모듈과 피드백 루프를 둔다. GeAR는 BM25 같은 기본 검색기에 그래프 확장(graph expansion)을 더하고 에이전트가 검색 경로를 고른다.
- **Agentic Document Workflows (ADW)**: LlamaIndex가 제안한 개념. 문서 파싱 → 상태 유지 → 지식 검색 → 에이전트 조율(업무 규칙 적용) → 구조화된 출력으로 이어진다. 예시는 송장 지급 추천 보고서.

## 강연에 쓸 만한 포인트
- **한 문장 정의 슬라이드**: 전통 RAG는 "한 번 찾고 한 번 답하는" 고정 파이프라인이다. Agentic RAG는 그 위에 "언제 찾을지, 무엇을 다시 찾을지, 이 정도면 충분한지"를 판단하는 제어 계층(에이전트)을 얹은 것이다(Singh 외 서론의 설명을 강연자가 요약).
- **패턴 두 층 구분**: 개별 에이전트의 행동 패턴 4가지(reflection, planning, tool use, multi-agent)와 시스템 수준의 워크플로 패턴 5가지(prompt chaining 등)를 이 서베이가 구분해 정리한다. 후자는 Anthropic "Building effective agents"에서 온 용어이고 서베이도 그렇게 인용한다. 강연에서 Anthropic 글(03_coding_agents 폴더)과 바로 연결할 수 있다.
- **분류표 슬라이드(Table 3 요약)**: 단일 에이전트는 지연시간 낮음·공학 복잡도 낮음 / 다중 에이전트는 확장성 높음·조율 부담 있음 / 계층·교정형은 신뢰성 높음·지연시간 높음 / 그래프·문서 중심은 관계 추론 강함·지식(그래프) 품질에 민감. 연구소 청중에게는 "어떤 구조가 정답인지보다 과업 복잡도에 맞추는 것이 중요하다"는 결론(§13)이 유용하다.
- **"항상 agentic이 답은 아니다"(§10.1)**: 단순 사실 검색은 modular RAG로 충분하다. agentic 설계는 과업 복잡도에 따라 선택적으로 쓰라는 권고. 환경 데이터처럼 정형 DB와 보고서가 섞인 경우에는 Single-Agent Router(Text-to-SQL + 문서 검색) 정도가 현실적인 출발점이라는 식으로 연결할 수 있다(강연자 해석).
- **검색 품질이 먼저(§10.3)**: 에이전트를 붙이기 전에 색인과 검색 파이프라인부터 튼튼히 하라는 조언. 인용(1개): "Agentic reasoning cannot compensate for consistently poor retrieval." — Singh 외 (arXiv 2501.09136v4, §10.3)
- **자율성에는 울타리가 필요(§10.4)**: 계획 범위 제한, 도구 접근 정책, 명시적 정지 기준. 코딩 에이전트의 권한 모드와 같은 논리로 설명할 수 있다.
- **비판적으로 읽을 점**: (1) 응용 사례 대부분이 벤더 블로그·데모 노트북에 근거한다. (2) 예시 답변 속 수치는 설명용이며 출처가 없다. (3) 아키텍처 범주의 근거가 Weaviate·LangGraph 블로그와 튜토리얼에 많이 기대고 있다. (4) arXiv 프리프린트이며 게재처가 확인되지 않는다. 대학원생에게 "서베이도 출처를 확인하며 읽어야 한다"는 사례로 쓸 수 있다.

## 원본 그림
v4 HTML 이미지(모두 HTTP 200 확인, 2026-10-23):
- Fig. 1 "An Overview of Agentic RAG"(전체 개요 지도: 프레임워크, RAG 패러다임, 에이전트 구성요소, 4가지 패턴, 5가지 워크플로, 분류 8종, 한계·장점): https://arxiv.org/html/2501.09136v4/images/taxonomy.png
- Fig. 2 RAG 핵심 구성요소: https://arxiv.org/html/2501.09136v4/images/rag_component.png
- Fig. 7 AI 에이전트 구성요소: https://arxiv.org/html/2501.09136v4/images/ai_agents.png
- Fig. 16 Single-Agent Agentic RAG: https://arxiv.org/html/2501.09136v4/images/single_agentic_RAG.png
- Fig. 17 Multi-Agent Agentic RAG: https://arxiv.org/html/2501.09136v4/images/multiagent_agentic_rag.png
- Fig. 18 Hierarchical Agentic RAG: https://arxiv.org/html/2501.09136v4/images/hierarchical_agentic_rag.png
- Fig. 19 Agentic Corrective RAG: https://arxiv.org/html/2501.09136v4/images/agentic_corrective_rag.png
- Fig. 20 Adaptive Agentic RAG: https://arxiv.org/html/2501.09136v4/images/adaptive_rag_agent.png
- Fig. 23 Agentic Document Workflows: https://arxiv.org/html/2501.09136v4/images/agentic_doc_workflow.png
- 그 밖의 그림(같은 경로 규칙): naive_rag.png, advanced_rag.png, modular_rag.png, graph_rag.png, agentic_self_reflection.png, agentic_planning.png, agentic_tool_use.png, multi_agent_pattern.png, prompt_chaining.png, routing.png, parallelization.png, orchestrator_worker.png, evaluator_optimizer.png, agent_g.png, gear_overview.png
- 슬라이드 사용 메모: Fig. 1은 정보량이 많아 한 장에 그대로 넣으면 글자가 작다. 가운데 "Agentic RAG" 박스(에이전트 구성요소, 패턴, 워크플로)만 잘라 쓰거나 다시 그리는 편이 낫다. 라이선스는 arXiv 비독점 배포 라이선스이므로 슬라이드에 쓸 때 출처를 표기해야 한다.

## Claude Code와의 연결점 (또는 다른 도구와의 비교점)
이 절은 모두 강연자 해석이다.
- 서베이의 에이전트 구성요소(LLM + 메모리 + 계획 + 도구, Fig. 7)는 강연의 프레임 "AI agent = LLM + harness(메모리·skills·도구)"와 거의 그대로 겹친다. Agentic RAG는 이 에이전트의 도구 상자 안에 "검색"이 들어간 특수한 경우로 설명할 수 있다.
- Corrective RAG의 흐름(검색 → 관련성 평가 → 질의 재작성·추가 검색 → 종합)은 강연의 plan → act → verify 루프를 검색 과업에 적용한 것이다. 이때 verify 단계가 "검색된 증거가 질문에 맞는가"를 판정한다.
- Claude Code가 코드베이스에서 파일을 찾고(Grep·Glob), 읽고(Read), 웹을 검색하고(WebSearch·WebFetch), 결과를 보고 다시 찾는 과정은 Single-Agent Router가 지식원을 고르고 반복 검색하는 구조와 닮았다. 다만 Claude Code가 내부적으로 어떤 검색 방식을 쓰는지는 이 서베이가 다루지 않는다.
- 서베이가 말하는 "자율성에는 명시적 제약이 필요하다"(§10.4)는 Claude Code의 권한 모드, 도구 허용 목록, Plan 모드 같은 장치와 같은 문제의식이다.
- 워크플로 패턴 5가지가 Anthropic 글에서 왔으므로, 코딩 에이전트 편에서 소개한 Anthropic 패턴을 RAG 편에서 다시 불러와 "같은 설계 어휘가 검색 시스템에도 쓰인다"고 이어 갈 수 있다.