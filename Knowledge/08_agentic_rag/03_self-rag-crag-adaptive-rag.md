# Self-RAG · CRAG · Adaptive-RAG (검색을 스스로 판단·교정·선택하는 RAG)

- **저자/기관**:
  - Self-RAG: Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi / University of Washington, Allen Institute for AI, IBM Research AI
  - CRAG: Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, Zhen-Hua Ling / University of Science and Technology of China, UCLA, Google DeepMind (Yan·Gu 공동 1저자)
  - Adaptive-RAG: Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang, Jong C. Park / KAIST(전산학부, AI대학원)
- **발행일**: (2026-10-23 열람)
  - Self-RAG: arXiv 2023-10-17. ICLR 2024 (공식 GitHub README에 "ICLR 2024, Oral top 1%"로 표기. OpenReview 페이지는 봇 차단으로 직접 열람하지 못함)
  - CRAG: arXiv v1 2024-01-29, v3 2024-10-07. 학회 게재 정보는 arXiv·GitHub README 어디에도 없음(프리프린트로 취급)
  - Adaptive-RAG: arXiv 2024-03 (v2 HTML 기준 2024-03-28), NAACL 2024 Long Papers (2024년 6월, Mexico City, pp. 7036–7050)
- **URL**:
  - Self-RAG: https://arxiv.org/abs/2310.11511 (본문: https://ar5iv.labs.arxiv.org/html/2310.11511, 프로젝트: https://selfrag.github.io/, 코드: https://github.com/AkariAsai/self-rag)
  - CRAG: https://arxiv.org/abs/2401.15884 (본문: https://arxiv.org/html/2401.15884)
  - Adaptive-RAG: https://aclanthology.org/2024.naacl-long.389/ (DOI 10.18653/v1/2024.naacl-long.389), https://arxiv.org/abs/2403.14403
- **자료 유형**: 논문 (학회: ICLR 2024, NAACL 2024 / 프리프린트: CRAG)

## 핵심 요약
- **Self-RAG**(Self-Reflective Retrieval-Augmented Generation): 하나의 언어모델이 "검색할지 말지", "가져온 문서가 관련 있는지", "내 답이 문서에 근거하는지", "답이 쓸모 있는지"를 특수 토큰으로 스스로 표시하도록 학습시킨 방법이다.
  - 반성 토큰(reflection token) 4종(Table 1): `Retrieve`(yes / no / continue), `IsRel`(relevant / irrelevant), `IsSup`(fully / partially / no support), `IsUse`(5~1점).
  - 학습은 2단계다. (1) GPT-4로 토큰 종류별 4k~20k개 예시에 반성 토큰 라벨을 만들고, 이것으로 비평 모델(critic, Llama 2 7B에서 초기화)을 학습. (2) 비평 모델이 학습 말뭉치에 반성 토큰을 오프라인으로 끼워 넣고, 생성 모델(generator, Llama 2 7B·13B)을 일반적인 다음 토큰 예측으로 학습(지시-응답 쌍 150k개). 생성 모델 학습 중에는 비평 모델이 돌지 않는다.
  - 추론: `Retrieve=yes` 확률이 임계값(대부분 과제에서 0.2)을 넘으면 검색. 검색기는 Contriever-MS MARCO(최대 10개 문서). 구간(segment) 단위 빔 탐색(폭 2)에서 비평 토큰 확률의 가중합(IsRel 1.0, IsSup 1.0, IsUse 0.5)으로 후보를 고르며, 가중치는 재학습 없이 추론 시 조정할 수 있다.
  - 평가: PopQA, TriviaQA, PubHealth, ARC-Challenge, Biography(FactScore), ASQA(인용 포함 장문). 13B 모델이 PubHealth 74.5, PopQA 55.8, ASQA 인용 정밀도 70.3(검색 보강 ChatGPT 65.1)을 기록. 초록 기준으로 7B·13B 모두 ChatGPT와 검색 보강 Llama2-chat보다 여러 과제에서 우수.
