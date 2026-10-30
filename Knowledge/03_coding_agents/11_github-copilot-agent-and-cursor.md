# GitHub Copilot agents and Cursor (IDE 기반 에이전트)

- **저자/기관**: GitHub (Docs, Changelog), Anysphere/Cursor (pricing, changelog), 보조: Wikipedia
- **발행일**: 문서 상시 갱신 (2026-09-29 열람). 주요 날짜는 아래 참조
- **URL**:
  - https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
  - https://github.blog/changelog/2025-05-19-github-copilot-coding-agent-in-public-preview/
  - https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/
  - https://github.blog/changelog/2026-04-01-research-plan-and-code-with-copilot-cloud-agent/
  - https://github.com/features/copilot/plans
  - https://cursor.com/pricing
  - https://cursor.com/changelog
  - https://en.wikipedia.org/wiki/Cursor_(company) (보조)
- **자료 유형**: 공식문서 (+ 기사 보조)

## 핵심 요약
- GitHub Copilot의 에이전트는 두 갈래다. (1) **Agent mode**: VS Code·JetBrains 등 편집기 안에서 파일을 고르고 터미널 명령을 실행하며 오류를 반복 수정하는 동기식 에이전트. (2) **Copilot coding agent → 2026년 초 "Copilot cloud agent"로 개명**: GitHub 이슈를 Copilot에게 할당하면 백그라운드에서 작업해 PR을 연다.
- Cloud agent는 **GitHub Actions** 기반의 일회용(ephemeral) 개발 환경에서 코드 탐색·수정·테스트·린트를 수행. 한 세션 최대 59분. 개명과 함께 PR 흐름에 한정되지 않고 조사·계획 작업으로 확장.
- 작업 위임 경로: GitHub 이슈, Copilot Chat, Teams·Slack 연동. 모든 유료 Copilot 플랜에서 사용 가능(Business/Enterprise는 관리자 정책 활성화 필요). MCP 서버와 저장소 커스텀 지침(`.github/copilot-instructions.md`, AGENTS.md) 지원.
- 터미널용 **Copilot CLI**(2025-09-25 공개 프리뷰)와 데스크톱 "Copilot app"도 존재. 2026-08-12 Agent Plugins 1.0 GA(VS Code·CLI·SDK·app 공통, changelog 검색 결과 기준).
- Copilot 요금(2026-09 열람값, 크레딧 체계로 개편됨): Free $0(인라인 제안 월 2,000, 제한된 agent), Pro $10, Pro+ $39, Max $100. 초과분 크레딧당 $0.01. **인증된 학생·교원·OSS 메인테이너는 무료 접근** — 대학원생에게 중요.
- **Cursor**(Anysphere)는 VS Code 포크 기반 AI IDE. 2025-10 Cursor 2.0에서 자체 코딩 모델 **Composer**와 다중 에이전트 병렬 실행 도입, 2026-04-02 Cursor 3(Agents Window, Design Mode, 2차 출처), 이후 Composer 2.5까지(2차 출처).
- Cursor **background agents → cloud agents**: 저장소를 클라우드 VM에 복제해 자율 작업 후 PR 반환. 2026-08~09 changelog: 서브에이전트 격리 VM, `/goal`, self-hosted machines(2026-09-02), Cursor Projects(2026-09-10, 코디네이터가 다수 서브에이전트에 위임), Security Review 봇(2026-09-23).
- Cursor 요금: Hobby 무료, Individual $20/월(Pro/Pro+/Ultra 단계), Teams $40/user/월, Enterprise 별도. 자체 모델(Composer·Auto) 사용량과 타사 모델(Claude·GPT·Gemini) 사용량을 별도 풀로 계산.
- 기업 동향: 2025-11 기업가치 293억 달러·연매출 10억 달러+(Wikipedia 기준). SpaceX가 2026-04-21 인수 옵션 계약, 2026-06-16 600억 달러 전액 주식 인수 발표, 2026-08-14 인수 완료(SpaceXAI 산하 자회사) — CNBC(https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html)·SatNews로 교차확인(2026-09-29). 현재 pricing 페이지에 Grok 할당이 표기되는 것도 이 변화와 연관된 것으로 보임(추정).

