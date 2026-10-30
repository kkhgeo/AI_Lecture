# Best practices for Claude Code

- **저자/기관**: Anthropic (Claude Code 공식 문서). 2025-04 엔지니어링 블로그 "Claude Code: Best practices for agentic coding"이 문서로 이관·갱신된 것
- **발행일**: 상시 갱신 문서 (2026-09-29 열람, Claude Code v2.1.28x 기준 서술 포함)
- **URL**: https://code.claude.com/docs/en/best-practices
- **자료 유형**: 공식문서

## 핵심 요약

- 문서 전체가 한 가지 제약에서 출발한다: **컨텍스트 창은 빨리 차고, 찰수록 성능이 떨어진다.** 대화, 읽은 파일, 명령 출력이 모두 창에 쌓이며, 디버깅 한 번에도 수만 토큰이 든다. 그래서 컨텍스트가 관리해야 할 가장 중요한 자원이라고 명시한다.
- **검증 수단 제공**: 테스트·빌드·스크린샷처럼 Claude가 스스로 돌려 볼 수 있는 확인 장치를 주면 사람이 검증 루프가 되지 않아도 된다. 강도에 따라 프롬프트 → `/goal` → Stop hook → 검증 subagent 순.
- **탐색 → 계획 → 구현 → 커밋**: plan mode로 탐색과 실행을 분리. 단, 한 문장으로 설명되는 작은 수정은 계획 생략.
- **구체적 맥락 제공**: 파일·제약·기존 패턴을 지목하고, `@파일`, 이미지, URL, 파이프 입력으로 풍부한 자료를 준다.
- **환경 구성**: 짧은 CLAUDE.md, 권한 설정, CLI 도구, MCP, hooks, skills, custom subagents, plugins.
- **세션 관리**: 일찍 자주 교정(`Esc`, `/rewind`), 무관한 작업 사이 `/clear`, `/compact <지시>`, subagent로 조사 위임, 체크포인트, 세션 이름 붙여 재개.
- **대형 기능은 인터뷰 → SPEC.md → 새 세션에서 구현**: 구현 세션을 깨끗한 컨텍스트로 시작하기 위해.
- **흔한 실패 패턴 5가지**: 잡탕 세션, 반복 교정, 과잉 CLAUDE.md, 검증 없는 신뢰, 무한 탐색.

## 핵심 개념·용어 정의

| 용어 | 뜻 |
|---|---|
| Plan mode | 파일 수정 없이 읽기·질문만 하는 권한 모드 (`Shift+Tab` 또는 `--permission-mode plan`) |
| /clear | 컨텍스트 전체 초기화. 무관한 작업 사이에 사용 |
| /compact [지시] | 대화를 요약해 공간 확보. 지시로 보존 초점 지정 |
| /rewind, Esc+Esc | 체크포인트로 대화·코드 되돌리기, 또는 특정 지점부터/까지 요약 |
| /btw | 대화 기록에 남지 않는 곁가지 질문 |
| /context | 현재 컨텍스트 사용 내역 확인 |
| Writer/Reviewer 패턴 | 한 세션이 작성, 다른 새 세션(또는 subagent)이 검토. 자기 코드에 대한 편향 제거 |

**실패 패턴과 처방**

| 실패 패턴 | 증상 | 처방 |
|---|---|---|
| Kitchen sink session | 무관한 작업이 한 세션에 섞임 | 작업 사이 `/clear` |
| Correcting over and over | 실패한 시도가 컨텍스트를 오염 | 교정 2회 실패 시 `/clear` 후 더 나은 첫 프롬프트 |
| Over-specified CLAUDE.md | 길어서 중요한 규칙이 묻힘 | 과감히 삭제, 반드시 지켜야 할 것은 hook으로 |
| Trust-then-verify gap | 그럴듯하지만 엣지 케이스 누락 | 테스트·스크립트·스크린샷으로 검증 |
| Infinite exploration | 범위 없는 조사로 수백 파일 읽기 | 범위 좁히기 또는 subagent 위임 |

## 강연에 쓸 만한 포인트

- **강연의 중심 명제로 사용**: "Claude Code의 모든 모범 사례는 하나의 제약, 컨텍스트에서 나온다." 이후 기능을 하나씩 그 제약에 대한 해법으로 소개.
- **실패 패턴 5개 슬라이드**: 청중이 자기 경험을 떠올리기 좋다. 특히 "두 번 교정해도 안 되면 새로 시작"은 즉시 써먹을 수 있는 팁.
- **Before/After 프롬프트 표**: "로그인 버그 고쳐줘" vs "세션 만료 후 로그인 실패, src/auth/의 토큰 갱신 확인, 재현 테스트 먼저 작성 후 수정".
- **CLAUDE.md 넣을 것/뺄 것 표**: 넣을 것(추측 불가한 명령, 기본과 다른 스타일, 테스트 방법, 저장소 관례, 환경 특이사항), 뺄 것(코드 보면 아는 것, 일반 관례, 자주 바뀌는 정보, 파일별 설명, 긴 튜토리얼).
- 인용(1개): "The context window is the most important resource to manage." (Claude Code 공식 문서) — 10단어

## Claude Code와의 연결점

- 이 문서 자체가 실습 체크리스트다. 라이브 데모 순서 예: `/init` → `/context` → plan mode로 탐색 → `Ctrl+G`로 계획 편집 → 구현·테스트 → subagent 리뷰(`/code-review`) → `/clear`.
- 인터뷰 기법: "AskUserQuestion 도구로 나를 인터뷰해 SPEC.md를 작성해줘" → 새 세션에서 `@SPEC.md` 구현.
- 압축 보존 지시: CLAUDE.md에 "압축 시 수정한 파일 목록과 테스트 명령은 반드시 보존" 추가.
