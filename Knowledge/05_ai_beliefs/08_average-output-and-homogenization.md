# 왜 AI 결과물은 평균으로 수렴하는가: mode collapse, 균질화, model collapse, AI slop (평균적 결과물과 균질화)

- **저자/기관**: 복수 출처 (아래 목록)
  - Kirk et al. (UCL·Meta), "Understanding the Effects of RLHF on LLM Generalisation and Diversity" — arXiv 2310.06452 (2023-10-10 제출, 2024-02-19 개정; ICLR 2024)
  - Doshi & Hauser, "Generative AI enhances individual creativity but reduces the collective diversity of novel content" — *Science Advances* 10(28), 2024-07-12
  - Anderson, Shah & Kreminski, "Homogenization Effects of Large Language Models on Human Creative Ideation" — ACM Creativity & Cognition (C&C '24), 2024-06
  - Jiang et al. (UW·AI2 등), "Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)" — NeurIPS 2025 (Best Paper)
  - Shumailov et al., "AI models collapse when trained on recursively generated data" — *Nature* 631, 2024-07-25
  - Ted Chiang, "ChatGPT Is a Blurry JPEG of the Web" — *The New Yorker*, 2023-02-09
  - Simon Willison, "Slop is the new name for unwanted AI-generated content" — 2024-05-08; Merriam-Webster 2025 올해의 단어 "slop"(2025-12-15), Macquarie 2025 올해의 단어 "AI slop"(2025-11)
  - 반대 근거: Si, Yang & Hashimoto, "Can LLMs Generate Novel Research Ideas?" — arXiv 2409.04109 (2024-09-06; ICLR 2025); Si, Hashimoto & Yang, "The Ideation-Execution Gap" — arXiv 2506.20803 (2025-06-25); Hubert, Awa & Zabelina, *Scientific Reports* 2024-02 (GPT-4 divergent thinking)
- **발행일**: 위 출처별 표기 (2026-09-30 열람)
- **URL**:
  - https://arxiv.org/abs/2310.06452
  - https://www.science.org/doi/10.1126/sciadv.adn5290 (접속 차단(403), 요약은 SSRN·보도로 확인: https://papers.ssrn.com/abstract=4535536)
  - https://arxiv.org/abs/2402.01536
  - https://arxiv.org/abs/2510.22954
  - https://www.nature.com/articles/s41586-024-07566-y
  - https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web
  - https://simonwillison.net/2024/May/8/slop/ , https://simonwillison.net/2025/dec/15/2025-word-of-the-year-slop
  - https://arxiv.org/abs/2409.04109 , https://arxiv.org/abs/2506.20803
- **자료 유형**: 논문 + 기사 + 블로그

## 핵심 요약
- **다음 토큰 예측의 기본 성향**: LLM은 학습 분포에서 그럴듯한(확률 높은) 다음 토큰을 고르도록 훈련된다. 기본 설정에서는 흔한 표현, 흔한 구성이 나오기 쉽다. (이 문장은 원리 설명을 강연자가 재구성한 것이며 특정 논문의 수치 근거는 아님.)
- **RLHF가 다양성을 줄인다 (Kirk et al., 2023)**: RLHF는 SFT보다 새로운 입력에 더 잘 일반화하지만, 여러 척도에서 출력 다양성을 **유의하게 줄인다**. 일반화와 다양성 사이의 trade-off. 흔히 "mode collapse"라고 부르는 현상의 대표 실증.
- **모델끼리도 닮아 간다 (Artificial Hivemind, NeurIPS 2025)**: 실제 개방형 질문 2.6만 개(INFINITY-CHAT)로 70개 이상 모델을 평가. 한 모델 안에서 같은 답을 반복하고(intra-model), 서로 다른 회사 모델끼리도 비슷한 답으로 수렴(inter-model)하는 "인공 군집 사고"를 보고.
- **개인은 좋아지고 집단은 좁아진다 (Doshi & Hauser, 2024)**: 약 300명 작가가 GPT-4 아이디어(0개/1개/최대 5개)를 받아 8줄 이야기를 씀. AI 아이디어를 받은 이야기는 더 창의적·잘 쓰였다고 평가, 특히 창의성 낮은 작가에게 효과가 컸다. 그러나 AI 도움 이야기끼리는 **서로 더 비슷했다** → 개인 이득 vs 집단 새로움 감소의 사회적 딜레마. (참가자 수는 보도마다 약 300명/500명으로 다름 — 원문 확인 필요)
- **사람의 발상도 균질화 (Anderson et al., C&C 2024)**: 36명 비교 실험. ChatGPT 사용자들은 아이디어를 더 많고 자세하게 냈지만, **사용자 간 아이디어가 의미적으로 덜 구별**되었고, 자기 아이디어에 대한 책임감을 덜 느꼈다.
- **Model collapse (Shumailov et al., Nature 2024)**: AI 생성 데이터를 무분별하게 재학습하면 원래 분포의 **꼬리(tails, 드문 것)가 사라지고** 세대가 갈수록 품질이 비가역적으로 떨어진다. LLM·VAE·GMM 모두에서 관찰. 평균으로의 수렴이 "재귀적으로" 강화되는 메커니즘.
- **"흐릿한 JPEG" 비유 (Chiang, 2023)**: ChatGPT는 웹을 손실 압축한 것과 같아서, 정확한 원본 대신 문법적으로 매끄러운 근사를 돌려준다. 매끄러움 때문에 근사임을 알아채기 어렵다.
- **AI slop 담론**: Willison이 2024-05 "slop"(요청하지 않은, 검토되지 않은 AI 생성물)을 명명·확산. Macquarie(2025, "AI slop"), Merriam-Webster(2025, "slop")가 올해의 단어로 선정 → "평균적·저품질 대량 생산물"에 대한 사회적 피로가 언어로 굳음.
- **반대 근거 — AI가 평균 인간보다 낫다는 결과도 있다**: Si et al.(2024)에서 NLP 연구자 79명이 블라인드로 평가한 결과 LLM 연구 아이디어가 전문가 아이디어보다 **참신성에서 통계적으로 유의하게 높고(p<0.05)**, 실현 가능성은 약간 낮았다. GPT-4는 발산적 사고 과제 3종에서 인간 151명보다 독창적이었다(Hubert et al., 2024). BCG 실험(Dell'Acqua et al., 2023)도 AI 사용 시 품질이 40% 이상 높았다. **즉 "평균 이하"가 아니라 "평균 이상이지만 서로 닮은" 결과물**이 더 정확한 묘사다.
- **그러나 실행하면 역전 (Si et al., 2025 Ideation-Execution Gap)**: 전문가 43명이 무작위 배정된 아이디어를 각자 100시간 이상 구현해 4쪽 논문으로 만든 뒤 재평가하자, LLM 아이디어 점수가 모든 지표에서 전문가 아이디어보다 **유의하게 더 많이 떨어졌고**, 여러 지표에서 순위가 뒤집혔다. 같은 2024 연구에서 LLM이 만든 시드 아이디어 4,000개 중 중복 아닌 것은 약 200개뿐이었다(다양성 부족).

## 핵심 개념·용어 정의
- **Mode collapse**: 생성 모델이 가능한 출력 분포의 일부 봉우리(mode)에만 몰려 다양성을 잃는 현상. LLM에서는 주로 RLHF·instruction tuning 이후 관찰.
- **RLHF (Reinforcement Learning from Human Feedback)**: 사람 선호 데이터로 보상 모델을 학습하고 그 보상을 최대화하도록 모델을 조정하는 방법. "선호되는 평균적 답"으로 끌어당기는 힘이 생긴다.
- **Homogenization (균질화)**: 여러 사람(또는 여러 모델)의 산출물이 서로 비슷해지는 현상. 개인 품질과 별개인 **집단 수준** 지표.
- **Model collapse**: AI 생성 데이터를 재귀적으로 학습하며 분포 꼬리가 사라지는 세대 간 퇴화.
- **Artificial Hivemind**: 서로 다른 LLM들이 개방형 질문에 거의 같은 답을 내는 모델 간 균질화(Jiang et al., 2025).
- **AI slop**: 대량으로 만들어진 저품질·미검토 AI 생성 콘텐츠.
- **Ideation-execution gap**: 아이디어 단계에서 좋아 보이던 것이 실제 실행 후 평가에서 떨어지는 격차.

## 비판론(skeptic)과 반론의 대응
- **비판론**: "AI는 평균적인(generic) 결과물만 낸다. 완성도 높은 결과물은 만들 수 없다."
  - 근거: RLHF 다양성 감소(Kirk), 모델 간 수렴(Hivemind), 사용자 간 균질화(Doshi & Hauser, Anderson), 재귀 학습 붕괴(Shumailov), slop 담론, 실행 후 역전(Ideation-Execution Gap).
- **반론**: "평균 인간보다는 이미 낫다."
  - 근거: 참신성 평가 우위(Si 2024), 발산적 사고 과제 우위(Hubert 2024), 컨설팅 과제 품질 향상(Dell'Acqua 2023), 하위 작가의 창의성 향상(Doshi & Hauser).
- **정리(강연자 입장에 맞춘 해석)**: 두 증거는 모순이 아니다. AI는 **"평균 이상의 초안"을 빠르게, 그러나 모두에게 비슷하게** 준다. 초안이 "완성된 고품질 결과물"이 되려면 선택·실행·검증이라는 마지막 구간이 필요하고, 실행 후 평가(Ideation-Execution Gap)가 보여 주듯 그 구간에서 차이가 벌어진다. → 비판론의 "평균적" 지적에 동의하되, "그래서 쓸모없다"가 아니라 "그래서 완성은 사람 몫"으로 연결.
- **주의**: 벤치마크형 창의성 과제(AUT 등)는 "창의적 잠재력"을 재는 것이지 실제 창작 성취가 아니라고 Hubert et al. 스스로 명시. 또한 최신 모델(2026)은 2023–2024 실험 모델보다 강하므로 수치를 현재 모델에 그대로 일반화하면 안 된다.

## 강연에 쓸 만한 포인트
- **한 장 요약 그림 아이디어**: 종 모양 분포 두 개. 왼쪽 "사람들의 결과물"(넓게 퍼짐), 오른쪽 "AI 도움 결과물"(평균은 오른쪽으로 이동했지만 폭이 좁아짐). 캡션: "평균은 올리고, 폭은 좁힌다."
- **Model collapse 그림 아이디어**: 세대 0→n으로 갈수록 분포 꼬리가 잘려 나가는 히스토그램 → "드문 것이 먼저 사라진다."
- **비유**: 흐릿한 JPEG(Chiang) — 전체 인상은 맞지만 확대하면 디테일이 뭉개진다. 연구 결과물의 가치는 바로 그 디테일에 있다.
- **숫자 3개**: 4,000개 중 약 200개만 고유(아이디어 다양성), 전문가 43명 × 100시간+ 실행 후 순위 역전, 70개 이상 모델이 비슷한 답으로 수렴.
- **대학원생 메시지**: AI 초안이 "평균 이상"이라서 오히려 위험하다. 그럴듯하므로 멈추기 쉽고, 모두가 비슷한 초안에서 멈추면 분야 전체가 좁아진다.
- 인용(1개): "ChatGPT is a blurry JPEG of all the text on the Web." — Ted Chiang, *The New Yorker* (2023-02-09) [원문 문장 표현은 열람 불가로 재확인 필요 — 제목 "ChatGPT Is a Blurry JPEG of the Web"만 인용해도 충분]

## 원본 그림
- Si et al. (2024) Figure 1(연구 설계 개요: 79명 전문가가 세 조건 49개 아이디어 블라인드 리뷰), Figure 2(조건별 지표 비교) — 이미지 URL 미확인, 원문 https://arxiv.org/html/2409.04109 에서 직접 확인
- Shumailov et al. (2024) 세대별 분포 꼬리 소실 그림 — 이미지 URL 미확인, 원문 PDF https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf
- Artificial Hivemind 모델 간 유사도 그림 — 이미지 URL 미확인, https://arxiv.org/abs/2510.22954
- 그 외: 없음
