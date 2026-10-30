# Advanced Context Engineering for Coding Agents (Frequent Intentional Compaction)

- **저자/기관**: Dex Horthy (HumanLayer)
- **발행일**: 2025-08 (2025-08-20 Y Combinator/AI 행사 발표를 글로 정리)
- **URL**: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md
- **자료 유형**: 공개 문서 (발표 기반 기술 에세이, GitHub)

## 핵심 요약

- 문제의식: Stanford 연구 등은 AI 코딩 도구가 새 프로젝트(greenfield)에서는 잘하지만 복잡한 기존 코드베이스(brownfield)에서는 재작업을 부르는 "slop"을 만들어 생산성을 오히려 떨어뜨릴 수 있다고 보고한다.
- 해법은 더 좋은 모델이 아니라 **워크플로 전체를 컨텍스트 관리 중심으로 재설계**하는 것이다. 이를 **Frequent Intentional Compaction(잦고 의도적인 압축)**이라 부른다.
- 작업을 **Research → Plan → Implement** 세 단계로 나누고, 각 단계의 결과를 마크다운 산출물(research 문서, plan 문서)로 압축해 다음 단계의 새 컨텍스트에 넘긴다. 컨텍스트 사용률은 대략 **40~60%**를 유지하도록 한다.
- 컨텍스트 품질의 우선순위: 가장 나쁜 것은 **틀린 정보**, 다음은 **빠진 정보**, 그다음이 **잡음(과다 정보)**. 즉 정확성 > 완전성 > 크기.
- subagent는 역할 놀이가 아니라 **컨텍스트를 깨끗하게 유지하는 도구**로 쓴다: 검색·요약을 대신하고 결과만 돌려준다.
- 사람의 검토는 가장 레버리지가 큰 곳, 즉 **연구와 계획 단계**에 집중해야 한다. 잘못된 연구 한 줄이 수천 줄의 잘못된 코드로 번지기 때문이다.

## 핵심 개념·용어 정의

| 용어 | 뜻 |
|---|---|
| Intentional compaction | 컨텍스트가 넘치기 전에 사람이 의도적으로 진행 상황을 파일로 정리하고 새 세션을 시작하는 습관 |
| Frequent intentional compaction (FIC) | 이를 워크플로 전체에 걸쳐 단계마다 반복하는 방식 |
| Research / Plan / Implement | 이해(파일·흐름 파악) → 구체적 수정 계획(파일별 변경, 검증 방법) → 단계별 구현 및 상태 재압축 |
| Context utilization target | 40~60% 정도로 여유를 두고 운영 |
| Mental alignment | 팀이 수천 줄 생성 코드를 다 읽을 수 없으니, spec·plan을 읽고 합의하는 것이 새로운 코드 리뷰 |
| Specs as the real code | 계획·명세 문서가 사실상 핵심 산출물이 된다는 관점 |

## 강연에 쓸 만한 포인트

- **레버리지 피라미드 도식**: 잘못된 연구 1줄 → 잘못된 계획 수십~수백 줄 → 잘못된 코드 수천 줄. 사람의 검토를 위쪽에 두라는 메시지.
- **3단계 파이프라인 그림**: 각 단계 사이에 "압축된 문서"라는 병목(필터)이 있고, 매 단계는 깨끗한 새 컨텍스트에서 시작.
- **수치/사례**: 30만 줄 Rust 코드베이스(BAML)에서 Rust 비전문가가 몇 시간 만에 버그 수정 PR을 내고 다음 날 병합, 7시간에 약 3.5만 줄 규모 기능 추가(시니어 기준 기능당 3~5일 추정). 3인 팀이 Opus 사용료 월 약 1.2만 달러.
- **정직한 한계**: 마법 프롬프트는 없다. 저자가 잘못된 연구 결과를 직접 읽고 거절한 뒤 다시 연구시킨 과정이 성공의 핵심이었다.
- 인용(1개): "A bad line of research could lead to thousands of bad lines of code" (Dex Horthy, 2025) — 14단어

## Claude Code와의 연결점

- 저자 팀이 Claude Code 기반으로 이 워크플로를 운영하며, research/plan/implement용 slash command·subagent를 공개했다.
- 공식 기능으로 그대로 재현 가능:
  - **Research**: plan mode(`Shift+Tab`) 또는 Explore subagent로 읽기 전용 탐색 → 결과를 `research.md`로 저장
  - **Plan**: plan mode에서 계획 작성, `Ctrl+G`로 편집 → `plan.md`로 저장 (plan은 compaction 후에도 디스크에서 재주입됨)
  - **Implement**: `/clear` 후 `@plan.md`만 참조해 구현, 단계마다 진행 상황 갱신
- `/context`로 사용률 40~60% 유지 확인, 넘으면 진행 상황을 파일로 정리하고 새 세션.
- 공식 best practices의 "Explore → Plan → Implement → Commit" 4단계와 거의 같은 구조임을 보여주면 설득력이 높다.
