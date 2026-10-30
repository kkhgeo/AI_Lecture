# Claude Code overview / How Claude Code works + 출시 연혁 (Claude Code 개요·실행 환경)

- **저자/기관**: Anthropic (Claude Code 공식 문서, anthropic.com 뉴스, claude.com 블로그)
- **발행일**: 공식 문서는 상시 갱신(2026-09-29 열람). 연혁 출처별 날짜는 아래 "출시 연혁" 참조
- **URL**:
  - https://code.claude.com/docs/en/overview
  - https://code.claude.com/docs/en/how-claude-code-works
  - https://www.anthropic.com/news/claude-3-7-sonnet (2025-02-24, research preview)
  - https://www.anthropic.com/news/claude-4 (2025-05-22, GA)
  - https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously (2025-09-29)
  - https://claude.com/blog/claude-code-on-the-web (2025-10-20, 2026-09-23 갱신)
  - https://claude.com/blog/claude-code-and-slack (2025-12-08)
  - https://claude.com/blog/claude-code-desktop-redesign (2026-04-14, 검색 결과 기준)
  - https://www.anthropic.com/news/introducing-claude-tag (2026-06-23)
  - https://claude.com/pricing
- **자료 유형**: 공식문서 + 블로그

## 핵심 요약
- 공식 정의: Claude Code는 **agentic coding tool**로, 코드베이스를 읽고, 파일을 편집하고, 명령을 실행하며, 개발 도구와 연동한다. 현재 파일만 보는 인라인 자동완성 도구와 달리 **프로젝트 전체**를 탐색·수정한다.
- 작동 원리는 **agentic loop**: ① 맥락 수집(gather context) → ② 행동(take action) → ③ 결과 검증(verify results)을 작업이 끝날 때까지 반복한다. 사용자는 언제든 `Esc`로 멈추거나 메시지를 끼워 넣어 방향을 틀 수 있다.
- 문서는 모델 바깥에서 도구를 제공하고 모델이 보는 context를 관리하는 층을 **agentic harness**라 부르고, Claude Code를 바로 그 harness로 설명한다. 즉 "모델(추론) + 도구(행동) + 맥락 관리"가 제품의 본체다.
- 실행 표면(**surface**): Terminal CLI, VS Code(및 Cursor) 확장, JetBrains 플러그인, Desktop 앱(Chat/Cowork/Code 탭 중 Code), Web(claude.ai/code), iOS·Android Claude 앱, Slack, GitHub Actions / GitLab CI/CD, Chrome 연동. 모든 surface가 **같은 엔진**을 쓰므로 CLAUDE.md·설정·MCP 서버가 공유된다.
- 실행 환경은 3가지: **Local**(내 PC), **Cloud**(Anthropic 관리 VM 또는 조직의 self-hosted 환경), **Remote Control**(실행은 내 PC, 조작은 브라우저·폰). 세션을 surface 간에 옮길 수 있다(`claude --teleport`, `/desktop`, `claude --cloud`).
- 설치(2026-09 기준 문서): 권장은 native installer — macOS/Linux/WSL `curl -fsSL https://claude.ai/install.sh | bash`, Windows PowerShell `irm https://claude.ai/install.ps1 | iex`. 대안으로 Homebrew(`brew install --cask claude-code`), WinGet(`winget install Anthropic.ClaudeCode`), apt/dnf/apk. 설치 후 프로젝트 폴더에서 `claude` 실행. native 설치는 백그라운드 자동 업데이트.
- 요금(claude.com/pricing, 2026-09-29 열람): Free에는 미포함. Pro $20/월(연간 결제 시 $17), Max $100/월부터(Pro 대비 5배 또는 20배 사용량), Team Standard $25(연 $20)/Premium $125(연 $100) per seat, Enterprise $20/seat + API 요율 사용량. 또는 Anthropic Console(API 키) 종량제, Amazon Bedrock·Google Cloud·Microsoft Foundry 등 third-party provider도 지원(CLI·VS Code·JetBrains).
- 반복 작업 자동화: **Routines**(클라우드 예약 실행, API·GitHub 이벤트 트리거), Desktop scheduled tasks, `/loop`. Unix 철학대로 `claude -p`로 파이프·스크립트·CI에 끼워 넣을 수 있다.

### 출시 연혁 (1차 출처 날짜)
| 날짜 | 사건 | 출처 |
|---|---|---|
| 2025-02-24 | Claude 3.7 Sonnet과 함께 **limited research preview**로 공개(터미널 도구) | anthropic.com/news/claude-3-7-sonnet |
| 2025-05-22 | Claude 4(Opus 4/Sonnet 4) 발표와 함께 **GA**. VS Code·JetBrains 베타 확장, GitHub Actions 백그라운드 작업, Claude Code SDK 공개 | anthropic.com/news/claude-4 |
| 2025-09-29 | Checkpoints(`/rewind`), 네이티브 VS Code 확장(베타), subagents·hooks·background tasks 강조, Claude Code SDK → **Claude Agent SDK** 개명. 기본 모델 Sonnet 4.5 | anthropic.com/news/enabling-claude-code-to-work-more-autonomously |
| 2025-10-09 | Plugins public beta (`/plugin`) | claude.com/blog/claude-code-plugins |
| 2025-10-16 | Agent Skills 발표(2025-12-18 open standard로 확장) | claude.com/blog/skills |
| 2025-10-20 | **Claude Code on the web**(클라우드 샌드박스) + iOS 앱 research preview, 로컬 sandboxing 기능 | claude.com/blog/claude-code-on-the-web |
| 2025-12-08 | Slack에서 @Claude로 코딩 작업 위임(beta, research preview) | claude.com/blog/claude-code-and-slack |
| 2026-03-24 | Auto mode research preview(Team) → 2026-07-10 전 사용자 GA | claude.com/blog/auto-mode |
| 2026-04-14 | Desktop 앱 Code 탭 재설계(병렬 세션 사이드바, 통합 터미널·에디터) | claude.com/blog/claude-code-desktop-redesign (검색 요약 기준, 본문 미확인) |
| 2026-06-23 | **Claude Tag**: Slack 팀원형 Claude(beta, Team/Enterprise). Anthropic은 이를 Claude Code의 진화로 설명 | anthropic.com/news/introducing-claude-tag |
- 미확인: Desktop 앱에 Code 탭이 처음 들어간 날짜, Android 지원 시점은 1차 출처로 확인하지 못함.