## 타임라인
- 2025-02-06: VS Code Copilot agent mode 프리뷰(날짜 기억 기반, 재확인 권장)
- 2025-05-19: Copilot coding agent 공개 프리뷰(Microsoft Build)
- 2025-09-25: Copilot coding agent GA / Copilot CLI 공개 프리뷰
- 2026-03-19: coding agent 시작 속도 50% 개선
- 2026-04-01 무렵: "Copilot cloud agent"로 개명(changelog), 구 필드명은 2026-08-01까지 호환
- Cursor: 2025-05 background agents 프리뷰, 2025-06 Cursor 1.0, 2025-10 Cursor 2.0 + Composer, 2026-04-02 Cursor 3, 2026-05-20 Cursor 3.5 cloud agents(2차 출처), 2026-09 Projects·Security Review

## 핵심 개념·용어 정의
- **Agent mode (Copilot)**: IDE 안 대화형 에이전트. 사람이 지켜보며 승인.
- **Copilot cloud agent (구 coding agent)**: 이슈 할당 → Actions 러너에서 작업 → PR. "비동기 팀원" 모델.
- **Premium request / AI credits**: 에이전트·챗·리뷰에 소모되는 사용량 단위(인라인 자동완성은 제외).
- **Composer (Cursor)**: Cursor가 직접 학습한 에이전트용 코딩 모델. 빠른 응답 지향.
- **Cloud agents (Cursor)**: 원격 VM에서 병렬 실행되는 에이전트(구 background agents).
- **Bugbot**: Cursor의 PR 자동 코드리뷰 봇.

## 강연에 쓸 만한 포인트
- 도식 아이디어: 2x2 표 — 가로축 "동기(옆에서 같이) vs 비동기(맡기고 나중에)", 세로축 "IDE vs 클라우드". Copilot agent mode·Cursor agent = 동기/IDE, Copilot cloud agent·Cursor cloud agents·Codex cloud·Jules = 비동기/클라우드, Claude Code = 양쪽 모두.
- 대학원생 팁: GitHub Education 인증으로 Copilot 무료 → 이슈 하나를 Copilot에 할당해 PR을 받아 보는 실습이 저비용으로 가능.
- 숫자: cloud agent 세션 상한 59분; Copilot 초과 크레딧 $0.01; Cursor 개인 $20/월.
- 인용(1개): Copilot cloud agent는 "just like a human developer" 배경에서 독립 작업 — GitHub Docs

## 원본 그림
- GitHub Docs about-coding-agent 페이지: 이미지 확인되지 않음 — 없음
- Cursor changelog 2026-09-10(Cloud agent dashboard), 2026-09-02(Remote Machines 메뉴) 항목에 스크린샷 존재하나 직접 이미지 URL은 확보 못함 — 없음(changelog 페이지에서 캡처 필요)

## Claude Code와의 비교점
- **형태**: Copilot·Cursor는 IDE가 출발점, CLI·클라우드로 확장. Claude Code는 CLI가 출발점, IDE·데스크톱·웹으로 확장. 결과적으로 표면 구성은 수렴.
- **모델**: Copilot·Cursor는 다중 모델(Claude, GPT, Gemini 등 선택) + Cursor는 자체 모델 Composer. Claude Code는 Claude 전용.
- **권한·샌드박스**: Copilot cloud agent는 Actions 러너 + 브랜치 규칙(ruleset bypass 필요 사례). Cursor는 클라우드 VM·self-hosted machines. Claude Code는 로컬 permission 체계 + 클라우드 세션.
- **지침 파일**: Copilot = `.github/copilot-instructions.md` + AGENTS.md, Cursor = `.cursor/rules/`(구 `.cursorrules`) + AGENTS.md. Claude Code `/init`은 이 두 파일을 읽어 CLAUDE.md로 흡수.
- **확장**: 셋 다 MCP·skills·hooks·plugins 지원(Copilot Agent Plugins 1.0, Cursor plugins marketplace).
