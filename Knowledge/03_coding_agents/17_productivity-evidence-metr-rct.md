# AI 코딩 도구의 생산성 효과: METR RCT와 후속 연구, DORA 보고서 (Productivity evidence)

- **저자/기관**: METR (Joel Becker, Nate Rush 외); Google Cloud DORA; Microsoft Research (Murphy-Hill, Butler, Savelieva)
- **발행일**: METR RCT 2025-07-10 (arXiv 2507.09089); METR 실험설계 변경·후속 결과 2026-02-24; METR 자기보고 설문 2026-05-11; DORA 2025 보고서 2025-09-23; DORA "ROI of AI-assisted Software Development" 2026 초(InfoQ 2026-05 보도); Microsoft CLI 에이전트 도입 연구 arXiv 2607.01418 (2026-07-01) (2026-09-29 열람)
- **URL**:
  - https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
  - https://arxiv.org/abs/2507.09089
  - https://metr.org/blog/2026-02-24-uplift-update/
  - https://metr.org/blog/2026-05-11-ai-usage-survey/
  - https://dora.dev/dora-report-2025/
  - https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/
  - https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/
  - https://arxiv.org/abs/2607.01418
- **자료 유형**: 논문 | 보고서

## 핵심 요약
- **METR RCT(2025-07-10)**: 숙련 오픈소스 개발자 16명이 자신이 관리하는 대형 저장소(평균 별 2.2만+, 100만+ LOC)에서 실제 이슈 246개를 수행. 이슈마다 AI 허용/금지를 무작위 배정. 주 도구 Cursor Pro + Claude 3.5/3.7 Sonnet. 결과: AI 허용 시 완료 시간 **19% 증가(느려짐)**.
- 인식과 측정의 괴리: 개발자는 시작 전 24% 단축을 예상, 끝난 뒤에도 20% 빨라졌다고 믿음. 경제·ML 전문가 예측도 속도 향상 쪽이었음.
- METR 스스로 한계 명시: 이 결과가 "대부분 개발자에게 AI가 도움이 안 된다"거나 "미래 모델도 그렇다"는 증거는 아니라고 밝힘. 고숙련·익숙한 대형 코드베이스·높은 품질 기준이라는 특수 조건.
- **METR 후속(2026-02-24)**: 2025-08 이후 Claude Code 등 에이전트 도구로 57명·143개 저장소·800+ 과제 재실험. 재참여자(n=10) 추정 −18%(속도 향상 방향, 95% CI −38%~+9%), 신규(n=47) −4%(CI −15%~+9%). 음수=빨라짐. 단 30~50%의 개발자가 "AI 없이 하기 싫은 과제"를 제출하지 않는 등 선택 편향이 커서 METR은 "매우 약한 증거"라 평가하고 실험 설계를 바꾸겠다고 발표.
- **METR 자기보고 설문(2026-05-11)**: 기술직 349명(학계·박사과정 129명 포함), 2026-02~04. 중앙값 응답자는 AI로 업무 "가치" 1.4~2배, "속도" 3배 향상을 보고. 그러나 METR은 이전 실험에서 참가자들이 약 40%p 과대추정했음을 들어 자기보고를 신중히 해석하라고 경고.
- **Microsoft 현장 연구(2026-07-01)**: 2026년 초 Claude Code·GitHub Copilot CLI 사내 배포를 수만 명 규모로 분석. 도입자는 4개월간 미도입 반사실 대비 PR 병합이 약 24% 많았고, 첫 사용은 주로 동료 네트워크를 통해 확산. (관찰 연구·PR 수 지표라는 한계)
- **DORA 2025(2025-09-23)**: AI 도입은 **처리량(throughput) 증가**와 동시에 **배포 불안정성(instability) 증가**와 연관. AI는 "증폭기(amplifier)" — 좋은 팀은 더 좋아지고 약한 팀은 문제가 커짐. 7가지 역량으로 구성된 DORA AI Capabilities Model 제시.
- **DORA ROI 보고서(2026)**(InfoQ 등 2차 보도 기준): 단순 과제 35~40% 향상, 복잡한 레거시 코드에선 10% 미만; 초기 생산성 하락 후 회복하는 J-curve, 생성된 코드를 검증하는 "verification tax" 개념 제시. (원문 미열람 — 수치 재확인 권장)

## 핵심 개념·용어 정의
- **RCT(무작위 대조 실험)**: 과제 단위로 AI 사용 여부를 무작위 배정해 인과 효과를 추정하는 설계.
- **Perception gap(인식 격차)**: 체감 생산성과 측정 생산성의 차이.
- **Selection effect(선택 편향)**: AI 이득이 큰 사람·과제가 실험에서 빠져 효과가 과소/과대 추정되는 문제.
- **Throughput vs stability (DORA)**: 변경을 얼마나 빨리·많이 내보내나 vs 배포가 얼마나 안정적인가.
- **Verification tax**: AI 산출물을 확인·검토하는 데 드는 추가 비용.

## 강연에 쓸 만한 포인트
- 핵심 한 장: "예상 −24%, 체감 −20%, 실제 +19%" 막대 3개(METR 원 그림 활용) → "느낌은 증거가 아니다".
- 균형 메시지: 2025 RCT(느려짐) → 2026 후속(약한 속도 향상 신호) → 대규모 현장 데이터(PR +24%) → DORA(속도↑·안정성↓). "효과는 과제·숙련도·조직 역량에 따라 다르다."
- 대학원생용 비유: "AI는 연구실의 새 장비 — 캘리브레이션(검증 절차) 없이 쓰면 데이터가 빨리 나오지만 틀린 데이터도 빨리 나온다."
- 인용(1개): METR은 2026 후속 결과를 "very weak evidence"라고 스스로 평가(METR, 2026-02-24).

## 원본 그림
- METR 2025 예상 vs 관측 속도 차이(대표 그림) — https://metr.org/assets/images/downlift/forecasted-vs-observed.png (슬라이드용 1순위)
- METR 2025 방법론 도식 — https://metr.org/assets/images/downlift/methodology.png
- METR 2025 핵심 결과 — https://metr.org/assets/images/downlift/core-result.png
- METR 2025 요인 분석 표 — https://metr.org/assets/images/downlift/factor-analysis.png
- METR "벤치마크는 과대, RCT는 과소 추정할 수 있다" 도식 — https://metr.org/assets/images/downlift/benchmarks-overestimate.png , https://metr.org/assets/images/downlift/rct-underestimates.png
- METR 2026 후속 결과 타임라인 — https://metr.org/assets/images/uplift-2026-post/uplift_timeline.png
- METR 2026 자기보고 설문 헤드라인 — https://metr.org/assets/images/ai-usage-survey/headline.png
- DORA 2025 보고서 PDF(그림 다수) — https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf

## Claude Code와의 연결점
- METR 2026 후속 실험은 Claude Code 같은 에이전트형 도구 시기를 다룸 → 2025 RCT(Cursor 채팅·자동완성 중심)와 도구 세대가 다름을 강조.
- Microsoft 연구는 Claude Code가 대기업 현장에서 실제 PR 산출과 연관됨을 보여주는 드문 대규모 데이터.
- DORA의 "검증 없는 속도 = 불안정성" 메시지는 Claude Code에서 테스트 먼저, plan mode, diff 검토, hooks로 검증 자동화하는 습관의 근거.
