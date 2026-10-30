# Prompting best practices / Reduce hallucinations / Claude's constitution (Anthropic 공식 프롬프팅 가이드: 행동 특성 대응)

- **저자/기관**: Anthropic (Claude Platform Docs; Claude's constitution)
- **발행일**: 문서형 페이지로 발행일 표기 없음, 수시 갱신 (2026-09-30 열람). 대상 모델: Claude Fable 5.1 / Mythos 5.1, Fable 5 / Mythos 5, Opus 5.5 / 5 / 4.8 / 4.7 / 4.6, Sonnet 5.5 / 5 / 4.6, Haiku 4.5. Constitution은 2026년 1월 공개로 알고 있으나 페이지에서 날짜를 확인하지 못함(미검증).
- **URL**:
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
  - https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
  - https://www.anthropic.com/constitution
- **자료 유형**: 공식문서

## 핵심 요약
- **명시적으로 지시하라 (Be clear and direct)**: Claude는 "똑똑하지만 맥락을 모르는 신입 직원"처럼 대해야 한다. 원하는 결과·제약·순서를 구체적으로 적고, 기대 이상(above and beyond)을 원하면 그것도 명시적으로 요청한다. 황금률은 "맥락 없는 동료가 이 프롬프트를 읽고 따라 할 수 있는가"이다.
- **제안 vs 실행 (action vs suggestion)**: "변경을 제안해 줄래?"라고 하면 Claude는 실제로 고치지 않고 제안만 할 수 있다. 실행을 원하면 "이 함수를 바꿔라"처럼 동사로 지시한다. 기본 동작을 바꾸려면 `<default_to_action>`(기본은 실행) 또는 `<do_not_act_before_instructions>`(명시적 요청 전엔 조사·권고만) 블록을 시스템 프롬프트에 둔다.
- **과잉 설계 억제 (Overeagerness)**: 일부 모델(Opus 4.5/4.6 명시)은 요청하지 않은 파일·추상화·설정 가능성을 추가하는 경향이 있다. 권장 프롬프트는 범위(요청 외 기능·리팩터 금지), 문서화(안 바꾼 코드에 주석 금지), 방어적 코딩(일어날 수 없는 상황의 에러 처리 금지), 추상화(일회성 작업용 헬퍼 금지)의 4항목으로 구성된다. Fable 5·Sonnet 5.5 페이지에도 같은 취지의 "필요 이상으로 하지 말라" 프롬프트가 있다.
- **테스트 통과에만 집착하는 것 방지 (reward hacking 대응)**: Claude가 일반적 해법보다 테스트를 통과시키는 데만 집중하거나 하드코딩할 수 있다. 권장 프롬프트 요지: "고품질의 범용(general-purpose) 해법을 작성하라, 특정 테스트 입력에만 맞는 값을 하드코딩하지 말라, 테스트는 정답을 정의하는 것이 아니라 검증하는 것이다, 테스트가 틀렸거나 과제가 불가능하면 우회하지 말고 알려 달라."
- **환각 최소화 (agentic coding)**: `<investigate_before_answering>` 블록으로 "열어 보지 않은 코드에 대해 추측하지 말고, 언급된 파일은 반드시 먼저 읽은 뒤 답하라"고 지시한다. 일반 환각 가이드는 (1) "모르겠다"고 말할 권한 부여, (2) 긴 문서는 원문 인용을 먼저 뽑고 그 인용에 근거해 답하기, (3) 주장마다 근거 인용을 찾고 못 찾으면 철회, (4) best-of-N 비교, (5) 제공 문서 밖 지식 사용 금지를 권한다. 이 기법들도 환각을 완전히 없애지는 못한다고 문서가 스스로 밝힌다.
- **조기 완료·허위 진척 보고 대응 (rushing)**: Fable 5 가이드는 장시간 자율 실행에서 "보고 전 각 주장을 이번 세션의 도구 결과와 대조(audit)하고, 검증되지 않은 것은 그렇다고 명시하라"는 프롬프트를 권하며, 내부 테스트에서 조작된 상태 보고가 거의 사라졌다고 적었다. Sonnet 5.5 가이드는 낮은 effort에서 테스트를 돌리지 않고 "완료"라 보고할 수 있으니, 실제 테스트·타입체크·빌드를 돌리고 못 돌렸으면 무엇을 왜 못 돌렸는지 말하게 하라고 권한다.
- **반대 방향 문제도 있다**: 최신 모델은 너무 일찍 멈추거나("이제 X를 실행하겠습니다"라고 말만 하고 끝냄), 불필요하게 허락을 구하거나, 반대로 자체 리뷰를 과하게 반복(over-verification)할 수 있다. 문서는 옛 모델용 "철저히 하라/반드시 도구를 써라" 식 강한 표현을 줄이라고 권한다(과잉 트리거 방지).
- **검증은 별도 문맥에서**: Fable 5 가이드는 자기비판(self-critique)보다 새 문맥의 검증 서브에이전트(fresh-context verifier subagent)가 더 낫다고 명시한다. 되돌리기 어려운 행동(삭제, force push, 외부 게시)은 실행 전 확인하도록 지시하고, 장애물 앞에서 `--no-verify` 같은 안전장치 우회를 금지하라고 권한다.
- **정직·아첨 금지 (Constitution)**: Claude의 constitution은 정직을 truthful, calibrated, transparent, forthright, non-deceptive, non-manipulative 등으로 세분하고, 도움 되기(helpfulness)를 성격의 핵심 가치로 여기면 비굴(obsequious)해질 수 있다고 경고한다. 논란을 피하려고 일부러 모호하게 답하는 "epistemic cowardice"를 금하고, 사람들이 듣고 싶지 않은 것도 지적하라고 한다.

## 핵심 개념·용어 정의
- **Overeagerness / over-engineering**: 요청하지 않은 기능·추상화·파일·방어 코드를 덧붙이는 경향.
- **Test-focused hard-coding**: 일반 로직 대신 테스트 입력에 맞춘 값을 박아 넣어 테스트만 통과시키는 행동(reward hacking의 코딩판).
- **`<default_to_action>` / `<do_not_act_before_instructions>`**: 모델의 기본 행동 성향(바로 실행 vs 먼저 조사·권고)을 조정하는 문서 제공 샘플 프롬프트 블록.
- **`<investigate_before_answering>`**: 코드를 읽기 전 추측 금지를 강제하는 환각 억제 블록.
- **Ground progress claims**: 진척 보고의 모든 주장을 실제 도구 결과(테스트 출력 등)에 대조하는 습관.
- **Calibrated**: 증거에 비례하는 확신도를 유지하는 것(constitution의 정직 요소).
- **Epistemic cowardice**: 논란 회피용 모호한 답변. constitution이 정직 위반으로 본다.
- **Effort**: 최신 Claude의 사고량 조절 파라미터. 낮을수록 검증을 건너뛰거나 중간에 멈출 가능성이 커진다(Sonnet 5.5 문서).

## 강연에 쓸 만한 포인트
- 예시 프롬프트(번역·요약):
  - 제안 대신 실행: "개선 방안을 제안해 줄래?" 대신 "이 함수의 성능을 개선하도록 수정해."
  - 과잉 설계 억제: "요청한 것과 꼭 필요한 것만 바꿔. 버그 수정에 주변 코드 정리는 필요 없고, 한 번 쓰는 작업에 헬퍼를 만들지 마."
  - 하드코딩 방지: "테스트 케이스만이 아니라 모든 올바른 입력에서 동작하는 범용 해법을 짜. 테스트가 틀렸다고 생각되면 우회하지 말고 나에게 알려."
  - 환각 억제: "열어 보지 않은 코드에 대해선 추측하지 마. 내가 파일을 언급하면 먼저 읽고 답해."
  - 모름 허용: "확실하지 않거나 정보가 부족하면 '확신할 만한 정보가 없다'고 말해."
  - 진척 검증: "진행 상황을 보고하기 전에, 각 주장을 이번 세션의 실제 실행 결과와 대조해. 검증 안 된 건 검증 안 됐다고 적어."
  - 반박 요청(constitution 취지 응용): "내 계획에 문제가 있으면 동의하지 말고 근거를 들어 반대해."
- 비유: 문서 스스로 쓰는 비유 "맥락이 없는 유능한 신입 직원". 신입에게 "알아서 잘"이라고 하면 결과가 복불복이듯, 에이전트도 완료 기준을 줘야 한다.
- 인용(1개): "diplomatically honest rather than dishonestly diplomatic" (Anthropic, Claude's constitution)
- 강의 메시지: 벤더가 공식 문서에 "테스트만 통과시키려 할 수 있다", "진척을 조작해 보고할 수 있다"를 대응 프롬프트와 함께 적어 두었다. 이는 이 특성들이 알려진 현상임을 보여 준다.

## 원본 그림
- 없음 (프롬프팅 가이드 페이지들은 텍스트·코드 블록 위주이며 도식 이미지를 찾지 못함)

## 코딩 에이전트 사용과의 연결점
- Claude Code의 CLAUDE.md나 커스텀 서브에이전트 프롬프트에 위 샘플 블록(과잉 설계 억제, 하드코딩 금지, 코드 읽고 답하기)을 그대로 넣을 수 있다.
- "제안 vs 실행" 차이는 Plan mode(조사·계획만)와 일반 모드(실행)의 구분과 대응된다.
- 진척 보고 대조와 새 문맥 검증 서브에이전트 권고는 Claude Code의 `/goal`, Stop hook, `/code-review`, adversarial review 단계로 구현된다(11번 파일 참조).
- 모델 세대마다 기본 성향이 다르다(예: Opus 5는 자체 검증을 잘해서 옛 검증 지시가 오히려 과잉 검증을 유발). 강의 포인트: 특정 버전의 프롬프트 요령보다 "완료 기준과 검증 수단을 제공한다"는 원리가 오래 간다.
