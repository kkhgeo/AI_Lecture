# How Claude remembers your project (CLAUDE.md, rules, auto memory)

- **저자/기관**: Anthropic (Claude Code 공식 문서)
- **발행일**: 상시 갱신 문서 (2026-09-29 열람)
- **URL**: https://code.claude.com/docs/en/memory
- **자료 유형**: 공식문서

## 핵심 요약

- 모든 세션은 **빈 컨텍스트 창**으로 시작한다. 세션을 넘어 지식을 전달하는 장치는 두 가지다: 사람이 쓰는 **CLAUDE.md**(지시·규칙)와 Claude가 스스로 쓰는 **auto memory**(학습한 선호·교정 사항).
- 둘 다 강제 설정이 아니라 **컨텍스트**로 취급된다. 무조건 막아야 하는 행동은 PreToolUse hook으로 처리하라고 명시한다.
- **CLAUDE.md 로드 방식**: 작업 디렉터리와 그 상위 모든 디렉터리의 CLAUDE.md·CLAUDE.local.md를 **덮어쓰지 않고 이어 붙인다**(루트에서 작업 폴더 순). 하위 디렉터리의 CLAUDE.md는 그 폴더 파일을 읽을 때 로드. 블록 HTML 주석은 컨텍스트에 넣기 전 제거된다.
- **작성 원칙**: 파일당 **200줄 이하** 목표. 길수록 컨텍스트를 먹고 준수율이 떨어진다. 구체적으로 쓰고, 서로 모순되는 규칙은 주기적으로 정리. 여러 단계 절차나 일부 코드에만 해당하는 내용은 skill이나 path-scoped rule로.
- **import**: `@path/to/file`로 다른 파일을 가져올 수 있으나(최대 4단계), 가져온 파일도 시작 시 컨텍스트에 들어간다.
- **`.claude/rules/`**: 주제별 규칙 파일. `paths:` frontmatter로 특정 파일 작업 시에만 로드 → 잡음·토큰 절약.
- **auto memory**: 기본 활성. `~/.claude/projects/<project>/memory/`에 `MEMORY.md` 색인 + 주제별 파일. 매 세션 `MEMORY.md`의 **앞 200줄 또는 25KB**만 로드하고 주제 파일은 필요할 때 읽는다. 저장 유형은 user(역할·선호), feedback(교정), project(코드로 알 수 없는 진행·결정), reference(외부 정보 위치). 코드에서 알 수 있는 것은 저장하지 않는다.
- **AGENTS.md**: 다른 코딩 에이전트용 AGENTS.md도 읽을 수 있다(최신 버전).

## 핵심 개념·용어 정의

| 구분 | CLAUDE.md | Auto memory |
|---|---|---|
| 작성자 | 사람 | Claude |
| 내용 | 지시와 규칙 | 학습한 패턴·선호 |
| 범위 | 조직/사용자/프로젝트/로컬 | 저장소 단위(워크트리 공유) |
| 로드 | 매 세션 전체 | 매 세션 MEMORY.md 앞 200줄 또는 25KB |

- **메모리 계층**: 관리형(조직) → 사용자(`~/.claude/CLAUDE.md`) → 프로젝트(`./CLAUDE.md`) → 로컬(`CLAUDE.local.md`, git 제외) → 하위 폴더.
- **/init**: 코드베이스를 분석해 초기 CLAUDE.md 생성. **/memory**: 메모리 파일 열람·편집, auto memory 토글.
- **claudeMdExcludes**: 모노레포에서 무관한 팀의 CLAUDE.md 제외.

## 강연에 쓸 만한 포인트

- **"신입 사원 온보딩 문서" 비유**: CLAUDE.md는 매일 아침 새로 출근하는(기억 없는) 동료에게 주는 한 장짜리 안내문. 길면 안 읽힌다.
- **계층 도식**: 조직 → 사용자 → 프로젝트 → 하위 폴더, 위에서 아래로 이어 붙여지는 모습.
- **CLAUDE.md vs auto memory 대비표**(위 표)를 그대로 슬라이드로.
- **MEMORY.md = 색인 + 주제 파일** 구조는 그 자체로 progressive disclosure의 사례.
- **"줄 하나마다 자문하라"**: 이 줄을 지우면 Claude가 실수할까? 아니면 지워라(best practices).
- 인용(1개): Claude는 이 파일들을 "context, not enforced configuration"으로 취급 (Claude Code 문서)

## Claude Code와의 연결점

- 실습 1: 빈 프로젝트에서 `/init` → 생성된 CLAUDE.md를 200줄 이하로 다듬기 → `/context`로 로드 확인.
- 실습 2: `.claude/rules/api.md`에 `paths: ["src/api/**"]` 지정 후, API 파일을 읽을 때만 규칙이 로드되는 것 확인.
- 실습 3: 작업 중 선호를 교정("항상 pnpm 써")한 뒤 `/memory`로 auto memory에 저장됐는지 확인.
- 개인용 설정은 `CLAUDE.local.md`(gitignore) 또는 `~/.claude/CLAUDE.md`, 팀 공유는 커밋된 `CLAUDE.md`.
- `/doctor`로 체크인된 CLAUDE.md에서 코드로 유추 가능한 내용 삭제 제안 받기.
