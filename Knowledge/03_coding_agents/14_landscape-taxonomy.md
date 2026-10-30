# AI 코딩 도구 지형도: 실행 위치 × 개발 주체 (Landscape taxonomy)

- **저자/기관**: (종합) a16z — Guido Appenzeller, Yoko Li / Thoughtworks Technology Radar Vol.34 / The Pragmatic Engineer — Gergely Orosz 외 / 보조: Kingy.ai 시장지도
- **발행일**: a16z 2025-10-09; Thoughtworks Radar Vol.34 2026-04; Pragmatic Engineer 2026-03-03 (설문 2026-01-27~02-17) (2026-09-29 열람)
- **URL**:
  - https://a16z.com/the-trillion-dollar-ai-software-development-stack/
  - https://www.thoughtworks.com/en-us/radar/tools/claude-code
  - https://www.thoughtworks.com/radar/techniques/team-of-coding-agents
  - https://newsletter.pragmaticengineer.com/p/ai-tooling-2026
  - https://kingy.ai/blog/state-of-ai-coding-tools-2026/ (보조, 2차 자료)
- **자료 유형**: 보고서 | 블로그

## 핵심 요약
- a16z(2025-10-09)는 AI 코딩을 "AI의 첫 번째 진짜 큰 시장"으로 보고, 전 세계 개발자 약 3천만 명의 부가가치를 약 3조 달러(프랑스 GDP 수준)로 추산했다. 워크플로를 **Plan → Code → Review**로 정리하고, 계획·코드 생성·리뷰·테스트·문서·레거시 마이그레이션·코드 검색·실행 샌드박스 등 영역별 시장지도를 제시했다.
- a16z에 따르면 기업 고객 기준 현재 ROI가 가장 높은 용도는 **레거시 코드 마이그레이션**이다.
- Thoughtworks Technology Radar는 Claude Code를 2025-11 Trial → 2026-04(Vol.34) **Adopt**로 올렸다. 근거는 실제 프로덕션 납품에서 일상적으로 쓰이고 "기준점(benchmark)"처럼 취급된다는 점. 경쟁 CLI로 Codex CLI, Gemini CLI, OpenCode, pi를 열거했다.
- 같은 Radar는 "team of coding agents"를 Assess, 수십~수백 개 에이전트를 투입하는 "coding agent swarms"를 **Caution**으로 분류했다(2026-04).
- Pragmatic Engineer 설문(906명, 2026-01-27~02-17): Claude Code가 2025-05 정식 출시 후 약 8개월 만에 사용량 1위. "가장 좋아하는 도구" 46% Claude Code, 19% Cursor, 9% GitHub Copilot. 55%가 에이전트를 정기적으로 사용, 70%가 2~4개 도구를 병행.
- 같은 설문에서 회사 규모별 차이: 스타트업은 Claude Code(75%)·Cursor(42%), 직원 1만 명 이상 기업은 GitHub Copilot(56%)이 기본값.
- 2026년 시장 요약 자료들(예: Kingy.ai, 2차 자료)은 AI IDE / CLI 에이전트 / 클라우드 에이전트 / GitHub-native 에이전트 / 오픈소스·로컬 에이전트 / 앱 빌더로 영역이 나뉘되 서로 겹쳐지고 있다고 정리한다. (시장 규모·ARR 수치는 2차 자료라 강의에는 쓰지 않는 것을 권장)

