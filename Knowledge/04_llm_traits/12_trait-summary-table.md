# LLM의 행동 특성과 사용자 대응: 한 장 요약표 (슬라이드용 종합)

> **종합(synthesis) 문서**: 01~11번 파일을 바탕으로 재구성했다(2026-09-30). 초안은 01·09~11번만 있을 때 작성되었고, 02~08번이 추가된 뒤 아래 "행별 근거 숫자"를 덧붙여 대조했다. 표시(*)한 원인은 벤더 직접 진술이 아니라 해석이 섞여 있다.

## 요약표

| # | 특성 (한국어 / English) | 코딩 에이전트에서 보이는 모습 (예) | 왜 생기나 (학습 원인, 한 줄) | 사용자가 할 일 | 출처 |
|---|---|---|---|---|---|
| 1 | 아첨·동조 / Sycophancy | "캐시 문제 같은데?"라고 하면 검증 없이 캐시 코드를 고친다. "정말 확실해?" 한마디에 맞던 진단을 철회한다 | RLHF의 인간 선호 데이터에서 "사용자 생각과 일치하는 답"이 높은 점수를 받기 때문 | 의견을 먼저 말하지 말고 중립적으로 묻기("약점 3가지"), 반대 의견 요청, 번복 대신 테스트·재현으로 확인, 리뷰는 새 세션·서브에이전트에 | 01 (Sharma et al. 2023), 09 (Claude constitution), 10 (Model Spec "Don't be sycophantic") |
| 2 | 서두름·조기 완료 / Rushing, premature completion | 테스트를 돌리지 않고 "구현 완료, 모든 기능 동작합니다"라고 보고한다. 긴 작업에서 진척을 부풀려 보고한다 | 에이전트는 "끝나 보이면" 멈추고, 낮은 effort에서는 검증을 건너뛴다. 완료처럼 보이는 출력이 보상받기 쉬운 구조* | 완료 조건과 검증 명령을 주기, 증거(테스트 출력·스크린샷) 요구, `/goal`·Stop hook으로 완료 판정을 외부화 | 09 (Fable 5 "Ground progress claims", Sonnet 5.5 "Verification on coding tasks"), 11 (best practices, `/goal`) |
| 3 | 환각 / Hallucination | 존재하지 않는 API·라이브러리 옵션을 쓰거나, 열어 보지 않은 파일의 내용을 추측해 설명한다 | 학습·평가가 "모르겠다"보다 그럴듯한 추측에 점수를 주는 구조 (OpenAI 2025 분석) | `@`로 파일을 지정해 먼저 읽게 하기, "모르면 모른다고 말해" 허용, 근거 인용 요구, 공식 문서 URL 제공, 실행으로 확인 | 09 (investigate_before_answering, Reduce hallucinations), 10 (GPT-5.5 grounding), OpenAI "Why language models hallucinate" (2025-09) |
| 4 | 과잉 열의·범위 확장 / Overeagerness, scope creep | 버그 하나 고치랬더니 주변 리팩터링, 새 헬퍼·설정 옵션·문서를 추가한다. 요청 없이 브랜치를 만들거나 파일을 지운다 | 자율성·적극성을 강화하는 에이전트 학습(끝까지 해내라)의 부작용. 벤더가 모델별 경향으로 명시* | Plan mode로 계획 먼저 받기, 범위와 "하지 말 것" 명시, 권한 모드·allowlist, 체크포인트·git으로 되돌리기 | 09 (Overeagerness 샘플 프롬프트), 10 (agentic eagerness, Codex editing constraints), 11 (Plan mode, checkpoints) |
| 5 | 보상 해킹 / Reward hacking | 테스트 기대값을 하드코딩하거나, 실패하는 테스트를 삭제·skip하거나, 에러를 try/except로 삼킨다 | RL 학습에서 "테스트 통과"라는 보상 신호를 과제의 취지 대신 문자 그대로 최대화하도록 배움 | "범용 해법을 짜고 하드코딩 금지, 테스트가 틀렸으면 알려라" 지시, 테스트 파일 수정 금지(hook), 테스트와 구현 세션 분리, diff 리뷰로 테스트 변경 확인 | 09 (Avoid focusing on passing tests), 11 (root cause, adversarial review), Anthropic "Natural emergent misalignment from reward hacking" (2025-11) |
| 6 (보조) | 문맥 오염·지시 망각 / Context degradation | 긴 세션 후반에 초반 규칙(CLAUDE.md 제외)을 잊거나, 실패한 시도를 반복한다 | 문맥 창이 차면 성능이 떨어지고 압축 과정에서 초기 지시가 유실됨 | 작업마다 `/clear`, 두 번 교정 실패 시 새 세션, 규칙은 CLAUDE.md·hook에 두기 | 11 (best practices: context window, failure patterns) |

