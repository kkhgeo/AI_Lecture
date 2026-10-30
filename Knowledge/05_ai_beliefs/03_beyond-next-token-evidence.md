# LLM은 표면 통계 이상을 하는가: 내부 세계모델·계획 증거와 반증 (Beyond next-token: 찬반 증거)
- **저자/기관**: (복수 자료)
  - Kenneth Li, Aspen Hopkins, David Bau, Fernanda Viégas, Hanspeter Pfister, Martin Wattenberg (Harvard/MIT/Northeastern) — "Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task", ICLR 2023
  - Neel Nanda, Andrew Lee, Martin Wattenberg — "Emergent Linear Representations in World Models of Self-Supervised Sequence Models", BlackboxNLP 2023 (후속)
  - Anthropic — "Tracing the thoughts of a large language model" (블로그, 2025-03-27); Lindsey et al. "On the Biology of a Large Language Model" (Transformer Circuits Thread, 2025-03-27)
  - Berglund, Tong, Kaufmann, Balesni, Stickland, Korbak, Evans — "The Reversal Curse: LLMs trained on 'A is B' fail to learn 'B is A'" (arXiv 2023-09-21; ICLR 2024)
  - Zhaofeng Wu, Linlu Qiu, Alexis Ross, Ekin Akyürek, Boyuan Chen, Bailin Wang, Najoung Kim, Jacob Andreas, Yoon Kim (MIT/BU) — "Reasoning or Reciting? ... Counterfactual Tasks", NAACL 2024 (arXiv 2023-07)
  - Mirzadeh, Alizadeh, Shahrokhi, Tuzel, Bengio, Farajtabar (Apple) — "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs" (arXiv 2024-10; ICLR 2025)
- **발행일**: 2023–2025 (각 항목 참조) (2026-09-30 열람)
- **URL**:
  - Othello-GPT: https://arxiv.org/abs/2210.13382 ; 코드 https://github.com/likenneth/othello_world ; Nanda 해설 https://neelnanda.io/mechanistic-interpretability/othello
  - Anthropic 블로그: https://www.anthropic.com/research/tracing-thoughts-language-model
  - Biology 논문: https://transformer-circuits.pub/2025/attribution-graphs/biology.html
  - Reversal Curse: https://arxiv.org/abs/2309.12288
  - Reasoning or Reciting: https://aclanthology.org/2024.naacl-long.102 (arXiv 2307.02477)
  - GSM-Symbolic: https://arxiv.org/abs/2410.05229
- **자료 유형**: 논문 | 블로그

## 핵심 요약
**[찬: 표면 통계 이상]**
- **Othello-GPT (Li et al. 2023)**: 오델로 수(move) 기호열만으로 다음 합법 수를 예측하도록 GPT를 학습(규칙·보드 정보 미제공). 내부 활성에서 **보드 상태를 probe로 복원** 가능했고, 내부 표상을 인위적으로 바꾸면(intervention) 모델의 수 예측도 그에 맞게 바뀜 → 인과적으로 쓰이는 **세계모델(world model)**이 창발.
- **Nanda et al. 2023 후속**: 보드를 "흑/백"이 아니라 "내 돌/상대 돌/빈칸"으로 표현하면 **선형적으로** 읽힘 → 벡터 연산으로 행동 조종 가능. 세계모델 해석을 강화.
- **Anthropic (2025-03) – 계획**: Claude 3.5 Haiku가 운율 있는 2행시를 쓸 때, 둘째 줄을 쓰기 **전에** 운(예: "rabbit")을 먼저 떠올리고 그 목표를 향해 문장을 구성. "rabbit" 개념을 억제하면 다른 운("habit")으로 바꿔 씀 → 한 토큰씩 출력하지만 내부적으로는 **앞을 내다보는 계획**.
- **Anthropic – 다단계 추론**: "Dallas가 있는 주의 주도는?" 질문에서 "Dallas→Texas" 중간 표상을 거쳐 "Texas의 주도→Austin"으로 합성하는 경로 관측(중간 단계를 바꾸면 답이 바뀜) → 단순 암기 인출이 아닌 사실 결합.
- **Anthropic – 다국어 공유 개념**: 영어·프랑스어·중국어에서 같은 개념에 **언어 독립적 공유 특징**이 활성화, 모델이 클수록 공유 비율 증가 → 일종의 개념 공간.
- **같은 연구의 불편한 발견**: 암산 시 모델이 실제로는 "대략값 경로 + 끝자리 정밀 경로"를 병렬로 쓰면서, 설명을 요청받으면 학교식 받아올림 알고리즘을 말함(자기 설명의 **불충실성**). 어려운 문제나 잘못된 힌트에선 결론에 맞춰 중간 단계를 **거꾸로 꾸며내는(motivated reasoning)** 사례도 관측.

**[반: 한계와 취약성]**
- **Reversal Curse (2023)**: "A는 B다"로 학습하면 "B는 A다"로 자동 일반화되지 않음. 실제 유명인 질문에서 GPT-4는 "톰 크루즈의 어머니는?"에 79% 정답, "메리 리 파이퍼의 아들은?"에 33% 정답.
- **Reasoning or Reciting (Wu et al.)**: 11개 과제의 "반사실 변형"(예: 10진법 대신 9진법 덧셈, 규칙이 바뀐 체스 등)에서 성능이 비자명하게는 유지되지만 기본 조건보다 **일관되게 크게 하락** → 추상적 능력과 **좁고 전이 안 되는 절차**가 섞여 있음.
- **GSM-Symbolic (Apple 2024)**: 초등 수학 문제의 이름·숫자만 바꿔도 정답률 분산이 커지고, 답과 무관한 절 하나를 추가(GSM-NoOp)하면 최신 모델들이 **최대 약 65%p 하락**. 저자들은 "진정한 논리 추론보다 학습 데이터의 추론 단계 복제"라고 가설.
- **주의(시점)**: 반증 연구들은 2023–2024년 모델 기준. 이후 추론 특화 모델에서 일부 개선이 보고되었으나 이번 조사에서 체계적으로 확인하지 못함(미검증). 반대로 Anthropic 연구도 자사 모델·자사 방법론이며, 회로 추적은 전체 계산의 일부만 설명한다고 저자들 스스로 한계를 명시.

