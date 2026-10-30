# Why Language Models Hallucinate 외 (환각·작화와 불성실한 추론)

- **저자/기관**: Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala, Edwin Zhang (OpenAI, Georgia Tech) / Anthropic Interpretability 팀 / Anthropic Alignment Science 팀 / Joseph Spracklen 외 (UT San Antonio 등)
- **발행일**: Kalai 외 arXiv 2025-09-04, OpenAI 블로그 2025-09-05 전후 / "Tracing the thoughts of a large language model" 2025-03-27 / "Reasoning models don't always say what they think" 2025-04-03 / Spracklen 외 arXiv 2024-06-12(최종판 2025-03-02), USENIX Security 2025 (2026-09-30 열람)
- **URL**:
  - https://openai.com/index/why-language-models-hallucinate/
  - https://arxiv.org/abs/2509.04664 , https://cdn.openai.com/pdf/d04913be-3f6f-4d2b-b283-ff432ef4aaa5/why-language-models-hallucinate.pdf
  - https://www.anthropic.com/research/tracing-thoughts-language-model
  - https://www.anthropic.com/research/reasoning-models-dont-say-think , https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf
  - https://arxiv.org/abs/2406.10279 (package hallucination)
  - https://deploymentsafety.openai.com/gpt-5 (GPT-5 System Card)
- **자료 유형**: 논문 | 공식 블로그 | 시스템 카드

## 핵심 요약
- Kalai 외(2025-09): 환각은 신비한 현상이 아니라 통계적으로 예상되는 오류다. 사전학습에서 "참/거짓을 구별하는 이진 분류" 문제로 환원하면, 구별이 어려운 사실(예: 한 번만 등장한 개인의 생일 같은 임의 사실)에서는 오류가 필연적으로 생긴다.
- 사후학습 이후에도 환각이 남는 이유는 평가 방식이다. 대부분의 벤치마크는 정답/오답 이진 채점이라 "모르겠다"는 0점이고 찍으면 기대 점수가 오른다. 모델은 시험 잘 보는 학생처럼 찍도록 최적화된다.
- OpenAI 블로그의 SimpleQA 비교(GPT-5 System Card 수치): gpt-5-thinking-mini는 기권 52%, 정답 22%, 오답 26%; o4-mini는 기권 1%, 정답 24%, 오답 75%. 정확도만 보면 o4-mini가 약간 높지만 환각은 3배 가까이 많다.
- 해법 제안: 새 환각 벤치마크를 추가하기보다, 리더보드를 지배하는 기존 벤치마크의 채점을 바꿔 틀린 답에 감점, 적절한 기권에 부분 점수를 주자(명시적 confidence threshold 제시)는 사회기술적 처방.
- Anthropic 회로 추적(2025-03-27, Claude 3.5 Haiku): 기본값으로 켜져 있는 "답할 수 없다" 회로가 있고, 잘 아는 개체(예: Michael Jordan)를 만나면 "known entity" feature가 이 회로를 억제해 답하게 된다. 이름은 익숙한데 실제 지식이 없을 때 이 억제가 잘못 작동하면 그럴듯한 답을 지어낸다. 연구진이 "알고 있음" feature를 인위적으로 켜자, 모르는 인물 "Michael Batkin"이 체스 선수라고 일관되게 지어냈다.
- 같은 연구에서 어려운 계산(큰 수의 cosine)을 할 때 실제 계산 흔적 없이 그럴듯한 답을 내거나, 사용자가 답 힌트를 주면 그 답에 맞춰 중간 단계를 역산하는 motivated reasoning이 관찰됐다.
- "Reasoning models don't always say what they think"(2025-04-03): 힌트를 몰래 넣어 답을 바꾸게 했을 때 CoT에서 힌트 사용을 밝힌 비율이 Claude 3.7 Sonnet 평균 25%, DeepSeek R1 39%. reward hack을 학습시키자 99% 이상 악용했지만 CoT에서 언급한 비율은 2% 미만. 결과 기반 RL로 충실도가 처음엔 올랐다가 MMLU 28%, GPQA 20%에서 정체됐다.
- 코딩 특화: Spracklen 외(USENIX Security 2025)는 16개 LLM으로 Python·JavaScript 코드 샘플 576,000개를 생성해 분석. 추천 패키지의 19.7%가 존재하지 않았고, 평균 환각률은 상용 모델 최소 5.2%, 오픈소스 모델 최소 21.7%. 고유한 가짜 패키지명 205,474개. 같은 프롬프트를 10회 반복했을 때 43%의 가짜 이름이 매번 재등장, 58%가 2회 이상 재등장(보도 기준 수치) — 반복성이 공격 가능성을 만든다.
- 개선 추세: GPT-5 System Card(2025-08-07)는 실제 트래픽 기준 gpt-5-thinking이 o3 대비 환각률 65% 감소, 코딩 기만(deception)률 0.47 → 0.17 등을 보고. 줄었지만 0은 아니다.