- **CRAG**(Corrective Retrieval Augmented Generation): "검색이 실패하면 어떻게 되나?"에서 출발한다. 생성 모델 앞단에 가벼운 검색 평가기(retrieval evaluator)를 두어 검색 결과를 채점하고, 점수에 따라 세 가지 행동 중 하나를 택한다.
  - 평가기: T5-large(0.77B)를 미세조정. 질문과 문서 쌍마다 -1~1 점수를 매김.
  - 세 행동(데이터셋별 상·하한 임계값 사용, 예: PopQA 0.59 / -0.99):
    - **Correct**: 한 문서라도 상한을 넘으면 → 검색 문서를 정제해 사용.
    - **Incorrect**: 모든 문서가 하한 미만이면 → 검색 문서를 버리고 웹 검색으로 대체.
    - **Ambiguous**: 그 밖의 경우 → 정제한 내부 문서와 웹 검색 결과를 함께 사용.
  - 분해 후 재구성(decompose-then-recompose): 문서를 몇 문장 단위의 조각(strip)으로 쪼개 평가기로 각각 채점하고, 관련 없는 조각을 걸러낸 뒤 남은 조각을 순서대로 이어 붙인다.
  - 웹 검색: ChatGPT(GPT-3.5 Turbo)가 질문을 키워드 3개 이내 질의로 바꾸고, Google Search API로 상위 5개 URL을 가져오되 Wikipedia 페이지를 우선한다. 가져온 페이지도 같은 조각 단위 정제를 거친다.
  - 기존 RAG 방법에 덧붙이는 플러그인(plug-and-play) 형태다. PopQA 정확도: LLaMA2-7B 기반 RAG 50.5 → CRAG 54.9, Self-RAG 54.9 → Self-CRAG 61.8. Biography(SelfRAG-LLaMA2-7b 생성기) FactScore: RAG 59.2 → CRAG 74.1.
- **Adaptive-RAG**: 질문의 복잡도를 먼저 분류하고, 그에 맞춰 검색 전략을 고르는 방법이다. 쉬운 질문에 다단계 검색을 돌리면 비용 낭비, 어려운 질문에 단일 검색을 하면 정확도 부족이라는 문제를 겨냥한다.
  - 분류기: T5-Large(770M). 라벨 A(검색 없음), B(단일 단계 검색), C(다단계 검색).
  - 라벨 자동 수집: 무검색으로 맞히면 A, 무검색은 틀리고 단일·다단계가 모두 맞히면 B(더 단순한 방법 우선). 어느 방법도 못 맞힌 질문은 출처 데이터셋 성격을 이용해 단일 홉 데이터셋이면 B, 다중 홉이면 C.
  - 세 경로: 무검색(LLM 단독), 단일 단계(BM25로 한 번 검색 후 답), 다단계(IRCoT 방식으로 검색과 추론 반복).
  - 데이터: 단일 홉 SQuAD v1.1, Natural Questions, TriviaQA / 다중 홉 MuSiQue, HotpotQA, 2WikiMultiHopQA. 모델: FLAN-T5-XL(3B), FLAN-T5-XXL(11B), GPT-3.5(gpt-3.5-turbo-instruct).
  - 결과(FLAN-T5-XL 평균, Table 1): F1은 단일 단계 44.31, 다단계 48.85, Adaptive-RAG 46.94. 소요 시간(단일 단계 대비 상대값)은 다단계 8.81, Adaptive-RAG 3.60. GPT-3.5에서는 F1 50.91로 다단계(50.87)와 같은 수준이면서 시간은 1.46 대 3.33. 질문당 실측 시간은 A 0.35초, B 3.08초, C 27.18초.

## 핵심 개념·용어 정의
- **반성 토큰(reflection token)**: Self-RAG가 생성 중 함께 출력하는 특수 토큰. 검색 필요성(Retrieve)과 비평(IsRel, IsSup, IsUse)을 나타낸다.
- **비평 모델(critic model) / 생성 모델(generator)**: Self-RAG에서 반성 토큰 라벨을 다는 모델과, 그 라벨이 들어간 데이터로 학습되어 실제 답을 내는 모델.
- **IsSup (지지 여부)**: 생성한 문장이 검색 문서에 의해 뒷받침되는지(전부/일부/없음). "근거 확인"을 모델 출력의 일부로 만든 장치.
- **검색 평가기(retrieval evaluator)**: CRAG에서 질문-문서 관련성을 점수화하는 소형 모델(T5-large).
- **교정 행동(Correct / Incorrect / Ambiguous)**: 평가기 점수에 따라 검색 결과를 쓰거나, 버리고 웹 검색하거나, 둘을 섞는 CRAG의 분기.
- **분해 후 재구성(decompose-then-recompose)**: 문서를 작은 조각으로 쪼개 관련 조각만 남기는 지식 정제 절차.
- **질문 복잡도 분류기(query complexity classifier)**: Adaptive-RAG에서 질문을 A/B/C로 나눠 검색 경로를 정하는 소형 모델.
- **라우팅(routing)**: 입력을 분류해 서로 다른 처리 경로로 보내는 구조. Adaptive-RAG는 RAG에 라우팅을 적용한 사례로 볼 수 있다.

## 강연에 쓸 만한 포인트
- 세 논문을 한 줄로: Self-RAG는 "모델이 스스로 판단하도록 학습", CRAG는 "검색 결과를 검사하고 틀리면 교정", Adaptive-RAG는 "질문 난이도에 따라 경로 선택".
- 비교표(아래 강연자 정리, ReAct·FLARE는 02번 파일 참조):