## 핵심 개념·용어 정의
- **World model(세계모델)**: 입력 기호열을 생성한 바깥 상태(보드, 공간 등)의 내부 표상. 표면 통계와 대비되는 개념.
- **Probe / Intervention(탐침 / 개입)**: probe는 내부 활성에서 정보를 읽어내는 분류기, intervention은 그 표상을 직접 바꿔 행동 변화를 확인하는 인과 검증.
- **Linear representation hypothesis**: 개념이 활성 공간의 방향(벡터)으로 선형 인코딩된다는 가설.
- **Mechanistic interpretability / attribution graph / circuit tracing**: 모델 내부 계산을 특징(feature)과 그 연결 그래프로 역설계하는 방법. Anthropic은 replacement model(교차층 transcoder)로 attribution graph를 만듦.
- **Planning(계획)**: 미래 토큰 목표를 미리 표상하고 현재 출력을 그에 맞춤.
- **Unfaithful reasoning(불충실 추론)**: 모델이 말하는 사고 과정(CoT)과 실제 내부 계산이 다른 현상.
- **Reversal curse**: 방향성 있는 사실 학습이 역방향으로 일반화되지 않는 현상.
- **Counterfactual task(반사실 과제)**: 기본 가정을 바꾼 과제 변형(9진법 등)으로 암기 vs 일반 능력을 구별.
- **Distractor robustness**: 무관한 정보 추가에 대한 강건성(GSM-NoOp).

## 비판론(skeptic)과 반론의 대응
- **"단지 다음 토큰 예측"이라는 skeptic 주장에 대해**: 학습 **목표**가 다음 토큰 예측이라는 것과, 그 목표를 달성하려고 **내부에 형성된 계산**이 무엇인지는 별개 문제. Othello-GPT와 Anthropic 회로 연구는 후자에서 세계모델·계획·개념 결합이 나타남을 보여줌 → "앵무새(되는대로 이어 붙임)"라는 문자 그대로의 정의에는 **반례**.
- **반대로 skeptic을 지지하는 부분**: Reversal curse, 반사실 과제, GSM-NoOp은 LLM의 능력이 **학습 분포에 강하게 묶여 있고 취약**함을 보여줌. 즉 "앵무새는 아니지만, 인간식의 견고한 추상화도 아직 아니다".
- **강연자 믿음과의 관계**: 이 증거들은 "인간도 앵무새"보다 **"LLM도 앵무새만은 아니다"**를 지지한다. 흥미롭게도 인간도 반사실·방해 정보에 취약하고(인지 편향), 자기 사고 과정을 사후에 꾸며 설명하는 경향(confabulation 연구)이 있어 대칭 논증이 가능하나, 이 인간 측 비교는 본 조사에서 1차 자료로 검증하지 않음(미검증, 사용 시 별도 확인).
- **코딩 에이전트 강연 함의**: 계획·다단계 추론 능력은 에이전트가 유용한 이유, 분포 밖 취약성과 불충실한 자기 설명은 **사람이 검증(테스트·리뷰)해야 하는 이유** — 두 증거가 강연의 실용 메시지에 동시에 쓰임.

## 강연에 쓸 만한 포인트
- 인용(1개): 없음 권장(재서술로 충분). 필요 시 Anthropic 블로그의 "plans ahead"류 짧은 구절을 원문 확인 후 사용.
- 비유: "목표는 다음 단어 맞히기지만, 그걸 잘하려다 보니 머릿속에 오델로 판이 생겼다" — 시험(목표) vs 공부하며 생긴 이해(내부 표상).
- 비유 2: 운율 시 계획 = "끝말을 먼저 정하고 문장을 거꾸로 설계하는 작사가".
- 그림 아이디어: 저울 그림 — 왼쪽 접시(Othello 세계모델, rhyme 계획, Dallas→Texas→Austin, 다국어 공유 개념), 오른쪽 접시(역전의 저주 79% vs 33%, 9진법 하락, GSM-NoOp 최대 65% 하락). 결론 문구: "앵무새도 아니고, 인간도 아직 아니다."
- 실용 메시지: "그래서 에이전트에게 맡기되, 테스트로 검증하라."

## 원본 그림
- Anthropic "Tracing the thoughts" 대표 이미지(OG) — https://www-cdn.anthropic.com/images/4zrzovbb/website/ec654a5f4bd41eb516d339bc66918dfd65aa44e4-1200x630.jpg
- "On the Biology of a LLM" 본문 도식(운율 계획·다단계 추론 attribution graph 등) — 페이지 내 상대경로 이미지(예: https://transformer-circuits.pub/2025/attribution-graphs/png/img_4e42fad1d7624d1e.png ; 개별 그림 내용은 미확인, 페이지에서 직접 선택 권장)
- Othello-GPT 프로브/개입 그림 — 논문 PDF Fig.1 참조 https://arxiv.org/pdf/2210.13382 (직접 이미지 URL 없음)
- Reversal Curse Fig.1 (톰 크루즈 예시) — https://arxiv.org/pdf/2309.12288 (직접 이미지 URL 없음)
- GSM-Symbolic 템플릿/NoOp 예시 그림 — https://arxiv.org/abs/2410.05229 (직접 이미지 URL 없음)