## 핵심 개념·용어 정의
- **Agentic coding tool**: 자연어 목표를 받아 스스로 계획·도구 호출·검증을 반복하며 코드를 수정하는 도구(자동완성과 대비).
- **Agentic loop**: gather context → take action → verify results의 반복 구조.
- **Agentic harness**: 모델을 감싸 도구를 제공하고 context를 관리하는 소프트웨어 층. Claude Code 자체.
- **Surface**: Claude Code에 접근하는 인터페이스(터미널, IDE, Desktop, Web, 모바일, Slack, CI).
- **Remote Control / Teleport**: 로컬 세션을 다른 기기에서 이어서 조작 / 클라우드 세션을 터미널로 끌어오기.
- **Routines**: 클라우드에서 일정·이벤트로 돌아가는 예약 에이전트 작업.
- **Headless mode (`claude -p`)**: 대화형 UI 없이 한 번 실행하는 비대화형 모드. 스크립트·CI용.

## 강연에 쓸 만한 포인트
- 비유: "자동완성이 옆자리에서 단어를 불러주는 조수라면, Claude Code는 일감을 받아 폴더를 뒤지고 테스트까지 돌려보는 인턴". 문서도 "지시하지 말고 위임하라(Delegate, don't dictate)"고 권한다.
- 도식 아이디어: 가운데 "Claude Code 엔진(harness + 모델)"을 두고 바깥 원에 Terminal·IDE·Desktop·Web·Mobile·Slack·CI를 배치 → "surface는 여러 개, 엔진은 하나".
- 타임라인 슬라이드: 2025-02 research preview → 2025-05 GA → 2025-10 web·sandbox·plugins·skills → 2026-03 auto mode → 2026-06 Claude Tag. 약 1년 반 만에 "터미널 도구 → 멀티 surface 플랫폼".
- 예시 명령(슬라이드용): `tail -200 app.log | claude -p "이상 징후 있으면 알려줘"` — Unix 파이프 조합성 강조.
- 인용(1개): "Claude Code is an agentic coding tool that reads your codebase" (Claude Code Docs, Overview)
- 대학원생 관점: 요금 최소 진입점은 Pro($20/월). Free 플랜에는 Claude Code가 없다는 점을 명시.

## 원본 그림
- Agentic loop 다이어그램(프롬프트 → 맥락 수집 → 행동 → 검증 → 반복, 언제든 개입 가능) — https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/agentic-loop.svg?fit=max&auto=format&n=ikqp3_70mqIahteV&q=85&s=4a30fb7ce2815012a9f27c955e2c6bb0 (다크 버전: https://mintcdn.com/claude-code/_xqph1dUOslCOwsj/images/agentic-loop-dark.svg?fit=max&auto=format&n=_xqph1dUOslCOwsj&q=85&s=75e1d55ed76857a952f9a2dffbab02df)
- 세션 resume vs fork 다이어그램 — https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/session-continuity.svg?fit=max&auto=format&n=ikqp3_70mqIahteV&q=85&s=04ed0984a58e4127e05b3640265241a3
- 2025-02 research preview 당시 Claude Code 온보딩 화면 스크린샷(터미널) — https://www-cdn.anthropic.com/images/4zrzovbb/website/4a4df6b6629f9814aec4eb9323028130f43a8d70-1920x1080.png
- 2025-09 "work more autonomously" 발표 이미지(VS Code 확장 화면으로 추정, 본문 미확인) — https://www-cdn.anthropic.com/images/4zrzovbb/website/3613f360926fae004521197488623465eb0cd751-1920x1035.png
- Claude Code on the web 히어로 일러스트(브라우저·지구본) — https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg

## 다른 도구와의 비교점
- **OpenAI Codex**도 CLI·IDE 확장·클라우드(웹) 에이전트·모바일로 surface를 넓혀 왔다는 점에서 구조가 비슷하다. Claude Code는 로컬 터미널에서 출발해 클라우드로 확장했고, 클라우드 우선으로 출발한 흐름과는 순서가 다르다(Codex 세부는 해당 파일 참조).
- **GitHub Copilot / Cursor**: 출발점이 IDE 내 자동완성·채팅이다. Claude Code는 터미널 에이전트에서 출발해 IDE로 들어갔다. Cursor에서도 Claude Code 확장을 설치할 수 있다.
- **AGENTS.md 호환**: Claude Code는 다른 코딩 에이전트용 `AGENTS.md`도 읽을 수 있어(문서 명시), 도구 간 프로젝트 지시문 공유가 가능하다.
- 요금 구조: 구독(Pro/Max) 정액제 + API 종량제를 모두 허용한다. 순수 API 과금 도구(예: 일부 오픈소스 에이전트)와 비용 모델이 다르다.
