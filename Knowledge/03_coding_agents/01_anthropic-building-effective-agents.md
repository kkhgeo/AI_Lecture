# Building effective agents (Anthropic의 에이전트 정의: workflow vs agent)

- **저자/기관**: Erik Schluntz, Barry Zhang / Anthropic (보조 출처: Anthropic Applied AI 팀 "Effective context engineering for AI agents"; Thariq Shihipar "Building agents with the Claude Agent SDK")
- **발행일**: 2024-12-19 (보조 출처 2건은 모두 2025-09-29) (2026-09-29 열람)
- **URL**: https://www.anthropic.com/engineering/building-effective-agents
  - 보조: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - 보조: https://claude.com/blog/building-agents-with-the-claude-agent-sdk (구 주소 anthropic.com/engineering/building-agents-with-the-claude-agent-sdk 에서 308 리다이렉트)
- **자료 유형**: 엔지니어링 블로그

## 핵심 요약
- Anthropic은 "agentic system"을 두 갈래로 나눈다. **Workflow**는 LLM과 도구가 개발자가 미리 짠 코드 경로를 따라 움직이는 시스템이고, **Agent**는 LLM이 스스로 과정과 도구 사용을 결정하며 작업 방식에 대한 통제권을 쥐는 시스템이다.
- 모든 agentic system의 기본 블록은 **augmented LLM**이다. 즉 검색(retrieval), 도구(tools), 기억(memory)이 붙은 LLM으로, 모델이 스스로 검색 질의를 만들고 도구를 고르고 무엇을 기억할지 정한다.
- Workflow 패턴 5가지: prompt chaining, routing, parallelization(sectioning/voting), orchestrator-workers, evaluator-optimizer. 복잡도가 낮은 순으로 제시된다.
- 권고의 핵심은 "가장 단순한 해법부터". 단일 LLM 호출 + 검색 + 예시로 충분하면 agent를 만들지 말라고 한다. Agent는 지연시간·비용을 늘리는 대신 성능을 얻는 트레이드오프다.
- Agent가 맞는 경우: 단계 수를 미리 예측할 수 없고 경로를 하드코딩할 수 없는 열린(open-ended) 문제, 그리고 모델의 판단을 어느 정도 신뢰할 수 있는 통제된 환경. 단점은 비용 증가와 오류 누적(compounding errors).
- Agent는 실행 중 매 단계마다 환경으로부터 "ground truth"(도구 실행 결과, 코드 실행 결과)를 받아 진행 상황을 평가하고, 필요하면 사람에게 확인을 받으며, 정지 조건(최대 반복 횟수 등)을 둔다.
- 설계 3원칙: 단순성(simplicity), 투명성(계획 단계를 드러낼 것), 그리고 **ACI(agent-computer interface)**를 도구 문서화·테스트로 공들여 설계할 것.
- 코딩은 agent가 특히 잘 맞는 분야로 제시된다. 결과를 자동 테스트로 검증할 수 있고, 테스트 결과를 피드백으로 반복 개선할 수 있으며, 문제 공간이 잘 정의되어 있기 때문이다. 글 작성 시점에 Anthropic의 구현은 PR 설명만 보고 SWE-bench Verified의 실제 GitHub 이슈를 해결했지만, 사람 리뷰는 여전히 필요하다고 명시한다.
- 이후(2025-09-29) Anthropic은 더 짧은 정의로 수렴했다. "Effective context engineering" 글은 agent를 "LLM이 도구를 루프 안에서 자율적으로 사용하는 것"으로 요약하고, Claude Agent SDK 글은 agent loop를 **gather context → take action → verify work → repeat**의 4단계로 정리한다.

## 핵심 개념·용어 정의
- **Agentic system**: workflow와 agent를 모두 포함하는 상위 개념.
- **Workflow**: LLM과 도구가 사전에 정의된 코드 경로로 오케스트레이션되는 시스템. 예측 가능성과 일관성이 강점.
- **Agent**: LLM이 자기 프로세스와 도구 사용을 동적으로 지휘하는 시스템. 유연성과 모델 주도 의사결정이 강점.
- **Augmented LLM**: retrieval, tools, memory로 확장된 LLM. 모든 agentic system의 기본 단위.
- **ACI (Agent-Computer Interface)**: 사람에게 HCI가 있듯 에이전트에게 주는 도구 인터페이스. 도구 설명, 파라미터 이름, 예시, 오류를 낼 여지를 줄이는 설계(poka-yoke)를 포함.
- **Orchestrator-workers**: 중앙 LLM이 작업을 동적으로 쪼개 worker LLM에 맡기고 결과를 합치는 패턴. 코딩처럼 수정할 파일 수를 미리 알 수 없는 작업에 적합하다고 설명됨.
- **Evaluator-optimizer**: 한 LLM이 생성하고 다른 LLM이 평가·피드백하는 반복 루프.
- **Agent loop (Claude Agent SDK 글)**: gather context → take action → verify work → repeat.

