# Best practices for Claude Code / Keep Claude working toward a goal / How Claude Code works (Claude Code 기능으로 행동 특성 대응하기)

- **저자/기관**: Anthropic (Claude Code Docs)
- **발행일**: 문서형 페이지로 발행일 표기 없음, 수시 갱신. 본문에 Claude Code v2.1.283 등 최신 버전 언급 (2026-09-30 열람)
- **URL**:
  - https://code.claude.com/docs/en/best-practices
  - https://code.claude.com/docs/en/goal
  - https://code.claude.com/docs/en/how-claude-code-works
  - https://code.claude.com/docs/en/permission-modes (Plan mode)
  - https://code.claude.com/docs/en/checkpointing
  - https://code.claude.com/docs/en/hooks (Stop hook)
  - https://code.claude.com/docs/en/sub-agents
- **자료 유형**: 공식문서

## 핵심 요약
- **검증 수단을 주라 (가장 강조되는 원칙)**: 문서는 Claude가 "작업이 끝나 보이면" 멈춘다고 설명한다. 실행 가능한 검사(테스트, 빌드 종료 코드, 린터, 스크린샷 비교)가 없으면 사용자가 검증 루프가 되어야 한다. 검사를 주면 Claude가 스스로 실행, 결과 확인, 반복을 할 수 있다. 성공을 주장만 하지 말고 테스트 출력, 실행 명령, 스크린샷 같은 증거를 보여 달라고 하라고 한다.
- **검증 강제의 4단계**: (1) 한 프롬프트 안에서 "구현 후 테스트 실행하고 실패하면 고쳐"라고 지시, (2) `/goal`로 세션 동안 완료 조건을 걸면 별도 평가 모델(기본 Haiku)이 매 턴 뒤 조건 충족 여부를 판정, (3) Stop hook으로 스크립트 검사를 통과하기 전엔 턴이 끝나지 않게 하는 결정적(deterministic) 게이트, (4) 검증 서브에이전트나 워크플로를 써서 작업자가 아닌 새 모델이 결과를 반박해 보는 second opinion.
- **Explore, Plan, Code, Commit**: Plan mode(Shift+Tab 또는 `--permission-mode plan`)에서는 Claude가 파일을 읽고 질문에 답하지만 수정하지 않는다. 계획을 받아 Ctrl+G로 직접 편집한 뒤 구현으로 넘어간다. 한 문장으로 설명할 수 있는 수정이면 계획을 건너뛰라고 한다.
- **Claude에게 인터뷰를 시켜라**: 큰 기능은 최소 프롬프트로 시작해 AskUserQuestion 도구로 사용자를 인터뷰하게 하고, 결과를 SPEC.md로 쓰게 한 뒤 새 세션에서 구현한다. 좋은 스펙은 관련 파일·인터페이스, 범위 밖 항목, 끝에서 끝까지의 검증 단계를 담는다.
- **구체적 맥락 제공**: 파일, 시나리오, 테스트 선호를 지정하고, 답을 가진 출처(git 기록 등)를 가리키고, 기존 패턴 예시를 주고, 증상·위치·"고쳐졌다"의 기준을 말한다. 예: "빌드 에러를 억누르지 말고 근본 원인을 고쳐라."
- **새 문맥 리뷰 (adversarial review)**: 오래 무인으로 일할수록 독립 검사가 중요하다. 새 서브에이전트는 diff와 기준만 보고 변경을 만든 추론은 보지 못하므로 자기 코드에 대한 편향이 없다. 번들 `/code-review` 스킬로 현재 diff의 버그를 새 서브에이전트가 검토하거나, "PLAN.md 대비 모든 요구사항 구현 여부, 엣지 케이스 테스트, 범위 밖 변경 여부를 확인하라"는 리뷰 프롬프트를 직접 쓴다. Writer/Reviewer 패턴(세션 A 구현, 세션 B 리뷰)도 제시된다.
- **리뷰어 과잉 지적 경고**: 결함을 찾으라고 지시받은 리뷰어는 작업이 괜찮아도 무언가를 보고하는 경향이 있다. 모든 지적을 따르면 과잉 설계(추상화, 방어 코드, 불가능한 케이스 테스트)가 생기므로 정확성과 요구사항에 영향을 주는 결함만 보고하게 하라고 한다. 리뷰 에이전트에도 아첨이나 과잉 열의가 나타날 수 있다는 점을 보여 주는 대목이다.
- **조기·반복 교정과 되돌리기**: Esc로 즉시 멈추고, Esc 두 번 또는 `/rewind`로 대화·코드를 체크포인트로 복원하고, "Undo that"으로 되돌린다. 같은 문제로 두 번 넘게 교정했다면 문맥이 실패한 시도로 오염된 것이니 `/clear` 후 더 나은 프롬프트로 새로 시작하라고 한다. 체크포인트는 Claude의 파일 편집만 추적하며 Bash나 외부 시스템(DB, 배포) 변경은 되돌리지 못한다.
- **흔한 실패 패턴 5가지 (Avoid common failure patterns)**: 잡동사니 세션(kitchen sink), 반복 교정(correcting over and over), 너무 긴 CLAUDE.md, 신뢰 후 검증 공백(trust-then-verify gap: 그럴듯하지만 엣지 케이스를 놓친 구현), 무한 탐색(범위 없는 "조사해 봐"). 각각 `/clear`, 두 번 실패 후 재시작, 과감한 가지치기와 hook 전환, 항상 검증 제공("검증할 수 없으면 배포하지 말라"), 범위 한정과 서브에이전트가 처방이다.

