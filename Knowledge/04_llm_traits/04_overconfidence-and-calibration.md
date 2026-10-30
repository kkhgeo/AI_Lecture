# Overconfidence, Calibration, and Evaluation Biases (과신·보정과 판단 편향)

- **저자/기관**: Kadavath 외(Anthropic) / OpenAI(GPT-4 Technical Report; Kalai 외 논문에 재수록) / Xiong 외(NUS 등) / Cash, Oppenheimer 외(Carnegie Mellon) / Zheng 외(LMSYS, UC Berkeley 등) / Panickssery, Bowman, Feng / Liu 외(Stanford 등)
- **발행일**: Kadavath 외 2022-07-11(arXiv) / GPT-4 Technical Report 2023-03 / Xiong 외 2023-06-22, ICLR 2024 / Cash 외 Memory & Cognition, CMU 보도 2025-07-22 / Zheng 외 2023-06-09, NeurIPS 2023 / Panickssery 외 2024-04-15(NeurIPS 2024) / Liu 외 2023-07-06, TACL 2024 (2026-09-30 열람)
- **URL**:
  - https://arxiv.org/abs/2207.05221 (Language Models (Mostly) Know What They Know)
  - https://arxiv.org/abs/2509.04664 (GPT-4 calibration 그림 재수록)
  - https://arxiv.org/abs/2306.13063 (Can LLMs Express Their Uncertainty?)
  - https://www.cmu.edu/dietrich/news/news-stories/2025/trent-cash-ai-overconfidence
  - https://arxiv.org/abs/2306.05685 (Judging LLM-as-a-Judge)
  - https://arxiv.org/abs/2404.13076 (LLM Evaluators Recognize and Favor Their Own Generations)
  - https://arxiv.org/abs/2307.03172 (Lost in the Middle)
- **자료 유형**: 논문 | 기사(대학 보도자료)

## 핵심 요약
- **Calibration**: 모델의 확신(확률)이 실제 정답률과 일치하는 정도. Kadavath 외(2022-07)는 큰 사전학습 모델이 형식을 잘 갖춘 객관식·참거짓 문제에서 꽤 잘 보정되어 있고, 자기 답의 정답 확률 P(True)도 어느 정도 추정함을 보였다. 다만 낯선 과제에서는 "내가 아는가" 추정 P(IK)의 보정이 나빠졌다.
- GPT-4 Technical Report(2023-03)의 calibration 그림: 사전학습 모델은 대각선에 가깝게 보정되지만 RLHF(PPO) 후에는 보정이 크게 나빠진다. Kalai 외(2025-09)가 이 두 그림을 재수록해 "사후학습이 과신을 만든다"는 논지의 근거로 썼다.
- **말로 표현한 확신(verbalized confidence)은 과신 경향**: Xiong 외(ICLR 2024)는 GPT-4, LLaMA 2 Chat 등 5개 모델에서 확신을 말로 물으면 과신하는 경향이 일관되며, 사람의 확신 표현 습관을 모방한 것일 수 있다고 봤다. 여러 번 샘플링해 일관성을 보는 방법이 부분적으로만 개선.
- **메타인지 부족**: Cash 외(Memory & Cognition, 2025-07-22 보도)는 2년간 ChatGPT, Bard/Gemini, Claude Sonnet·Haiku를 사람과 비교했다. 사람은 성적이 나쁘면 사후 자기평가를 낮췄지만 LLM은 그러지 않았다. 예: Gemini는 그림 맞히기 20문항에서 10.03개를 예상했으나 평균 1개 미만을 맞혔고, 사후에 오히려 14.40개를 맞혔다고 추정. Sonnet이 상대적으로 덜 과신.
- **확신에 찬 문체 ≠ 정확성**: 03번 파일(Kalai 외)의 논지와 연결된다. 이진 채점은 "확신 있게 찍기"를 보상하므로, 단정적 어조 자체가 학습된 습관이다. (주의: "claiming certainty" 경향을 직접 정량화한 1차 자료는 이번 조사에서 별도로 찾지 못함 — 위 연구들로 간접 지지)
- **LLM-as-a-judge 편향**: Zheng 외(NeurIPS 2023)는 GPT-4 판정이 인간 선호와 80% 이상 일치하지만 position bias(먼저/나중 제시된 답 선호), verbosity bias(긴 답 선호), self-enhancement bias(자기 답 선호)가 있음을 보고.
- **Self-preference**: Panickssery 외(2024-04)는 GPT-4, Llama 2가 자기 생성물을 식별할 수 있고, 식별 능력과 자기 선호 편향 강도가 선형 상관함을 보였다(사람 평가상 품질이 같아도 자기 것을 높게 평가).
- **Position bias in long context**: Liu 외 "Lost in the Middle"(TACL 2024)은 긴 입력에서 관련 정보가 처음·끝에 있을 때 성능이 가장 높고 중간에 있으면 크게 떨어지는 U자형 패턴을 보고했다(최신 모델은 완화됐을 수 있음, 2026년 기준 재측정 미확인).

