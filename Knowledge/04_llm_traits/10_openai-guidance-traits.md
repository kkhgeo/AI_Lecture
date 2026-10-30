# GPT-5 / GPT-5.5 Prompting Guides, Codex Prompting Guide, OpenAI Model Spec (OpenAI 공식 가이드: 행동 특성 대응)

- **저자/기관**: OpenAI (Developers Cookbook, API Docs, Model Spec)
- **발행일**: GPT-5 prompting guide 2025-08(GPT-5 출시 시점), GPT-5.5 prompt guidance는 제3자 블로그 기준 2026-04경(페이지 자체에서 날짜 미확인), Codex Prompting Guide는 현재 `gpt-5.3-codex` 기준으로 갱신됨(날짜 미표기), Model Spec 2026-08-18 버전 (모두 2026-09-30 열람)
- **URL**:
  - https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide
  - https://developers.openai.com/api/docs/guides/prompt-guidance?model=gpt-5.5
  - https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
  - https://learn.chatgpt.com/docs/prompting (구 developers.openai.com/codex/prompting에서 리다이렉트)
  - https://model-spec.openai.com/2026-08-18.html
  - (배경) https://openai.com/index/sycophancy-in-gpt-4o/ (2025-04-29, GPT-4o 아첨 업데이트 롤백 경위, 이번 조사에서 본문 재확인은 안 함)
- **자료 유형**: 공식문서 | 가이드

## 핵심 요약
- **Agentic eagerness를 조절 대상으로 본다**: GPT-5 가이드는 "얼마나 적극적으로 스스로 움직일지"를 프롬프트와 `reasoning_effort`로 조절하라고 한다. 덜 적극적이게 하려면 effort를 낮추고, 탐색 기준·조기 종료 기준·도구 호출 예산(예: "최대 2회")을 명시한다. 더 적극적이게 하려면 effort를 높이고 persistence 프롬프트를 쓴다.
- **Persistence 프롬프트**: 요지는 "너는 에이전트다. 사용자의 요청이 완전히 해결될 때까지 멈추지 말고, 문제가 해결됐다고 확신할 때만 턴을 끝내라. 불확실하다고 사용자에게 넘기지 말고 합리적 가정을 하고 진행한 뒤 가정을 기록하라." 이는 중간에 멈추는 문제(under-eagerness)를 겨냥한 것이다. 반대로 과잉 행동이 문제면 끄거나 약화해야 한다.
- **Tool preambles**: 도구를 쓰기 전에 목표를 다시 말하고, 계획을 제시하고, 진행 상황을 짧게 알리고, 끝나면 무엇을 했는지 요약하게 한다. 사용자가 에이전트의 궤적을 따라가며 이른 단계에서 교정할 수 있게 하는 장치다.
- **모순된 지시가 성능을 떨어뜨린다**: GPT-5는 지시를 정밀하게 따르기 때문에 서로 충돌하는 지시가 있으면 조정하느라 추론을 낭비한다. 프롬프트 최적화 도구로 모순을 점검하라고 권한다.
- **GPT-5.5: 결과 중심(outcome-first) 프롬프트**: 절차를 세세히 지시하지 말고 기대 결과, 성공 기준, 허용되는 부작용, 증거 규칙, 출력 형태를 정의하라고 한다. 옛 모델용 과잉 절차 지시는 줄이라고 권하며, 높은 reasoning effort가 늘 좋은 것은 아니라고 경고한다(과잉 탐색·과잉 사고).
- **검증을 명시하라**: GPT-5.5 가이드는 변경 후 가장 관련성 높은 검증(단위 테스트, 타입 체크 등)을 실행하게 하라고 한다. 초안 작성 시에는 글을 그럴듯하게 만들려고 이름·수치·데이터 주장을 지어내지 말고, 근거가 없으면 가정이라고 표시하게 하라고 권한다(환각 대응).
- **Codex Prompting Guide (gpt-5.3-codex)**: "자율적인 시니어 엔지니어"로서 맥락 수집, 계획, 구현, 테스트, 개선을 끝까지 수행하고, 분석이나 부분 수정에서 멈추지 말라는 persistence·bias-to-action 지시가 기본이다. 동시에 품질 제약도 둔다. 속도보다 정확성, 위험한 지름길 금지, 조용한 실패·광범위 catch 금지, 기존 패턴 재사용, 내가 만들지 않은 변경 되돌리기 금지, `git reset --hard` 같은 파괴적 명령 금지, 같은 파일을 진척 없이 반복 수정하면 멈추기. 계획 도구로 세운 계획은 끝날 때 항목마다 Done/Blocked/Cancelled로 정리하게 한다.
- **Codex 사용자 프롬프트 구조**: 목표(Goal), 맥락(Context), 제약(Constraints/Boundaries), 완료 조건(Done when)을 적고, 다단계 작업은 `/plan`으로 조사·계획을 먼저 받은 뒤 편집하게 한다. 재현 단계, 테스트, 린트를 돌릴 수 있을 때 결과 품질이 높아진다고 설명한다.
- **Model Spec: 아첨 금지와 불확실성 표현**: "Be honest and transparent" 아래에 "Do not lie", "Don't be sycophantic", "Express uncertainty", "Highlight possible misalignments"가 있다. 아첨 금지 섹션은 코드 리뷰나 피드백 요청 때 칭찬만 하지 말고 솔직한 평가를 주며, 원칙에 어긋나면 정중히 반박하되 최종 결정은 사용자에게 맡기라고 한다. 불확실성 섹션은 정보가 불완전하거나 해석이 여럿일 때 가정을 밝히고 확인 질문을 하라고 한다. 에이전트 맥락에서는 "합의된 자율 범위 안에서 행동"하고 부작용을 통제·공지하라고 한다.

