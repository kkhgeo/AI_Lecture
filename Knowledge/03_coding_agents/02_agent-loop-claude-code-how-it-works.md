# How Claude Code works (Claude Code의 agentic loop)

- **저자/기관**: Anthropic (Claude Code 공식 문서)
- **발행일**: 페이지에 발행일 표기 없음, 지속 갱신되는 문서. 본 요약은 2026-09-29 열람 버전 기준 (2026-09-29 열람)
- **URL**: https://code.claude.com/docs/en/how-claude-code-works
  - 관련: https://code.claude.com/docs/en/tools-reference , https://code.claude.com/docs/en/permission-modes , https://code.claude.com/docs/en/checkpointing , https://code.claude.com/docs/en/context-window
- **자료 유형**: 공식문서

## 핵심 요약
- Claude Code는 터미널에서 도는 agentic assistant로, 코딩뿐 아니라 명령줄에서 할 수 있는 일(문서 작성, 빌드, 파일 검색, 조사 등) 전반을 돕는다고 스스로 정의한다.
- **Agentic loop**는 3단계: **gather context → take action → verify results**. 세 단계는 칼같이 나뉘지 않고 섞이며, 작업에 따라 달라진다. 코드베이스 질문은 맥락 수집만으로 끝날 수 있고, 버그 수정은 세 단계를 여러 번 돈다. 모델은 이전 단계에서 배운 것을 바탕으로 다음 행동을 정하고, 수십 개의 행동을 이어 붙이며 궤도를 수정한다.
- 사용자도 루프의 일부다. 언제든 끼어들어(Esc로 중단, 또는 메시지를 입력해 대기열에 넣기) 방향을 바꿀 수 있다.
- 루프를 움직이는 두 요소는 **추론하는 model**과 **행동하는 tools**다. Claude Code 자체는 모델을 둘러싸고 도구를 제공하고 모델이 보는 context를 관리하는 층이며, 문서는 이것을 **agentic harness**라고 부른다.
- 도구가 없으면 모델은 텍스트로만 답할 수 있다. 내장 도구는 5개 범주: 파일 작업, 검색, 실행(shell·테스트·git), 웹, 코드 인텔리전스(플러그인 필요). 그 밖에 subagent 생성, 사용자에게 질문하기 등 오케스트레이션 도구가 있다. Skills, MCP, hooks, subagents는 이 루프 위에 얹는 확장층이다.
- 접근 범위: 현재 디렉터리의 프로젝트 파일, 사용자가 쓸 수 있는 모든 터미널 명령, git 상태, CLAUDE.md(그리고 AGENTS.md), auto memory(MEMORY.md 앞 200줄 또는 25KB 중 먼저 닿는 쪽까지 세션 시작 시 로드), 설정한 확장. 문서는 이것이 현재 파일만 보는 inline code assistant와 다르다고 강조한다.
- 실행 환경은 Local / Cloud / Remote Control 세 가지이고, 인터페이스는 터미널, 데스크톱 앱, IDE 확장, 웹(claude.ai/code), Slack, CI/CD 등 여러 가지지만 **루프 자체는 어디서나 동일**하다.
- 세션은 로컬 JSONL로 저장되어 resume·fork·rewind가 가능하다. 새 세션은 빈 context window로 시작하며, 세션 간 지속되는 것은 CLAUDE.md와 auto memory뿐이다. Context가 차면 오래된 도구 출력부터 지우고 필요하면 대화를 요약(compaction)한다.
- 안전장치 두 가지: **checkpoints**(파일 편집 전 스냅샷, Esc 두 번으로 되감기; 단 DB·API·배포 같은 원격 부작용은 되돌릴 수 없음)와 **permissions**(Shift+Tab으로 Auto / Manual / Accept edits / Plan 모드 전환, settings.json에 허용 명령 지정). 열람 버전 문서 기준으로 v2.1.283 이상에서는 Auto가 대화형 세션의 기본 시작 모드다.

