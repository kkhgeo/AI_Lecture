# 코딩 에이전트 벤치마크: SWE-bench Verified·Pro, Terminal-Bench 2.0, METR Time Horizon (Benchmarks)

- **저자/기관**: SWE-bench(Princeton/Stanford), OpenAI(Verified 선별·은퇴 공지), Scale AI(SWE-bench Pro), Terminal-Bench 팀(Stanford·Laude Institute 등, ICLR 2026), METR
- **발행일**: METR "Measuring AI Ability to Complete Long Tasks" 2025-03-19; METR Time Horizon 1.1 2026-01-29; METR time-horizons 페이지 최종 갱신 2026-05-08; OpenAI Verified 평가 중단 공지 2026-02(보도 기준); Terminal-Bench 논문 arXiv 2601.11868 (2026-01); "Coding Agents Have Converged" arXiv 2609.17394 (2026-09-15) (2026-09-29 열람)
- **URL**:
  - https://metr.org/time-horizons/
  - https://metr.org/blog/2026-1-29-time-horizon-1-1/
  - https://arxiv.org/abs/2503.14499 (METR 원 논문)
  - https://x.com/METR_Evals/status/2052896621760004602 (Mythos Preview 측정)
  - https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
  - https://labs.scale.com/leaderboard/swe_bench_pro_public
  - https://arxiv.org/abs/2601.11868 (Terminal-Bench)
  - https://www.tbench.ai/leaderboard
  - https://llm-stats.com/benchmarks/terminal-bench-2 (집계 사이트, 자가보고 점수)
  - https://www.swebench.com/
  - https://arxiv.org/abs/2609.17394
- **자료 유형**: 논문 | 보고서 | 공식문서

## 핵심 요약
- **SWE-bench Verified**: 실제 GitHub 이슈(주로 Django·Astropy 등 인기 Python 저장소) 500개를 사람이 검수한 부분집합. 에이전트가 패치를 만들고 숨겨진 테스트로 채점. 2026년 상위권은 90%대(집계 사이트 기준 최고 90%대 중후반; 대부분 벤더 자가보고)로 사실상 포화.
- OpenAI는 2026-02 Verified를 더 이상 프런티어 능력 지표로 쓰지 않겠다고 발표: 모델들이 자주 실패하던 문제(전체의 27.6%)를 감사한 결과 최소 59.4%가 올바른 답도 거부하는 결함 테스트였고, 주요 모델들이 정답 패치에 오염(contamination)된 흔적이 있다고 보고. 대안으로 SWE-bench Pro를 권고. (OpenAI 원문은 403으로 직접 열람 실패, 다수 보도로 교차 확인)
- **SWE-bench Pro**(Scale AI): 41개 저장소, 1,865 과제(Python·Go·TypeScript·JavaScript). 공개셋 731개(카피레프트 저장소), 스타트업 비공개 코드 276개(18개 코드베이스) 포함 → 오염 방지. Scale 표준화 공개 리더보드(2026-09 열람) 1위 Muse Spark 1.1 61.5%, GPT-5.4(xHigh) 59.1%, Claude Opus 4.6(thinking) 51.9%. 비공개셋에서는 점수가 더 떨어짐(예: Claude Opus 4.1 22.7%→17.8%). 벤더 자체 발표 점수는 이보다 훨씬 높게 나오는 경우가 많아 "누가 돌렸나"를 반드시 구분해야 함.
- **Terminal-Bench 2.0**: 터미널 환경의 어려운 실제형 과제 89개(시스템 관리, 빌드, 보안, 과학 코드 포팅 등), 과제마다 사람 3명이 검수. Harbor 하네스로 실행. 논문(ICLR 2026) 시점 프런티어 에이전트 < 65%. 2026-09 집계(llm-stats) 최고는 GPT-5.5 82.7%, Claude Mythos Preview 82.0% — 단 상위 10개 모두 **자가보고(self-reported)**, 독립 검증 0건.
- **METR Time Horizon**: "사람 전문가가 X시간 걸리는 과제를 AI가 50% 확률로 해내는 X"를 측정. 원 논문(2025-03)은 2019~2025년 동안 약 **7개월마다 2배**. TH1.1(2026-01-29, 과제 228개)에서는 전체 기간 196일(~7개월), 2023년 이후 131일, 2024년 이후 89일로 **가속**.
- TH1.1 추정치: Claude Opus 4.5 약 320분(95% CI 170~729분), GPT-5 214분, o3 121분. METR은 2026-03 초기 버전 Claude Mythos Preview를 **최소 16시간**(95% CI 8.5~55시간)으로 추정하며, 이는 현 과제셋으로 잴 수 있는 상한에 가까워 불안정하다고 명시(16시간 이상 과제는 228개 중 5개뿐).
- 리더보드 해석 경고: arXiv 2609.17394(2026-09-15)는 254개 제출을 분석해 Verified 상위 30개 인접 쌍 29개 중 어느 것도 통계적으로 구분되지 않으며(McNemar, α=0.05), 같은 모델도 스캐폴드(하네스)에 따라 최대 약 30%p 차이가 난다고 보고.