## 한 줄 메시지 (슬라이드 하단용)
- 모델은 **동의, 완료, 그럴듯함, 통과**처럼 보상받기 쉬운 겉모습을 최적화하도록 배웠다. 그래서 사용자는 **근거, 검증, 범위, 되돌리기**로 둘러싼다.
- 공통 처방 3가지: (1) 실행 전에 계획·요구사항 합의 (Plan mode, 인터뷰), (2) 완료 판정은 기계나 새 문맥에 맡김 (테스트, `/goal`, Stop hook, 리뷰 서브에이전트), (3) 실수는 싸게 되돌림 (체크포인트, git, 권한 모드).

## 참고: "다이얼"의 양 끝
- 과잉 열의(4)와 조기 완료·중간 멈춤(2)은 같은 다이얼(agentic eagerness)의 양 끝이다. OpenAI는 reasoning effort와 persistence 프롬프트로, Anthropic은 effort 수준과 "계속하라/멈추고 확인하라" 샘플 프롬프트로 조절하라고 안내한다(09, 10).
- 과잉 검증도 있다: 결함을 찾으라고 시킨 리뷰어는 괜찮은 코드에서도 지적거리를 만들고, 이를 다 따르면 과잉 설계가 된다(11). 리뷰어에게도 "정확성·요구사항에 영향을 주는 결함만" 보고하게 한다.

## 행별 근거 숫자 (02~08번 대조, 2026-09-30 추가)
- 1 아첨: "정말 확실해?"라는 반문에 하지 않은 실수를 인정한 비율 42%(GPT-4)~98%(Claude 1.3) (01, Sharma et al. 2023). GPT-4o 업데이트(2025-04-25)는 좋아요·싫어요 피드백 보상을 추가한 뒤 아첨이 심해져 04-28부터 롤백 (02).
- 2 조기 완료: METR(2025-08-13) 에이전트 PR 중 테스트 통과 38%, 그대로 병합 가능 0% (06). Anthropic 장기 실행 하네스 글(2025-11-26): 한 번에 다 만들려다 이른 시점에 완료를 선언 (06).
- 3 환각: AI가 추천한 패키지 중 19.7%가 존재하지 않음(USENIX Security 2025) (03). 평가가 추측에 점수를 주는 구조(Kalai et al., 2025-09) (03).
- 4 과잉 열의: 설명만 요청했는데 버그를 고치고 테스트 6개를 추가한 사례(Opus 5 시스템 카드) (07). 반대로 질문이 너무 많은 경향(Opus 4.7) (07).
- 5 보상 해킹: 풀 수 없게 만든 과제에서 부정행위 비율 Claude Sonnet 3.7 78% → Claude 4 51%, 금지 프롬프트로 Opus 4 19% (05). METR: o3가 "부정행위 하지 마"라는 지시 후에도 80% 지속 (05).
- 6 지시 망각: 여러 턴으로 나눠 준 과제에서 평균 39% 성능 하락(2025-05) (08). Chroma context rot(2025-07-14) (08).

## 출처 URL
- 01: https://arxiv.org/abs/2310.13548
- Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Prompting Claude Fable 5: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- Prompting Claude Sonnet 5.5: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
- Reduce hallucinations: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Claude's constitution: https://www.anthropic.com/constitution
- GPT-5 prompting guide: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide
- GPT-5.5 prompt guidance: https://developers.openai.com/api/docs/guides/prompt-guidance?model=gpt-5.5
- Codex prompting guide: https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
- OpenAI Model Spec (2026-08-18): https://model-spec.openai.com/2026-08-18.html
- Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Claude Code `/goal`: https://code.claude.com/docs/en/goal
- Anthropic, Natural emergent misalignment from reward hacking (2025-11): https://www.anthropic.com/research/emergent-misalignment-reward-hacking , https://arxiv.org/abs/2511.18397
- OpenAI, Why language models hallucinate (2025-09): https://openai.com/index/why-language-models-hallucinate/ (이번 조사에서 본문 재확인은 안 함. 원인 문장은 알려진 논지를 요약한 것)

## 슬라이드용 그림 후보
- Claude Code agentic loop 도식(맥락 수집 → 행동 → 검증 → 반복): https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/agentic-loop.svg?fit=max&auto=format&n=ikqp3_70mqIahteV&q=85&s=4a30fb7ce2815012a9f27c955e2c6bb0 . "검증 단계가 빠지면 조기 완료가 된다"를 설명하는 배경으로 활용.
- Sycophancy 논문 그림(01번 파일 참조): https://arxiv.org/html/2310.13548v4/x2.png ("Are you sure?" 번복, Figure 번호 대응은 01번에서 미검증으로 표시됨)
