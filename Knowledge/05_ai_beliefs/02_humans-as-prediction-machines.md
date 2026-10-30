# 인간도 예측 기계인가: Predictive Processing과 뇌의 다음 단어 예측 (반론 측 근거와 그 한계)
- **저자/기관**: (복수 자료)
  - Andy Clark (Univ. of Sussex) — *Surfing Uncertainty: Prediction, Action, and the Embodied Mind* (Oxford UP, 2016); *The Experience Machine: How Our Minds Predict and Shape Reality* (Pantheon/Allen Lane, 2023-03)
  - Karl Friston (UCL) — "The free-energy principle: a unified brain theory?" *Nature Reviews Neuroscience* 11 (2010)
  - Schrimpf, Blank, Tuckute, Kauf, Hosseini, Kanwisher, Tenenbaum, Fedorenko (MIT) — *PNAS* 118(45) e2105646118 (2021)
  - Caucheteux, Gramfort, King (Meta AI / ENS / Inria) — *Nature Human Behaviour* 7, 430–441 (2023-03-02)
  - Goldstein et al. (Hasson Lab, Princeton; Google Research) — *Nature Neuroscience* 25, 369–380 (2022-03)
  - Sam Altman (OpenAI) — X/Twitter 게시물 (2022-12, ChatGPT 공개 수일 후)
  - Chomsky, Roberts, Watumull — "The False Promise of ChatGPT", *New York Times* 기고 (2023-03-08)
- **발행일**: 위 각 항목 참조 (2026-09-30 열람)
- **URL**:
  - Schrimpf 2021: https://www.pnas.org/doi/10.1073/pnas.2105646118 (MIT DSpace: https://hdl.handle.net/1721.1/138214)
  - Caucheteux 2023: https://www.nature.com/articles/s41562-022-01516-2 (PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC10038805/)
  - Goldstein 2022: https://www.nature.com/articles/s41593-022-01026-4 (PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC8904253)
  - Friston 2010: https://www.nature.com/articles/nrn2787
  - Chomsky 2023: https://www.nytimes.com/2023/03/08/opinion/noam-chomsky-chatgpt-ai.html
  - Altman 트윗: 원 게시물 URL 미확인 (위키백과 "Stochastic parrot" 항목에서 인용 확인)
- **자료 유형**: 논문 | 책 | 기사

## 핵심 요약
- **Predictive processing(예측 처리)**: 뇌는 감각을 수동적으로 받아들이는 기관이 아니라, 끊임없이 다음 입력을 예측하고 **예측 오차(prediction error)**만 위로 올려 보내며 모델을 갱신하는 계층적 예측 기계라는 틀(Clark 2016, 2023). 지각·행동·통증 경험까지 기대(prior)에 의해 형성된다.
- **Free-energy principle(Friston)**: 생명체는 감각 입력의 "놀람(surprise)"의 상한인 자유에너지를 최소화하도록 작동한다는 일반 원리. 지각(모델 갱신)과 **행동(세계를 예측에 맞게 바꿈, active inference)** 둘 다로 오차를 줄인다.
- **Schrimpf et al. 2021**: 43개 언어 모델을 fMRI·ECoG 언어 반응 데이터와 비교. 최고 성능 transformer(GPT 계열)가 설명 가능한 신경 반응 분산의 거의 전부를 예측했고, 모델의 "brain score"는 **다음 단어 예측 성능과만** 강하게 상관(다른 언어 과제 성능과는 약함) → 뇌 언어 영역의 핵심 목표가 예측이라는 계산적 증거.
- **Goldstein et al. 2022**: 9명 뇌전증 환자(ECoG)가 30분 팟캐스트를 들을 때, 뇌와 자기회귀 언어모델이 세 원리를 공유: (1) 단어가 들리기 **전에** 다음 단어를 연속적으로 예측, (2) 실제 단어와 비교해 놀람(surprise) 계산, (3) 맥락 임베딩으로 단어 표상.
- **Caucheteux, Gramfort & King 2023**: 304명 fMRI(이야기 청취). 언어모델 활성이 뇌 반응에 선형 매핑되고, 여기에 **더 먼 미래(여러 단어 뒤)**의 예측을 추가하면 매핑이 개선됨. 전두–두정 피질은 더 길고 추상적인 예측, 측두 피질은 짧고 저수준 예측을 담당 → 뇌는 LM보다 **더 긴 시간 척도·계층적** 예측을 한다. 즉 "인간 ≈ LM"이 아니라 "인간 ⊃ LM식 예측 + α".
- **Altman 트윗 (2022-12)**: "i am a stochastic parrot, and so r u" — skeptic의 용어를 뒤집어 인간에게 적용한 대중적 프레이밍. 논증이라기보다 도발이며, 이해관계자(OpenAI CEO)의 발언이라는 점을 감안해야 함.
- **Chomsky et al. 2023 (비판)**: 인간 정신은 방대한 데이터에서 패턴을 외삽하는 통계 엔진이 아니라, 적은 정보로 **설명(explanation)**을 만들고 "무엇이 아닌지, 무엇일 수 없는지"를 말하는 체계라는 주장. LLM은 반사실·인과 설명 능력이 없다고 봄.
- **체화·의도 비판**: Clark 자신의 예측 처리 이론도 **몸과 행동(embodied, active inference)**을 핵심에 둔다. 인간의 예측은 감각·운동·내수용(interoception) 신호에 접지되어 있고 생존 목표를 가진다. 텍스트 토큰만 예측하는 LM과는 예측 대상·목적이 다르다(이는 Clark 이론에서 도출되는 해석; Clark의 LLM 관련 구체 발언은 이번 조사에서 미확인).
- **정리**: 신경과학 증거는 "인간 언어 처리의 상당 부분이 **다음 단어 예측**을 포함한다"를 강하게 지지하지만, "인간은 **단지** 예측 기계다"까지는 지지하지 않는다.

