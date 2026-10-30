# AI Fatigue and Workload: Surveys and Empirical Studies 2024–2026 (AI 피로·업무량 실증 자료)
- **저자/기관**: Upwork Research Institute & Workplace Intelligence; BCG(Bedard, Kropp, Hsu, Karaman, Hawes, Kellerman) / HBR; Aruna Ranganathan & Xingqi Maggie Ye(UC Berkeley Haas) / HBR; Google Cloud DORA; METR; Microsoft Research & CMU(Hao-Ping Lee 외); Tang 외(Notre Dame 등); Brandebusemeyer 외(HPI); Anthropic(Shen & Tamkin)
- **발행일**: 2024-07 ~ 2026-03 (2026-10-01 열람)
- **URL**:
  - Upwork 보도자료(2024-07-23) — https://investors.upwork.com/news-releases/news-release-details/upwork-study-finds-employee-workloads-rising-despite-increased-c
  - BCG "When Using AI Leads to 'Brain Fry'"(2026-03-05) — https://www.bcg.com/publications/2026/when-using-ai-leads-to-brain-fry
  - Berkeley/HBR "AI Doesn't Reduce Work—It Intensifies It"(2026-02) — Simon Willison 경유 https://simonwillison.net/2026/Feb/9/ai-intensifies-work/ (HBR 원문 URL 확인 필요)
  - DORA 2025 State of AI-assisted Software Development — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
  - METR RCT(2025-07) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ; 2026-02 후속 설계 변경 공지
  - Lee 외, CHI 2025 — https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf
  - Tang 외(2024) 시선추적 — https://arxiv.org/abs/2405.16081
  - Brandebusemeyer 외(2025-12) NASA-TLX 현장연구 — https://arxiv.org/abs/2512.19926
  - Anthropic(2026-01-29) AI 지원과 코딩 기술 형성 — https://www.anthropic.com/research/AI-assistance-coding-skills
- **자료 유형**: 보고서 | 논문 | 기사

## 핵심 요약
- **Upwork(2024-04-16~05-05 조사, 미·영·호·캐 2,500명: 경영진 1,250, 정규직 625, 프리랜서 625)**: 경영진 96%는 AI가 생산성을 높일 것으로 기대했지만, AI를 쓰는 정규직의 77%는 AI가 업무량을 늘렸다고 응답. 늘어난 이유는 AI 산출물 검토·조정(39%), 도구 학습(23%), AI 때문에 더 많은 일을 요구받음(21%). 47%는 기대 생산성을 어떻게 달성할지 모른다고 답함. 정규직 71%가 번아웃 보고.
- **BCG "AI brain fry"(미국 대기업 정규직 1,488명 설문, HBR 2026-03-05)**: AI를 쓰는 응답자의 14%가 "인지 용량을 넘는 AI 사용·상호작용·감독으로 인한 정신적 피로"를 경험. 감독(oversight) 요구가 높은 집단은 낮은 집단보다 정신적 노력 +14%, 피로 +12%, 정보 과부하 +19%(2차 보도 수치). brain fry 경험자는 의사결정 피로 +33%, 큰 오류 +39%, 이직 의향 25% → 34%. 반대로 AI가 반복 업무를 대신해 줄 때는 번아웃 점수가 약 15% 낮았음. 동시 사용 도구 3개에서 생산성 정점, 4개 이상에서 하락. → 같은 AI가 부하를 줄이기도 늘리기도 하며, 갈림길은 "덜어주기 vs 감독하기".
- **Berkeley Haas 현장연구(200명 규모 미국 테크기업, 8개월 참여관찰 + 40회 이상 인터뷰, HBR 2026-02)**: AI는 일을 줄이지 않고 강화했다. 세 경로 — 과제 확장(PM이 코드 작성 등 역할 경계 붕괴), 업무·휴식 경계 흐려짐(점심·밤에도 작업), 멀티태스킹 과부하(직접 코딩하는 동안 AI가 대안 생성, 여러 프로세스 병행). 아무도 더 하라고 요구하지 않았는데 스스로 업무를 늘림. 연구진은 지속적 주의 전환, 잦은 AI 출력 확인, 늘어나는 열린 과제를 지적.
- **DORA 2025(약 5,000명 기술 전문가 설문)**: 같은 조건의 두 사람을 비교하면 AI 도입 수준이 높아도 번아웃·마찰(friction) 수준은 비슷 — 줄지도 늘지도 않음. AI 도입은 처리량과는 양(+)의 관계로 바뀌었으나 전달 불안정성(instability) 증가와는 계속 연관. 약 30%는 AI 출력을 "조금" 또는 "전혀" 신뢰하지 않음. 핵심 메시지: AI는 팀의 기존 상태를 증폭한다.
- **METR RCT(2025-02~06, 숙련 오픈소스 개발자 16명, 실제 과제 246개)**: AI 허용 시 완료 시간 19% 증가(느려짐). 그런데 개발자들은 사전에 24% 빨라질 것으로 예상했고, 사후에도 20% 빨라졌다고 믿음 → 체감과 실측의 괴리. 2026-02 후속(57명, 800+ 과제)에서는 복귀자 기준 약 18% 빨라짐 추정이나 신뢰구간이 넓고, AI 없이 일하기를 거부한 참가자 증가로 METR 스스로 신호가 불안정하다고 밝힘.
- **Lee 외(CHI 2025, 지식노동자 319명, 사례 936건)**: 생성형 AI는 비판적 사고의 노력을 줄인다고 자기보고되지만, 그 성격을 정보 검증·응답 통합·과제 관리(stewardship)로 옮긴다. AI에 대한 신뢰가 높을수록 비판적 사고는 덜, 자기 확신이 높을수록 더.
- **Tang 외(2024, 개발자 28명, 시선추적 + IDE 로그 + 인지부하 평가)**: Copilot 생성 코드를 검증·수정할 때, 그 코드가 AI 생성물임을 안 집단이 더 높은 인지 부하를 보고하고 더 잘 수행. 알리지 않으면 AI 코드임을 자주 알아채지 못함 → 제대로 검증하면 부하가 오르는 게 정상.
- **Brandebusemeyer 외(2025-12, 기업 현장 혼합연구, NASA-TLX)**: 인라인 제안이나 채팅을 *적당히* 쓰면 과제 시간과 체감 부하가 줄었지만, 둘을 과도하게 섞어 쓰면 이점이 사라짐. 실제 업무 기간에는 AI 사용 시 생산성과 인지 부하가 *둘 다* 높다고 보고.
- **Anthropic RCT(2026-01-29, 주로 주니어 개발자 52명, 새 라이브러리 Trio 학습)**: AI 사용 집단의 이해도 퀴즈 점수가 손코딩 집단보다 17%p 낮음(평균 50% vs 67%), 격차는 디버깅 문항에서 최대. 다만 AI에게 설명·개념 질문을 하며 쓴 참가자는 이해를 유지. → 단기 부하 절감이 장기 역량 비용이 될 수 있음.
- **(참고, 예비 결과)** MIT Media Lab Kosmyna 외(2025-06 arXiv, 54명, EEG): LLM으로 에세이를 쓴 집단의 뇌 연결성이 가장 약했다는 보고("cognitive debt"). 동료심사 전 소표본 연구로, 인용 시 주의.

