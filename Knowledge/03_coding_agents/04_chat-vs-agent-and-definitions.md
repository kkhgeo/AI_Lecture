# Agent 정의 모음: chatbot vs copilot vs agent, vibe coding vs agentic engineering (슬라이드용 정의집)

- **저자/기관**: 복수 출처 — Simon Willison(개인 블로그), Andrej Karpathy(X 게시물, 개인 블로그), Anthropic(Claude Code 문서, 엔지니어링 블로그), OpenAI(엔지니어링 블로그)
- **발행일**: 출처별로 아래 표기 (2026-09-29 열람)
- **URL**:
  - Simon Willison, "I think "agent" may finally have a widely enough agreed upon definition to be useful jargon now" (2025-09-18): https://simonwillison.net/2025/Sep/18/agents/
  - Simon Willison, "Not all AI-assisted programming is vibe coding (but vibe coding rocks)" (2025-03-19): https://simonwillison.net/2025/Mar/19/vibe-coding/
  - Andrej Karpathy, "vibe coding" 최초 게시물 (2025-02-02, UTC): https://x.com/karpathy/status/1886192184808149383
  - Andrej Karpathy, vibe coding 1주년 회고 및 "agentic engineering" 제안 (2026-02-04, UTC): https://x.com/karpathy/status/2019137879310836075
  - Andrej Karpathy, "Sequoia Ascent 2026 summary" (2026-04-30): https://karpathy.bearblog.dev/sequoia-ascent-2026/
  - Anthropic, "Effective context engineering for AI agents" (2025-09-29): https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - Claude Code Docs, "How Claude Code works" (발행일 표기 없음): https://code.claude.com/docs/en/how-claude-code-works
- **자료 유형**: 블로그 (+ 공식문서, 엔지니어링 블로그 보조)

## 핵심 요약
- **Agent의 합의된 최소 정의**: Simon Willison은 X에서 211개의 정의를 모아 13개 유형으로 묶어 본 뒤, 업계가 "도구를 루프로 돌려 목표를 달성하는 LLM"이라는 정의로 수렴했다고 정리했다(2025-09-18). 그는 이 용어가 수십 년간 합의 없이 쓰였다는 점(1994년 논문의 지적)도 함께 언급한다.
- 같은 시기 Anthropic도 agent를 "LLM이 도구를 루프 안에서 자율적으로 사용하는 것"으로 요약했다(2025-09-29). OpenAI의 Codex 글(2026-01-23)도 agent의 심장을 "agent loop"로 설명한다. 즉 2025년 하반기 이후 세 주체의 정의가 **LLM + tools + loop + goal**로 겹친다.
- **Vibe coding (Karpathy, 2025-02-02)**: 분위기에 몸을 맡기고 코드가 존재한다는 사실 자체를 잊는 코딩 방식. diff를 읽지 않고 변경을 모두 수락하고, 에러 메시지는 그대로 LLM에 붙여 넣는 식. Karpathy는 이를 주말 토이 프로젝트용이라고 했다. (Willison의 글은 이 게시물 날짜를 2월 6일로 적었으나, 게시물 ID에서 계산한 시각은 2025-02-02 23:17 UTC다.)
- **Willison의 구분 (2025-03-19)**: AI 도움을 받는 모든 프로그래밍이 vibe coding은 아니다. 생성된 코드를 리뷰하고 테스트하고 이해한다면 그것은 그냥 소프트웨어 개발이다. vibe coding이라는 말을 AI 보조 프로그래밍 전체로 넓혀 쓰는 것에 반대했다.
- **Agentic engineering (Karpathy, 2026-02-04)**: 1주년 회고 게시물에서 Karpathy는 LLM 에이전트로 프로그래밍하는 것이 전문가의 기본 작업 방식이 되었으며, 다만 감독과 검증이 더해졌다고 보고 새 이름을 제안했다. "agentic"은 코드를 직접 쓰기보다 에이전트를 지휘하고 감독한다는 뜻, "engineering"은 배우고 숙련할 수 있는 전문성이 있다는 뜻이다. (주의: x.com 원문은 직접 열람하지 못했고, 검색 결과 요약과 보도를 통해 확인했다.)
- **Sequoia Ascent 2026 (2026-04-30)**: Karpathy는 vibe coding이 누구나 소프트웨어를 만들 수 있게 **바닥(floor)을 높이고**, agentic engineering은 보안·유지보수성·정확성을 지키면서 전문가의 **천장(ceiling)을 높인다**고 대비했다.
- **Chatbot vs copilot vs agent**: 세 범주를 한 번에 정의한 단일 1차 출처는 찾지 못했다. 아래 분류표는 위 출처들(Claude Code 문서의 inline code assistant와의 대비, Anthropic·Willison·OpenAI의 agent 정의)을 근거로 강연자가 재구성한 것이다.

