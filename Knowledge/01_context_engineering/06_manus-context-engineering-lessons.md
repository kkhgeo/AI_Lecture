# Context Engineering for AI Agents: Lessons from Building Manus

- **저자/기관**: Yichao "Peak" Ji (Manus 공동창업자)
- **발행일**: 2025-07-18
- **URL**: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- **자료 유형**: 블로그 (제품 개발 회고)

## 핵심 요약

- Manus 팀은 모델을 직접 학습시키는 대신 **context engineering에 베팅**했다. 모델이 발전하면 그 위에 떠오르는 배처럼 함께 좋아지기 때문이다. 에이전트 프레임워크를 네 번 갈아엎으며 얻은 교훈을 정리했다.
- 여섯 가지 교훈: ① KV-cache 중심 설계 ② 도구를 제거하지 말고 마스킹 ③ 파일 시스템을 컨텍스트로 사용 ④ 되뇌기(recitation)로 주의 조작 ⑤ 실패 기록을 남겨두기 ⑥ few-shot 패턴에 갇히지 않기.
- 에이전트는 입력 대 출력 토큰 비율이 약 **100:1**로 입력이 압도적이라, 캐시 적중률이 비용과 지연을 좌우한다. Claude Sonnet 기준 캐시된 입력은 미캐시 대비 **10배** 저렴(0.30 vs 3 USD/MTok).
- 전형적 과제는 평균 **약 50회 도구 호출**이 필요하다. 그래서 목표를 잊지 않도록 `todo.md`를 계속 갱신하며 목표를 컨텍스트 끝(최근 위치)으로 다시 끌어온다.

## 핵심 개념·용어 정의

| 교훈 | 설명 |
|---|---|
| KV-cache hit rate | 프롬프트 앞부분(prefix)을 안정적으로 유지하고, 컨텍스트는 추가만(append-only), 직렬화는 결정적으로. 시스템 프롬프트 맨 앞에 초 단위 타임스탬프를 넣는 것 같은 실수가 캐시를 깬다 |
| Mask, don't remove | 도구를 중간에 빼면 캐시가 깨지고 과거 기록과 모순이 생긴다. 대신 디코딩 단계에서 선택 가능한 도구를 마스킹 |
| File system as context | 파일 시스템을 무제한·영속적 외부 기억으로 사용. 웹페이지 본문은 버려도 URL은 남기는 식의 **복원 가능한 압축** |
| Recitation | todo 목록을 반복 갱신해 목표를 최근 주의 범위에 둠 → lost-in-the-middle와 목표 표류 방지 |
| Keep the wrong stuff in | 에러와 실패한 행동을 지우지 않고 남겨두면 모델이 암묵적으로 같은 실수를 피함 |
| Don't get few-shotted | 비슷한 행동-관찰 쌍이 반복되면 모델이 패턴을 흉내 내며 표류. 직렬화 형식에 약간의 변주를 줌 |

## 강연에 쓸 만한 포인트

- **"배와 밀물" 비유**: 모델 학습은 해저에 박힌 기둥, context engineering은 밀물(모델 발전)에 따라 떠오르는 배.
- **숫자 3종**: 입력:출력 = 100:1, 캐시 유무 비용 10배 차이, 과제당 도구 호출 약 50회.
- **todo.md 데모**: 긴 작업에서 에이전트가 스스로 체크리스트를 갱신하는 모습. Claude Code의 할 일(Todo) 목록과 동일한 발상.
- **반직관 포인트**: "실패를 지우지 말라" — 사람은 실수를 감추고 싶지만, 에이전트에게는 실수 기록이 학습 신호다. 다만 HumanLayer(08번)는 반복 교정으로 오염된 컨텍스트는 새로 시작하라고 하므로, 두 입장의 차이를 토론거리로 제시 가능.
- 인용(1개): 교훈 제목 "Use the File System as Context" (Manus 블로그, 2025-07-18)

## Claude Code와의 연결점

- **KV-cache**: Claude Code 문서의 prompt caching 항목과 연결. 세션 중 도구·MCP 구성을 자주 바꾸면 캐시된 prefix가 무효화된다는 점을 설명.
- **Mask, don't remove**: Claude Code는 MCP 도구 이름만 먼저 싣고 스키마는 tool search로 지연 로드한다. 또 subagent의 `tools:`/`disallowedTools:`로 권한 범위를 제한.
- **File system as context**: Claude Code 자체가 파일 시스템 기반 에이전트. 조사 결과를 파일로 저장하고 경로만 대화에 남기는 습관.
- **Recitation**: Claude Code의 TodoWrite(할 일 목록) 기능, plan mode의 계획 파일(compaction 후 디스크에서 재주입됨).
- **Keep errors in**: 테스트 실패 로그를 그대로 보여주고 수정하게 하는 검증 루프(best practices의 "give Claude a way to verify").
