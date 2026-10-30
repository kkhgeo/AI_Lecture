# 06_cognitive_load 자료 색인

- 수집일: 2026-10-01
- 주제: AI를 사용할 때의 인지 부하 — 줄어드는 곳, 옮겨 가는 곳, 늘어나는 곳
- 수록: 15개 파일
- 저작권: 요약·재서술 중심, 직접 인용은 파일당 1개(15단어 미만)

## 1. 자료 목록

### A. 이론과 고전 연구
| 파일 | 한 줄 설명 |
|---|---|
| 01_cognitive-load-theory-and-ai.md | Sweller 인지 부하 이론(내재적·외재적·본유적), 작업 기억 약 4덩어리(Cowan), AI가 외재적 부하를 줄이지만 생각을 맡기면 학습 부하도 사라짐, 오프로딩 vs 아웃소싱 |
| 02_ironies-of-automation.md | Bainbridge(1983) 자동화의 역설, 경계 저하(Mackworth, 30분 내 10~15%), 자동화 안주·편향, 루프 이탈, 생성형 AI의 4가지 역설(Simkute 2024) |
| 03_shift-from-production-to-verification.md | Lee 외(CHI 2025, 319명): 노력이 생산에서 검증·통합·관리로 이동, 평가 노력 감소는 55%뿐, AI 신뢰↑ 비판적 사고↓ / 검증 시간 22.4%(CHI 2024) / TiCoder 부하 45→28 |

### B. 최근 실무와 실증
| 파일 | 한 줄 설명 |
|---|---|
| 04_supervising-parallel-agents.md | 여러 에이전트 감독의 비용: 작업 전환(Gloria Mark), Anthropic 내부 조사(2025-12, 업무 59%에 사용, 완전 위임 0~20%), 실무자 보고 |
| 05_workslop-and-burden-shifting.md | 워크슬롭(HBR 2025-09, 40% 수신, 건당 약 2시간), curl 버그 신고의 약 20%가 AI 슬롭, 오픈소스의 AI PR 부담 |
| 06_ai-fatigue-and-workload-surveys.md | Upwork 2024(직원 77% 업무 증가, 1위 원인 AI 결과 검토 39%), BCG 2026 "brain fry"(14%, 도구 4개 이상에서 생산성 하락), DORA 2025, METR |
| 07_managing-cognitive-load-synthesis.md | 줄어듦/옮겨감/늘어남 정리, 근거 있는 대응 9가지, 슬라이드 문구 3안, 그림 아이디어 2안(01~03과 동시 작성되어 상호 참조 없음) |

### C. 상호작용 중의 인지 부하
| 파일 | 한 줄 설명 |
|---|---|
| 08_metacognitive-demands-and-envisioning-gap.md | Tankelevitch(CHI 2024) 메타인지 요구(목표 자각·분해·확신 보정·유연성), Subramonyam(CHI 2024) 구상의 간극(능력·지시·의도), Zamfirescu-Pereira(CHI 2023, n=10) 기회주의적·사람식 프롬프팅, Prather(CS1 19명) 제안이 사고를 끊음 |
| 09_flow-waiting-and-reading-burden.md | 대기·알림·끼어듦이 사고를 자름(Parnin 재개 1분 내 10%, Leroy 주의 잔여, Kuo IUI 2026 작업 중 끼어듦 62% 거절), 읽기 238wpm vs 생성 속도, YapBench 과잉 길이, 멀티턴 성능 39% 하락(Laban 2025) |
| 10_practitioner-voices-thinking-with-ai.md | 1인칭 증언 4갈래: 생각이 끊긴다(Hashimoto·Prather P13) / 내 생각을 잃는다(Graham·Willison·Storey 인지 부채·Ronacher) / 판단할 게 너무 많다(Stack Overflow 결정 피로·Osmani) / 지친다(Willison 오전 11시·Yegge), 원문/2차 표기 |
| 11_interaction-load-synthesis.md | 상호작용이 어려운 5가지 메커니즘(이중 과제·의도 미성숙·사고 단절·읽기 병목·미시 판단), 대응 8가지(먼저 쓰기·한 번에 모으기·작은 턴·짧은 출력·계획 모드·대기 관리), 슬라이드 문구 3안, 그림 2안 |

### D. 출력 해석과 표현 방식
| 파일 | 한 줄 설명 |
|---|---|
| 12_visual-interactive-output-research.md | HCI 연구: Graphologue(UIST 2023, 형성 연구 10명이 꼽은 장황함·부분 질문 불가·정리 불가), Sensecape(n=12, 탐색 개념 22.8→68.3), Luminate(작가 14명), Gero(CHI 2024, n=24), 추론 그래프화(n=125, 오류 탐지 73.5→85.6%), 개념 지도(부하 31.5%↓), 구조화 설명(IUI 2025) |
| 13_generative-ui-and-industry.md | 산업계: Vercel 생성형 UI(2024-03), Artifacts(2024-06), Canvas(2024-10), NotebookLM 마인드맵·영상(2025), Claude Code 출력 스타일(Concise·Explanatory·Learning, "Diagrams first" 예시), Google Generative UI(2025-11), Claude 인라인 시각화(2026-03) |
| 14_practitioner-views-output-interfaces.md | 실무자: Karpathy(2025-06 강연: 채팅=터미널, diff·GUI로 감사, AI를 짧은 줄에; 2025-12 회고: 사람은 시각·공간 선호), Wattenberger(2023), Willison(인지 부채, 선형 워크스루·인터랙티브 설명), Appleton, Linus Lee(2022) |
| 15_output-interpretation-synthesis.md | 종합: 해석이 어려운 5가지 메커니즘, 도움이 되는 표현 9가지와 근거·주의, Claude Code 실전 프롬프트, 슬라이드 문구 3안, 그림 2안, 한계 |

## 2. 미확인 항목
- BCG 2026 세부 수치(HBR 유료 기사, 발표·2차 기사 기준), 워크슬롭 표본 수(1,150 vs 1,004)
- Karpathy·Cherny·Yegge 발언은 2차 요약 기준, MIT 뇌파 연구는 동료 심사 전
- 한 사람이 동시에 다룰 수 있는 에이전트 수에 대한 통제 실험은 찾지 못함
- 대화 중 '생각하기 어려움'을 직접 측정한 통제 실험은 찾지 못함(08–11은 개념 틀·관찰 연구·실무자 증언 조합). Chiang·Litt·Zechner 발언은 2차 자료
- (D) Google Generative UI 선호 퍼센트는 블로그에서 미확인, NotebookLM 마인드맵·Claude Code 출력 스타일 도입일·Imagine with Claude는 2차 자료, Appleton 글 정확한 날짜 미확인, Karpathy 강연은 자동 전사본 기준. 코딩 에이전트 출력(작업 보고·diff)을 대상으로 텍스트 vs 시각 표현을 비교한 통제 실험은 찾지 못함
