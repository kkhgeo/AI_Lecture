# Unrolling the Codex agent loop (OpenAI Codex의 agent loop 해부)

- **저자/기관**: Michael Bolin (Member of the Technical Staff) / OpenAI
- **발행일**: 2026-01-23 (2026-09-29 열람)
- **URL**: https://openai.com/index/unrolling-the-codex-agent-loop/
- **자료 유형**: 엔지니어링 블로그 (OpenAI Engineering; Codex 동작 방식 연재의 첫 글)

## 핵심 요약
- 글의 대상은 Codex CLI, Codex Cloud, VS Code 확장 등 모든 Codex 제품 밑에 깔린 **Codex harness**, 즉 핵심 agent loop와 실행 로직이다. Harness는 사용자, 모델, 모델이 부르는 도구 사이의 상호작용을 오케스트레이션한다. 구현은 오픈소스(github.com/openai/codex).
- **Agent loop**: 사용자 입력으로 prompt를 만든다 → 모델에 추론(inference)을 요청한다 → 모델은 (1) 최종 답을 내거나 (2) 도구 호출을 요청한다 → (2)면 harness가 도구를 실행하고 그 출력을 prompt에 덧붙여 다시 모델을 부른다 → 모델이 도구 호출을 멈추고 assistant message를 낼 때까지 반복.
- 사용자 입력부터 assistant message까지가 한 **turn**(Codex에서는 thread 안의 한 턴)이다. 한 턴 안에서 추론과 도구 호출이 여러 번 오갈 수 있다. 코딩 에이전트의 진짜 산출물은 대개 메시지가 아니라 내 컴퓨터에서 수정된 코드다.
- 매 턴마다 이전 대화 전체(메시지와 도구 호출)가 다시 prompt에 들어가므로 prompt는 계속 길어진다. 모델마다 context window(입력+출력 토큰 한도)가 있어 **context window 관리가 harness의 핵심 책임** 중 하나다.
- Codex는 **Responses API**로 추론한다. 요청 JSON의 핵심 필드는 세 가지: `instructions`(모델별 기본 지시), `tools`(Codex 내장 shell·update_plan 도구, API 제공 web_search, 사용자가 붙인 MCP 도구), `input`(항목 리스트). 엔드포인트는 ChatGPT 로그인, API 키, 로컬 gpt-oss(ollama/LM Studio), Azure 등으로 바꿀 수 있다.
- `input` 앞부분에 Codex가 넣는 것: sandbox·승인 규칙을 설명하는 developer 메시지(이 sandbox는 Codex 내장 shell 도구에만 적용, MCP 도구는 자체 안전장치 책임), config의 developer instructions(선택), AGENTS.md 등에서 모은 user instructions와 skill 메타데이터(선택), cwd와 shell을 알려 주는 environment context. 그 뒤에 사용자 메시지가 붙는다. 역할 우선순위는 system > developer > user > assistant.
- 모델 응답은 SSE 스트림으로 오고, reasoning·function_call 항목과 도구 출력(function_call_output)이 다음 요청의 input 끝에 덧붙는다. 이전 prompt가 새 prompt의 정확한 접두사(prefix)가 되도록 설계한 것이 핵심이다.
- **성능**: 대화 길이에 따라 전송량이 이차적으로 늘어난다. `previous_response_id`로 줄일 수 있지만 Codex는 요청을 완전히 stateless로 유지하고 Zero Data Retention(ZDR)을 지원하려고 쓰지 않는다. 대신 **prompt caching**(정확한 접두사 일치 시 재사용)으로 샘플링 비용을 사실상 선형으로 만든다. 도구 목록·모델·sandbox·cwd 변경은 cache miss를 부르므로, 설정 변경은 앞 메시지를 고치지 않고 새 메시지를 덧붙여 반영한다. MCP 도구 순서가 일정하지 않아 cache miss가 났던 버그도 사례로 든다.
- **Compaction**: 토큰이 임계치(auto_compact_limit)를 넘으면 대화를 더 작은 항목 리스트로 대체한다. 초기에는 사용자가 `/compact`로 요약을 요청했으나, 이제는 Responses API의 `/responses/compact` 엔드포인트가 모델의 잠재적 이해를 담은 암호화된 compaction 항목을 돌려주고 Codex가 이를 자동 사용한다.

