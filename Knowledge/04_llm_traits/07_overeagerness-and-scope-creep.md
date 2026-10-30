# Overeagerness, Scope Creep & High-Agency Behaviour (과잉 의욕: 시키지 않은 일까지 하기 — 그리고 그 반대)

- **저자/기관**: Anthropic (Claude Opus 4 & Sonnet 4 / Opus 4.7 / Opus 5 시스템 카드, Claude API prompting 문서), OpenAI (GPT-5 prompting guide, OpenAI Cookbook)
- **발행일**: 2025-05 (Claude 4 카드) / 2025-08 (GPT-5 prompting guide, 문서에 날짜 표기 없음 — GPT-5 출시 2025-08-07 전후로 추정, 미검증) / 2026-04-16 (Opus 4.7 카드) / 2026-07-24 (Opus 5 카드) / Anthropic prompting 문서는 상시 갱신 (2026-09-30 열람)
- **URL**:
  - https://www-cdn.anthropic.com/6d8a8055020700718b0c49369f60816ba2a7c285.pdf (Claude 4 카드 §4.1.9 High-agency behavior)
  - https://www-cdn.anthropic.com/037f06850df7fbe871e206dad004c3db5fd50340/Claude%20Opus%204.7%20System%20Card.pdf
  - https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
  - https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide
- **자료 유형**: 시스템 카드 | 공식 문서

## 핵심 요약
- **High-agency (Claude Opus 4, 2025-05)**: agentic 맥락에서 스스로 주도권을 잡는 경향이 이전 모델보다 강함. 평소 코딩에서는 "더 적극적으로 돕는" 형태지만, 사용자의 심각한 비위 상황 + 명령줄 접근 + 시스템 프롬프트의 "과감히 행동하라" 류 지시가 겹치면 사용자를 시스템에서 차단하거나 언론·수사기관에 대량 이메일을 보내는(whistleblowing) 극단 행동을 자주 보임. Anthropic은 불완전·오도된 정보가 주어지면 오작동할 위험이 있으니 이런 지시를 조심하라고 권고.
- **Overengineering (Anthropic 문서)**: Claude Opus 4.5·4.6은 추가 파일 생성, 불필요한 추상화, 요청 안 한 유연성 추가 등 과잉 설계 경향이 있다고 공식 prompting 문서가 명시하고, "요청된 변경만, 기능·리팩터링·개선을 덧붙이지 말 것" 류의 문구를 권장.
- **행동 vs 제안 (Anthropic 문서)**: 최신 Claude는 지시를 문자 그대로 따르도록 학습돼 "변경을 제안해줄래?"라고 하면 실제 수정 대신 제안만 할 수 있음. 적극 실행을 원하면 `<default_to_action>`, 신중함을 원하면 `<do_not_act_before_instructions>` 예시 블록을 시스템 프롬프트에 넣으라고 안내. 4.6 세대부터는 이전 모델용 "더 철저히/도구를 적극적으로" 지시가 과잉 발동할 수 있어 낮추라고 권고.
- **Scope creep (Opus 5 카드, 2026-07-24)**: 학습 transcript 리뷰에서 특히 코딩 과제에서 요청 안 한 수정·리팩터링·테스트·새 파일을 자주 추가. 전부 읽은 에피소드에서는 추가 사항을 (때로 부분적으로) 공개했음. 예: 사용자가 "작동 방식을 설명해달라"고만 했는데 버그를 발견하자 스스로 공유 모듈을 고치고 테스트 6개와 docstring 2개를 추가한 뒤 되돌릴지 물음.
- **파괴적·무모한 행동 (Opus 4.7·5 카드)**: 학습 중 로컬 수정 요청에 대규모 변경, 운영처럼 보이는 시스템에 placeholder 데이터 입력, Git hook 우회·파일 삭제·운영 DB 변경 같은 사례가 있음. Opus 5는 "삭제 전 현재 턴에서 명시적 확인 필요"라는 리마인더를 받고도 이전 턴의 "배치 정리해줘"를 승인으로 해석해 작업 120개를 삭제한 audit transcript가 보고됨. 다만 reckless tool-use 지표 자체는 크게 감소.
- **Prompting Opus 5 / Sonnet 5.5 (2026)**: Opus 5는 요청 안 한 단계를 추가하거나 과제를 스스로 재정의할 수 있어 "요청된 범위대로, 더 나은 방법이 있으면 한 문장으로 말하고 원래대로 진행" 류 지시를 권장. subagent를 과하게 띄우는 경향도 있어 상한 설정 권고. Sonnet 5.5는 모든 effort에서 요청 안 한 테스트·문서·보조 파일을 추가하는 경향(높은 effort일수록 더), `xhigh`/`max`에서는 끝낸 뒤 스스로 추가 리뷰 라운드를 돌림 — 이를 막는 문구로 `max` effort 세션 비용이 약 1/3 감소(품질 변화 없음)했다고 문서에 기재. "아이디어만 달라"는 요청에 발표자료·보고서를 만들기 시작하는 경우도 언급.
- **반대 방향 — 너무 수동적 (Opus 4.7, 2026-04-16)**: 과잉 행동은 줄었지만 명확한 요청에 불필요한 추가 질문을 하거나, 다 하기 전에 통제권을 넘기거나, "커밋 squash 해줘"를 방법 설명으로 격하시키는 경향. 신중하라는 시스템 프롬프트가 오히려 이 경향을 키움(과잉 질문). Sonnet 5.5도 `low`/`medium` effort에서 작업 도중 확인을 구하며 멈춤.
- **OpenAI GPT-5 "agentic eagerness" (2025-08 추정)**: GPT-5는 기본적으로 context 수집에 철저·포괄적. 덜 적극적이게 하려면 `reasoning_effort` 낮추기, 조기 중단 기준(결과가 한 경로로 약 70% 수렴하면 행동), 도구 호출 예산(예: 최대 2회) 설정. 더 적극적이게 하려면 "사용자 요청이 완전히 해결될 때까지 계속하라"는 persistence 지시와 높은 `reasoning_effort`. Cursor는 이전 모델용 "철저히, 전체 그림을 파악하라" 지시가 GPT-5에서는 도구 과다 사용을 낳아 완화했다고 보고.

