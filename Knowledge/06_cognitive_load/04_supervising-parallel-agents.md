# Supervising Parallel Agents: Context Switching, Review Fatigue, Babysitting (병렬 에이전트 감독의 인지 비용)
- **저자/기관**: 복수 출처 묶음. (1) Gloria Mark 외(UC Irvine) 주의·중단 연구, (2) Anthropic Societal Impacts 팀, (3) 실무자 보고: Boris Cherny(Anthropic), Simon Willison, Andrej Karpathy, Steve Yegge, Addy Osmani, (4) BCG/HBR "AI brain fry"(병렬 도구 수 측정)
- **발행일**: 2005–2026 (2026-10-01 열람)
- **URL**:
  - Mark, Gudith & Klocke (2008) "The Cost of Interrupted Work: More Speed and Stress", CHI 2008 — https://www.ics.uci.edu/~gmark/chi08-mark.pdf
  - Gloria Mark 인터뷰(47초 주의 지속) — https://www.universityofcalifornia.edu/news/cant-pay-attention-youre-not-alone
  - Anthropic (2025-12-02) "How AI is transforming work at Anthropic" — https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
  - Simon Willison (2025-10-05) "Embracing the parallel coding agent lifestyle" — https://simonwillison.net/2025/Oct/5/parallel-coding-agents/
  - Simon Willison (2026-02-09) AI intensifies work 링크 글 — https://simonwillison.net/2026/Feb/9/ai-intensifies-work/
  - Pragmatic Engineer (2026-02-10) Steve Yegge 인터뷰 — https://newsletter.pragmaticengineer.com/p/steve-yegge-on-ai-agents-and-the
  - Addy Osmani (2026-06) "Agentic Code Review" — https://addyosmani.com/blog/agentic-code-review/
  - Boris Cherny 워크플로 (Pragmatic Engineer 인터뷰 및 X 스레드, 2026-01) — https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny
  - BCG/HBR (2026-03-05) "When Using AI Leads to 'Brain Fry'" — https://www.bcg.com/publications/2026/when-using-ai-leads-to-brain-fry
- **자료 유형**: 논문 | 보고서 | 블로그 (혼합)

## 핵심 요약
- **주의 전환은 공짜가 아니다**: Mark 연구팀 관찰에서 화면 하나에 머무는 평균 시간은 2003년 약 2분 30초 → 2012년 75초 → 최근 약 47초로 줄었다(UC 뉴스 인터뷰, 2023). 중단된 작업으로 돌아오기까지 평균 약 25분이 걸린다는 수치도 Mark가 반복해 언급(현장 관찰 연구 기반; 원 논문은 2005 CHI "No task left behind?" — 수치는 인터뷰 경유, 2차 인용 주의).
- **중단되면 빨라지지만 스트레스가 오른다**: Mark·Gudith·Klocke(CHI 2008, 실험) — 중단된 과제를 오히려 더 짧은 시간에, 품질 차이 없이 끝냈지만 스트레스·좌절·시간 압박·노력(NASA-TLX 계열 자기보고)이 더 높았다. 병렬 에이전트 운영과 구조가 같다: 처리량은 유지되나 비용은 사람 내부로 이동.
- **Anthropic 내부 조사(2025-08 조사, 2025-12-02 공개; 엔지니어·연구자 132명 설문 + 53명 인터뷰 + Claude Code 사용 데이터)**: 업무의 59%에 Claude 사용(1년 전 28%), 자기보고 생산성 +50%. 그러나 대부분이 "완전히 위임"할 수 있는 업무는 0–20%뿐이라고 답해 상시 감독·검증이 필요. 일부는 "항상 Claude 인스턴스 몇 개를 돌린다"고 보고.
- **자율성 증가 = 감독 방식 변화**: 같은 보고서에서 Claude Code가 사람 개입 없이 연속 수행한 도구 호출은 9.8 → 21.2회(+116%), 대화당 사람 턴은 6.2 → 4.1회(−33%). 사람은 "자주 짧게 개입"에서 "드물게 크게 검토"로 이동.
- **감독의 역설(supervision paradox)**: Anthropic 직원 인터뷰 — Claude를 잘 쓰려면 감독이 필요하고, 감독에는 AI 과다 사용으로 위축될 수 있는 바로 그 코딩 실력이 필요하다는 지적. 일부는 일부러 AI 없이 연습해 감을 유지.
- **실무자 보고 — 병렬 운영의 상한은 "리뷰 속도"**: Simon Willison(2025-10)은 처음엔 "병목은 내가 결과를 리뷰하는 속도"라 회의적이었고, 결국 *중요한 변경은 한 번에 하나만* 리뷰·머지하고, 조사·프로토타입·사소한 유지보수처럼 인지 부담이 적은 일만 병렬로 돌린다고 정리. 본인이 쓴 명세에서 나온 코드는 리뷰 부담이 훨씬 작다고 언급.
- **Boris Cherny(Claude Code 창시자)**: 터미널 탭 5개(각각 별도 체크아웃) + 웹 세션 5–10개를 병렬로 돌리고, 시스템 알림으로 입력이 필요한 세션만 확인, 계획 모드에서 계획을 다듬은 뒤 실행시키는 방식(2026-01 공개 스레드·인터뷰; 2차 요약 다수, 원 스레드 직접 확인 권장). 즉 "많이 돌리기"는 계획·알림·검증 자동화가 전제.
- **피로 보고**: Simon Willison(2026-02)은 병렬 에이전트로 한두 시간 일하면 하루 정신 에너지가 거의 소진된다고 씀. Steve Yegge(2026-02)는 AI 코딩의 "흡혈귀 효과"를 말하며 낮잠을 자게 된다고, 최고 속도로 바이브 코딩하는 사람에게서 하루 생산적 시간은 약 3시간뿐일 수 있다고 주장(개인 관찰, 측정 아님). 그의 "AI 도입 8단계" 중 6단계(여러 에이전트)에서는 에이전트 사이를 멀티플렉싱하느라 자리를 뜰 수 없게 된다고 묘사.
- **Karpathy(2026-01, X 게시물; 2차 보도로 확인)**: 코딩의 약 80%를 에이전트에 맡기게 됐지만, 모델이 "조금 서두르는 주니어"처럼 미묘한 개념 오류를 내므로 중요한 코드라면 IDE 옆에 띄워 놓고 매처럼 지켜보라고 조언. 2025-06 YC 강연에서는 "AI를 짧은 목줄에" 두고 생성–검증 루프를 빠르게 돌리라고 강조.
- **몇 개까지 감당하나(측정)**: BCG(1,488명 미국 정규직 설문, HBR 2026-03) — 동시에 쓰는 AI 도구 수가 3개일 때 자기보고 생산성이 정점, 4개 이상에서는 하락하고 인지 부담만 증가(설문 상관, 코딩 에이전트 한정 아님; 2차 보도 수치). 코딩 에이전트 동시 운영 수에 대한 통제 실험은 2026-10 현재 찾지 못함.

