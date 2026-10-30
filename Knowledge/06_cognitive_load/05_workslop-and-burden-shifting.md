# Workslop and Burden Shifting: AI Output That Moves Effort to the Receiver (워크슬롭과 부담 전가)
- **저자/기관**: (1) Kate Niederhoffer, Gabriella Rosen Kellerman, Angela Lee, Alex Liebscher, Kristina Rapuano, Jeffrey T. Hancock — BetterUp Labs & Stanford Social Media Lab, Harvard Business Review; (2) Daniel Stenberg(curl 메인테이너); (3) GitHub·오픈소스 메인테이너 논의(The Register 보도)
- **발행일**: HBR 2025-09-22(2025-09-25 수정); curl 블로그 2025-07-14, 2026-01-26; The Register 2026-02-03 (2026-10-01 열람)
- **URL**:
  - HBR "AI-Generated 'Workslop' Is Destroying Productivity" — https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity (유료벽)
  - BetterUp 요약 페이지 — https://www.betterup.com/workslop , 블로그 — https://www.betterup.com/blog/hidden-costs-workslop
  - Stenberg "Death by a thousand slops" — https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/
  - Stenberg "The end of the curl bug-bounty" — https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
  - The Register "GitHub ponders kill switch for pull requests" — https://www.theregister.com/2026/02/03/github_kill_switch_pull_requests_ai/
- **자료 유형**: 기사(HBR, 설문 기반) | 블로그 | 기사

## 핵심 요약
- **정의**: 워크슬롭(workslop) = 좋은 결과물처럼 보이지만 과제를 실질적으로 진전시킬 내용이 없는 AI 생성 업무물. 그럴듯한 슬라이드, 긴 보고서, 맥락 없는 코드 등. 생산자가 아낀 노력이 수신자의 해석·수정·재작업으로 넘어간다.
- **규모(미국 정규직 사무직 설문, 2025-09)**: 지난 한 달간 워크슬롭을 받은 적 있다 40%. 받은 업무물 중 워크슬롭 비율 추정 평균 15.4%. 표본은 HBR/보도 기준 1,150명, BetterUp 블로그 기준 1,004명으로 출처마다 다름(조사가 진행형이라 갱신된 것으로 보임 — 인용 시 "약 1천 명" 권장).
- **시간·비용**: 건당 처리 시간 평균 약 2시간(보도 1시간 56분, BetterUp 블로그 1시간 51분). 1인당 월 186달러 상당, 1만 명 조직이면 연 900만 달러 이상 손실 추정(연구진의 환산치).
- **흐름 방향**: 주로 동료 간(40%), 부하→관리자(18–19%), 관리자→부하(16%). 관리자의 수신 비율이 더 높다는 보고(BetterUp 블로그: 관리자 54% vs 개인 기여자 38.5% — 2차 페이지, 원문 미확인).
- **관계 비용**: 받은 사람의 약 절반이 보낸 사람을 덜 창의적·덜 유능·덜 신뢰할 만하다고 봤고, 42%는 덜 믿을 만하다, 약 3분의 1은 덜 똑똑하다고 평가. 짜증(53–54%), 혼란(38%), 불쾌(22%). 약 30%는 그 사람과 협업할 의향이 줄었다고 응답(BetterUp 블로그).
- **오픈소스의 코드 버전 — curl**: 2025년 보안 보고 중 약 20%가 AI 슬롭, 진짜 취약점은 약 5%(2025-07 기준). 보안팀 7명, 보고 1건마다 3–4명이 30분~최대 3시간 투입. 결국 2026-01-31 버그바운티 종료(2019년 이후 확인 취약점 87건, 상금 10만 달러 이상).
- **GitHub 차원**: 2026-02 GitHub가 PR 비활성화·협업자 한정 등 "킬 스위치"를 검토. 한 메인테이너는 AI로 만든 PR 10건 중 1건만 기준을 충족한다고 말함(개인 추정). Microsoft의 한 메인테이너는 리뷰어가 작성자가 코드를 이해했다고 가정할 수 없게 되어 "리뷰 신뢰 모델이 깨졌다"고 지적. 이후 tldraw는 외부 PR 자동 종료, Ghostty는 초대제 기여로 전환했다는 보도(2차, 원 정책 문서 미확인).
- **공통 구조**: 생성 비용은 거의 0으로 떨어졌지만 검토 비용은 그대로 → 노력이 생산자에서 수신자(동료, 리뷰어, 메인테이너)에게로 이전.

## 핵심 개념·용어 정의
- **워크슬롭(workslop)**: work + slop. 실질 없는 AI 생성 업무물(Niederhoffer 외, 2025).
- **AI 슬롭(AI slop)**: 저품질 AI 생성물 전반. 오픈소스에서는 근거 없는 버그 보고·PR.
- **부담 전가(burden shifting)**: 작성자의 인지 노력 절감이 수신자의 해석·검증 노력 증가로 바뀌는 현상(본 정리의 용어).
- **파일럿 마인드셋(pilot mindset)**: 연구진 제안. 높은 주체성 + 높은 낙관으로 AI를 목적 있게 쓰는 태도. 반대는 "승객(passenger)" — 일을 피하려고 AI를 쓰는 태도.
- **리뷰 신뢰 모델**: "PR 작성자는 자기 코드를 이해한다"는 오픈소스 리뷰의 암묵적 전제.

## 코딩 에이전트 사용과의 연결점
- 에이전트가 만든 큰 diff를 그대로 PR로 올리면 그 순간 나의 작업은 끝나도 팀의 리뷰 작업이 시작된다. 대학원 연구실에서는 지도교수·공동연구자가 수신자.
- 자기 검증 없이 넘기는 것이 곧 워크슬롭. 예방책: 작은 diff, 목적 설명, 테스트 결과·실행 증거 첨부(Osmani 2026-06이 제안한 PR 접수 요건과 같음).
- 대학원생에게 특히 중요한 비용은 평판: 받은 사람 약 절반이 보낸 사람의 역량을 낮게 평가.

## 강연에 쓸 만한 포인트
- 인용: "AI 슬롭으로 사실상 DDoS를 당하고 있다"는 취지의 Stenberg 발언(2025-05, LinkedIn; 원문 단어는 확인 후 사용) — 또는 Joe Zhou "Review trust model is broken" (The Register, 2026-02-03).
- 숫자 한 줄: 40%가 한 달 안에 워크슬롭을 받았고, 건당 약 2시간.
- 숫자 한 줄: curl — 보고서 20%가 슬롭, 1건에 3–4명 × 30분~3시간 → 버그바운티 종료.
- 그림 아이디어: 저울 그림 — 왼쪽 "보내는 사람이 아낀 10분", 오른쪽 "받는 사람이 쓴 2시간".
- 그림 아이디어: 화살표 흐름도 "생성(기계 속도, 비용≈0) → 리뷰(사람 속도, 비용 그대로)".

## 원본 그림
- BetterUp 워크슬롭 인포그래픽(PDF/이미지) — https://betterup.com/workslop-infographic
- BetterUp 페이지 내 인식 변화 차트 — https://www.betterup.com/hs-fs/hubfs/undefined-Mar-11-2024-03-14-36-0983-AM.png (파일명이 2024년이라 다른 자료일 가능성, 사용 전 육안 확인)
- curl 관련 그림 — 없음