## 핵심 개념·용어 정의
- **Terminal CLI agent**: 터미널에서 실행되어 파일을 읽고/고치고 셸 명령을 직접 실행하는 에이전트. 예: Claude Code, OpenAI Codex CLI, Gemini CLI, OpenCode, Aider, Goose.
- **IDE agent / AI IDE**: 에디터 안에 통합된 채팅·자동완성·에이전트 모드. 예: Cursor, GitHub Copilot(VS Code), Windsurf, JetBrains AI/Junie, Google Antigravity, Cline·Roo(확장).
- **Cloud / async agent**: 원격 샌드박스에서 비동기로 작업하고 PR로 결과를 돌려주는 형태. 예: Claude Code on the web, Codex (cloud), GitHub Copilot coding agent, Google Jules, Devin.
- **App builder**: 비개발자도 자연어로 웹앱 전체를 생성·배포하는 호스팅형 도구. 예: Lovable, Replit Agent, v0(Vercel), Bolt.
- **Model lab vs IDE vendor vs open source**: 모델을 직접 만드는 회사가 자사 에이전트를 내는지(Anthropic·OpenAI·Google), 에디터/플랫폼 회사가 여러 모델을 얹는지(Anysphere/Cursor, GitHub/Microsoft, JetBrains, Cognition), 커뮤니티 오픈소스인지(Cline, Aider, OpenHands, OpenCode, Goose)의 구분.
- **Harness(하네스)**: 모델을 감싸 도구 호출·권한·컨텍스트를 관리하는 실행 틀. 같은 모델이라도 하네스에 따라 성능이 크게 달라짐(→ 15번 파일 참고).

## 강연에 쓸 만한 포인트
- **슬라이드용 2축 표 (제안)** — 행: 실행 위치, 열: 개발 주체

| 실행 위치 \ 개발 주체 | 모델 연구소 (Model labs) | IDE·플랫폼 기업 | 오픈소스 |
|---|---|---|---|
| 터미널 CLI | Claude Code, Codex CLI, Gemini CLI | Copilot CLI | Aider, OpenCode, Goose |
| IDE 통합 | Claude Code(VS Code/JetBrains 확장), Google Antigravity | Cursor, GitHub Copilot, Windsurf, JetBrains Junie | Cline, Roo Code, Continue |
| 클라우드·비동기 | Claude Code on the web, Codex cloud, Jules | Copilot coding agent, Devin | OpenHands |
| 앱 빌더(비개발자) | (Claude Artifacts 등 일부) | Lovable, Replit Agent, v0, Bolt | — |

  - 주의: 도구 소속은 2026-09 기준 저자 정리이며, 각 칸은 "대표 예시"이지 전수 목록이 아님. Windsurf는 2025-07 Cognition에 인수됨(사실관계 재확인 권장).
- 비유: "같은 엔진(모델)을 서로 다른 차체(하네스·UI)에 얹는다" — Cursor는 여러 회사 엔진을 쓰는 차, Claude Code는 엔진 제조사가 직접 만든 차.
- 도식 아이디어: 가로축 "사람이 얼마나 지켜보나(동기 ↔ 비동기)", 세로축 "사용자 코딩 숙련도(개발자 ↔ 비개발자)" 2×2 평면에 도구 배치.
- 숫자: Pragmatic Engineer 2026 설문 "가장 좋아하는 도구" 46% Claude Code (n=906, 2026-01~02).

## 원본 그림
- a16z 시장지도(SDLC 단계별 AI 코딩 스타트업 배치) — https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-5-r9.png
- a16z Plan → Code → Review 흐름도 — https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-1-r3.png
- Pragmatic Engineer 설문 도구 사용량 차트 — substackcdn 이미지(직접 URL 미확인; 기사 페이지에서 확인 필요)
- Thoughtworks Radar 블립 페이지 — 별도 이미지 없음

## Claude Code와의 연결점
- Claude Code는 "모델 연구소가 직접 만든 터미널 CLI 에이전트"로 출발해, IDE 확장·데스크톱·웹(클라우드) 표면으로 확장 → 표의 여러 칸에 동시에 걸쳐 있음(05번 파일 참고).
- Thoughtworks가 Adopt 사유와 함께 제시한 주의점(컨텍스트 엔지니어링, 팀 공유 지침, 하네스 엔지니어링, 코드 리뷰 경계)은 CLAUDE.md·skills·hooks·권한 설정과 그대로 대응.
- 경쟁 도구와 비교할 때 "모델 성능"보다 "실행 위치·권한·검증 루프"가 사용자 경험을 가른다는 메시지로 연결.