## 핵심 개념·용어 정의
- **Agentic loop**: 맥락 수집 → 행동 → 결과 검증을 작업이 끝날 때까지 반복하는 순환. 각 도구 사용 결과가 다음 결정의 입력이 된다.
- **Agentic harness**: 모델을 감싸고 도구를 제공하며 모델이 보는 context를 관리하는 층. Claude Code가 바로 이것.
- **Tools**: 모델이 행동할 수 있게 하는 기능. "Tools are what make Claude Code agentic"이라는 것이 문서의 요지.
- **Context window**: 대화 이력, 파일 내용, 명령 출력, CLAUDE.md, memory, 로드된 skill, 시스템 지시가 담기는 공간. `/context`로 사용량 확인.
- **Compaction**: context 한계에 가까워지면 오래된 도구 출력 제거 및 대화 요약으로 공간을 확보하는 것. 초기 지시가 소실될 수 있으므로 지속 규칙은 CLAUDE.md에 두라고 권고.
- **Checkpoint**: 파일 편집 직전의 스냅샷. git과 별개.
- **Permission mode**: 에이전트가 묻지 않고 할 수 있는 범위(Auto, Manual, Accept edits, Plan).
- **Subagent**: 별도 context window에서 일하고 요약만 돌려주는 하위 에이전트.

## 강연에 쓸 만한 포인트
- "failing test 고쳐줘" 예시의 6단계(테스트 실행 → 에러 읽기 → 관련 파일 검색 → 파일 읽기 → 수정 → 테스트 재실행)는 agentic loop를 가장 구체적으로 보여 주는 슬라이드 소재. 1–4는 gather context, 5는 take action, 6은 verify results로 색을 나눠 표시하면 좋다.
- 공식: **Agent = Model(추론) + Harness(도구 + context 관리)**. Claude Code와 Codex를 비교하는 틀로도 쓸 수 있다(03번 파일).
- "Delegate, don't dictate": 유능한 동료에게 맡기듯 맥락과 방향만 주고, 어떤 파일을 읽을지는 에이전트가 정하게 하라는 문서의 조언. 챗봇 사용법과의 차이를 설명할 때 유용.
- 안전장치 두 축(되돌리기 = checkpoint, 사전 통제 = permission)을 2x1 도식으로. "로컬 파일은 되돌릴 수 있지만 원격 시스템 부작용은 되돌릴 수 없다"는 한계도 함께.
- 인용(1개): "Tools are what make Claude Code agentic." — Claude Code Docs, How Claude Code works

## 원본 그림
- Agentic loop 다이어그램 (라이트): 사용자 prompt → gather context → take action → verify results → 작업 완료까지 반복, 사용자가 어느 지점에서든 개입 가능함을 표시 — https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/agentic-loop.svg?fit=max&auto=format&n=ikqp3_70mqIahteV&q=85&s=4a30fb7ce2815012a9f27c955e2c6bb0
- Agentic loop 다이어그램 (다크 버전) — https://mintcdn.com/claude-code/_xqph1dUOslCOwsj/images/agentic-loop-dark.svg?fit=max&auto=format&n=_xqph1dUOslCOwsj&q=85&s=75e1d55ed76857a952f9a2dffbab02df
- Session continuity 다이어그램 (라이트): resume은 같은 세션 ID를 이어가고 fork는 새 ID로 분기함 — https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/session-continuity.svg?fit=max&auto=format&n=ikqp3_70mqIahteV&q=85&s=04ed0984a58e4127e05b3640265241a3
- Session continuity 다이어그램 (다크) — https://mintcdn.com/claude-code/_xqph1dUOslCOwsj/images/session-continuity-dark.svg?fit=max&auto=format&n=_xqph1dUOslCOwsj&q=85&s=886a384bce8298594e43f124617ea665
- 참고: mintcdn URL의 해시 경로는 문서 갱신 시 바뀔 수 있음.

## Claude Code와의 연결점 (또는 다른 도구와의 비교점)
- 이 문서 자체가 Claude Code의 1차 정의다. 01번(Anthropic의 agent 정의)의 "LLM이 도구를 루프로 사용"을 제품 수준에서 구현한 형태.
- OpenAI Codex도 같은 구조(모델 + harness + 도구 루프)를 쓴다(03번 파일). 차이는 구현 세부: Codex는 Responses API 호출 구조와 sandbox 설명을 developer 메시지로 넣는 방식을 공개했고, Claude Code 문서는 사용자 관점의 루프·권한·체크포인트를 설명한다.
- 지속 지시 파일: Claude Code는 CLAUDE.md, Codex는 AGENTS.md를 쓰며, Claude Code는 저장소에 AGENTS.md가 있으면 그것도 읽을 수 있다고 문서에 명시되어 있다.
- 문서는 inline code assistant(현재 파일만 보는 자동완성형 도구)와의 차이를 "프로젝트 전체를 보고 여러 파일을 조율해 수정하고 테스트로 검증한다"는 점으로 설명한다. 04번 파일의 분류표에 근거로 쓸 수 있다.