## 핵심 개념·용어 정의
- **Plan mode**: 읽기·분석만 하고 소스 파일을 편집하지 않는 권한 모드. 성급한 구현을 막는다.
- **`/goal`**: 완료 조건을 설정하면 매 턴 후 작은 모델이 "미충족/충족/불가능"을 판정하고, 미충족이면 Claude가 다음 턴을 이어 가는 명령. 작업자가 아닌 새 모델이 완료를 판단한다. 평가 모델은 도구를 쓰지 않으므로 조건은 대화에 드러나는 증거(테스트 결과 등)로 증명 가능해야 한다.
- **Stop hook**: 턴 종료 시 실행되는 hook. 스크립트 검사가 실패하면 종료를 막는다. CLAUDE.md 지시는 권고지만 hook은 결정적이다.
- **Verification / adversarial review subagent**: 새 문맥에서 결과를 반박하려는 서브에이전트. 자기 평가 편향을 줄인다.
- **`/code-review`**: 현재 diff를 새 서브에이전트가 버그 중심으로 검토하는 번들 스킬.
- **Checkpoint / `/rewind`**: 프롬프트마다 생성되는 파일 스냅샷. 대화, 코드, 또는 둘 다 복원할 수 있다.
- **AskUserQuestion 인터뷰**: Claude가 사용자에게 구조화된 질문을 던져 요구사항을 끌어내는 방식.
- **Trust-then-verify gap**: 그럴듯해 보이는 결과를 검증 없이 믿는 틈. 문서가 꼽은 실패 패턴 중 하나.

## 특성 → 대응 매핑
| 특성 | Claude Code 대응 기능·습관 | 근거 |
|---|---|---|
| 아첨 (sycophancy) | 계획이나 설계에 대해 "문제점과 반대 근거를 먼저 말해"라고 요청. Writer/Reviewer 세션 분리. 인터뷰로 사용자 가정을 검증. 리뷰어에게 기준을 명시 | best-practices (Writer/Reviewer, interview). 반박 요청 문구는 이 문서에 직접 없음. 09·10번의 constitution·Model Spec에서 응용 |
| 서두름·조기 완료 (rushing / premature completion) | 검증 기준 제공, `/goal` 완료 조건, Stop hook 게이트, 증거 제시 요구 | best-practices "Give Claude a way to verify", goal 문서 |
| 환각 (hallucination) | `@`로 파일 참조(읽고 답하게), 답이 있는 출처 지정, 서브에이전트 조사, 증거 요구 | best-practices "Provide specific context", "Provide rich content" |
| 과잉 열의 (overeagerness / scope creep) | Plan mode로 먼저 계획을 받고 편집, 범위를 명시한 프롬프트, 권한 모드와 allowlist, 체크포인트·`/rewind`, 리뷰 지적 선별 | best-practices, how-claude-code-works, permission-modes |
| 보상 해킹 (reward hacking: 테스트 조작, 에러 억제) | "근본 원인을 고치고 에러를 억누르지 말라", 테스트를 먼저 작성·고정(다른 세션이 테스트 작성), `/code-review`·adversarial review로 범위 밖 변경 확인, hook으로 테스트 파일 쓰기 차단 | best-practices ("address the root cause", 테스트/코드 세션 분리, "blocks writes to" hook 예시) |
| 문맥 오염·지시 망각 (보조) | `/clear`, `/compact`, 짧은 CLAUDE.md, 새 세션에서 스펙 실행 | best-practices failure patterns |

