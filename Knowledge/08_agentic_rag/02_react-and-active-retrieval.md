# ReAct · FLARE · IRCoT (추론과 검색을 번갈아 하는 에이전트형 검색의 출발점)

- **저자/기관**:
  - ReAct: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao / Princeton University, Google Research(Brain team) (Yao는 Google 인턴 기간 중 수행)
  - FLARE: Zhengbao Jiang, Frank F. Xu, Luyu Gao, Zhiqing Sun, Qian Liu, Jane Dwivedi-Yu, Yiming Yang, Jamie Callan, Graham Neubig / Carnegie Mellon University(LTI) 중심, Sea AI Lab, Meta FAIR
  - IRCoT: Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, Ashish Sabharwal / (기관은 열람한 페이지에서 확인하지 않음)
- **발행일**: (2026-10-23 열람)
  - ReAct: arXiv v1 2022-10-06, v3 2023-03-10 (v3가 ICLR 카메라레디 버전이라고 arXiv 코멘트에 명시). ICLR 2023
  - FLARE: arXiv v1 2023-05-11, v2 2023-10-22. EMNLP 2023 (2023년 12월, Singapore, pp. 7969–7992)
  - IRCoT: arXiv v1 2022-12-20, v2 2023-06-23. ACL 2023 (Long Papers, 2023년 7월, Toronto, pp. 10014–10037)
- **URL**:
  - ReAct: https://arxiv.org/abs/2210.03629 (본문: https://ar5iv.labs.arxiv.org/html/2210.03629, 프로젝트: https://react-lm.github.io/)
  - FLARE: https://arxiv.org/abs/2305.06983 / https://aclanthology.org/2023.emnlp-main.495/ (DOI 10.18653/v1/2023.emnlp-main.495)
  - IRCoT: https://arxiv.org/abs/2212.10509 / https://aclanthology.org/2023.acl-long.557/ (DOI 10.18653/v1/2023.acl-long.557)
- **자료 유형**: 논문 (학회: ICLR 2023, EMNLP 2023, ACL 2023)

## 핵심 요약
- **ReAct**: LLM이 "생각(Thought)"과 "행동(Action)"을 번갈아 생성하게 하는 프롬프트 방식이다. 행동을 실행하면 환경이 "관찰(Observation)"을 돌려주고, 모델은 그 결과를 보고 다음 생각을 이어간다. 생각은 환경을 바꾸지 않고 계획을 세우고 추적·수정하는 데 쓰이며, 행동은 외부 정보를 가져온다.
  - 질의응답(HotpotQA)과 사실 검증(FEVER)에서는 행동 공간을 단순한 Wikipedia API 3종으로 한정했다: `search[entity]`(해당 문서의 앞 5문장 반환, 없으면 유사 항목 5개 제안), `lookup[string]`(문서 안에서 해당 문자열이 든 다음 문장 반환, Ctrl+F와 유사), `finish[answer]`(답을 내고 종료).
  - 주 모델은 고정된(frozen) PaLM-540B이며, 사람이 쓴 few-shot 궤적(HotpotQA 6개, FEVER 3개)으로 프롬프트했다. 부록에서 GPT-3(text-davinci-002)도 시험했다.
  - 결과(Table 1): HotpotQA EM은 Standard 28.7, CoT 29.4, CoT-SC 33.4, Act 25.7, ReAct 27.4, ReAct→CoT-SC 35.1. FEVER 정확도는 CoT 56.3, CoT-SC 60.4, ReAct 60.9, CoT-SC→ReAct 64.6. 즉 ReAct 단독이 HotpotQA에서 CoT를 이기지는 못했고, 내부 지식(CoT)과 외부 검색(ReAct)을 섞은 조합이 가장 좋았다.
  - 오류 분석(HotpotQA 200개 표본): CoT 실패 사례의 56%가 환각(hallucination)이었고 ReAct는 0%였다. 반면 ReAct의 주된 실패 원인은 추론 오류(47%)와 쓸모없는 검색 결과(23%)였다. 검색이 사실 근거를 주는 대신, 검색 품질과 추론 유연성이 새 병목이 된다는 뜻이다.
  - 의사결정 과제: ALFWorld에서 ReAct 71%(Act 45%, BUTLER 37%), WebShop에서 성공률 40.0%(Act 30.1%, IL 29.1%, IL+RL 28.7%, 사람 전문가 59.6%). 초록 기준으로 모방학습·강화학습 대비 절대 성공률 34%p, 10%p 향상이며 예시는 1~2개만 썼다.
