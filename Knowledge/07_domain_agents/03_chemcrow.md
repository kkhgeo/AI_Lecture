# ChemCrow: Augmenting large language models with chemistry tools (화학 도구를 붙인 LLM 화학 에이전트)

- **저자/기관**: Andres M. Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, Philippe Schwaller / EPFL(스위스), University of Rochester(미국), IBM Research Europe 등
- **발행일**: 프리프린트 v1 2023-04-11 (v5 2023-10-02). 학술지판 *Nature Machine Intelligence* 6(5):525–535, 2024-05-08 출판 (접수 2023-09-13, 게재승인 2024-03-27) (2026-10-23 열람)
- **URL**:
  - 학술지판: https://doi.org/10.1038/s42256-024-00832-8 (nature.com은 로그인 리다이렉트로 직접 열지 못함)
  - 학술지판 전문(PMC, 실제로 확인한 본문): https://pmc.ncbi.nlm.nih.gov/articles/PMC11116106/
  - 프리프린트: https://arxiv.org/abs/2304.05376
- **자료 유형**: 논문 (학술지, 오픈액세스 / 프리프린트 선행)

## 핵심 요약
- ChemCrow는 범용 LLM에 전문가가 설계한 화학 도구를 연결해 유기합성, 신약 탐색, 소재 설계 과제를 풀게 한 화학 에이전트다. 저자들의 출발점은 두 가지다. LLM 단독으로는 화학 문제(계산, 반응 예측 등)에 약하고 외부 지식에 접근하지 못한다는 점, 그리고 기존 계산화학 도구는 많지만 배우기 어려워 접근성이 낮다는 점이다.
- 구동 LLM은 GPT-4(temperature 0.1)이며, LangChain으로 도구를 연결하고 ReAct·MRKL 방식의 루프(Thought → Action → Action Input → Observation 반복, 최종 답에 도달할 때까지)로 동작한다(PMC 학술지판 Methods 기준). arXiv 초록에는 구동 모델 이름이 나오지 않는다.
- 도구 수는 판본마다 다르다. arXiv v1 초록은 13개, arXiv v5 초록과 학술지판 본문은 18개라고 쓴다. 다만 학술지판 Methods에 나열된 도구를 세면 19개(일반 4, 분자 8, 안전 3, 반응 4)다. 강연에서는 "18개(학술지판 기준)"로 쓰고, 판본 간 차이가 있음을 각주로 두는 것이 안전하다.
- 도구 분류(학술지판 Methods): 일반(WebSearch, LitSearch, Python REPL, Human), 분자(Name2SMILES, SMILES2Price, Name2CAS, Similarity, ModifyMol, PatentCheck, FuncGroups, SMILES2Weight), 안전(ControlledChemicalCheck, ExplosiveCheck, SafetySummary), 반응(NameRXN, ReactionPredict, ReactionPlanner, ReactionExecute). ReactionExecute는 IBM Research의 클라우드 자동합성 플랫폼 RoboRXN에서 실제 합성을 실행한다.
- 실험 검증: 곤충기피제 DEET와 thiourea 계열 유기촉매 3종(Schreiner's, Ricci's, Takemoto's)의 합성을 스스로 계획하고 RoboRXN에서 실행했으며, 4건 모두 목표 화합물을 얻었다.
- 신규 발색단(chromophore) 탐색: 에이전트가 데이터 정리, random forest 모델 학습, 후보 선정을 이어서 수행했다. 목표 흡수 극대 파장 369 nm에 대해 합성된 화합물의 측정값은 336 nm였다(목표와 근접하나 일치는 아님).
- 평가: 14개 사용 사례에서 ChemCrow와 GPT-4 단독을 비교했다. 화학 전문가 4명은 정확성·추론·과제 완수 측면에서 대체로 ChemCrow를 더 높게 평가했고, 특히 복잡한 과제에서 차이가 컸다. 반면 DEET, paracetamol처럼 잘 알려진 분자에서는 GPT-4 단독이 나았다.
- 핵심 발견: LLM 평가자(EvaluatorGPT, GPT-4 기반)는 오히려 GPT-4 단독 답변을 선호했다. 저자들은 그 이유를 답변의 유창성으로 보고, 사실 정확성이 중요한 과제에서 LLM 기반 평가는 전문가 평가를 대신할 수 없다고 결론 내린다.
- 안전·오용: ControlledChemicalCheck가 화학무기 목록·전구체 목록과 대조해 일치하면 실행을 멈추고 경고하며, 목록 화합물과 유사도 0.35 이상이면 경고한다. ExplosiveCheck는 PubChem의 GHS 분류로 폭발물을 표시한다. 저자들은 이 도구들의 위험이 원래 오픈소스 도구를 각각 쓸 때의 위험과 비슷한 수준이라고 본다.
- 한계(저자 명시): 결과가 도구 품질과 에이전트 추론에 좌우되고, 폐쇄형 API 모델이라 재현성이 제한되며, 도구 세트와 평가 과제가 제한적이다. 실험실 안전, 환각(hallucination), 지식재산권 문제도 함께 언급된다.

## 핵심 개념·용어 정의
- **ReAct**: 추론(Reasoning)과 행동(Acting)을 번갈아 수행하는 프롬프트 방식. 모델이 생각을 쓰고, 도구를 고르고, 결과를 관찰한 뒤 다음 생각으로 넘어간다.
- **MRKL (Modular Reasoning, Knowledge and Language)**: LLM이 여러 외부 모듈(도구) 중 하나를 골라 호출하도록 하는 구조. ChemCrow는 ReAct와 MRKL을 함께 따른다고 밝힌다.
- **LangChain**: LLM에 도구·프롬프트를 연결하는 오픈소스 프레임워크. ChemCrow의 구현 기반.
- **RoboRXN**: IBM Research의 클라우드 연결 자동 합성 플랫폼. ChemCrow가 합성 절차를 넘겨 실제 반응을 수행한 장비.
- **EvaluatorGPT**: 논문에서 GPT-4를 채점자로 쓴 평가 설정. 전문가 평가와 결과가 엇갈렸다.
- **SMILES**: 분자 구조를 문자열로 표기하는 방식. 여러 분자 도구의 입출력 형식.

## 강연에 쓸 만한 포인트
- 메시지 1: "같은 GPT-4라도 도구를 붙이면 다른 에이전트가 된다." ChemCrow의 차별점은 모델이 아니라 18개 화학 도구와 RoboRXN 연결이다.
- 메시지 2(평가 함정): LLM에게 채점을 맡기면 "그럴듯하게 쓴 답"이 높은 점수를 받는다. 전문가 4명과 GPT-4 평가자의 판정이 반대로 나온 사례는 연구소 청중에게 설득력이 있다.
- 메시지 3(안전은 도구로 구현): 금지 물질 검사를 프롬프트 지시가 아니라 별도 도구(ControlledChemicalCheck)로 넣어 실행 경로에서 차단한다. 환경 분야라면 규제 물질·배출 기준 검사 도구로 바꿔 생각해볼 수 있다(이 응용은 정리자 해석).
- 도식 아이디어: 왼쪽에 GPT-4, 가운데 Thought/Action/Observation 순환, 오른쪽에 4개 도구 묶음(일반·분자·안전·반응), 맨 끝에 RoboRXN 로봇. 원본 Fig. 1이 거의 이 구성이다.
- 주의할 숫자: 13개(arXiv v1) → 18개(v5·학술지판 본문) → 19개(학술지판 Methods 목록 집계). 슬라이드에는 18개로 쓰고 출처를 학술지판으로 표기.
- 인용(1개): "18 expert-designed tools" — Bran et al., arXiv 2304.05376 v5 초록

## 원본 그림
- Fig. 1 개요와 도구 세트(a: DEET 합성 예시로 본 과제 해결 과정, b: 반응·분자·안전·검색·표준 도구 묶음) — https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7971/11116106/4fad4a4ad489/42256_2024_832_Fig1_HTML.jpg
- Fig. 2 실험 검증(a: ChemCrow 실행 스크립트, b: thiourea 유기촉매 질의와 합성, c: RoboRXN 플랫폼, d: 검증된 화합물) — https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7971/11116106/99ea794d4cd3/42256_2024_832_Fig2_HTML.jpg
- 참고: 이미지 URL은 PMC 본문에서 추출한 것이며 개별 파일을 직접 열어 확인하지는 않음. 논문은 오픈액세스로 공개되어 있으나 슬라이드 사용 시 출처 표기 필요.

## Claude Code와의 연결점
- 강연 틀(AI 에이전트 = LLM + 하네스)에 대입하면, ChemCrow의 LLM은 GPT-4이고 하네스는 LangChain 기반 ReAct 루프와 18개 도구다. 도메인 특화는 모델을 바꾼 것이 아니라 도구 목록을 화학용으로 바꾼 것이다. (이 대응은 정리자의 해석이며, 논문은 "harness"라는 용어를 쓰지 않는다.)
- Claude Code의 구조와 비교하면: Python REPL 도구 ↔ Bash/코드 실행, WebSearch/LitSearch ↔ 웹 검색·MCP 문헌 검색, Human 도구 ↔ 사용자 확인 요청, ControlledChemicalCheck ↔ 권한 규칙·hook으로 특정 행동을 차단하는 장치. 대응 관계는 정리자 해석이다.
- 하네스의 세 요소(기억·스킬·도구) 중 ChemCrow는 "도구"에 집중한 사례다. 장기 기억이나 재사용 가능한 절차(skill)에 해당하는 구성 요소는 논문에 뚜렷하게 나오지 않는다.
- EvaluatorGPT 결과는 Claude Code로 연구 작업을 할 때도 그대로 적용된다. 에이전트 결과를 다른 LLM에게만 검토시키면 유창성에 끌린 판정이 나올 수 있으므로, 도메인 전문가 검토나 실행 가능한 검증(테스트, 측정값 대조)을 남겨야 한다.
