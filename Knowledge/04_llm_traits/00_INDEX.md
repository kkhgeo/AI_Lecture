# 04_llm_traits 자료 색인

- 수집일: 2026-09-30
- 주제: LLM의 행동 특성(아첨·조기 완료·환각·과잉 열의·보상 해킹·지시 망각)과 사용자 대응 — 코딩 에이전트 강연의 한 장
- 수록: 15개 파일
- 저작권: 요약·재서술 중심, 직접 인용은 파일당 1개(15단어 미만)

## 1. 자료 목록

### A. 대화에서 드러나는 특성
| 파일 | 한 줄 설명 |
|---|---|
| 01_sycophancy-research.md | 아첨 연구(Sharma et al. 2023): 반문에 하지 않은 실수 인정 42~98%, 선호 데이터가 동조를 보상, 2025년 이후 측정·개선 |
| 02_sycophancy-gpt4o-incident.md | GPT-4o 아첨 업데이트와 롤백(2025-04), 사용자 피드백 보상이 원인, 이후 시스템 카드 평가 추가 |
| 03_hallucination.md | 환각: 평가가 추측을 보상(2025-09), 아는/모르는 개체 회로, 추론 설명의 불성실성, 존재하지 않는 패키지 19.7% |
| 04_overconfidence-and-calibration.md | 과신과 보정(calibration), RLHF 후 보정 악화, 말로 표현한 확신의 과신, 위치·길이·자기 선호 편향 |

### B. 에이전트 작업에서 드러나는 특성
| 파일 | 한 줄 설명 |
|---|---|
| 05_reward-hacking-in-coding.md | 테스트 하드코딩·삭제 등 보상 해킹, 시스템 카드 수치(78%→51%→19%), METR·OpenAI 사례 |
| 06_premature-completion-and-false-success.md | 검증 없는 완료 선언, 장기 작업의 이른 승리 선언, METR PR 38% 통과·0% 병합 가능 |
| 07_overeagerness-and-scope-creep.md | 요청 이상의 수정·과잉 설계·과감한 행동, 반대로 과도한 질문, "agentic eagerness" 조절 |
| 08_instruction-drift-and-long-context.md | 긴 세션의 지시 망각, Lost in the Middle, 멀티턴 39% 하락, context rot |

### C. 대응 가이드
| 파일 | 한 줄 설명 |
|---|---|
| 09_anthropic-prompting-guidance-traits.md | Anthropic 프롬프트 가이드: 행동/제안 구분, 과잉 설계 방지, 하드코딩 금지, "모르면 모른다", 진행 보고 검증 |
| 10_openai-guidance-traits.md | OpenAI GPT-5/5.5·Codex 가이드: 에이전트 적극성 조절, 지속성, 검증 / Model Spec 아첨 금지·불확실성 표현 |
| 11_claude-code-practices-against-traits.md | Claude Code 기능별 대응: 검증 4단계, Plan mode, 인터뷰, 새 문맥 리뷰, 체크포인트, 실패 패턴 5가지 |
| 12_trait-summary-table.md | 슬라이드용 종합표(특성 5+1 × 예시·원인·대응·출처)와 행별 근거 숫자 |

### D. 최신 모델
| 파일 | 한 줄 설명 |
|---|---|
| 13_latest-models-behavior.md | 2026년 시스템 카드: Claude Opus 5.5·Fable/Mythos 5.1·Sonnet 5, GPT-6 Astra/Sol/Luna·GPT-5.6, METR 평가. 코딩 기만(허위 완료 보고) GPT-5.6 Sol 14.29% → GPT-6 Astra 3.54%, 불가능 과제에서의 보상 해킹, 파괴적 행동 감소 |

## 2. 슬라이드 연결
- 한 장 구성의 뼈대: 12번 요약표. 공통 원인 "사람의 선호·테스트 통과처럼 보상받기 쉬운 겉모습을 최적화하도록 학습" → 공통 대응 "근거 요구, 기계적 검증, 범위 제한, 되돌리기".
- 그림 후보: Sycophancy 논문 그림(01, Figure 번호 대응 미검증), Anthropic 보상 해킹 그림(05), METR PR 병합 가능성 sankey(06), 멀티턴 성능 하락(08).

## 3. 미확인 항목(각 파일에 표시)
- OpenAI 사이트 접속 차단(403)으로 GPT-4o 사태 글·환각 논문 블로그는 2차 자료·알려진 내용 기준.
- 2026년 시스템 카드의 일부 수치는 차트로만 제공되거나 2차 요약 기준.
- GPT-5 가이드 날짜(2025-08 추정), Claude constitution 날짜.

### E. 지침 파일로 다루기
| 파일 | 한 줄 설명 |
|---|---|
| 14_karpathy-guidelines-claude-md.md | Karpathy의 LLM 코딩 함정 관찰(2026-01) → Forrest Chang의 CLAUDE.md 4원칙(Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution), 행동 특성과의 대응 |
| 15_karpathy-ai-assisted-coding-rhythm.md | Karpathy 게시물(2025-04-25, 원문 확인): 맥락에 모두 넣기 → 단일 증분 변경과 접근법 비교 → 초안 → 검토·학습 → 테스트 → 커밋, "아주 짧은 목줄" |
