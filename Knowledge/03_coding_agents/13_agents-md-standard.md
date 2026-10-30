# AGENTS.md — a simple, open format for guiding coding agents, and MCP (공통 지침 파일 표준과 도구 표준)

- **저자/기관**: AGENTS.md 공동 작업(OpenAI 주도, Google·Cursor·Factory·Sourcegraph/Amp 참여) → Agentic AI Foundation(Linux Foundation) 관리; MCP는 Anthropic 제안 → AAIF
- **발행일**: AGENTS.md 형식 공개 2025-08; AAIF 창립 발표 2025-12-09; Claude Code 문서는 상시 갱신 (2026-09-29 열람)
- **URL**:
  - https://agents.md/
  - https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
  - https://openai.com/index/agentic-ai-foundation/
  - https://factory.ai/news/agents-md
  - https://code.claude.com/docs/en/memory (Claude Code의 AGENTS.md 처리)
  - https://developers.openai.com/codex/guides/agents-md (Codex의 탐색 규칙)
  - https://geminicli.com/docs/cli/gemini-md/ (GEMINI.md와 AGENTS.md 설정)
  - https://goose-docs.ai/blog/2026/04/07/goose-moves-to-aaif/
- **자료 유형**: 공식문서 + 보도자료

## 핵심 요약
- **AGENTS.md**는 "에이전트를 위한 README". 사람용 README에 넣기 번잡한 빌드·테스트 명령, 코드 스타일, 테스트 방법, 보안 주의, 커밋/PR 규칙을 **평범한 Markdown**으로 적는다. 필수 필드·스키마가 없다.
- 2025년 8월 OpenAI, Google, Cursor, Factory, Sourcegraph(Amp) 등이 벤더별로 흩어진 파일(`.cursorrules`, `CLAUDE.md`, `GEMINI.md`, `copilot-instructions.md` …)을 하나로 모으자는 취지로 공개. agents.md 기준 6만 개+ 오픈소스 프로젝트가 사용.
- 채택 도구(agents.md 표기 + 각사 문서): OpenAI Codex, GitHub Copilot(2025-08 네이티브 지원), Cursor, Gemini CLI(설정 필요), Jules, VS Code, Windsurf, Zed, Aider(설정 필요), goose, Factory, Amp, Devin, JetBrains Junie, UiPath, 그리고 **Claude Code(v2.1.277부터 직접 읽기)**.
- **중첩·우선순위**: 모노레포에서는 하위 폴더마다 AGENTS.md를 둘 수 있고, 편집 중인 파일에서 **가장 가까운 파일이 우선**. OpenAI 자체 저장소에 AGENTS.md가 88개 있다(agents.md 표기).
- 도구마다 읽는 방식이 다르다: Codex는 디렉터리마다 `AGENTS.override.md` → `AGENTS.md` → fallback 파일명 순, 합산 32 KiB 한도, 전역 `~/.codex/AGENTS.md`. Gemini CLI는 기본 GEMINI.md, `context.fileName`에 AGENTS.md 지정. Claude Code는 **CLAUDE.md가 없을 때만** AGENTS.md를 읽는 것이 기본(`claude-md-or-agents-md`), 설정으로 둘 다 읽기(`claude-md-and-agents-md`) 가능. `AGENTS.override.md`·`.agents/`는 Claude Code가 읽지 않음.
- 호환 요령: CLAUDE.md에 `@AGENTS.md` 한 줄 import(권장, 특히 Windows) 또는 `ln -s AGENTS.md CLAUDE.md` 심볼릭 링크. Claude Code `/init`·`/import`는 Cursor rules, Copilot instructions, AGENTS.md, `.clinerules` 등을 읽어 CLAUDE.md로 흡수.
- **거버넌스**: 2025-12-09 Linux Foundation 산하 **Agentic AI Foundation(AAIF)** 창립. 창립 기증 프로젝트 = Anthropic의 **MCP**, Block의 **goose**, OpenAI의 **AGENTS.md**. Platinum 회원: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI.
- **MCP(Model Context Protocol)**: 2024-11 Anthropic이 공개한, 에이전트가 외부 도구·데이터에 연결하는 개방형 프로토콜(“AI용 USB-C” 비유가 흔함). 이번 조사 범위의 모든 도구(Codex, Gemini CLI/Antigravity, Copilot, Cursor, Cline, OpenCode, Goose, Kilo 등)가 MCP를 지원 → **지침은 AGENTS.md, 도구는 MCP**로 벤더 간 표준이 양분되어 정착.

