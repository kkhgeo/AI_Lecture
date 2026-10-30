# Codex — OpenAI's coding agent (CLI · IDE · cloud · app) (OpenAI Codex)

- **저자/기관**: OpenAI (공식문서·블로그·GitHub), 보조: Wikipedia, TechCrunch
- **발행일**: 문서는 상시 갱신(2026-09-29 열람). 주요 발표일은 아래 타임라인 참조
- **URL**:
  - https://learn.chatgpt.com/docs (구 developers.openai.com/codex → 308 리다이렉트)
  - https://learn.chatgpt.com/docs/models
  - https://learn.chatgpt.com/docs/pricing
  - https://learn.chatgpt.com/docs/agent-approvals-security
  - https://developers.openai.com/codex/guides/agents-md
  - https://github.com/openai/codex
  - https://openai.com/index/introducing-gpt-6-sol-and-luna/ (2026-09-22)
  - https://openai.com/index/introducing-the-codex-app/
  - https://en.wikipedia.org/wiki/Codex_(AI_agent) (타임라인 보조)
- **자료 유형**: 공식문서 (+ 기사 보조)

## 핵심 요약
- Codex는 하나의 에이전트를 여러 "표면(surface)"에서 쓰는 제품군이다: 터미널용 **Codex CLI**(오픈소스), VS Code 계열 **IDE extension**, 브라우저에서 비동기 작업을 맡기는 **Codex cloud**, 여러 에이전트를 관리하는 **데스크톱 앱**(macOS·Windows·Linux). 2026-07-09 Codex 앱은 ChatGPT 데스크톱 앱에 통합되었다(Wikipedia 기준, 공식 발표문 미확인).
- Codex CLI는 Apache-2.0 라이선스, 핵심 구현은 Rust(`codex-rs`). npm(`@openai/codex`), Homebrew, 설치 스크립트로 설치하며 GitHub 스타 약 12.7만(2026-09-29 열람).
- 로그인은 "Sign in with ChatGPT"(구독 사용량 소진) 또는 API key(표준 API 요금, 포함 한도 없음) 두 방식.
- 로컬 실행 시 **sandbox mode**(무엇이 기술적으로 가능한가)와 **approval policy**(언제 사람에게 묻는가)를 분리해 설정한다. 기본은 workspace-write + 네트워크 차단.
- Codex cloud는 작업마다 격리된 컨테이너를 만든다: setup 단계에서만 네트워크로 의존성 설치, agent 단계는 기본 오프라인(도메인 allowlist로 개방 가능). 결과는 diff/PR로 돌아온다.
- 모델은 세대가 빠르게 교체된다: codex-1(o3 기반, 2025-05) → GPT-5-Codex(2025-09) → GPT-5.x-Codex 계열 → GPT-5.5(2026-04-23) → **GPT-6 Astra/Sol/Luna**(2026-09). GPT-5.5는 2026-10-14 Codex에서 퇴역 예정.
- 요금: Codex는 ChatGPT Free/Go/Plus/Pro/Business/Edu/Enterprise 플랜에 포함되며 "ChatGPT Work와 Codex가 사용량 공유". Plus $20/월, Pro $100/월(Plus 대비 5x 또는 20x 한도), Business $20/user/월부터(pricing 페이지 열람값, 변동 잦음).
- 지침 파일은 **AGENTS.md**(OpenAI가 주도한 형식). 디렉터리마다 `AGENTS.override.md` → `AGENTS.md` → fallback 파일명 순으로 찾고, 합산 32 KiB(`project_doc_max_bytes`) 한도.
- 사용자 규모: 주간 활성 개발자 약 160만(2026-02) → 200만+(2026-03) → 약 400만(검색 결과 인용, 원 출처 미확인).

## 타임라인 (정확한 날짜)
- 2025-04-16: Codex CLI 오픈소스 공개(당시 TypeScript, 이후 Rust 재작성)
- 2025-05-16: Codex cloud research preview (codex-1 모델, Pro/Team/Enterprise 우선; Plus는 2025-06)
- 2025-09-15: GPT-5-Codex 및 "Introducing upgrades to Codex" (IDE extension 포함) — 날짜는 기억 기반, 재확인 권장
- 2025-10-06: Codex 정식 출시(GA, DevDay) — 재확인 권장
- 2025-11-19: GPT-5.1-Codex-Max — 재확인 권장
- 2026-02 초(VentureBeat 2026-02-02 보도): Codex 데스크톱 앱 macOS 출시 / 2026-03-04 Windows
- 2026-02-05: GPT-5.3-Codex / 2026-02-12: GPT-5.3-Codex-Spark(저지연)
- 2026-03-05: GPT-5.4 / 2026-03-10: Codex Security / 2026-03-19: Astral(uv, ruff 제작사) 인수 발표
- 2026-04-23: GPT-5.5
- 2026-07-09: Codex 앱이 ChatGPT 데스크톱 앱에 통합(Wikipedia)
- 2026-09-03: GPT-6 Astra(제한 프리뷰), 2026-09-04 유료 사용자
- 2026-09-22: GPT-6 Sol·Luna 출시 (API 가격 Sol $2/$10, Luna $0.10/$0.50 per 1M in/out tokens) — TechCrunch(https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/)·GitHub Changelog로 교차확인(2026-09-29)
- 2026-08-31: gpt-5.4 / 5.4-mini ChatGPT 로그인 Codex에서 퇴역 → 2026-10-14 GPT-5.5 퇴역 예정