## 핵심 개념·용어 정의
- **Agentic eagerness**: 모델이 명시적 지시 없이 스스로 탐색·행동하려는 정도. OpenAI는 이를 켜고 끌 수 있는 다이얼로 본다.
- **Persistence**: 과제가 끝날 때까지 턴을 끝내지 않고 계속하게 하는 지시. 조기 종료에 대응하지만 과잉 행동을 부를 수 있다.
- **Tool preamble**: 도구 호출 전후의 짧은 사용자용 설명(목표 재진술, 계획, 진행 보고, 요약).
- **reasoning_effort**: 사고 깊이와 도구 호출 적극성을 함께 조절하는 API 파라미터(minimal/low/medium/high 등).
- **Outcome-first prompting**: 절차 대신 결과·성공 기준·증거 규칙을 지정하는 방식(GPT-5.5).
- **Sycophancy**: 사용자의 말에 비판 없이 동의하거나 과하게 칭찬하는 경향. OpenAI는 2025년 4월 GPT-4o 업데이트가 지나치게 아첨적이어서 롤백한 사례를 공개했다(배경 사례, 세부는 본문 재확인 필요).
- **Scope of autonomy**: 에이전트가 사용자와 합의한 행동 범위(Model Spec). 범위 밖 행동과 예기치 않은 부작용을 피한다.

## 강연에 쓸 만한 포인트
- 예시 프롬프트(번역·요약):
  - 덜 적극적으로: "맥락 수집은 빠르게 끝내. 도구 호출은 최대 2번. 정확한 수정 위치를 특정할 수 있으면 바로 멈추고 진행해."
  - 더 끈질기게: "요청이 완전히 해결될 때까지 턴을 끝내지 마. 불확실하면 되묻지 말고 가장 합리적인 가정으로 진행한 뒤 그 가정을 기록해."
  - Tool preamble: "도구를 쓰기 전에 목표를 한 문장으로 다시 말하고 단계별 계획을 보여 줘. 끝나면 무엇을 했는지 따로 요약해."
  - 검증: "변경 후에는 가장 관련 있는 테스트나 타입 체크를 실행하고 결과를 보여 줘."
  - 환각 억제: "그럴듯하게 보이려고 이름·수치·데이터를 지어내지 마. 근거가 없으면 가정이라고 표시해."
  - 아첨 방지: "칭찬 말고 비판적 리뷰를 해 줘. 문제가 있으면 분명하게 반대해."
- 비유: eagerness는 "다이얼"이다. 끝까지 해내라고 돌리면 멈추지 않는 대신 범위를 넘어갈 수 있고, 줄이면 안전하지만 중간에 손을 놓을 수 있다. 사용자는 과제에 맞게 다이얼 위치를 정한다.
- 인용(1개): "keep going until the user's query is completely resolved" (OpenAI, GPT-5 prompting guide)
- 대비 포인트: OpenAI는 Codex에 "끝까지, 되묻지 말고"라는 bias to action을 기본값으로 준다. Anthropic 문서는 모델에 따라 "멈추고 확인하라"와 "계속하라"를 모두 제공한다. 두 벤더 모두 조기 종료와 과잉 행동을 한 다이얼의 양 끝으로 다룬다.

## 원본 그림
- 없음 (GPT-5 prompting guide, GPT-5.5 prompt guidance, Codex prompting guide 페이지에서 도식 이미지를 찾지 못함. 가이드 원문 페이지 캡처 사용을 권함)

## 코딩 에이전트 사용과의 연결점
- Codex 사용자는 AGENTS.md에 완료 조건과 검증 명령(테스트·린트)을 적어 두면 persistence 기본값이 "테스트 통과까지 계속"으로 이어진다.
- `/plan`(Codex)과 Plan mode(Claude Code)는 같은 기능이다. 조사와 계획을 실행과 분리해 성급한 구현과 잘못된 문제 풀이를 막는다.
- Tool preamble과 진행 보고는 사용자가 에이전트의 잘못된 방향을 일찍 알아차리게 한다. 중간 메시지를 흘려 넘기지 않는 것이 사용자 쪽 대응이다.
- Model Spec의 "Don't be sycophantic"은 모델의 기본값일 뿐이다. 코드 리뷰를 맡길 때 "비판적으로", "문제가 없으면 없다고, 있으면 근거와 함께"를 명시하면 기본값을 강화할 수 있다.
- "내가 만들지 않은 변경을 되돌리지 말라", "파괴적 git 명령 금지"는 과잉 행동이 실제 손실로 이어지는 지점을 벤더가 직접 막는 예시로 강의에 쓸 수 있다.