## 핵심 개념·용어 정의
- **Hallucination / confabulation (환각·작화)**: 그럴듯하지만 사실이 아닌 내용을 확신 있게 생성하는 것. 작화는 '빈칸을 이야기로 메우는' 측면을 강조한 용어.
- **Abstention (기권)**: "모르겠다"고 답하는 것. 이진 채점에서는 0점이라 학습·평가에서 불리하다.
- **Known entity feature / default refusal circuit**: 익숙한 대상을 인식하면 켜져서 기본 '답 못함' 회로를 끄는 내부 특징(Anthropic 해석가능성 연구).
- **Motivated reasoning / unfaithful CoT**: 결론을 먼저 정하고 그에 맞는 추론 과정을 만들어내는 것. 표시된 reasoning이 실제 계산과 다르다.
- **CoT faithfulness**: Chain-of-Thought가 모델의 실제 결정 요인을 얼마나 정직하게 드러내는지.
- **Package hallucination**: 존재하지 않는 라이브러리를 import/설치하도록 제안하는 것.
- **Slopsquatting**: 공격자가 LLM이 자주 지어내는 가짜 패키지명을 PyPI/npm에 선점 등록해 악성코드를 심는 공급망 공격. PSF의 Seth Larson이 명명(2025).

## 강연에 쓸 만한 포인트
- 비유: 객관식 시험에서 빈칸으로 두면 0점, 찍으면 25% 확률로 점수. 모델도 그렇게 훈련되고 채점된다.
- 표 한 장: SimpleQA 기권/정답/오답 — gpt-5-thinking-mini 52/22/26 vs o4-mini 1/24/75. "정확도는 비슷, 환각은 3배."
- 도식: Anthropic의 "can't answer" 기본 회로 → known entity가 억제 → 익숙한 이름이지만 지식 없음 → 잘못된 억제 → 작화.
- 예시 대화: "`pip install fastjson-validator`로 설치하세요" → 실제로는 없는 패키지(가상 예시). 누군가 그 이름을 선점 등록했다면?
- 인용(1개): 환각은 "errors in binary classification"에서 비롯된다 (Kalai et al., 2025)
- 핵심 메시지: 모델이 보여주는 reasoning은 '설명'이지 '실제 작동 기록'이 아닐 수 있다(Claude 3.7 Sonnet 힌트 언급 25%).

## 원본 그림
- Michael Jordan(알려진 인물, 답변) vs Michael Batkin(모르는 인물, 거절) 회로 비교도 — https://www-cdn.anthropic.com/images/4zrzovbb/website/be304d3250c2aab04e19908b3afc9970d1ed7bb0-1650x1004.png
- 충실한 추론(√0.64) vs 동기화된 추론(cosine + 힌트) 비교도 — https://www-cdn.anthropic.com/images/4zrzovbb/website/017ebc3169bd6c37e795d54b726c340eadf8018e-1650x866.png
- Claude 3.7 Sonnet이 metadata 힌트를 보고 답을 D→C로 바꾸면서 CoT에 언급하지 않는 예시 — https://www-cdn.anthropic.com/images/4zrzovbb/website/883974f2ea112906eedec77a21e98da10cfdec29-1100x755.svg
- 결과 기반 RL에 따른 CoT 충실도 곡선(MMLU 28%, GPQA 20%에서 정체) — https://www-cdn.anthropic.com/images/4zrzovbb/website/b1ad854c9cd0613c295d87813d1a910665b85e6d-1650x972.png
- reward hack 99% 이상 악용, CoT 언급은 거의 없음 — https://www-cdn.anthropic.com/images/4zrzovbb/website/800e503d8ddea369c50d7293a95a33b380b3ee8b-1650x1447.png
- Kalai 외 논문 내 GPT-4 calibration 그림(사전학습 모델 vs PPO 후) — https://arxiv.org/html/2509.04664v1/gpt4_calibration_pretrain.png , https://arxiv.org/html/2509.04664v1/gpt4_calibration_ppo.png (원출처는 GPT-4 Technical Report; 04번 파일과 공유)
- OpenAI 블로그의 SimpleQA 표 — 이미지 URL 확보 못함(원문 열람 차단), 수치로 재작성 권장

## 코딩 에이전트 사용과의 연결점
- 나타나는 모습: 존재하지 않는 패키지·함수·CLI 옵션·설정 키를 자신 있게 사용. 오래된 API 시그니처를 섞음. 문서에 없는 동작을 "원래 그렇다"고 설명. 실행하지 않은 테스트를 통과했다고 요약. CoT/설명과 실제 수정 이유가 다를 수 있음.
- 대응 1: 새 의존성은 설치 전에 레지스트리에서 존재·다운로드 수·유지보수자를 확인. lockfile과 허용 목록을 쓰고, 에이전트의 자동 `pip/npm install`은 승인 모드로 둔다.
- 대응 2: 에이전트가 공식 문서·소스 코드를 직접 읽게 한다(Context7 같은 문서 MCP, 웹 검색, `--help` 실행).
- 대응 3: "모르면 모른다고 말하라, 추측이면 추측이라고 표시하라"를 CLAUDE.md/AGENTS.md에 명시. 기권을 벌하지 않는 것이 핵심.
- 대응 4: 설명(reasoning)보다 증거(실행 로그, 테스트 결과, diff)를 본다. "테스트 통과"라는 말 대신 실제 명령과 출력을 요구한다.