## 핵심 개념·용어 정의
- **Resolve rate(해결률)**: 제출 패치가 숨겨진 테스트를 모두 통과한 과제 비율.
- **Contamination(오염)**: 평가 문제·정답이 학습 데이터에 섞여 점수가 부풀려지는 현상.
- **Scaffold / Harness**: 모델을 감싸 도구·루프·프롬프트를 제공하는 실행 틀. 벤치마크 점수는 "모델+하네스" 조합의 점수.
- **Self-reported vs verified**: 벤더가 자체 발표한 점수 vs 벤치마크 운영자·제3자가 동일 조건으로 재현한 점수.
- **50% time horizon**: AI 성공 확률 50%가 되는 과제 길이(사람 전문가 소요시간 기준).
- **Doubling time**: time horizon이 2배가 되는 데 걸리는 기간.

## 강연에 쓸 만한 포인트
- 메시지: "벤치마크는 시험지다 — 시험지가 새면(오염) 점수는 의미를 잃는다." Verified 포화 → Pro·Terminal-Bench로 이동한 흐름을 한 장으로.
- 숫자 대비: 같은 시기 Verified 90%대 vs Pro(표준화) 60% 안팎 → "쉬운 시험 vs 비공개 시험".
- METR 차트는 로그 축 위 직선(지수 성장)이라 대학원생에게 직관적. "2019년 GPT-2는 몇 초짜리 과제, 2026년 초 모델은 반나절~하루짜리"로 설명.
- 주의 문구: time horizon은 "소프트웨어·연구형 과제, 명확한 채점, 50% 성공" 기준이며 실제 업무 생산성과 동일하지 않음(→ 17번 파일의 RCT와 대비).
- 인용(1개): METR은 Mythos 측정치를 "at the upper end of what we can measure"라고 표현(METR, X 게시물 2026-05-08).

## 원본 그림
- METR TH1.1 모델별 time horizon 추이(로그 축) — https://metr.org/assets/images/time-horizon-1-1/models.png (슬라이드용 1순위)
- METR TH1 vs TH1.1 추세 비교(전체 기간) — https://metr.org/assets/images/time-horizon-1-1/time-horizon-1-vs-1-1-hybrid.png
- METR TH1 vs TH1.1 추세(2023년 이후) — https://metr.org/assets/images/time-horizon-1-1/time-horizon-1-vs-1-1-since-2023.png
- METR 과제 길이 분포 비교 — https://metr.org/assets/images/time-horizon-1-1/task-distribution-comparison.png
- METR 도메인별 time horizon 증가 — https://metr.org/assets/images/time-horizon-domains/time-horizons-increasing.png
- METR 인터랙티브 최신 차트 — https://metr.org/time-horizons/ (이미지 파일 직접 URL 없음, 캡처 필요)
- SWE-bench Pro / Terminal-Bench 리더보드 — 표 형태 웹페이지, 별도 이미지 없음

## Claude Code와의 연결점
- Terminal-Bench는 Claude Code 같은 터미널 에이전트의 작업 방식(셸 명령 실행·반복 수정)을 직접 겨냥한 벤치마크.
- 하네스 효과(최대 ~30%p)는 "Claude Code = 모델 + 하네스(도구·권한·컨텍스트 관리)"라는 강의 핵심 개념의 실증 근거.
- time horizon 증가는 Claude Code가 긴 작업(수 시간 자율 실행, 서브에이전트, 장기 작업용 진행 파일)을 지원하는 방향으로 진화하는 배경.
- 주의: 벤더 발표 점수(예: 신모델 출시 블로그)는 자가보고이므로, 강의에서는 Scale 표준화 리더보드·METR처럼 제3자 측정치를 우선 인용할 것.