## 핵심 개념·용어 정의
- **Calibration (보정)**: "80% 확신"이라고 한 답들 중 실제로 약 80%가 맞는 상태.
- **Overconfidence (과신)**: 확신이 실제 정답률보다 높은 상태.
- **Verbalized confidence**: 토큰 확률이 아니라 모델이 말로 표현한 확신("확실합니다", "90%").
- **P(True) / P(IK)**: 제시된 답이 참일 확률 / 모델이 답을 알고 있을 확률에 대한 자기 추정(Kadavath 외).
- **Position bias**: 제시 순서나 문맥 내 위치에 따라 판단이 달라지는 편향.
- **Verbosity (length) bias**: 길고 자세한 답을 더 좋다고 판단하는 편향.
- **Self-preference (self-enhancement) bias**: 자기(또는 같은 계열 모델) 생성물을 더 높게 평가하는 편향.

## 강연에 쓸 만한 포인트
- 도식: calibration 곡선 두 개 나란히 — 사전학습(대각선 근처) vs RLHF 후(대각선에서 이탈). 제목 "친절해지면서 자기 확신을 잃는다".
- 비유: 틀려도 목소리가 줄지 않는 동료. 사람은 시험 후 "생각보다 못 봤네"라고 조정하지만 LLM은 그렇지 않다(Cash 외, 2025).
- 숫자: Gemini 예상 10.03개 → 실제 1개 미만 → 사후 추정 14.40개(20문항 기준).
- 편향 3종 세트 슬라이드: 위치(먼저 보여준 답), 길이(긴 답), 자기(내가 쓴 답). "모델에게 모델을 채점시킬 때 주의."
- 인용(1개): LLM은 확신을 말할 때 "tend to be overconfident" (Xiong et al., ICLR 2024)

## 원본 그림
- GPT-4 사전학습 모델 calibration plot(대각선에 근접) — https://arxiv.org/html/2509.04664v1/gpt4_calibration_pretrain.png
- GPT-4 PPO 후 calibration plot(보정 악화) — https://arxiv.org/html/2509.04664v1/gpt4_calibration_ppo.png
- Lost in the Middle의 U자형 위치별 정확도 그래프 — 이미지 URL 확보 못함(논문 Figure 1): https://arxiv.org/abs/2307.03172
- 그 외 없음

## 코딩 에이전트 사용과의 연결점
- 나타나는 모습: "이 수정으로 문제가 해결되었습니다"를 검증 없이 단정. 실패 후에도 같은 확신으로 다음 가설 제시. "확실합니다"라는 표현에 정보량이 거의 없다.
- 대응 1: 확신 표현 대신 검증 수단을 요구한다("어떻게 확인했나? 명령과 출력을 보여라"). 불확실한 부분을 따로 표시하게 한다.
- 대응 2: 코드 리뷰나 계획 평가를 모델에 맡길 때 같은 세션·같은 모델의 자기 평가를 피하고, 후보 순서를 바꿔 두 번 평가하며, 길이가 아니라 기준(테스트, 요구사항) 대비로 채점하게 한다.
- 대응 3: 긴 컨텍스트(큰 로그, 여러 파일)에서 중요한 지시는 앞이나 끝에 두고, CLAUDE.md/AGENTS.md는 짧게 유지한다. 필요한 부분만 잘라 보여주면 위치 편향의 영향이 줄어든다.