## 핵심 개념·용어 정의
- **작업 전환 비용(task-switching cost)**: 과제를 바꿀 때 규칙·목표를 다시 불러오는 데 드는 시간·오류 증가(Rubinstein, Meyer & Evans, 2001, JEP:HPP). 
- **주의 잔여(attention residue)**: 이전 과제에 대한 생각이 남아 다음 과제 수행을 떨어뜨리는 현상(Leroy, 2009, OBHDP).
- **운동적 주의(kinetic attention)**: Gloria Mark의 용어. 화면·기기를 빠르게 옮겨 다니는 주의 패턴.
- **베이비시팅(babysitting agents)**: 에이전트가 권한 요청·질문·오류로 멈출 때마다 사람이 돌아와 풀어주는 감시형 노동. 실무 은어.
- **감독의 역설**: 감독에 필요한 역량이 바로 위임으로 인해 약해질 수 있다는 구조(Anthropic, 2025-12).
- **리뷰 병목**: 생성은 기계 속도, 이해·검증은 사람 속도라서 처리량 상한이 리뷰 쪽으로 이동(Osmani, 2026-06).

## 코딩 에이전트 사용과의 연결점
- 에이전트 N개 = 열린 맥락 N개. 사람 작업기억(대략 4±1 청크; Cowan 2001)은 그대로이므로, 각 세션의 목표·상태를 머릿속에 들고 있으면 전환할 때마다 재적재 비용이 든다. → 상태는 파일(PLAN.md, 진행 로그, 세션 이름)에 적어 둔다.
- 권한 요청 알림이 잦으면 Mark가 말한 "자기·외부 중단"이 계속 발생. Claude Code 문서도 수동 승인 모드에서 "열 번째 승인쯤엔 리뷰가 아니라 클릭"이 된다고 지적 → 허용목록·샌드박스·자동 모드로 사소한 중단을 줄인다.
- 병렬화하기 좋은 일: 조사, 프로토타입, 문서화, 저위험 유지보수, 명세가 분명한 작업. 병렬화하기 나쁜 일: 설계 판단이 필요한 핵심 변경(한 번에 하나).
- 강연 기존 슬라이드("병목이 작성 → 리뷰로 이동")와 직결: 병렬 수의 실질 상한 = 내가 제대로 리뷰할 수 있는 양.

## 강연에 쓸 만한 포인트
- 인용: 병목은 "how fast I can review the results" — Simon Willison, 2025-10 (번역: "내가 결과를 리뷰하는 속도")
- 숫자 한 줄: Anthropic 내부 — 업무의 59%에 AI, 하지만 완전 위임 가능은 0–20%.
- 숫자 한 줄: 중단된 일은 더 빨리 끝나지만 스트레스·노력은 증가(Mark 2008).
- 그림 아이디어: 가로축 "동시 에이전트 수", 세로축 두 곡선 — 산출(포화) vs 리뷰 부담(선형~가속) 교차점 = "내 리뷰 용량". BCG의 "3개 정점" 결과를 점선 주석으로.
- 그림 아이디어: 사람 1명 ↔ 터미널 5개 사이의 주의 이동 화살표, 각 화살표에 "재적재 비용" 라벨.

## 원본 그림
- Anthropic 보고서 Figure 3: Claude Code 자율성 추세(연속 도구 호출 증가, 사람 턴 감소) — https://www-cdn.anthropic.com/images/4zrzovbb/website/d23e1b8d8af84b45d5cffcc6f0a029d635508153-3840x2160.png
- Anthropic 보고서 Figure 2: 작업 범주별 시간·산출 변화 — https://www-cdn.anthropic.com/images/4zrzovbb/website/9449bf9393743105a414e17324f30970208ce14b-3840x2160.png
- Anthropic 보고서 Figure 1: 작업 유형별 Claude 사용 빈도 — https://www-cdn.anthropic.com/images/4zrzovbb/website/64a18b1756d8954a93e1356f1330ec11075fbe54-3840x2160.png
- BCG "brain fry" 도구 수–생산성 곡선 — 이미지 URL 확보 못함(HBR 유료). 없음.
