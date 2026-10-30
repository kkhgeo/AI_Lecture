# Extend Claude Code (features overview) + Skills / Hooks / Agent SDK / Plugins (확장 기능 지도)

- **저자/기관**: Anthropic (Claude Code 공식 문서, claude.com 블로그)
- **발행일**: 공식 문서 상시 갱신(2026-09-29 열람). Plugins 블로그 2025-10-09, Agent Skills 블로그 2025-10-16(2025-12-18 open standard 갱신), Agent SDK 개명 2025-09-29
- **URL**:
  - https://code.claude.com/docs/en/features-overview
  - https://code.claude.com/docs/en/skills
  - https://code.claude.com/docs/en/hooks
  - https://code.claude.com/docs/en/agent-sdk/overview
  - https://claude.com/blog/claude-code-plugins
  - https://claude.com/blog/skills
- **자료 유형**: 공식문서 + 블로그

## 핵심 요약
- 공식 문서는 확장 기능을 "agentic loop의 서로 다른 지점에 꽂히는 부품"으로 설명한다. 내장 도구가 대부분의 코딩을 처리하고, 확장은 **무엇을 아는가(context)**, **무엇에 연결되는가(external)**, **언제 자동으로 도는가(automation)**를 바꾼다.
- 한 줄 정의:
  - **CLAUDE.md**: 매 세션 시작 시 자동으로 읽히는 프로젝트 규칙 파일("pnpm 써라, 커밋 전 테스트"). 권장 200줄 이하. `/init`으로 초안 생성. `AGENTS.md`도 읽을 수 있음. 여기에 Claude가 스스로 쌓는 **auto memory**(MEMORY.md)가 더해짐.
  - **Skills**: `SKILL.md`(+ 스크립트·참고자료) 폴더. 평소엔 이름·설명만 보이다가 필요할 때 본문 전체를 불러온다(progressive disclosure). `/skill-name`으로 직접 호출하거나 Claude가 자동으로 고른다. **Agent Skills open standard**(agentskills.io)를 따른다.
  - **Slash commands**: `/help`, `/compact`, `/rewind`, `/init` 같은 내장 명령 + 사용자 정의 명령. 문서상 **custom commands는 skills로 통합**되었다(`.claude/commands/deploy.md`와 `.claude/skills/deploy/SKILL.md` 모두 `/deploy`가 됨).
  - **MCP (Model Context Protocol)**: 외부 서비스·데이터(DB, Slack, Google Drive, Jira, 브라우저)를 도구로 연결하는 개방형 프로토콜. 도구 이름만 먼저 로드하고 스키마는 필요할 때 불러온다(tool search).
  - **Subagents**: 독립 context window에서 따로 일하고 **요약만 돌려주는** 보조 에이전트. 병렬 작업, 많은 파일 탐색 격리에 쓴다(내장 Explore·Plan 등).
  - **Hooks**: 수명주기 이벤트(`PreToolUse`, `PostToolUse`, `SessionStart`, `Stop` 등 30여 종)에 셸 명령·HTTP·MCP 도구·LLM prompt·agent를 **결정적으로** 실행. `PreToolUse`에서 exit code 2면 행동 차단.
  - **Plugins**: skills·hooks·subagents·MCP 서버를 하나로 묶어 설치·배포하는 패키지 층(`/plugin`, marketplace). 2025-10-09 public beta.
  - **Claude Agent SDK**: Claude Code의 도구·agent loop·context 관리를 Python/TypeScript 라이브러리로 제공. 2025-09-29 "Claude Code SDK"에서 개명.
  - 그 밖(최신 문서): Output styles(응답 역할·어조), Code intelligence(LSP), Dynamic workflows(스크립트로 다수 subagent 조율), Cross-session messaging, Artifacts.
- **context 비용 비교**: CLAUDE.md는 매 요청 전체 비용 / Skills는 설명만 상시, 본문은 사용 시 / MCP는 도구 이름만 상시 / Subagent는 주 세션과 격리 / Hooks는 출력이 없으면 0.
- **"결정성" 축**: CLAUDE.md·skill의 지시는 "요청"이지 보장이 아니다. 반드시 지켜야 할 규칙(예: `.env` 수정 금지)은 hook으로 강제하라고 문서가 명시한다.
- **도입 순서 권장**(문서 표): 같은 실수 2번 → CLAUDE.md, 같은 프롬프트 반복 → skill, 브라우저에서 복사해 오는 데이터 → MCP, 부수 작업 출력이 대화를 덮음 → subagent, 매번 자동 실행 → hook, 두 번째 저장소에도 같은 설정 → plugin.
- 우선순위: CLAUDE.md는 모든 수준(관리·사용자·프로젝트)이 **누적**, skills·subagents·MCP는 같은 이름이면 **덮어쓰기**, hooks는 모두 **병합** 실행.

