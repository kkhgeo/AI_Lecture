# Context Engineering for Agents (Write · Select · Compress · Isolate)

- **저자/기관**: Lance Martin (LangChain). 동일 내용이 LangChain 공식 블로그에도 게재
- **발행일**: 2025-06-23 (개인 블로그) / 2025-07-02 (LangChain 블로그)
- **URL**: https://rlancemartin.github.io/2025/06/23/context_engineering/ , https://www.langchain.com/blog/context-engineering-for-agents
- **자료 유형**: 블로그 (실무자 에세이)

## 핵심 요약

- Karpathy의 "LLM은 새로운 운영체제" 비유를 빌려, LLM을 CPU로, 컨텍스트 창을 용량이 제한된 **RAM**으로 본다. 운영체제가 RAM에 무엇을 올릴지 관리하듯, context engineering은 창에 무엇을 올릴지 관리하는 일이다.
- 관리해야 할 컨텍스트는 세 종류다: **지시(instructions)**(프롬프트, 메모리, few-shot, 도구 설명), **지식(knowledge)**(사실, 기억), **도구(tools)**(도구 호출 결과 피드백).
- 에이전트는 긴 작업과 많은 도구 호출로 컨텍스트가 계속 불어나 비용·지연·성능 저하가 생긴다. Drew Breunig의 네 가지 실패 유형(poisoning, distraction, confusion, clash)을 인용한다.
- 이를 다루는 전략을 네 범주로 분류했다: **Write(쓰기)**, **Select(고르기)**, **Compress(압축)**, **Isolate(격리)**. 이 4분류가 이후 업계 표준 틀로 널리 인용되었다.
- 개인 블로그판은 Claude Code를 예로 든다: CLAUDE.md는 절차적 기억(procedural memory), auto-compact는 컨텍스트 95% 도달 시 작동(당시 기준).

## 핵심 개념·용어 정의

| 전략 | 뜻 | 예시 |
|---|---|---|
| **Write** | 컨텍스트 창 밖에 저장 | scratchpad(작업 중 메모), 장기 memory(세션 간 기억, Reflexion·Generative Agents 방식) |
| **Select** | 필요한 것만 창으로 끌어오기 | 메모리 검색(episodic/procedural/semantic), 도구 설명에 RAG 적용, 코드 검색(grep, AST, 임베딩, 재순위화) |
| **Compress** | 필요한 토큰만 남기기 | 요약(summarization, 예: auto-compact), 트리밍(trimming, 오래된 메시지 제거, Provence 같은 학습된 pruner) |
| **Isolate** | 컨텍스트를 나눠 담기 | 멀티에이전트(각자 창), 샌드박스(무거운 객체는 실행 환경에 보관), state 스키마로 필드 분리 |

- **Memory 3유형**: episodic(과거 사례), procedural(지시·규칙), semantic(사실).
- 인용된 수치: 도구 설명에 RAG를 적용하면 도구 선택 정확도가 약 3배 개선(인용 논문 기준), Anthropic 멀티에이전트는 채팅 대비 최대 약 15배 토큰 사용.

## 강연에 쓸 만한 포인트

- **가장 쓰기 좋은 도식**: 2×2 또는 4칸 그림. 가운데 "Context Window(RAM)", 바깥에 Write(→디스크로 내보내기), Select(←디스크에서 불러오기), Compress(창 안에서 줄이기), Isolate(창을 여러 개로 나누기).
- **OS 비유**: CPU=모델, RAM=컨텍스트 창, 디스크=파일시스템·메모리 저장소, 프로세스 분리=subagent. 비개발자 청중에게도 직관적.
- **강연 구조 뼈대로 활용**: 이후 모든 사례(Claude Code 기능, Manus, HumanLayer)를 이 네 칸에 분류해 넣으면 강연 전체의 지도가 된다.
- **Memory의 위험**: Simon Willison 사례(ChatGPT가 원치 않게 위치 정보를 이미지 생성에 끌어온 일)로 "잘못된 select"가 사용자 신뢰를 해칠 수 있음을 보여준다.

## Claude Code와의 연결점

| 전략 | Claude Code 기능 |
|---|---|
| Write | `CLAUDE.md`, auto memory(`MEMORY.md`), plan 파일, `PROGRESS.md` 같은 노트 파일, git 커밋 |
| Select | `@파일` 참조, Read/Grep/Glob just-in-time 검색, skills의 on-demand 로드, MCP tool search(도구 스키마 지연 로드), path-scoped rules |
| Compress | 자동 compaction, `/compact <초점>`, `/rewind`의 "Summarize from here" |
| Isolate | subagents(Explore/Plan/custom), `context: fork` skill, git worktree 병렬 세션, hooks(컨텍스트 밖에서 실행) |

- 데모: 같은 과제를 (a) 메인 세션에서 직접 조사 (b) subagent에 위임, 두 경우 `/context` 수치 비교 → Isolate 효과 체감.
