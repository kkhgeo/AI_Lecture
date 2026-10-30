# 03_coding_agents 자료 색인

- 수집일: 2026-09-29
- 주제: 코딩 에이전트(Coding agent) — Claude Code란 무엇인가, Codex·Gemini·Copilot·Cursor·오픈소스 도구까지
- 청중: 대학원생
- 수록: 19개 파일 (한 파일에 같은 주제의 짧은 자료 여러 개를 묶은 경우 있음)
- 저작권: 요약·재서술 중심, 직접 인용은 파일당 1개(15단어 미만)

## 1. 자료 목록

### A. 개념: 에이전트와 에이전트 루프

| 파일 | 한 줄 설명 |
|---|---|
| 01_anthropic-building-effective-agents.md | workflow vs agent, augmented LLM, 다섯 가지 workflow 패턴, "도구를 루프로 쓰는 LLM" 정의 |
| 02_agent-loop-claude-code-how-it-works.md | 맥락 수집 → 행동 → 검증 루프, model + harness, 도구 5범주, 체크포인트·권한 |
| 03_openai-codex-agent-loop.md | OpenAI의 Codex 루프 해부(2026-01-23): harness, turn, 프롬프트 구성, 캐싱, 압축 |
| 04_chat-vs-agent-and-definitions.md | chatbot / copilot / agent 구분표(재구성), vibe coding(2025-02) vs agentic engineering(2026-02) |

### B. Claude Code

| 파일 | 한 줄 설명 |
|---|---|
| 05_claude-code-overview-and-surfaces.md | 실행 환경(터미널·IDE·데스크톱·웹·모바일·Slack·CI), 요금제, 출시 연혁(2025-02 프리뷰 → 2025-05 GA → …) |
| 06_claude-code-tools-permissions-sandbox.md | 내장 도구, 권한 모드 6종, 샌드박스(승인 요청 84% 감소), 권한 요청 93% 승인, auto mode |
| 07_claude-code-extensibility.md | CLAUDE.md·skills·MCP·hooks·subagents·plugins·Agent SDK 한 줄 정의와 로드 시점·비용 |
| 08_claude-code-non-coding-and-research-use.md | 세션 27%가 비코딩, 계획은 사람 70%·실행은 20%, 전공 지식 > 코딩 실력, Economic Index |

### C. 다른 도구와 공통 표준

| 파일 | 한 줄 설명 |
|---|---|
| 09_openai-codex.md | Codex CLI(오픈소스)·IDE·cloud·앱, 샌드박스·승인 모드, 요금제, 모델 연혁(→ GPT-6 Sol/Luna 2026-09-22) |
| 10_google-gemini-cli-and-jules.md | Gemini CLI → Antigravity CLI 전환(2026-05-19 발표, 2026-06-18 개인용 종료), Antigravity, Jules |
| 11_github-copilot-agent-and-cursor.md | Copilot agent mode·cloud agent(이슈 → PR), 학생·교원 무료, Cursor(SpaceX 인수 2026-08-14 완료) |
| 12_open-source-agents.md | OpenCode·Cline·Aider·Goose·OpenHands·Kilo, 로컬 모델, 비용·프라이버시·재현성 |
| 13_agents-md-standard.md | AGENTS.md 공통 지침 파일(2025-08, 6만+ 프로젝트), AAIF(2025-12-09), MCP |

### D. 지형·근거·주의점

| 파일 | 한 줄 설명 |
|---|---|
| 14_landscape-taxonomy.md | 실행 위치(CLI/IDE/cloud/앱 빌더) × 개발 주체(모델 회사/IDE 회사/오픈소스) 표, a16z 지도, Thoughtworks Radar |
| 15_benchmarks-swe-bench-terminal-bench.md | SWE-bench Verified 포화·Pro, Terminal-Bench 2.0, METR 작업 길이 약 7개월마다 2배 |
| 16_adoption-surveys.md | Stack Overflow 2025(84% 사용, 46% 불신, 31% 에이전트), JetBrains·Octoverse·DORA 2025 |
| 17_productivity-evidence-metr-rct.md | METR RCT(19% 느려짐, 본인은 20% 빨라졌다고 믿음), 2026 후속, Microsoft 연구, DORA |
| 18_research-and-academia-use.md | 사회과학자 설문(20% 에이전트 사용), 장기 과학 계산 사례, Nature의 연구 훈련 약화 우려 |
| 19_risks-security-cost.md | 프롬프트 인젝션(lethal trifecta), Replit·Amazon Q 사고, 비밀 유출률, 샌드박스, 비용(하루 약 $13) |

## 2. 슬라이드 구상과 자료 연결

| 슬라이드 | 주 자료 | 그림 후보 |
|---|---|---|
| 1. 코딩 에이전트(Coding agent) | 01, 04, 08 | Anthropic augmented LLM / autonomous agent 그림 (01) |
| 2. 에이전트 루프(Agent loop) | 02, 03 | Claude Code agentic-loop.svg (02, 다크 버전 있음), OpenAI agent loop (03) |
| 3. 도구 지형(Landscape) | 14, 05, 09–12 | 직접 표로 작성 (14의 표 초안), a16z 시장 지도 참고 |
| 4. 공통 구조(Common anatomy) | 06, 07, 13 | 컨텍스트 파트 4장과 같은 네 줄 형식 |
| (후보) 근거와 주의점 | 15, 17, 19, 18 | METR 작업 길이 그래프, METR RCT 예상 vs 실제 그래프 |

## 3. 교차확인 결과와 남은 미확인 항목

- 확인함(2026-09-29): Cursor의 SpaceX 인수(CNBC 등), GPT-6 Sol·Luna 출시(TechCrunch·GitHub Changelog), Gemini CLI → Antigravity CLI 전환(Google Developers Blog).
- 미확인(각 파일에 표시):
  - Codex 앱의 ChatGPT 앱 통합 날짜(2026-07-09, Wikipedia 기준)
  - Jules 정식 출시
  - Claude Code 데스크톱 개편 날짜
  - 카파시의 2026-02-04 X 게시물 원문
  - Nature 기사 본문(유료)
  - DORA 2026 ROI 수치(2차 보도)
- 제품 정보는 1~2개월 단위로 바뀐다. 강연 직전에 09–12의 요금·모델명을 다시 확인할 것.