## 핵심 개념·용어 정의
- **Agent loop**: 사용자·모델·도구 사이 상호작용을 조율하는 핵심 로직. 모델이 도구 호출을 멈출 때까지 추론과 도구 실행을 반복.
- **Harness**: 모델을 감싸 agent loop와 실행 로직을 제공하는 소프트웨어. OpenAI는 "agent"와 "harness"를 거의 같은 뜻으로 씀.
- **Inference**: prompt를 토큰으로 바꿔 모델에서 출력 토큰을 샘플링하는 과정.
- **Turn / thread**: 사용자 메시지 하나에서 assistant message 하나까지. 여러 번의 추론·도구 호출을 포함.
- **Assistant message**: 턴의 종료 신호. 제어권이 사용자에게 돌아감.
- **Context window**: 한 번의 추론에서 모델이 다룰 수 있는 최대 토큰 수(입력+출력).
- **Prompt caching**: 이전 요청과 정확히 같은 접두사 부분의 계산을 재사용하는 기법.
- **Compaction**: 긴 대화를 대표 요약 항목으로 바꿔 context를 확보하는 것.
- **Sandbox / approval mode**: Codex 내장 shell 도구의 파일·네트워크 권한과 사용자 승인 규칙.
- **AGENTS.md**: Codex가 읽는 프로젝트별 지시 파일(기본 32 KiB 한도로 프로젝트 루트에서 cwd까지 탐색).

## 강연에 쓸 만한 포인트
- "Agent loop를 펼쳐 보면 결국 **점점 길어지는 하나의 prompt**"라는 관점. 스냅샷 1→2→3 그림을 순서대로 보여 주면 도구 결과가 prompt 끝에 쌓이는 과정이 직관적으로 보인다.
- 숫자·사실: 한 턴 안에서 에이전트가 수백 번 도구를 부를 수 있다는 언급, AGENTS.md 기본 32 KiB 한도, 전송량이 대화 길이에 대해 이차적으로 증가한다는 점.
- 대학원생용 포인트: prompt caching은 "정확한 접두사 일치"에만 적용되므로, 정적인 것은 앞에, 변하는 것은 뒤에 두는 설계 원칙이 에이전트 구조 전체를 규정한다.
- 비유: harness는 모델이라는 엔진에 핸들·브레이크·계기판을 붙인 차체.
- 인용(1개): "the primary output of a software agent is the code it writes" — Michael Bolin, OpenAI (2026-01-23)