## 강연에 쓸 만한 포인트
- 도식 아이디어: "자율성 스펙트럼" 한 줄 — 단일 LLM 호출 → augmented LLM → workflow(정해진 경로) → agent(스스로 경로 결정). 오른쪽으로 갈수록 유연성↑, 비용·예측불가능성↑.
- 비유: workflow는 "레시피대로 조리하는 주방", agent는 "냉장고를 열어보고 메뉴를 스스로 정하는 요리사".
- 코딩이 agent에 잘 맞는 이유 3가지(테스트로 검증 가능, 피드백으로 반복 가능, 품질을 객관적으로 측정 가능)는 "왜 코딩 에이전트가 가장 먼저 성공했나"라는 슬라이드로 바로 쓸 수 있다.
- 메시지: "agent를 만들기 전에 더 단순한 방법이 안 되는지 먼저 확인하라"는 것이 Anthropic의 1순위 조언.
- 인용(1개): "LLMs autonomously using tools in a loop" — Anthropic, Effective context engineering for AI agents (2025-09-29)

## 원본 그림
- The augmented LLM (LLM 상자에 Retrieval·Tools·Memory가 입출력으로 연결된 그림) — https://www-cdn.anthropic.com/images/4zrzovbb/website/d3083d3f40bb2b6f477901cc9a240738d3dd1371-2401x1000.png
- Prompt chaining workflow (LLM 호출이 직렬로 이어지고 중간에 gate 검사) — https://www-cdn.anthropic.com/images/4zrzovbb/website/7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png
- Routing workflow (입력을 분류해 서로 다른 LLM 경로로 보냄) — https://www-cdn.anthropic.com/images/4zrzovbb/website/5c0c0e9fe4def0b584c04d37849941da55e5e71c-2401x1000.png
- Parallelization workflow (여러 LLM 호출을 병렬 실행 후 aggregator로 합침) — https://www-cdn.anthropic.com/images/4zrzovbb/website/406bb032ca007fd1624f261af717d70e6ca86286-2401x1000.png
- Orchestrator-workers workflow (orchestrator가 worker들에 하위작업 배분, synthesizer가 결합) — https://www-cdn.anthropic.com/images/4zrzovbb/website/8985fc683fae4780fb34eab1365ab78c7e51bc8e-2401x1000.png
- Evaluator-optimizer workflow (generator ↔ evaluator 피드백 루프) — https://www-cdn.anthropic.com/images/4zrzovbb/website/14f51e6406ccb29e695da48b17017e899a6119c7-2401x1000.png
- Autonomous agent (Human ↔ LLM Call ↔ Environment 사이 action/feedback 루프, stop 조건) — https://www-cdn.anthropic.com/images/4zrzovbb/website/58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.png
- High-level flow of a coding agent (사람 질의 → 명확화 → 코드베이스 탐색·수정·테스트 반복 → 완료 보고의 흐름; 강연용으로 가장 유용) — https://www-cdn.anthropic.com/images/4zrzovbb/website/4b9a1f4eb63d5962a6e1746ac26bbc857cf3474f-2400x1666.png
- (보조) Agent feedback loop — Claude Agent SDK 글의 gather context → take action → verify work → repeat 순환도 — https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4b28db0e40fd93e63875_image.png
- (보조) Prompt engineering vs. context engineering 비교도 — https://www-cdn.anthropic.com/images/4zrzovbb/website/faa261102e46c7f090a2402a49000ffae18c5dd6-2292x1290.png
- 참고: 페이지 안에서는 위 URL들이 `/_next/image?url=...` 형태로 감싸져 있음. 직접 URL은 URL 인코딩을 풀어 얻은 것이며 개별 파일 접근 여부는 확인하지 않음.

## Claude Code와의 연결점 (또는 다른 도구와의 비교점)
- Claude Code는 이 글의 분류상 "workflow"가 아니라 "agent"에 해당한다. 어떤 파일을 읽고 어떤 명령을 실행할지 모델이 매 단계 결정한다.
- Claude Agent SDK 글의 gather context → take action → verify work 루프는 Claude Code 공식 문서의 agentic loop 3단계와 같은 틀이다(02번 파일 참조). SDK 글은 Claude Code를 만든 인프라를 일반 에이전트용으로 공개한 것이라고 설명한다.
- 글이 강조한 ACI(도구 설계)와 "사람의 체크포인트"는 Claude Code의 도구 체계, 권한 모드, 체크포인트 기능으로 구체화되어 있다.
- 글의 orchestrator-workers 패턴은 Claude Code의 subagent 위임 구조와 개념적으로 겹친다(다만 원문이 Claude Code를 이 패턴의 구현이라고 명시하지는 않음).
