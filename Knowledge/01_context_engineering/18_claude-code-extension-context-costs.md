# Extend Claude Code: CLAUDE.md, Skills, Subagents, Hooks, MCP의 컨텍스트 비용

- **저자/기관**: Anthropic (Claude Code 공식 문서)
- **발행일**: 상시 갱신 문서 (2026-09-29 열람)
- **URL**: https://code.claude.com/docs/en/features-overview (관련: https://code.claude.com/docs/en/hooks-guide , https://code.claude.com/docs/en/mcp )
- **자료 유형**: 공식문서

## 핵심 요약

- Claude Code의 확장 기능을 "무엇을 하는가"와 **"언제, 얼마나 컨텍스트를 차지하는가"**로 비교하는 문서다. 모든 기능은 컨텍스트를 소비하며, 과하면 창이 차는 것뿐 아니라 잡음이 늘어 스킬이 제대로 발동하지 않거나 규칙을 놓친다.
- 기능은 **항상 켜진 컨텍스트**(CLAUDE.md, output style) → **필요 시 로드**(skills, MCP 스키마, path-scoped rules) → **격리**(subagents) → **컨텍스트 밖 자동화**(hooks)의 스펙트럼으로 배치된다.
- **점진적 도입 순서(트리거 기반)**: 같은 실수 두 번 → CLAUDE.md / 같은 프롬프트 반복 → 사용자 호출 skill / 같은 절차 세 번째 붙여넣기 → skill / 브라우저에서 데이터 복사 반복 → MCP / 곁가지 작업이 대화를 범람 → subagent / 매번 반드시 일어나야 함 → hook / 다른 저장소도 같은 설정 → plugin.
- **Hook은 결정적**: CLAUDE.md 지시는 권고(request)지만, PreToolUse hook의 차단은 강제(enforcement)다. hook은 출력을 돌려주지 않는 한 컨텍스트 비용이 0이다.

## 핵심 개념·용어 정의

**기능별 컨텍스트 비용 (공식 표 재구성)**

| 기능 | 로드 시점 | 로드 내용 | 비용 |
|---|---|---|---|
| CLAUDE.md | 세션 시작 | 전체 | 매 요청 |
| Output style | 세션 시작/전환 시 | 스타일 지시 전체 | 매 요청 |
| Skills | 시작 + 사용 시 | 시작 시 설명만, 사용 시 전체 | 낮음 |
| MCP | 세션 시작 | 도구 이름만, 스키마는 필요 시 | 사용 전까지 낮음 |
| Code intelligence(LSP) | 편집 후·조회 시 | 진단, 심볼 위치 | 낮음, 파일 읽기를 줄여 순감 가능 |
| Subagents | 생성 시 | 새 격리 컨텍스트 | 메인과 분리 |
| Hooks | 이벤트 발생 시 | 없음(외부 실행) | 0 (출력 반환 시 제외) |

**비슷한 기능 구분**

- Skill vs Subagent: 재사용 콘텐츠(메인 창에 추가) vs 격리된 작업자(별도 창, 요약만 반환).
- CLAUDE.md vs Skill: 항상 로드 vs 필요 시 로드. CLAUDE.md는 200줄 이하로.
- CLAUDE.md vs Rules vs Skill: 전 프로젝트 핵심 규약 / 경로·언어별 지침 / 가끔 필요한 참고·워크플로.
- MCP vs Skill: 외부 서비스 연결(도구·데이터) vs 그 도구를 잘 쓰는 법(지식·절차).
- Hook vs Skill: 이벤트에 반드시 실행(결정적) vs Claude가 해석해 적용(가변적).

## 강연에 쓸 만한 포인트

- **스펙트럼 도식(강연 핵심 그림 후보)**: 왼쪽 "항상 컨텍스트에"(CLAUDE.md) → "필요할 때만"(Skills, MCP, rules) → "다른 창에서"(Subagents) → "컨텍스트 밖에서"(Hooks). 각 칸 아래 비용 막대.
- **"요청 vs 강제"**: "`.env` 수정 금지"를 CLAUDE.md에 쓰면 부탁, hook으로 막으면 규칙. 청중이 잘 기억하는 대비.
- **트리거 표**: 청중이 "언제 무엇을 추가할지" 바로 적용 가능한 체크리스트.
- **조합 예**: CLAUDE.md(규약) + skill(배포 절차) + MCP(DB 연결) + hook(편집 후 린트).
- 인용(1개): "Every feature you add consumes some of Claude's context." (Claude Code 문서) — 9단어

## Claude Code와의 연결점

- 명령: `/context`, `/context all`, `/mcp`, `/hooks`, `/agents`, `/skills`, `/plugin`, `/doctor`.
- 실습: 편집 후 자동 포맷 hook(PostToolUse)을 Claude에게 만들어 달라고 요청 → 이후 매 편집마다 실행되지만 CLAUDE.md에는 한 줄도 추가되지 않음을 보여주기.
- 실습: 자주 쓰는 긴 절차를 CLAUDE.md에서 skill로 옮긴 전후 `/context` 비교.