## 핵심 개념·용어 정의
- **Codex CLI**: 로컬 터미널에서 도는 오픈소스 에이전트. 파일 읽기·수정·명령 실행을 샌드박스 안에서 수행.
- **Codex cloud**: 웹(chatgpt.com/codex)이나 GitHub에서 작업을 맡기면 원격 컨테이너에서 병렬·비동기로 수행해 PR을 만드는 모드.
- **Sandbox mode**: `read-only` / `workspace-write`(기본) / `danger-full-access`(샌드박스·승인 모두 없음).
- **Approval policy**: `on-request`(워크스페이스 밖 편집·네트워크 시 승인 요청) / `never` / `granular`(범주별로 묻기·자동거부 혼합). 구버전 `untrusted`, `on-failure`도 있었음.
- **Auto-review**: 승인 요청을 사람 대신 reviewer 에이전트가 먼저 심사(데이터 유출·자격증명·파괴적 명령 패턴 점검).
- **GPT-6 Astra / Sol / Luna**: 2026-09 기준 최상위(복잡 작업·computer use) / 코딩·에이전트 주력 / 저비용·대량 처리 모델.
- **Credits**: 플랜 한도 초과 시 구매하는 사용 단위(예: Luna 입력 1M 토큰당 2.5 credits, Astra 250 credits).

## 강연에 쓸 만한 포인트
- 비유: sandbox = "울타리", approval = "초인종". 울타리 안에서는 자유롭게 일하고, 울타리 밖으로 나갈 때만 초인종을 누른다. Claude Code의 permission mode와 대응시켜 설명하기 좋다.
- 도식 아이디어: 한 모델(GPT-6 Sol) → 네 개 표면(CLI·IDE·cloud·app)으로 갈라지는 부채꼴 그림. "모델은 엔진, 표면은 차체".
- 숫자: 주간 활성 사용자 160만(2026-02) → 400만(2026-09 무렵, 미확인). 모델 교체 주기 약 1~2개월. GPT-6 Sol API 가격이 이전 세대 대비 절반.
- 대학원생 관점: Free 플랜에도 GPT-6 Luna로 Codex가 들어간다(pricing 페이지 기준) — 비용 부담 없이 체험 가능.
- 인용(1개): "Codex can read files, make edits, and run commands in the workspace." — OpenAI Codex docs (workspace-write 모드 설명)

## 원본 그림
- Codex CLI 터미널 스플래시 스크린샷 — https://github.com/openai/codex/raw/main/.github/codex-cli-splash.png
- 공식 블로그(Introducing the Codex app, GPT-6 Sol/Luna)에 히어로 이미지가 있으나 직접 이미지 URL은 확인하지 못함 — 없음(미확인)

## Claude Code와의 비교점
- **형태**: 둘 다 CLI + IDE + 데스크톱 + 클라우드(비동기) 표면을 모두 가진다. Codex CLI는 오픈소스(Apache-2.0), Claude Code는 소스 비공개.
- **모델**: Codex는 OpenAI GPT 계열(GPT-6 Sol 등) 고정, Claude Code는 Anthropic Claude 계열. 둘 다 구독 로그인 또는 API key.
- **권한·샌드박스**: Codex는 OS 수준 sandbox(기본 네트워크 차단) + approval policy 2축. Claude Code는 permission mode·allow/deny 규칙·hooks 중심에 선택적 sandbox. Codex의 auto-review는 Claude Code의 auto mode 분류기와 비슷한 발상.
- **지침 파일**: Codex = AGENTS.md(+override), Claude Code = CLAUDE.md(현재는 AGENTS.md도 직접 읽음, v2.1.277+).
- **확장**: 둘 다 MCP 지원, skills·plugins 개념 보유. 클라우드 모드에서 둘 다 결과를 PR로 반환.
