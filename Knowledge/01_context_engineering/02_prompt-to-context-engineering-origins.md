# Prompt engineering에서 Context engineering으로: 용어의 등장과 확산

이 파일은 용어를 확산시킨 짧은 글·발언 여러 개를 한데 묶었다.

| 자료 | 저자/기관 | 발행일 | URL | 유형 |
|---|---|---|---|---|
| X(Twitter) 게시물 | Tobi Lütke (Shopify CEO) | 2025-06-19 | https://twitter.com/tobi/status/1935533422589399127 | SNS 발언 |
| X(Twitter) 게시물 | Andrej Karpathy | 2025-06-25 | https://x.com/karpathy/status/1937902205765607626 | SNS 발언 |
| Context engineering | Simon Willison | 2025-06-27 | https://simonwillison.net/2025/Jun/27/context-engineering/ | 블로그 |
| The New Skill in AI is Not Prompting, It's Context Engineering | Philipp Schmid | 2025-06-30 | https://www.philschmid.de/context-engineering | 블로그 |
| Prompt engineering best practices | Anthropic (Claude 팀) | 2025-11-10 (2026 업데이트 문구 포함) | https://claude.com/blog/best-practices-for-prompt-engineering | 공식 블로그 |

> 참고: X 게시물 원문은 로그인 없이 직접 열람이 제한되어, 문구와 날짜는 Simon Willison의 글과 검색 결과(X 페이지 스니펫)로 교차 확인했다.

## 핵심 요약

- **Tobi Lütke**: "prompt engineering"보다 "context engineering"이 핵심 역량을 더 잘 묘사한다고 말했다. 요지는 LLM이 과제를 풀 수 있도록 필요한 맥락을 모두 제공하는 기술이라는 것.
- **Andrej Karpathy**: 6일 뒤 이에 동의하며, 사람들은 "프롬프트"를 일상에서 던지는 짧은 지시로 떠올리지만 실제 산업용 LLM 앱의 핵심은 다음 단계에 필요한 정보를 컨텍스트 창에 정확히 채워 넣는 일이라고 정리했다. 과제 설명, few-shot 예시, RAG, 관련 데이터, 도구, 상태·기록, 압축 등이 모두 여기에 포함된다고 봤다.
- **Simon Willison**: 용어는 "의도된 정의"가 아니라 사람들이 단어에서 "추론하는 정의"로 정착한다고 보고, "prompt engineering"은 챗봇에 글 치는 일로 가볍게 오해되지만 "context engineering"은 실제 작업의 복잡성을 더 잘 전달한다며 지지했다.
- **Philipp Schmid**: context engineering을 "정적 프롬프트"가 아닌 **동적 시스템**으로 정의했다. 적절한 정보와 도구를, 적절한 형식으로, 적절한 시점에 제공하는 시스템을 설계하는 분야라는 것. 그리고 오늘날 에이전트 실패 대부분은 모델 실패가 아니라 컨텍스트 실패라고 주장했다.
- **Anthropic(2025-11, 2026 갱신)**: prompt engineering은 context engineering의 기초 블록이며, Claude 5 세대에서는 둘이 수렴하여 "비계(scaffolding)는 줄이고 큐레이션은 늘리는" 방향이라고 설명한다. 반복되는 지시는 매번 프롬프트로 치지 말고 CLAUDE.md·skills로 옮기라고 권한다.

## 핵심 개념·용어 정의

- **Prompt engineering**: 한 번의 요청 문장을 잘 쓰는 기술. 단발성, 텍스트 중심.
- **Context engineering**: 모델이 한 스텝을 수행하기 직전 컨텍스트 창에 무엇이 들어갈지를 설계·조립하는 시스템 차원의 작업. 여러 턴, 여러 출처, 동적.
- **Schmid의 컨텍스트 7요소**: ① 지시/시스템 프롬프트 ② 사용자 프롬프트 ③ 상태/단기 기록 ④ 장기 기억 ⑤ 검색 정보(RAG) ⑥ 사용 가능한 도구 ⑦ 구조화 출력 형식.
- **Context failure**: 모델 능력이 아니라, 필요한 정보가 없거나 틀리거나 잡음이 많아서 생기는 실패.

## 강연에 쓸 만한 포인트

- **타임라인 슬라이드**: 2025-06-19 Lütke → 06-25 Karpathy → 06-27 Willison → 06-30 Schmid → 07월 LangChain·Chroma·Manus → 09-29 Anthropic 공식 글 → 2026-07 Anthropic "Claude 5 세대의 새 규칙". 한 달 사이 용어가 업계 표준어가 된 과정을 보여줌.
- **Schmid의 "싸구려 데모 vs 마법 같은 에이전트" 예**: 같은 모델에 "내일 잠깐 미팅 가능?"이라는 메일을 줄 때, 맥락이 없으면 기계적인 답을, 캘린더·이전 메일·상대 정보를 함께 주면 "목요일 오전 비어 있어요" 같은 자연스러운 답을 낸다. 청중 체감도가 높은 비교 데모.
- **7요소 원형 도식**: 가운데 "LLM 컨텍스트 창", 주변에 7개 입력원.
- Karpathy의 인용 1개(15단어 미만): "the delicate art and science of filling the context window" (Andrej Karpathy, X, 2025-06-25)
- **청중 질문 유도**: "여러분이 ChatGPT에 쓰는 한 줄은 모델이 보는 전체 입력의 몇 %일까?"

## Claude Code와의 연결점

- Claude Code에서 사용자가 친 프롬프트는 전체 컨텍스트의 극히 일부다. `/context`를 실행하면 시스템 프롬프트, 도구, MCP, skills 설명, CLAUDE.md, 메모리, 대화가 각각 몇 토큰인지 보여줘 "프롬프트 < 컨텍스트"를 눈으로 확인할 수 있다.
- Schmid의 7요소를 Claude Code 기능에 대응시키기: 지시=시스템 프롬프트·CLAUDE.md, 장기 기억=auto memory, RAG=Read/Grep/WebFetch, 도구=내장 도구·MCP, 구조화 출력=`--output-format json`.