## 핵심 개념·용어 정의
- **Progressive disclosure**: 메타데이터만 먼저 보여 주고 필요할 때 상세를 불러오는 로딩 방식(skills, MCP tool search).
- **Context isolation**: subagent가 자기 창에서 일하고 결과 요약만 반환해 주 대화를 가볍게 유지하는 것.
- **Lifecycle event**: 세션 시작, 프롬프트 제출, 도구 실행 전후, 종료 등 hook이 걸리는 시점.
- **Marketplace**: 플러그인 모음을 호스팅·배포하는 저장소(`/plugin marketplace add`).
- **Agent Skills open standard**: 스킬 폴더 형식을 다른 AI 도구에서도 쓰도록 공개한 규격(2025-12-18).
- **Agent SDK vs Client SDK**: 전자는 Claude Code의 도구·루프를 통째로 가져다 쓰는 라이브러리, 후자는 API를 직접 호출하고 도구 루프를 스스로 짜야 함. Anthropic이 호스팅하는 Managed Agents도 별도로 존재.

## 강연에 쓸 만한 포인트
- 비유(신입 연구원 온보딩): CLAUDE.md = 연구실 규칙 게시판(항상 봄), Skill = 실험 프로토콜 바인더(필요할 때 꺼냄), MCP = 장비·DB 접근 권한 카드, Subagent = 문헌조사를 맡긴 후배(요약만 보고), Hook = 실험실 안전 인터록(사람 판단 없이 무조건 작동), Plugin = 이 모두를 담은 "연구실 스타터 키트".
- 도식 아이디어: 가로축 "항상 로드 ↔ 필요 시 로드", 세로축 "지시(확률적) ↔ 강제(결정적)"에 6개 확장을 배치. hook은 우상단(결정적), CLAUDE.md는 좌하단(상시·확률적).
- 표 한 장: 기능 | 언제 로드 | context 비용 | 대표 예. 공식 문서 표를 한국어로 옮기면 바로 슬라이드가 된다.
- 인용(1개): "Custom commands have been merged into skills." (Claude Code Docs, Skills)
- 주의 문구: 이 절은 "무엇이 있는가"만 소개하고 context engineering 심화는 다른 강의 절에서 다룬다.

## 원본 그림
- Context loading 다이어그램(CLAUDE.md는 시작 시 상시, MCP는 이름만·스키마는 지연, skills는 설명→사용 시 본문, subagent 격리, hooks 외부 실행) — https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/context-loading.svg?fit=max&auto=format&n=ikqp3_70mqIahteV&q=85&s=aab139e750494a237ae2e0c8f9139b0a (다크: https://mintcdn.com/claude-code/_xqph1dUOslCOwsj/images/context-loading-dark.svg?fit=max&auto=format&n=_xqph1dUOslCOwsj&q=85&s=b274089ef9612d9c760bca9838557626)
- Plugins 블로그 관련 일러스트(플러그인 빌드) — https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg (관련 글 썸네일, 설명용 가치 낮음)
- 스킬 progressive disclosure 도식은 Anthropic Engineering "Equipping agents for the real world with Agent Skills"(https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)에 있는 것으로 알려져 있으나 이번에 이미지 URL은 확인하지 못함

## 다른 도구와의 비교점
- **AGENTS.md**(OpenAI Codex 등 여러 에이전트가 쓰는 공용 지시 파일)와 **CLAUDE.md**는 같은 역할이다. Claude Code는 AGENTS.md도 읽을 수 있다.
- **MCP**는 Anthropic이 제안한 개방형 프로토콜로, Codex·Cursor·VS Code Copilot 등 다수 도구가 지원한다. 확장 생태계가 도구 간 호환되는 부분.
- **Agent Skills open standard**도 다른 도구로 이식 가능하도록 공개되었다. 어느 도구가 실제 채택했는지는 이 파일에서 검증하지 않음.
- Hooks·plugins·subagents를 한 제품 안에서 모두 공식 지원하고 표로 비교해 준다는 점이 Claude Code 문서의 특징. 다른 도구의 대응 기능 여부는 각 도구 파일에서 확인할 것.
- Agent SDK는 "코딩 에이전트의 harness를 범용 에이전트 부품으로 재사용"한 사례다. 코딩 도구가 에이전트 플랫폼으로 확장되는 흐름을 보여 준다.
