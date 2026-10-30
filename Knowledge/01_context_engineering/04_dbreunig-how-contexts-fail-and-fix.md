# How Long Contexts Fail / How to Fix Your Context

- **저자/기관**: Drew Breunig (개인 블로그 dbreunig.com)
- **발행일**: 2025-06-22 (실패 편), 2025-06-26 (해결 편)
- **URL**: https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html , https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html
- **자료 유형**: 블로그 (연구 사례를 엮은 실무 분석)

## 핵심 요약

- 100만 토큰급 긴 컨텍스트가 나오면서 "다 넣으면 된다"는 기대가 생겼지만, 긴 컨텍스트는 그 자체로 새로운 실패를 만든다는 주장이다.
- 실패를 네 유형으로 명명했다: **Context Poisoning(오염)**, **Context Distraction(주의 분산)**, **Context Confusion(혼동)**, **Context Clash(충돌)**. 이 명명이 LangChain·Anthropic 등 이후 글에서 표준처럼 인용된다.
- 후속 글에서는 여섯 가지 처방을 제시한다: **RAG**, **Tool Loadout**, **Context Quarantine**, **Context Pruning**, **Context Summarization**, **Context Offloading**.
- 핵심 태도: 컨텍스트를 잡동사니 서랍처럼 쓰지 말 것. 들어간 모든 것이 출력에 영향을 준다.

## 핵심 개념·용어 정의

**네 가지 실패 유형과 근거 사례**

| 유형 | 정의 | 근거 |
|---|---|---|
| Poisoning | 환각·오류가 컨텍스트에 들어가 반복 참조되며 굳어짐 | Gemini 2.5의 포켓몬 플레이: 목표 섹션이 잘못된 정보로 오염되면 불가능한 목표에 집착 |
| Distraction | 컨텍스트가 너무 길어 모델이 학습된 지식보다 기록에 과의존 | Gemini 2.5는 약 10만 토큰 넘어서 새 계획보다 과거 행동 반복 경향. Databricks 연구에서 Llama 3.1 405B는 약 32k 토큰부터 정확도 하락 |
| Confusion | 불필요한 정보(특히 많은 도구 정의)가 응답 품질을 떨어뜨림 | Berkeley Function-Calling Leaderboard: 도구가 많을수록 성능 하락. 양자화된 Llama 3.1 8B는 도구 46개에서 실패, 19개에서 성공 |
| Clash | 누적된 정보끼리 모순되어 추론이 탈선 | Microsoft·Salesforce 연구: 정보를 여러 턴에 나눠(sharded) 주면 평균 39% 성능 하락. o3는 98.1→64.1 |

**여섯 가지 처방**

| 처방 | 뜻 | 근거 수치 |
|---|---|---|
| RAG | 관련 정보만 선택적으로 넣기 | - |
| Tool Loadout | 과제에 맞는 도구 정의만 골라 싣기 | 약 30개 이상에서 혼동. 도구 선택에 RAG 적용 시 Llama 3.1 8B 정확도 최대 44% 향상 |
| Context Quarantine | 과제를 별도 스레드·컨텍스트로 격리 | Anthropic 멀티에이전트가 단일 에이전트 대비 90.2% 우수 |
| Context Pruning | 무관한 정보 잘라내기 | Provence가 위키 문서를 95% 줄이며 필요한 내용 유지 |
| Context Summarization | 누적 컨텍스트를 요약 | 10만 토큰 이후 반복 행동 경향 대응 |
| Context Offloading | 외부 scratchpad 등에 저장 | Anthropic "think" 도구 + 도메인 프롬프트로 특화 벤치마크 54% 향상 |

## 강연에 쓸 만한 포인트

- **4칸 경고판 슬라이드**: 독(poison), 산만(distraction), 혼란(confusion), 충돌(clash) 아이콘. 청중이 자기 경험과 바로 연결한다(예: "AI가 한 번 틀린 가정을 끝까지 고집한 적 있나요?" = poisoning).
- **실패 ↔ 처방 매핑 도식**: Poisoning→Quarantine/Pruning, Distraction→Summarization/Offloading, Confusion→Tool Loadout/RAG, Clash→Pruning/새 세션.
- **수치 한 장**: "도구 46개면 실패, 19개면 성공", "나눠서 말하면 39% 하락". 짧고 강렬.
- 인용(1개): "a junk drawer" — 컨텍스트를 잡동사니 서랍처럼 다루지 말라는 비유 (Drew Breunig, 2025-06-26)

## Claude Code와의 연결점

- **Poisoning/Clash**: 잘못된 접근으로 두 번 이상 교정했다면 `/clear` 후 배운 점을 반영한 새 프롬프트로 시작(공식 best practices의 "correcting over and over" 실패 패턴과 동일). `/rewind`로 오염 이전 시점으로 되돌리기.
- **Distraction**: `/compact <초점>`, 작업 전환 시 `/clear`.
- **Confusion**: MCP 서버를 필요한 것만 연결하고 tool search(지연 로드)를 유지. subagent 정의에서 `tools:`로 도구 제한. skill은 `disable-model-invocation: true`로 설명 노출 최소화.
- **Quarantine**: subagent, `context: fork` skill.
- **Offloading**: plan 파일, `NOTES.md`, auto memory.
- 데모: CLAUDE.md에 서로 모순되는 규칙 두 개(예: "주석을 많이 달 것" / "주석 금지")를 넣고 결과 변동을 보여주는 "Clash 체험".