- **FLARE**(Forward-Looking Active REtrieval augmented generation): 긴 글을 생성하는 동안 "언제, 무엇을" 검색할지 모델이 정하게 하는 능동 검색(active retrieval) 방법이다.
  - 다음 문장을 먼저 임시로 생성한다. 그 문장에 확률이 임계값 θ보다 낮은 토큰이 하나라도 있으면, 그 임시 문장을 질의로 삼아 문서를 검색하고 문장을 다시 생성한다. 확신이 높으면 검색 없이 그대로 채택한다.
  - 질의 구성은 두 가지: 확신 낮은 토큰을 가리는 암묵적 방식(masked query, 임계값 β), 확신 낮은 구간을 겨냥한 질문을 생성하는 명시적 방식. 별도 변형인 FLARE-instruct는 모델이 생성 중 검색 질의를 직접 써넣게 한다.
  - 모델: text-davinci-003(GPT-3.5, API 사용), 명시적 질문 생성에는 gpt-3.5-turbo. 검색기: Wikipedia 덤프 대상 BM25, 개방형 요약 과제에는 Bing 검색 API.
  - 과제 4종: 2WikiMultihopQA(다중 홉 QA), StrategyQA(상식 추론), ASQA/ASQA-hint(장문 QA), WikiAsp(개방 도메인 요약). 2WikiMultihopQA EM 51.0으로 단일 검색(39.4), 질문 분해(47.8), 무검색(28.2)보다 높았다. 과제에 따라 문장의 약 30~60%에서만 검색이 일어났다.
  - 한계: Wizard of Wikipedia, ELI5에서는 유의미한 향상이 없었다고 저자가 밝혔다.
- **IRCoT**(Interleaving Retrieval with Chain-of-Thought): 다중 홉 질문에서는 원래 질문으로 한 번 검색하는 것만으로 부족하다는 문제의식에서 출발한다. 무엇을 검색해야 할지는 지금까지의 추론에 달려 있고, 그 추론은 앞선 검색 결과에 달려 있다.
  - CoT 문장 하나를 생성할 때마다 그 문장으로 다시 검색하고, 검색 결과를 넣어 다음 추론 문장을 생성하는 과정을 번갈아 반복한다.
  - GPT-3 기준 HotpotQA, 2WikiMultihopQA, MuSiQue, IIRC 4개 데이터셋에서 검색 성능 최대 21점, QA 성능 최대 15점 향상. Flan-T5-large 같은 작은 모델에서도 추가 학습 없이 비슷한 효과, 환각 감소도 보고. (주의: IRCoT는 초록만 확인)

## 핵심 개념·용어 정의
- **ReAct (Reason + Act)**: 추론 흔적(reasoning trace)과 과제별 행동(action)을 교차 생성하는 프롬프트 방식.
- **Thought / Action / Observation**: ReAct 한 스텝의 세 요소. Thought는 자유 형식의 내적 추론(환경에 영향 없음), Action은 도구 호출, Observation은 도구가 돌려준 결과.
- **CoT (Chain-of-Thought)**: 답 전에 단계적 추론을 글로 쓰게 하는 프롬프트. 외부 정보 없이 모델 내부 지식만 사용.
- **CoT-SC (Self-Consistency)**: CoT를 여러 번 샘플링해 다수결로 답을 고르는 방식.
- **환각(hallucination) / 오류 전파(error propagation)**: 근거 없는 사실을 지어내고, 그 잘못이 이후 추론 단계로 이어지는 현상.
- **능동 검색(active retrieval)**: 입력 시점에 한 번만 검색하지 않고, 생성 도중 필요할 때마다 검색 시점과 질의를 정하는 방식.
- **전망형 검색(forward-looking retrieval)**: 이미 생성한 앞 문장이 아니라 "앞으로 쓸 문장"의 초안을 질의로 쓰는 FLARE의 핵심 아이디어.
- **신뢰도 임계값(θ)**: 토큰 생성 확률이 이보다 낮으면 "모르는 상태"로 보고 검색을 발동하는 기준.
- **다중 홉 질문(multi-hop question)**: 두 개 이상의 문서를 거쳐야 답할 수 있는 질문. 예: A의 감독이 태어난 나라는?