## 핵심 개념·용어 정의
- **AI brain fry**: 인지 용량을 넘는 AI 사용·상호작용·감독으로 인한 정신적 피로(BCG, 2026). 정서적 탈진인 번아웃과 구별되는 인지적 피로.
- **작업 강화(work intensification)**: 같은 시간에 더 많은 과제·더 빠른 리듬·더 적은 휴지기(Ranganathan & Ye, 2026).
- **NASA-TLX**: 정신적 요구, 신체적 요구, 시간 압박, 수행, 노력, 좌절 6개 척도로 주관적 작업부하를 측정하는 표준 설문.
- **인지 부하 이론(Sweller)**: 내재적·외재적·본유적 부하. AI는 외재적 부하(문법 검색, 상용구)를 덜어주지만 검증이라는 새 부하를 만든다.
- **체감–실측 괴리**: 빨라졌다고 느끼지만 실제로는 느려질 수 있음(METR 2025).

## 코딩 에이전트 사용과의 연결점
- 가장 피로한 것은 "AI를 쓰는 것"이 아니라 "AI를 감독하는 것"(BCG). 에이전트 수를 늘리면 감독 부담이 직접 커진다.
- 검토 업무(39%, Upwork)가 업무 증가의 첫 번째 이유 — 강연의 "병목이 리뷰로 이동"과 같은 결론을 설문이 뒷받침.
- 자기 체감으로 효과를 판단하지 말 것(METR). 연구 코드라면 테스트 통과·재현 가능성 같은 객관 지표로 확인.
- 학습 단계의 대학원생은 AI를 "설명 요청" 방식으로 써야 실력이 남는다(Anthropic 2026).

## 강연에 쓸 만한 포인트
- 인용: "frequent checking of AI outputs" — Ranganathan & Ye, HBR 2026-02(Simon Willison 인용 경유). 작업 강화의 원인 중 하나로 제시된 구절.
- 숫자 한 줄: 경영진 96% 기대 vs 직원 77% 업무 증가(Upwork 2024).
- 숫자 한 줄: 감독 요구 높을수록 정보 과부하 +19%, brain fry 경험자 큰 오류 +39%(BCG 2026).
- 숫자 한 줄: 19% 느려졌는데 20% 빨라졌다고 믿음(METR 2025).
- 그림 아이디어: 2×2 — 가로 "AI가 일을 덜어줌 ↔ AI를 감독함", 세로 "부하 감소 ↔ 부하 증가". BCG 결과(반복 업무 대체 시 번아웃 −15% / 고감독 시 과부하 +19%)를 대각선에 배치.

## 원본 그림
- METR 2025 결과 그림(예상 vs 실측 속도) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ 페이지 내 그림(직접 이미지 URL 미확보)
- BCG/HBR brain fry 그림 — 없음(유료벽)
- DORA 2025 보고서 그림 — 없음(PDF 내, 직접 URL 미확보)
