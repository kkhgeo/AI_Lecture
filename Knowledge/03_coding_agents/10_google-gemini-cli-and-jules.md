# Gemini CLI, Jules, and Google Antigravity (Google 코딩 에이전트)

- **저자/기관**: Google (Google Developers Blog, Google Antigravity Blog, GitHub google-gemini, Google Labs)
- **발행일**: Gemini CLI→Antigravity CLI 전환 공지 2026-05-19 (Dmitry Lyalin, Taylor Mullen); Antigravity @ I/O 2026 2026-05-19 (2026-09-29 열람)
- **URL**:
  - https://github.com/google-gemini/gemini-cli
  - https://geminicli.com/docs/cli/gemini-md/
  - https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
  - https://github.com/google-gemini/gemini-cli/discussions/27274
  - https://antigravity.google/blog/google-io-2026
  - https://jules.google/
  - https://techcrunch.com/2025/08/06/googles-ai-coding-agent-jules-is-now-out-of-beta
  - https://en.wikipedia.org/wiki/Google_Antigravity (보조)
- **자료 유형**: 공식문서 + 엔지니어링 블로그 (+ 기사 보조)

## 핵심 요약
- **Gemini CLI**(2025-06-25 공개)는 Apache-2.0 오픈소스 터미널 에이전트. 개인 Google 계정 로그인만으로 분당 60회·일 1,000회 무료, 1M 토큰 컨텍스트로 "무료로 쓰는 코딩 에이전트"의 상징이었다(GitHub 스타 약 10.7만).
- 프로젝트 지침은 **GEMINI.md**: 전역 `~/.gemini/GEMINI.md` → 작업 디렉터리와 상위 → 도구가 파일에 접근할 때 just-in-time 탐색의 3단 계층. `/memory show`, `/memory reload`로 확인. `settings.json`의 `context.fileName`을 `["AGENTS.md"]`로 바꾸면 AGENTS.md를 읽는다.
- **큰 변화(2026-05-19, Google I/O)**: Google은 Gemini CLI를 **Antigravity CLI**로 전환한다고 발표. 2026-06-18부터 무료·Google AI Pro/Ultra 개인 사용자에 대한 Gemini CLI 요청 처리를 중단. Gemini Code Assist Standard/Enterprise 라이선스와 유료 API key 사용자는 계속 사용 가능.
- Gemini CLI 저장소는 Apache-2.0로 커뮤니티에 남지만, 후속작 Antigravity CLI는 Go로 작성된 **비공개(closed-source)** 제품(GitHub Discussion #27274 기준). Agent Skills·Hooks·Subagents·Extensions는 Antigravity plugin으로 이어진다. 커뮤니티 반응은 상당히 부정적.
- **Google Antigravity**(2025-11-18, Gemini 3와 함께 출시)는 "agent-first" IDE. Windsurf 팀 영입(약 24억 달러 규모 acqui-hire, 보도 기준) 기술 기반. 에이전트가 계획·실행·검증하고 결과물을 artifact로 보여 준다. Gemini 외 Claude 등 타사 모델도 선택 가능(출시 시점 보도).
- 2026-05 **Antigravity 2.0**: 독립 데스크톱 앱 + IDE + CLI + SDK(프리뷰)의 4제품 플랫폼, 동일 agent harness 공유. 기본 모델 Gemini 3.5 Flash. 프로젝트·worktree·cron 예약 작업 지원. Google AI Ultra $100/월 신설(Pro 대비 5배 용량).
- **Jules**: 비동기(async) 코딩 에이전트. GitHub 저장소를 Cloud VM에 복제 → Gemini로 계획 수립 → diff 제시 → PR 생성. 이슈에 `jules` 라벨을 붙여 할당 가능. 2024-12 Labs 실험 → 2025-05-20 공개 베타 → 2025-08-06 베타 종료.
- Jules 플랜(jules.google 열람값): 무료 15 tasks/일·동시 3개(Gemini 2.5 Pro), Pro 100 tasks/일·동시 15개(Gemini 3 Pro), Ultra 300 tasks/일·동시 60개. "I/O 2026에서 Jules GA" 및 V2 소문은 2차 블로그 출처뿐이라 **미확인**.

## 핵심 개념·용어 정의
- **GEMINI.md**: Gemini CLI가 매 세션 읽는 계층형 컨텍스트 파일. CLAUDE.md와 같은 역할.
- **Antigravity**: Google의 agent-first 개발 플랫폼(IDE·데스크톱·CLI·SDK). 사람은 "건축가", 에이전트는 "시공"을 맡는다는 설계 철학.
- **Antigravity CLI**: Gemini CLI 후속 터미널 도구(Go, 비공개). 백그라운드 에이전트 오케스트레이션을 지원.
- **Jules**: 클라우드 VM에서 도는 비동기 에이전트. 대화형이 아니라 "맡기고 나중에 PR 받기" 방식.
- **Trusted folders**: Gemini CLI에서 폴더 단위로 신뢰 여부를 정해 실행 정책을 달리하는 기능.

## 강연에 쓸 만한 포인트
- 교훈형 사례: "무료 오픈소스 CLI → 1년 만에 비공개 제품으로 대체". 도구 선택 시 벤더 종속·서비스 종료 위험을 보여 주는 실제 예. 연구 워크플로를 특정 도구에 묶지 말고 AGENTS.md 같은 공통 형식에 지식을 남기라는 메시지로 연결.
- 타임라인 도식: 2024-12 Jules(Labs) → 2025-06 Gemini CLI → 2025-08 Jules 정식 → 2025-11 Antigravity → 2026-05 Antigravity 2.0·CLI 전환 → 2026-06-18 Gemini CLI 개인 서비스 중단.
- 숫자: Gemini CLI 무료 한도 60 req/min, 1,000 req/day; Jules 무료 15 tasks/day.
- 비유: Jules = "숙제 맡기고 다음 날 채점만 하는 조교", CLI = "옆자리 페어 프로그래머".
- 인용(1개): "The project remains available to the community as an Apache 2.0 licensed repository" — Gemini CLI GitHub Discussion #27274

## 원본 그림
- Gemini CLI 터미널 화면 스크린샷 — https://github.com/google-gemini/gemini-cli/raw/main/docs/assets/gemini-screenshot.png
- Gemini CLI → Antigravity CLI 전환 공지 헤더 이미지(1200x600) — https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/GeminiCLI-AntigravityCLI_1200x600_BlogHeader.original.png
- Google Antigravity @ I/O 2026 헤더 이미지 — https://antigravity.google/assets/image/blog/Google-IO---Wide.jpg (상대경로에서 복원, 접속 확인 필요)
- Jules 작업 흐름(plan 단계) 그림 — https://jules.google/plan-01.png, https://jules.google/plan-02.gif, https://jules.google/plan-03.gif (상대경로에서 복원, 접속 확인 필요)

## Claude Code와의 비교점
- **형태**: Gemini CLI(CLI, 오픈소스) → Antigravity(IDE·데스크톱·CLI, 비공개) / Jules(클라우드 비동기). Claude Code는 CLI·IDE·데스크톱·웹(클라우드) 모두 한 제품군.
- **모델**: Gemini 3.x 중심(Antigravity는 일부 타사 모델 허용). Claude Code는 Claude 전용.
- **권한·샌드박스**: Gemini CLI는 trusted folders·sandbox 옵션, Jules는 격리 Cloud VM. Claude Code는 permission mode + sandbox + hooks.
- **지침 파일**: GEMINI.md(설정으로 AGENTS.md 사용 가능) ↔ CLAUDE.md(AGENTS.md 직접 읽기 지원). Antigravity CLI의 파일 규칙은 공식 공지에서 확인 못함.
- **확장**: Gemini CLI extensions·MCP·skills·hooks·subagents → Antigravity plugins로 이관. Claude Code의 plugins·skills·hooks·subagents·MCP와 구성이 매우 유사(업계 수렴).