## 강연에 쓸 만한 포인트
- 도식 아이디어: ReAct 루프를 원형으로 그리기 — Thought(무엇을 모르는가?) → Action(search/lookup) → Observation(검색 결과) → Thought ... → finish. 슬라이드 한 장으로 "에이전트형 RAG의 뼈대"를 보여줄 수 있다.
- 숫자 하나로 메시지 전달: "CoT 실패의 56%는 환각, ReAct는 0%". 단, 같은 표에서 ReAct 실패의 23%는 "검색 결과가 쓸모없음"이라는 점을 함께 보여주면 "검색 도구 품질이 곧 에이전트 품질"이라는 다음 메시지로 이어진다.
- 정직한 해석 포인트: ReAct 단독은 HotpotQA EM에서 CoT보다 낮았다(27.4 vs 29.4). 최고 성능은 내부 지식과 외부 검색을 상황에 따라 바꿔 쓴 조합에서 나왔다. "검색을 많이 할수록 좋다"가 아니라 "필요할 때 검색"이 핵심이며, 이 질문이 FLARE·Self-RAG·Adaptive-RAG로 이어진다.
- 세 논문의 "검색 시점 결정" 대비: ReAct는 모델이 행동으로 검색을 택함(프롬프트), IRCoT는 추론 문장마다 기계적으로 검색(고정 규칙), FLARE는 토큰 확신이 낮을 때만 검색(확률 기반 트리거).
- 환경연구 예시 비유: "어느 유역의 2020년 총인 농도는?"이라는 질문에 모델이 기억으로 숫자를 지어내는 대신, 측정망 DB를 search → 해당 지점 lookup → 값 확인 후 finish 하는 흐름.
- 인용(1개): "help the model induce, track, and update action plans" — Yao et al., ReAct 초록 (arXiv 2210.03629)

## 원본 그림
- ReAct Figure 1 계열 도식(Standard / CoT / Act-only / ReAct를 HotpotQA 질문 하나로 비교, ALFWorld 예시 포함) — 프로젝트 페이지 이미지: https://react-lm.github.io/files/diagram.png (이미지 응답 확인. 논문 Figure 1과 동일한지는 육안 대조하지 않음)
- FLARE Figure 1 (임시 문장 생성 → 저확신 토큰 확인 → 검색 후 재생성 루프) — https://ar5iv.labs.arxiv.org/html/2305.06983/assets/illustration.png
- FLARE Figure 2 (FLARE-instruct: 생성 중 검색 질의 삽입) — https://ar5iv.labs.arxiv.org/html/2305.06983/assets/illustration_search.png (경로만 본문에서 확인, 개별 접근은 미확인)
- FLARE Figure 3 (암묵적 masked query vs 명시적 질문 생성 비교) — https://ar5iv.labs.arxiv.org/html/2305.06983/assets/queryformulation.png (경로만 확인)
- IRCoT: 방법 그림 URL은 확인하지 못함.

## Claude Code와의 연결점 (강연자 해석)
- ReAct의 Thought → Action → Observation은 이 강연의 에이전트 루프(계획 → 실행 → 검증)와 같은 구조다. Claude Code가 "어떤 파일을 열어볼지 생각 → Grep/Read 실행 → 결과 확인 → 다음 행동 결정"을 반복하는 것도 같은 틀로 설명할 수 있다.
- ReAct에서 검색(search, lookup)은 에이전트가 쓰는 "도구 중 하나"일 뿐이다. 이 관점에서 RAG는 고정 파이프라인이 아니라 에이전트의 도구 상자에 든 검색 도구가 된다. Claude Code의 Grep·Glob·WebSearch·WebFetch가 같은 위치에 있다.
- ReAct의 `search`(문서 앞부분 요약)와 `lookup`(문서 안 문자열 찾기) 구분은 Claude Code의 "파일 찾기(Glob/Grep) → 필요한 부분만 읽기(Read)" 흐름과 닮았다. 원 논문이 이런 단순 도구를 일부러 택한 점은 "도구 설계(ACI)가 성능을 좌우한다"는 03번 폴더의 메시지와 연결된다.
- FLARE의 "모를 때만 검색"은 에이전트가 매번 검색하지 않고 필요할 때 도구를 부르는 판단과 같은 문제다. 다만 FLARE는 토큰 확률이라는 명시적 신호를 쓰고, Claude Code 같은 에이전트는 모델의 판단(프롬프트·학습)에 맡긴다는 차이가 있다.