| 방법 | 언제·무엇을 검색할지 누가 정하나 | 가져온 문서를 검사하나 | 루프 반복 |
|---|---|---|---|
| ReAct | 모델(few-shot 프롬프트)이 행동으로 선택 | 별도 검사 없음(모델이 관찰을 읽고 판단) | 예 (finish까지) |
| FLARE | 토큰 확률 임계값(규칙) + 모델 초안 | 별도 검사 없음 | 예 (문장마다) |
| Self-RAG | 학습된 모델 자신(Retrieve 토큰) | 예 (IsRel, IsSup, IsUse) | 구간마다 검색 여부 재판단 |
| CRAG | 고정 1회 검색 후 평가기가 행동 결정 | 예 (T5 평가기, 조각 단위 필터) | 아니오 (1회 교정, 필요 시 웹 검색 추가) |
| Adaptive-RAG | 별도 분류기가 질문 시작 시 경로 선택 | 아니오 (분류기는 질문만 봄) | C 경로만 반복(IRCoT) |

- 교훈 1: "검색 결과를 믿지 말고 확인하라." CRAG Figure 1은 품질 낮은 검색기가 생성 모델에 "a substantial amount of irrelevant information"을 넣는다고 보여준다(Yan et al., CRAG Figure 1 설명). 연구 현장의 문헌 검색에도 그대로 적용되는 메시지.
- 교훈 2: "모든 질문에 무거운 루프를 돌릴 필요는 없다." Adaptive-RAG의 질문당 시간(0.35초 / 3.08초 / 27.18초)은 비용-정확도 균형을 보여주는 좋은 숫자다.
- 교훈 3: Self-RAG는 판단을 학습으로 모델 안에 넣고, CRAG·Adaptive-RAG는 판단을 바깥의 작은 모델(T5)에 맡긴다. 같은 문제를 "모델 내부 vs 외부 부품"으로 푼 두 설계로 대비할 수 있다.
- 주의할 점: Adaptive-RAG 표의 Self-RAG 수치는 기반 모델이 달라(LLaMA2) 직접 비교가 어렵다고 원문이 단서를 달았다.

## 원본 그림
- Self-RAG 개요도(기존 RAG vs Self-RAG: 검색 필요 판단 → 병렬 생성 → 비평 → 선택) — https://selfrag.github.io/static/images/teaser_self_rag_v8.png (프로젝트 페이지 이미지, 접근 확인)
- Self-RAG 반성 토큰 표(4종 토큰의 입력·출력 값) — https://selfrag.github.io/static/images/special_tokens.png (접근 확인)
- CRAG Figure 2 (추론 시 개요: 검색 평가기 → Correct/Incorrect/Ambiguous → 정제·웹 검색) — https://arxiv.org/html/2401.15884v3/method.png (접근 확인)
- CRAG Figure 1 (품질 낮은 검색이 생성기를 오도하는 예시) — https://arxiv.org/html/2401.15884v3/demonstration.png (접근 확인)
- Adaptive-RAG Figure 2 (단일 단계 / 다단계 / 적응형 접근의 개념 비교) — https://arxiv.org/html/2403.14403v2/concept_figure.png (접근 확인)

## Claude Code와의 연결점 (강연자 해석)
- 에이전트 루프(계획 → 실행 → 검증)로 보면 세 논문은 각각 다른 칸을 강화한다. Adaptive-RAG는 "계획"(얼마나 깊게 찾을지 먼저 정함), Self-RAG는 "실행 중 판단"(검색할지 매 구간 결정), CRAG와 Self-RAG의 IsSup은 "검증"(가져온 근거와 답을 확인)에 해당한다.
- Claude Code 같은 범용 에이전트는 이 판단을 별도 분류기나 특수 토큰 없이 모델의 추론과 도구 선택으로 처리한다. 간단한 질문은 바로 답하고, 필요하면 Grep·WebSearch를 한 번, 복잡하면 여러 번 반복한다. Adaptive-RAG의 A/B/C 경로를 에이전트가 암묵적으로 고르는 셈이다.
- CRAG의 "검색이 틀리면 버리고 웹 검색으로 대체"는 에이전트가 검색 결과가 빈약할 때 질의를 바꿔 다시 찾거나 다른 도구(WebFetch 등)로 넘어가는 행동과 같은 발상이다. 강연에서는 "검색은 에이전트의 도구 중 하나이고, 결과를 검증하는 단계가 따로 있어야 한다"는 메시지로 연결할 수 있다.
- 03번 폴더 Anthropic 글의 routing 패턴(입력 분류 후 경로 분기)은 Adaptive-RAG와 구조가 같고, evaluator-optimizer 패턴은 CRAG·Self-RAG의 "생성 후 평가"와 겹친다(원 논문들이 Anthropic 글을 참조한 것은 아님).