## 핵심 개념·용어 정의
- **Predictive processing / predictive coding**: 상위 수준이 하위 수준 입력을 예측하고, 예측과 입력의 차이(오차)만 전달·학습하는 계층적 처리 원리.
- **Prediction error(예측 오차)**: 예측과 실제 입력의 차이. 학습·주의의 신호.
- **Free energy / surprise**: 모델 하에서 관측의 비개연성(놀람)과 그 상한. Friston 원리의 최소화 대상.
- **Active inference(능동 추론)**: 모델을 바꾸는 대신 **행동**해서 세계를 예측에 맞추는 방식으로 오차를 줄임. LLM과 인간의 결정적 차이 후보.
- **Brain score / encoding model**: 모델 내부 활성으로 뇌 신호를 선형 회귀 예측하는 정도.
- **Surprisal(놀람도)**: −log P(단어|맥락). 뇌 반응 크기와 상관.
- **Embodiment / grounding(체화 / 접지)**: 언어 기호가 감각·운동 경험 및 세계와 연결되는 것.

## 비판론(skeptic)과 반론의 대응
- **반론 측(강연자 믿음) 지지 근거**: Schrimpf, Goldstein, Caucheteux 세 논문은 모두 **독립 연구실, 서로 다른 측정법(fMRI, ECoG)**에서 "뇌도 다음 단어를 예측한다"는 결과로 수렴. "예측만 하는 시스템은 이해가 없다"는 skeptic 논증을 그대로 인간에 적용하면 인간 이해도 부정되는 **귀류(reductio)**가 생긴다 — 이것이 강연자 믿음의 가장 강한 형태.
- **제약**:
  1. 이 연구들은 **상관·부호화(encoding) 유사성**을 보인 것이지 "뇌 = LLM"이 아니다. 저자들 스스로 뇌가 더 긴 범위·계층적 예측을 한다고 강조(Caucheteux).
  2. 인간은 **적은 데이터**로 배운다(아이는 수천만 단어 수준, LLM은 수조 토큰) — Chomsky식 비판의 핵심. (정확한 수치는 출처별 차이가 커 슬라이드엔 "수십만 배 이상 차이" 정도로 완화 권장, 미검증.)
  3. 인간 예측은 몸·행동·목표·사회적 의도에 접지됨. Bender의 "소통 의도" 논점은 이 층위에서 여전히 유효.
  4. Altman 발언은 증거가 아니라 수사. 인용 시 "대중적 프레이밍"으로 표시.
- **결론적 위치**: "인간도 (어떤 의미에서는) 예측 기계다"는 **방어 가능**. "인간도 확률론적 앵무새다"는 Bender 정의(의미 참조 없음)를 그대로 받으면 **과장**이 된다. 권장 표현: "예측은 앵무새의 증거가 아니다 — 인간의 뇌도 예측으로 언어를 처리한다."

## 강연에 쓸 만한 포인트
- 인용(1개): Altman, 2022-12 — "i am a stochastic parrot, and so r u" (도발적 대중 프레이밍으로 소개하고 바로 한계 지적)
- 비유: "예측은 이해의 **반대말**이 아니라 **재료**일 수 있다." 뇌는 문장 끝을 미리 짐작하며 듣는다(청중에게 "나는 오늘 아침에 커피를 ___" 빈칸 채우기 즉석 실험 → 모두가 같은 단어를 예측 = 여러분도 방금 next-token prediction을 했다).
- 그림 아이디어: 좌 — 뇌 피질 지도(측두=짧은 예측, 전두·두정=긴 예측), 우 — transformer 층. 가운데 "≈ 부분적으로 대응" 화살표, 아래에 "≠ 몸·행동·의도" 주석.
- 균형 문구: "뇌도 예측한다. 하지만 뇌는 몸을 가지고 행동하며 예측한다."

## 원본 그림
- Caucheteux et al. 2023 Fig.1 (접근법 개요: LM 활성→뇌 매핑, 예측 창 추가) — https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c75f/10038805/b4868948eebe/41562_2022_1516_Fig1_HTML.jpg
- Caucheteux et al. 2023 Fig.2 — https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c75f/10038805/637277e42392/41562_2022_1516_Fig2_HTML.jpg
- Caucheteux et al. 2023 Fig.3 (피질 부위별 예측 거리 계층) — https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c75f/10038805/179834edae52/41562_2022_1516_Fig3_HTML.jpg
- Schrimpf 2021, Goldstein 2022 그림: 논문 PDF 내 Fig.1 참조 (직접 이미지 URL 미확인) — Goldstein PDF: https://hassonlab.princeton.edu/sites/g/files/toruqf3591/files/documents/Goldstein_et_al_NN_2022.pdf
