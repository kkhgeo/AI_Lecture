# 01_context_engineering 자료 색인

- 수집일: 2026-09-29
- 주제: Claude Code를 중심으로 본 context 개념과 context engineering
- 수록: 20개 파일 (일부 파일은 같은 주제의 짧은 자료 2~5개를 묶음)
- 저작권: 각 파일은 요약·재서술 중심이며 직접 인용은 파일당 1개(15단어 미만)로 제한

## 1. 자료 목록

### A. 개념과 용어의 등장 (prompt → context)

| 파일 | 한 줄 설명 | URL |
|---|---|---|
| 01_anthropic-effective-context-engineering.md | Anthropic 공식 정의. context rot, attention budget, just-in-time, compaction·note-taking·sub-agent | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| 02_prompt-to-context-engineering-origins.md | Lütke·Karpathy 발언(2025-06), Willison, Schmid의 7요소, Anthropic 프롬프트 가이드의 "수렴" 관점 | https://simonwillison.net/2025/Jun/27/context-engineering/ , https://www.philschmid.de/context-engineering , https://claude.com/blog/best-practices-for-prompt-engineering |
| 03_lance-martin-write-select-compress-isolate.md | Write/Select/Compress/Isolate 4분류, LLM=OS·컨텍스트=RAM 비유 | https://rlancemartin.github.io/2025/06/23/context_engineering/ |

### B. 왜 필요한가: 긴 컨텍스트의 실패

| 파일 | 한 줄 설명 | URL |
|---|---|---|
| 04_dbreunig-how-contexts-fail-and-fix.md | poisoning/distraction/confusion/clash 4대 실패와 6가지 처방 | https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html |
| 05_chroma-context-rot.md | 18개 모델 실험: 입력이 길수록 단순 과제도 성능 저하 (context rot) | https://www.trychroma.com/research/context-rot |

### C. 실무자의 교훈 (에이전트 제품·코딩 워크플로)

| 파일 | 한 줄 설명 | URL |
|---|---|---|
| 06_manus-context-engineering-lessons.md | KV-cache, 도구 마스킹, 파일 시스템을 컨텍스트로, todo.md 되뇌기, 실패 기록 유지 | https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus |
| 07_humanlayer-12-factor-agents.md | 12원칙, 특히 "Own your context window" | https://github.com/humanlayer/12-factor-agents |
| 08_humanlayer-advanced-context-engineering-coding-agents.md | Research→Plan→Implement, 잦은 의도적 압축, 사용률 40~60% | https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md |
| 09_cognition-dont-build-multi-agents.md | 맥락 공유 원칙, 병렬 멀티에이전트의 위험, 단일 스레드 권장 | https://cognition.com/blog/dont-build-multi-agents |

### D. Anthropic 엔지니어링: 격리·점진적 공개·장기 과제

| 파일 | 한 줄 설명 | URL |
|---|---|---|
| 10_anthropic-multi-agent-research-system.md | orchestrator-worker, 90.2% 향상, 토큰 15배, 계획을 외부 메모리에 | https://www.anthropic.com/engineering/multi-agent-research-system |
| 11_anthropic-agent-skills.md | SKILL.md와 3단계 progressive disclosure, 오픈 표준 | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills |
| 12_anthropic-tools-and-code-execution-mcp.md | 도구도 컨텍스트다. 토큰 효율적 도구, MCP 코드 실행으로 150k→2k 토큰 | https://www.anthropic.com/engineering/writing-tools-for-agents , https://www.anthropic.com/engineering/code-execution-with-mcp |
| 13_anthropic-long-running-agent-harness.md | 여러 컨텍스트 창을 잇는 progress 파일·기능 목록·git (교대 근무 비유) | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents |

### E. Claude Code 공식 문서와 2026년 가이드

| 파일 | 한 줄 설명 | URL |
|---|---|---|
| 14_claude-code-best-practices.md | "컨텍스트가 가장 중요한 자원", 탐색→계획→구현, /clear·/compact, 실패 패턴 5가지 | https://code.claude.com/docs/en/best-practices |
| 15_claude-code-context-window-compaction.md | 세션 시작 시 로드되는 것과 토큰 수, compaction 후 살아남는 것 | https://code.claude.com/docs/en/context-window |
| 16_claude-code-memory-claudemd.md | CLAUDE.md 계층·200줄 권장·rules·auto memory(MEMORY.md 200줄/25KB) | https://code.claude.com/docs/en/memory |
| 17_claude-code-subagents.md | 별도 컨텍스트 창, 요약만 반환, 언제 쓰고 언제 쓰지 않나 | https://code.claude.com/docs/en/sub-agents |
| 18_claude-code-extension-context-costs.md | CLAUDE.md·skills·MCP·subagents·hooks의 로드 시점과 비용 비교, 도입 트리거 | https://code.claude.com/docs/en/features-overview |
| 19_claude-steering-claude-code-2026.md | 7가지 지시 위치의 비용·지속성·강제력 비교, 안티패턴 5개 (2026-06) | https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more |
| 20_claude-new-rules-context-engineering-claude5-2026.md | 시스템 프롬프트 80% 삭제에도 성능 유지, Then→Now 6대 전환 (2026-07) | https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models |