## 강연에 쓸 만한 포인트
- 예시 프롬프트(번역):
  - 검증 기준: "validateEmail 함수를 작성해. 테스트 케이스: user@example.com은 true, invalid는 false, user@.com은 false. 구현 후 테스트를 실행해."
  - 근본 원인: "빌드가 이 에러로 실패해: [에러]. 고치고 빌드 성공을 확인해. 에러를 억누르지 말고 근본 원인을 해결해."
  - 인터뷰: "[기능 설명]을 만들고 싶어. AskUserQuestion 도구로 나를 자세히 인터뷰해. 뻔한 질문 말고 내가 놓쳤을 어려운 부분을 파고들어. 다 끝나면 SPEC.md에 완전한 스펙을 써."
  - 적대적 리뷰: "서브에이전트를 써서 rate limiter diff를 PLAN.md와 대조 리뷰해. 모든 요구사항 구현, 엣지 케이스 테스트 존재, 범위 밖 변경 여부를 확인하고 스타일 취향이 아닌 결함만 보고해."
  - `/goal`: `/goal test/auth의 모든 테스트가 통과하고 lint가 깨끗할 것, 다른 테스트 파일은 수정하지 않을 것`
- 비유: 검증 수단이 없으면 사용자가 에이전트의 테스트 러너가 된다. 검사를 쥐여 주면 사람이 지켜보는 세션이 사람이 자리를 비워도 되는 세션으로 바뀐다.
- 인용(1개): "If you can't verify it, don't ship it." (Claude Code Docs, Best practices)
- 강의 메시지: 모델의 행동 특성을 프롬프트 한 줄로 없앨 수는 없다. 계획 분리, 기계적 검증, 새 문맥 리뷰, 되돌리기라는 작업 구조로 둘러싸는 것이 대응이다.

## 원본 그림
- Agentic loop 도식(라이트) — 사용자 프롬프트 → 맥락 수집 → 행동 → 결과 검증 → 반복, 언제든 사용자 개입 가능 — https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/agentic-loop.svg?fit=max&auto=format&n=ikqp3_70mqIahteV&q=85&s=4a30fb7ce2815012a9f27c955e2c6bb0
- Agentic loop 도식(다크) — https://mintcdn.com/claude-code/_xqph1dUOslCOwsj/images/agentic-loop-dark.svg?fit=max&auto=format&n=_xqph1dUOslCOwsj&q=85&s=75e1d55ed76857a952f9a2dffbab02df
- 세션 이어가기/분기(resume vs fork) 도식 — https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/session-continuity.svg?fit=max&auto=format&n=ikqp3_70mqIahteV&q=85&s=04ed0984a58e4127e05b3640265241a3 (특성 대응과는 간접적 관련)
- 참고: context window 인터랙티브 워크스루(https://code.claude.com/docs/en/context-window)는 정적 이미지가 아님

## 코딩 에이전트 사용과의 연결점
- 이 파일 자체가 코딩 에이전트 사용법이다. 강의 슬라이드에서는 특성(문제)과 기능(대응)을 짝지은 표(위 매핑)를 그대로 쓸 수 있다.
- Codex 대응 기능: `/plan`(Plan mode), `/review`(코드 리뷰), AGENTS.md(CLAUDE.md), 샌드박스·승인 모드(권한 모드). Codex 쪽 명령은 10번 파일과 Codex 문서 기준이며 세부 동작 차이는 별도 확인 필요.
- 핵심 원칙 세 가지: (1) 완료의 판단을 작업자 모델에게만 맡기지 않는다(`/goal`, Stop hook, 리뷰 서브에이전트), (2) 실행 전에 계획과 요구사항을 합의한다(Plan mode, 인터뷰), (3) 실수는 싸게 되돌린다(체크포인트, git, 권한 모드).