## 핵심 개념·용어 정의
- **AGENTS.md**: 저장소 루트(및 하위)에 두는 에이전트용 지침 Markdown. 형식 제약 없음.
- **CLAUDE.md / GEMINI.md**: 각각 Claude Code, Gemini CLI 고유 지침 파일. 기능상 AGENTS.md와 같지만 계층(사용자·조직·로컬), import, 경로별 규칙 등 벤더 확장이 붙어 있다.
- **Proximity precedence**: 가장 가까운 디렉터리의 지침이 우선한다는 해석 규칙(AGENTS.md). Claude Code는 덮어쓰기가 아니라 상위→하위 순으로 **이어 붙임**.
- **AAIF (Agentic AI Foundation)**: 에이전트 관련 오픈 표준·프로젝트를 중립적으로 관리하는 Linux Foundation 산하 재단(directed fund).
- **MCP server / client**: 도구·데이터를 노출하는 쪽(server)과 이를 호출하는 에이전트 쪽(client). 한 번 만든 MCP 서버는 여러 에이전트에서 재사용.

## 강연에 쓸 만한 포인트
- 비유: AGENTS.md = "신입 연구원에게 주는 실험실 매뉴얼", MCP = "실험 장비 표준 콘센트". 매뉴얼은 무엇을 어떻게 할지, 콘센트는 어떤 장비를 꽂을 수 있는지.
- 도식 아이디어: 가운데 AGENTS.md 한 장, 주위에 Codex·Copilot·Cursor·Gemini·Claude Code 아이콘이 화살표로 읽어 가는 그림. 아래층에 MCP 버스가 모든 에이전트와 GitHub·DB·브라우저 서버를 잇는 2층 구조.
- 대학원생 실습 제안: 연구 저장소에 AGENTS.md(데이터 경로, 환경 설치, 테스트·재현 명령, "원자료 수정 금지" 규칙)를 쓰고 CLAUDE.md에는 `@AGENTS.md` 한 줄 → 어느 에이전트로 바꿔도 연구실 규칙이 유지된다.
- 숫자: 6만+ 프로젝트 채택, OpenAI 저장소 내 AGENTS.md 88개, Codex 기본 한도 32 KiB, Claude Code 권장 CLAUDE.md 200줄 이하.
- 주의점: 지침 파일은 "권고(context)"이지 강제 설정이 아니다 — 반드시 막아야 할 행동은 권한 설정·hooks로 강제(Claude Code 문서의 요지).
- 인용(1개): "a README for agents" — agents.md

## 원본 그림
- agents.md 사이트: 채택 도구 로고 목록이 있으나 직접 이미지 URL은 확인하지 못함 — 없음
- AAIF 보도자료: 이미지 URL 미확인 — 없음

## Claude Code와의 비교점
- **형태**: 형식 자체는 도구 중립. Claude Code는 CLAUDE.md를 1차로 쓰고 AGENTS.md를 2차(없을 때 대체, 또는 설정으로 병행)로 지원.
- **모델**: 무관(형식 표준).
- **권한·샌드박스**: AGENTS.md에는 권한 개념 없음. Claude Code는 권한을 settings/hooks로 분리, Codex는 sandbox/approval 설정(config.toml)으로 분리 — "지침(말)과 통제(설정)의 분리"가 공통 설계.
- **지침 파일**: CLAUDE.md는 managed/user/project/local 4단 스코프, `@import`, `.claude/rules/` 경로별 규칙, auto memory까지 있어 AGENTS.md보다 표현력이 크다. 이식성을 원하면 공통 내용은 AGENTS.md, Claude 전용 내용은 CLAUDE.md에.
- **확장**: MCP는 Anthropic이 만들어 AAIF에 기증 — Claude Code가 가장 이른 MCP 클라이언트 중 하나였고, 지금은 모든 경쟁 도구가 같은 서버를 공유한다.
