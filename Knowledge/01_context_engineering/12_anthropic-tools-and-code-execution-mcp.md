# 도구 설계와 MCP의 컨텍스트 효율: Writing effective tools for agents / Code execution with MCP

| 자료 | 저자/기관 | 발행일 | URL | 유형 |
|---|---|---|---|---|
| Writing effective tools for AI agents, using AI agents | Ken Aizawa 외 (Anthropic) | 2025-09-11 | https://www.anthropic.com/engineering/writing-tools-for-agents | 블로그 (공식) |
| Code execution with MCP: Building more efficient agents | Adam Jones, Conor Kelly (Anthropic) | 2025-11-04 | https://www.anthropic.com/engineering/code-execution-with-mcp | 블로그 (공식) |

## 핵심 요약

- 두 글 모두 "도구도 컨텍스트다"라는 관점을 공유한다. 도구 정의와 도구 결과가 컨텍스트 창을 차지하므로, 도구를 설계하는 일은 곧 context engineering이다.
- **도구 설계 글(2025-09)**: 기존 API를 그대로 감싸지 말고 에이전트의 소비 방식에 맞춰라. 기능 중복 없는 소수의 고영향 도구, 여러 단계를 하나로 묶은 도구(예: 일정 가능 여부 확인까지 하는 `schedule_event`), 일관된 이름 접두사(namespacing), 의미 있는 식별자(무작위 UUID 대신 사람이 읽을 이름) 반환, 페이지네이션·필터·잘라내기 기본값, concise/detailed 응답 형식 선택 옵션을 권장한다. Slack 예시에서 concise 응답은 detailed의 약 1/3 토큰.
- 같은 글은 Claude Code가 도구 응답을 기본 **25,000토큰**으로 제한한다고 소개한다(글 작성 시점 기준).
- **Code execution with MCP 글(2025-11)**: MCP 서버가 많아지면 ① 모든 도구 정의를 미리 로드해 컨텍스트가 부풀고 ② 중간 결과(예: 회의록 전문)가 모델을 여러 번 통과한다. 해법은 MCP 도구를 **파일 시스템 위의 코드 API**로 노출하고 에이전트가 코드를 써서 호출하게 하는 것. 필요한 도구 정의만 찾아 읽고(progressive disclosure), 대용량 데이터는 실행 환경에서 걸러 요약만 모델에 돌려준다.
- 예시에서 컨텍스트 사용량이 **15만 토큰에서 2천 토큰으로(98.7% 절감)** 줄었다.
- 부수 효과: 민감 데이터가 모델을 거치지 않아 프라이버시 향상, 작업 상태를 파일로 저장, 재사용 함수를 skill로 축적.

## 핵심 개념·용어 정의

- **Tool definition overload**: 사용하지 않는 도구 설명이 매 요청 컨텍스트를 점유하는 문제.
- **Intermediate result bloat**: 도구 간 데이터 전달이 모델 컨텍스트를 경유해 토큰이 중복 소모되는 문제.
- **Token-efficient tool response**: 필요한 신호만, 사람이 읽을 형태로, 적정 분량으로 반환.
- **Tool search / deferred loading**: 도구 이름만 먼저 싣고 스키마는 필요할 때 로드(현재 Claude Code 기본 동작).

## 강연에 쓸 만한 포인트

- **Before/After 도식**: [도구 정의 수백 개 + 원본 데이터가 모두 컨텍스트 통과] vs [파일 트리에서 필요한 도구만 읽고, 코드가 데이터를 걸러 요약만 반환].
- **숫자 한 장**: 150,000 → 2,000 토큰.
- **UUID vs 이름 예**: 무작위 ID 대신 "김철수 (마케팅팀)"을 돌려주면 정확도가 오른다는 점은 비개발자도 이해하기 쉽다.
- **메시지**: "도구를 많이 연결할수록 똑똑해진다"는 오해를 깨기. Drew Breunig의 context confusion(04번)과 연결.
- 인용(1개): 컨텍스트 사용이 "from 150,000 tokens to 2,000 tokens" 감소 (Anthropic, 2025-11-04)

## Claude Code와의 연결점

- MCP 연결은 `claude mcp add ...`. `/mcp`로 연결 상태, `/context all`로 MCP 도구별 토큰 사용량 확인.
- Claude Code는 기본적으로 **MCP tool search**를 켜 도구 이름만 싣고 스키마는 필요할 때 로드한다(`ENABLE_TOOL_SEARCH` 설정으로 조절).
- 공식 best practices: 외부 서비스는 CLI 도구(`gh`, `aws` 등)가 가장 컨텍스트 효율적이라고 권장.
- 데모: MCP 서버 여러 개를 연결한 상태와 뺀 상태에서 `/context` 비교, 또는 큰 로그 파일을 통째로 읽힐 때와 `grep`/스크립트로 걸러 요약만 보게 할 때 비교.