## 핵심 개념·용어 정의
- **Chatbot (대화형 LLM)**: 사람이 질문하고 모델이 텍스트로 답한다. 코드를 실행하거나 파일을 바꾸지 않으며, 결과를 옮겨 붙이고 실행하는 것은 사람 몫이다. Claude Code 문서의 표현대로 도구가 없으면 모델은 텍스트로만 응답할 수 있다.
- **Copilot / autocomplete (inline code assistant)**: 에디터 안에서 현재 파일과 커서 주변을 보고 다음 코드를 제안한다. 사람이 운전하고 AI는 제안만 한다. Claude Code 문서는 이런 도구를 "현재 파일만 보는 inline code assistant"로 부르며 자신과 구분한다. (주의: 2025–2026년에는 Copilot류 제품도 agent 모드를 갖추어 제품명과 범주가 1:1로 대응하지 않는다.)
- **Agent / coding agent**: 목표를 받으면 도구(파일 읽기·수정, shell, 테스트, 웹)를 루프로 사용해 스스로 계획하고 실행하고 검증한 뒤 결과를 보고한다. 프로젝트 전체를 보고 여러 파일을 조율해 수정한다. 예: Claude Code, Codex.
- **Agent (Willison, 2025)**: 목표를 달성하기 위해 도구를 루프로 실행하는 LLM.
- **Agent (Anthropic, 2025)**: LLM이 도구를 루프 안에서 자율적으로 사용하는 것. 더 엄밀하게는 workflow(정해진 경로)와 구분되는, 스스로 경로를 정하는 시스템(01번 파일).
- **Harness**: 모델을 감싸 도구와 context를 제공하는 소프트웨어 층(02·03번 파일).
- **Vibe coding**: 코드를 읽거나 이해하지 않고 결과만 보며 AI에게 맡기는 방식. 진입장벽을 낮춘다.
- **Agentic engineering**: 에이전트를 지휘·감독하되 명세, 테스트, 리뷰, 권한 관리로 품질과 책임을 사람이 지는 전문적 실천.

## 강연에 쓸 만한 포인트
- 분류표 슬라이드 (강연자 재구성):
  | 구분 | 누가 운전하나 | 보는 범위 | 행동 | 검증 |
  |---|---|---|---|---|
  | Chatbot | 사람 | 대화창에 붙인 내용 | 텍스트 답변 | 사람 |
  | Copilot/autocomplete | 사람 | 현재 파일·커서 주변 | 코드 제안 | 사람 |
  | Coding agent | 에이전트(사람은 감독) | 프로젝트 전체+터미널 | 파일 수정·명령 실행 | 에이전트가 테스트 후 사람이 리뷰 |
- 한 줄 공식: **Agent = LLM + Tools + Loop + Goal**. 네 요소 중 하나라도 빠지면 무엇이 되는지 묻는 퀴즈형 슬라이드(Tools가 빠지면 chatbot, Loop가 빠지면 1회성 도구 호출, Goal이 없으면 멈출 기준이 없다).
- 타임라인: 2024-12 Anthropic "Building effective agents" → 2025-02-02 Karpathy "vibe coding" → 2025-03-19 Willison "모든 AI 코딩이 vibe coding은 아니다" → 2025-09 Willison·Anthropic 정의 수렴 → 2026-01-23 OpenAI Codex 루프 공개 → 2026-02-04 Karpathy "agentic engineering" → 2026-04-30 Sequoia Ascent의 floor/ceiling 대비.
- 대학원생 메시지: 연구 코드는 재현성과 정확성이 핵심이므로 vibe coding이 아니라 agentic engineering의 태도(명세, 테스트, diff 리뷰, 책임)가 필요하다.
- 숫자: Willison이 모은 정의 211개, 13개 유형.
- 인용(1개): "An LLM agent runs tools in a loop to achieve a goal." — Simon Willison (2025-09-18)

## 원본 그림
- Willison 글, Karpathy 게시물·블로그: 슬라이드용 원본 다이어그램 없음.
- 대신 쓸 만한 그림: Anthropic "Autonomous agent" 다이어그램 — https://www-cdn.anthropic.com/images/4zrzovbb/website/58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.png (01번 파일 참조), OpenAI "Agent loop" 다이어그램 — https://images.ctfassets.net/kftzwdyauwt9/6eFpyKRVVEF6nNnKv7Tp1o/557f226a1f0e9c704af62a5c842a3037/oai_Unrolling_the_Codex_agent_loop_Agent_loop_desktop-light.svg (03번 파일 참조).
- 분류표와 타임라인은 직접 그려야 함.

## Claude Code와의 연결점 (또는 다른 도구와의 비교점)
- Claude Code와 Codex는 위 분류에서 모두 "coding agent"에 해당한다. 둘 다 LLM + harness + 도구 루프 구조다(02·03번 파일).
- Claude Code 공식 문서는 자신을 현재 파일만 보는 inline code assistant와 명시적으로 구분한다. 이것이 copilot/autocomplete와 agent를 가르는 1차 근거다.
- Claude Code의 권한 모드, checkpoint, Plan 모드, CLAUDE.md는 agentic engineering이 요구하는 "감독과 책임" 장치로 설명할 수 있다. 반대로 모든 변경을 묻지 않고 자동 수락하는 사용법은 vibe coding에 가깝다(이 연결은 강연자 해석).
- Karpathy의 최초 vibe coding 게시물은 당시 도구로 Cursor Composer와 Sonnet을 예로 들었다. 이 개념이 특정 제품이 아니라 작업 태도를 가리킨다는 점을 짚어 둘 만하다.