### 찾지 못함 / 제한 사항

- Tobi Lütke·Andrej Karpathy의 X 게시물 원문은 직접 열람하지 못했다(로그인 제한). 문구·날짜는 Simon Willison 글과 검색 결과로 교차 확인해 02번에 반영.
- 12-factor-agents 저장소의 정확한 최초 공개일은 확인하지 못했다(2025년으로만 표기).
- 2025-04 원본 블로그 "Claude Code: Best practices for agentic coding"은 따로 열지 않고, 이를 이관·갱신한 공식 문서(14번)를 사용했다.
- plan mode, hooks, MCP는 독립 파일로 만들지 않고 14·15·18번에 필요한 범위만 반영했다.

## 2. Context engineering 핵심 개념 지도

```
Context engineering  (추론 시점에 모델이 보는 토큰 전체를 설계·유지하는 일)
│
├─ 0. 전제: 컨텍스트는 한정 자원이다
│    ├─ Attention budget, n² 관계 (01)
│    ├─ Context rot: 길수록 성능 저하 (05)
│    └─ 실패 4유형: Poisoning / Distraction / Confusion / Clash (04)
│
├─ 1. 무엇이 컨텍스트인가 (구성요소)
│    ├─ 지시: 시스템 프롬프트(right altitude), CLAUDE.md, rules, output style (01, 16, 19)
│    ├─ 지식: 기억(memory), 검색 결과(RAG), 파일 (02, 03)
│    ├─ 도구: 도구 정의 + 도구 결과 (12)
│    └─ 기록: 대화·상태·에러 (06, 07)
│
├─ 2. 네 가지 전략 (Lance Martin 분류, 03)
│    ├─ Write  : 창 밖에 기록한다
│    │    └─ scratchpad, NOTES/PROGRESS 파일, plan 파일, auto memory, git (01, 06, 13, 16)
│    ├─ Select : 필요한 것만 들인다
│    │    ├─ Just-in-time retrieval (01)
│    │    ├─ Progressive disclosure: skills 3단계, MCP tool search, path-scoped rules (11, 12, 18, 20)
│    │    └─ Tool loadout: 도구 수 줄이기 (04, 12)
│    ├─ Compress : 줄인다
│    │    ├─ Compaction(/compact, auto-compact), tool result clearing (01, 15)
│    │    ├─ Frequent intentional compaction: Research→Plan→Implement (08)
│    │    └─ 복원 가능한 압축: 내용은 버리고 경로·URL은 남김 (06)
│    └─ Isolate : 나눠 담는다
│         ├─ Subagents / orchestrator-worker (10, 17)
│         ├─ 한계: 결정 충돌 → 읽기는 위임, 쓰기는 신중 (09)
│         └─ 컨텍스트 밖 실행: hooks, 코드 실행 환경 (12, 18)
│
├─ 3. 시간 축: 세션을 넘는 연속성
│    ├─ 세션 내: compaction 후 무엇이 재주입되나 (15)
│    └─ 세션 간: CLAUDE.md, auto memory, progress 파일, 기능 목록, git (13, 16)
│
└─ 4. 진화 방향 (2026)
     ├─ Scaffolding → Curation, 규칙 → 판단 (20)
     ├─ 지시 위치 선택: 비용 × 지속성 × 강제력 (19)
     └─ "요청(CLAUDE.md) vs 강제(hook)" 구분 (18, 19)
```

## 3. 강연 구성 흐름 제안

1. **도입 (프롬프트에서 컨텍스트로)**: Karpathy·Lütke 발언 타임라인(02)과 `/context` 라이브 화면으로 "내가 친 한 줄은 모델이 보는 것의 일부"임을 보여준다.
2. **문제 제기 (왜 더 넣으면 안 되나)**: Chroma의 context rot 그래프(05)와 Breunig의 4대 실패(04)로 "컨텍스트 창 크기 ≠ 잘 쓸 수 있는 양"을 납득시킨다.
3. **틀 제시 (Write·Select·Compress·Isolate)**: Anthropic 정의(01)와 4분류(03)를 뼈대로 삼고, Manus·HumanLayer·Cognition·Anthropic 멀티에이전트 사례(06~10)를 각 칸에 배치한다.
4. **Claude Code 실습 (전략을 기능으로)**: CLAUDE.md·rules·auto memory(Write) → skills·MCP tool search(Select) → /compact·/clear·Research→Plan→Implement(Compress) → subagents·hooks(Isolate). 문서 14~18과 context-window 시뮬레이션(15)을 사용하고, `/context` 수치 변화를 데모로 보여준다.
5. **마무리 (2026년의 원칙)**: 시스템 프롬프트 80% 삭제 사례와 Then→Now(20), 지시 위치 결정 트리(19)로 "적게, 고신호로, 제자리에"를 정리하고 청중 자신의 CLAUDE.md 다이어트 과제를 제시한다.