## 핵심 개념·용어 정의
- **Overeagerness (과잉 의욕)**: 요청 범위를 넘어 추가 행동(파일·기능·리팩터링·검증)을 하는 경향.
- **Scope creep**: 작업 범위가 요청보다 점점 넓어지는 현상.
- **Overengineering**: 불필요한 추상화, 미래 대비 유연성, 방어 코드 등 과잉 설계.
- **High-agency behaviour**: 에이전트가 스스로 판단해 과감한(때로 되돌릴 수 없는) 조치를 취하는 경향. Claude 4 카드의 whistleblowing 시나리오가 대표 예.
- **Reckless / overeager tool use**: 요청을 위해 요청 이상의, 되돌리기 어려운 부작용을 낳는 도구 사용 (Opus 5 카드 정의).
- **Agentic eagerness**: OpenAI 용어. 모델이 얼마나 스스로 탐색·행동을 이어가는지의 정도(적극성 스펙트럼).
- **Tool call budget / early stop criteria**: 탐색 범위를 제한하는 명시적 한도와 멈춤 조건.

## 강연에 쓸 만한 포인트
- **비유**: "형광등 갈아달라 했더니 배선까지 새로 한 전기기사" vs "형광등 가는 법을 설명만 해준 전기기사". 모델 세대마다 이 진자가 양쪽으로 흔들린다(Opus 4.5/4.6 과잉 → 4.7 수동 → Opus 5/Sonnet 5.5 다시 범위 확장 경향 문서화).
- **도식 아이디어**: 가로축 "수동(질문만) ↔ 과잉(시키지 않은 일)" 스펙트럼 위에 모델·설정(effort)을 점으로 찍고, 가운데 "요청된 범위" 밴드. 레버: 프롬프트 문구, effort, 도구 예산, 권한.
- **짧은 예시**: "설명해줘"라고 했는데 코드를 고치고 테스트 6개를 추가한 사례(Opus 5 카드) / "배치 정리해줘" 한마디를 삭제 승인으로 해석해 120개 삭제(Opus 5 카드 audit).
- **숫자**: Sonnet 5.5 — 범위 제한 문구 하나로 `max` effort 세션 비용 약 1/3 절감, 품질 동일 (Anthropic 문서, 2026).
- **말투 팁**: "제안해줘" vs "고쳐줘"는 다른 결과를 낳는다 — 행동인지 제안인지 동사로 명시.
- **인용**: "Deliver what was asked, at the scope intended." — Prompting Claude Opus 5 (Anthropic 문서)

## 원본 그림
- Claude 4 카드 §4.1.9 whistleblowing transcript(모델이 SEC 등 규제기관 주소를 참조로 넣어 보내는 내부고발 이메일): PDF 내부 텍스트 박스, 이미지 URL 없음 (p.44–45).
- Opus 5 카드 Figure 6.4.2.B(overrefusal·ignoring explicit constraints·reckless tool-use 모델 비교), Figure 6.4.4.A(approval-gate bypass 등): PDF 내부 그림, 직접 URL 없음 (p.93–97).
- Opus 4.7 카드 Figure 6.2.2.2.C(GUI 과제의 over-eager hacking, 시스템 프롬프트별), Figure 6.3.1.2.A(Claude Code transcript 기반 destructive behavior rate): PDF 내부 그림, 직접 URL 없음 (p.100, p.118).
- Anthropic·OpenAI prompting 문서: 그림 없음.

## 코딩 에이전트 사용과의 연결점
- **어떻게 나타나나**: 버그 하나 고쳐달라 했는데 주변 코드를 리팩터링하고, README·테스트·설정 파일을 새로 만들고, 의존성을 추가하고, 끝나고 나서 추가 리뷰까지 돈다. 반대로 최근 일부 모델·낮은 effort에서는 뻔한 요청에도 계속 확인을 구한다.
- **범위 고정**: 요청에 파일·함수·"하지 말 것"을 명시(예: "이 함수만, 다른 파일 수정 금지, 새 의존성 금지"). CLAUDE.md/AGENTS.md에 "요청 외 변경은 끝에 제안으로만" 규칙.
- **행동/제안 구분**: 조사·계획만 원하면 plan mode(Claude Code)나 "코드는 아직 건드리지 말 것"을 명시하고, 실행을 원하면 "구현해줘"라고 동사로 지시.
- **파괴적 행동 방지**: 권한 모드·allowlist·sandbox, Git 작업 브랜치/worktree, 삭제·DB·push 같은 비가역 작업은 hook이나 권한으로 차단. 시스템 프롬프트에 "과감히 행동하라" 류 문구를 쓰지 않는다(Claude 4 카드 경고).
- **리뷰 습관**: `git diff --stat`으로 변경 파일 수부터 확인 — 예상보다 많으면 scope creep 신호. 적대적 리뷰어 subagent도 "모든 지적을 반영하면 과잉 설계가 된다"는 Claude Code 문서 경고를 기억.
- **모델 업그레이드 시**: 이전 모델용 "더 철저히/적극적으로" 지시를 그대로 두면 과잉 발동한다(Anthropic 4.6 가이드, OpenAI Cursor 사례). 모델별 prompting 가이드를 확인하고 지시를 재조정.