## 원본 그림
- (모든 그림은 light/dark, desktop/mobile 변형이 있음. 아래는 desktop-light 기준, 괄호에 dark 버전)
- Agent loop: 사용자 입력 → 모델 추론 → 도구 호출 → 결과 관찰 → 최종 응답의 기본 순환 — https://images.ctfassets.net/kftzwdyauwt9/6eFpyKRVVEF6nNnKv7Tp1o/557f226a1f0e9c704af62a5c842a3037/oai_Unrolling_the_Codex_agent_loop_Agent_loop_desktop-light.svg (dark: https://images.ctfassets.net/kftzwdyauwt9/4ZoHTAsUlfq4eyu8D6yDSz/dba20936bb96d1e45e24a50af670fb78/oai_Unrolling_the_Codex_agent_loop_Agent_loop_desktop-dark.svg)
- Multi-turn agent loop: 여러 턴에 걸쳐 이전 대화가 다음 턴 prompt에 포함되는 구조 — https://images.ctfassets.net/kftzwdyauwt9/67Y5AbWYQzVzoHA0ncwx6X/08404ec338d7c29e8bc0cc662172e4b0/oai_Unrolling_the_Codex_agent_loop_Multi-turn_agent_loop_desktop-light.svg (dark: https://images.ctfassets.net/kftzwdyauwt9/7E3hMjLsKIV8DTg2YcChYl/be5f33a8e4d2aa1134b82d898be90ce7/oai_Unrolling_the_Codex_agent_loop_Multi-turn_agent_loop_desktop-dark.svg)
- Snapshot 1: 첫 요청에서 서버가 구성하는 prompt(system, tools, instructions, input 항목 순서) — https://images.ctfassets.net/kftzwdyauwt9/6CSnMeSFYZBLfSYRTUD7ez/13a686c9ff4ccde76e3a85df0d994c12/oai_Unrolling_the_Codex_agent_loop_Snapshot_1_desktop-light.svg (dark: https://images.ctfassets.net/kftzwdyauwt9/2CNhKAWCXaUoKJM9P2aJIV/9e5c05009e2f7500115f74e9747a3b4e/oai_Unrolling_the_Codex_agent_loop_Snapshot_1_desktop-dark.svg)
- Snapshot 2: 도구 호출 후 reasoning·function_call·function_call_output이 덧붙은 prompt(이전 prompt가 접두사) — https://images.ctfassets.net/kftzwdyauwt9/1DzRt8bt6pC273urRPUVs1/716e333051c8839cffa2f4109d94661e/oai_EngBlog_Unrolling_the_Codex_agent_loop_Snapshot_2_desktop-light.svg (dark: https://images.ctfassets.net/kftzwdyauwt9/673WKbsll8u4bAMZRosFJN/d8442bf08cb913a9b950d2ba6a9afc00/oai_EngBlog_Unrolling_the_Codex_agent_loop_Snapshot_2_desktop-dark.svg)
- Snapshot 3: 다음 턴에서 assistant message와 새 user message까지 붙어 더 길어진 prompt — https://images.ctfassets.net/kftzwdyauwt9/29dQVXimfduA5GoUR6uWhe/eb25359d27a683352878fe78c6d3e27b/oai_EngBlog_Unrolling_the_Codex_agent_loop_Snapshot_3_desktop-light.svg (dark: https://images.ctfassets.net/kftzwdyauwt9/6bSJRa6ldqZk0nvgbWYVte/34cd13125ff2bdf33d97dd62810268a2/oai_EngBlog_Unrolling_the_Codex_agent_loop_Snapshot_3_desktop-dark.svg)
- 주의: 그림 설명은 페이지의 alt 텍스트와 본문 맥락에서 추정한 것이며, 그림 파일 자체는 열어 보지 않았다. 스냅샷 1–3의 alt 텍스트는 "thought/action" 식으로 적혀 있어 본문 설명(prompt 항목 누적)과 표현이 다르다. 슬라이드에 쓰기 전 확인 권장.

## Claude Code와의 연결점 (또는 다른 도구와의 비교점)
- 구조는 Claude Code와 같다: 모델 + harness + 도구 루프, 사용자에게 제어권을 넘기는 assistant message, context 관리와 compaction. Claude Code 문서의 "agentic harness"와 이 글의 "harness"는 같은 개념이다(02번 파일).
- 지시 파일: Codex는 AGENTS.md(+AGENTS.override.md), Claude Code는 CLAUDE.md(AGENTS.md도 읽을 수 있음).
- 안전장치: Codex는 OS 수준 sandbox와 approval mode를 developer 메시지로 모델에 알려 주고, Claude Code는 permission mode와 checkpoint를 쓴다. Codex 글은 MCP 도구가 Codex sandbox 밖에 있다고 명시한다.
- 확장: 두 도구 모두 MCP 도구와 skills를 지원한다.
- 이 글은 API 요청 수준의 내부 구조를 공개한 반면, Claude Code 공식 문서는 사용자 관점의 동작 설명이 중심이라 공개 범위가 다르다. 두 제품의 내부 구현을 1:1로 비교할 1차 자료는 이번 조사에서 확인하지 못했다.
