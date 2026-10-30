# Context Rot: How Increasing Input Tokens Impacts LLM Performance

- **저자/기관**: Kelly Hong, Anton Troynikov, Jeff Huber (Chroma)
- **발행일**: 2025-07-14
- **URL**: https://www.trychroma.com/research/context-rot (구 주소 research.trychroma.com/context-rot 에서 리다이렉트)
- **자료 유형**: 연구 (기술 보고서, 코드 공개)

## 핵심 요약

- 모델들이 "바늘 찾기(Needle in a Haystack)" 벤치마크에서 거의 만점을 받지만, 이는 단순 어휘 일치 과제일 뿐이라는 문제의식에서 출발했다.
- Anthropic·OpenAI·Google·Alibaba의 최신 모델 **18개**를 대상으로, 입력 길이만 늘리고 과제 난이도는 고정한 통제 실험을 했다.
- 결론: 모델은 입력 길이 전 구간에서 성능이 균일하지 않으며, 길이가 늘면 단순한 과제에서도 성능이 떨어진다. 이 현상을 **context rot**이라 부른다.
- 성능 저하는 단순 길이뿐 아니라 질문-정답 유사도, 방해 정보(distractor), 문서 구조에 따라 달라진다. 즉 "정보가 들어있느냐"보다 "어떻게 제시되느냐"가 중요하다.
- 실용적 함의는 곧 context engineering이다: 관련 정보만 골라, 잘 구조화해서 넣어야 한다.

## 핵심 개념·용어 정의

| 실험 | 발견 |
|---|---|
| Needle-question 유사도 | 질문과 정답 문장의 의미 유사도가 낮을수록 길이 증가에 따른 성능 하락이 빠르다 |
| Distractor(방해 문장) | 방해 문장 1개만 있어도 성능 저하, 4개면 더 악화. 방해 문장마다 영향이 불균일 |
| Needle-haystack 유사도 | 정답이 주변 문서와 의미상 섞여 들지 않을 때 오히려 더 잘 찾음 |
| Haystack 구조 | 논리적 흐름이 유지된 원문보다 **문장을 무작위로 섞은 문서에서 성능이 더 좋았다**(18개 모델 일관) |
| LongMemEval | 관련 부분만 준 약 300토큰 "focused" 입력이 약 113k 토큰 "full" 입력보다 모든 모델에서 확연히 우수 |
| 반복 단어 복사 | 입력·출력 길이가 길어질수록 성능이 불균일해지고 엉뚱한 단어 생성 증가 |

- **모델별 실패 양상**: Claude 계열은 불확실하면 답을 보류(abstention)하는 경향, GPT 계열은 확신에 찬 오답(hallucination) 경향이 상대적으로 높았다.
- 규모: 약 19만 4천 회 LLM 호출.

## 강연에 쓸 만한 포인트

- **핵심 그래프 재현 아이디어**: x축 입력 토큰 수, y축 정확도. "focused(300토큰)" 막대 vs "full(113k 토큰)" 막대 비교가 가장 직관적.
- **의외성 포인트**: "문장을 뒤섞은 문서가 더 잘 읽힌다" → 청중의 직관을 깨는 질문으로 사용.
- **메시지**: 컨텍스트 창 크기(200k, 1M)는 "넣을 수 있는 양"이지 "잘 쓸 수 있는 양"이 아니다.
- **데모 아이디어**: 긴 문서 한 권 전체를 넣고 질문 vs 관련 절만 잘라 넣고 질문, 답변 품질 비교.
- 인용(1개): "LLMs do not maintain consistent performance across input lengths" (Chroma, 2025)

## Claude Code와의 연결점

- Anthropic 공식 글(01번)과 Claude Code best practices(14번)가 "컨텍스트가 찰수록 성능이 떨어진다"를 모든 권장 사항의 전제로 삼는데, 그 실증 근거로 이 연구를 제시하면 좋다.
- 실습: `/context`로 현재 사용률을 보여주고, 긴 세션에서 초기 지시를 "잊는" 현상을 관찰한 뒤 `/clear` 또는 `/compact`로 회복.
- "focused vs full" 원리 = subagent에게는 필요한 것만 담은 과제 프롬프트를 주고, 메인에는 요약만 받는 구조.
