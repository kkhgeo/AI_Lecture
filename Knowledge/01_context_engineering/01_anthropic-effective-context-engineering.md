# Effective context engineering for AI agents

- **저자/기관**: Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield (Anthropic Applied AI 팀)
- **발행일**: 2025-09-29
- **URL**: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **자료 유형**: 블로그 (Anthropic 공식 엔지니어링 블로그)

## 핵심 요약

- Anthropic은 context engineering을 prompt engineering의 "다음 단계"로 규정한다. prompt engineering이 지시문을 잘 쓰는 일이라면, context engineering은 추론 시점에 모델에 들어가는 **토큰 전체(시스템 지시, 도구, 외부 데이터, 대화 기록)를 선별하고 유지하는 일**이다.
- 에이전트는 여러 턴에 걸쳐 도구를 호출하며 계속 새 정보를 만들어내므로, "무엇을 넣을지"를 매 턴 다시 결정하는 반복적 큐레이션이 필요하다.
- 컨텍스트가 길어질수록 정확도가 떨어지는 **context rot** 현상이 있고, 모델에는 사람의 작업 기억처럼 유한한 **attention budget**이 있다. 트랜스포머는 n개 토큰 사이에 n² 쌍의 관계를 다뤄야 하므로 길이가 늘수록 주의가 얇게 퍼진다.
- 따라서 목표는 원하는 결과를 낼 확률을 최대화하는 "가장 작은 고신호(high-signal) 토큰 집합"을 찾는 것이다.
- 구성요소별 지침: 시스템 프롬프트는 "적절한 고도(right altitude)", 도구는 기능 중복 없이 자기완결적으로, 예시는 엣지 케이스 나열 대신 다양하고 대표적인 몇 개로.
- 검색 전략: 모든 데이터를 미리 넣지 않고 파일 경로·URL 같은 가벼운 식별자만 들고 있다가 필요할 때 도구로 불러오는 **just-in-time retrieval**, 탐색하며 점진적으로 맥락을 발견하는 **progressive disclosure**, 둘을 섞은 **hybrid** 전략.
- 장기 과제(long-horizon)를 위한 세 기법: **compaction(압축)**, **structured note-taking(구조화된 메모)**, **sub-agent architecture(하위 에이전트)**.

## 핵심 개념·용어 정의

| 용어 | 의미 |
|---|---|
| Context | 모델 추론 시 입력되는 토큰의 총합 (system prompt, tools, MCP, 외부 데이터, message history) |
| Context engineering | 그 토큰 집합을 에이전트 수명 전체에 걸쳐 최적으로 구성·유지하는 전략 |
| Context rot | 컨텍스트 토큰 수가 늘수록 정보 회상(recall) 정확도가 떨어지는 현상 |
| Attention budget | 모델이 쓸 수 있는 주의력의 한정된 예산. 토큰 하나하나가 이를 소모 |
| Right altitude | 경직된 if-else식 하드코딩과 모호한 지시 사이의 적정 수준의 시스템 프롬프트 |
| Just-in-time retrieval | 식별자(경로, 쿼리, 링크)만 유지하고 실행 중 도구로 필요한 데이터만 로드 |
| Progressive disclosure | 에이전트가 탐색을 통해 층층이 필요한 맥락을 발견하는 방식 |
| Compaction | 한계에 가까운 대화를 요약해 새 컨텍스트로 다시 시작. 가장 가벼운 형태는 tool result clearing |
| Structured note-taking | 컨텍스트 창 밖(파일 등)에 메모를 쓰고 나중에 다시 읽어오는 agentic memory |
| Sub-agent architecture | 하위 에이전트가 깨끗한 창에서 깊게 탐색한 뒤 요약(약 1,000~2,000 토큰)만 반환 |

## 강연에 쓸 만한 포인트

- **비유**: 사람의 작업 기억(working memory). 책상 위에 모든 서류를 쌓지 않고 서랍 위치만 기억했다가 필요할 때 꺼낸다(just-in-time).
- **도식**: "Prompt engineering(한 번의 지시문 작성)" 대 "Context engineering(매 턴 반복되는 큐레이션 루프)". 가운데 '가능한 컨텍스트 후보군'이 있고, 매 턴 필터를 거쳐 창에 들어가는 구조.
- **시스템 프롬프트 스펙트럼 그림**: [너무 구체적/취약] ─ [적정 고도] ─ [너무 모호] 세 칸.
- **장기 과제 3종 세트 표**: compaction(대화 흐름 유지가 중요한 작업) / note-taking(이정표가 분명한 반복 개발) / sub-agent(병렬 탐색이 이득인 연구형 작업).
- **사례**: Claude가 포켓몬을 플레이하며 수천 스텝 동안 메모 파일에 목표·지도·전략을 기록해, 컨텍스트가 리셋돼도 이어간 예.
- **수치**: 하위 에이전트는 수만 토큰을 탐색하고 1,000~2,000 토큰의 요약만 돌려준다.
- **한 줄 메시지**: 컨텍스트는 "넣을수록 좋은 것"이 아니라 수익이 체감하는 한정 자원이다.

## Claude Code와의 연결점

- 이 글이 Claude Code를 hybrid 전략의 예로 든다: `CLAUDE.md`는 처음부터 로드, 파일은 `grep`·`glob` 같은 도구로 필요할 때 읽음.
- Compaction: Claude Code는 대화 기록을 요약해 아키텍처 결정·미해결 버그는 남기고 중복 도구 출력은 버린 뒤, 최근 접근한 파일 5개와 함께 이어간다고 설명한다. 실습은 `/compact <보존할 초점>` 실행 전후를 `/context`로 비교.
- Structured note-taking: `NOTES.md`/`PROGRESS.md`에 진행 상황을 적게 하고, `/clear` 후 새 세션에서 그 파일만 읽혀 이어가기. auto memory(`MEMORY.md`)도 같은 원리.
- Sub-agent: "하위 에이전트로 X를 조사해줘"라고 요청해 메인 컨텍스트가 거의 늘지 않는 것을 `/context`로 확인.
