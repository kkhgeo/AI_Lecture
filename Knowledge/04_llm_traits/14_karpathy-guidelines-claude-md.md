# Karpathy 지침 CLAUDE.md (andrej-karpathy-skills): LLM 코딩의 함정과 네 가지 행동 원칙

- **저자/기관**: 원 관찰 Andrej Karpathy(X 게시물), 지침 파일 작성 Forrest Chang(GitHub forrestchang/andrej-karpathy-skills, 현재 multica-ai/andrej-karpathy-skills)
- **발행일**: Karpathy 게시물 2026-01-26(검색 결과 기준, x.com 원문 미열람) / 지침 파일 2026-01 말 / "10개 규칙" 확장본 2026-06-28 유포(작성자 미확인) (2026-10-01 열람)
- **URL**:
  - https://x.com/karpathy/status/2015883857489522876
  - https://github.com/multica-ai/andrej-karpathy-skills (CLAUDE.md 원문 확인)
  - https://www.techtimes.com/articles/319214/20260628/karpathy-claudemd-grows-ten-rules-new-self-check-protocol-ai-coding-loops.htm
- **자료 유형**: 게시물, GitHub 저장소, 기사

## 핵심 요약
- Karpathy는 약 두 달 사이 "손 코딩·자동완성 80%, 에이전트 20%"에서 "에이전트 80%, 수정·손질 20%"로 바뀌었다고 쓰고, 그 과정에서 본 LLM 코딩의 함정을 정리했다(2026-01-26, 검색 결과 요약 기준).
- 함정 1, **말없는 잘못된 가정**: 모델이 사용자 대신 잘못된 가정을 하고 확인 없이 밀고 나간다. 혼란을 관리하지 않고, 질문하지 않고, 모순을 드러내지 않고, 선택지를 제시하지 않고, 반대해야 할 때 반대하지 않는다.
- 함정 2, **과잉 복잡화**: 코드와 API를 지나치게 복잡하게 만들고, 추상화를 부풀리고, 죽은 코드를 정리하지 않는다. 100줄이면 될 일을 1000줄로 만든다.
- 함정 3, **관련 없는 수정**: 요청과 무관한 코드·주석을 바꾸거나 지운다(지침 파일이 정리한 세 번째 불만).
- 이 관찰을 Forrest Chang이 약 60줄짜리 CLAUDE.md로 옮겼고, GitHub 트렌딩 1위에 올랐다. Karpathy가 직접 쓴 파일은 아니다.
- 네 가지 원칙(원문 확인):
  1. **Think Before Coding** — 가정하지 말고, 혼란을 숨기지 말고, 선택지를 드러내라. 가정을 명시하고, 불확실하면 묻고, 해석이 여럿이면 말없이 고르지 말고 제시하라. 더 단순한 길이 있으면 말하고 필요하면 반대하라.
  2. **Simplicity First** — 문제를 푸는 최소한의 코드. 요청하지 않은 기능·추상화·설정 가능성·불가능한 경우의 오류 처리를 넣지 않는다. 200줄이 50줄로 될 수 있으면 다시 쓴다.
  3. **Surgical Changes** — 꼭 필요한 곳만 고치고, 자기가 만든 흔적만 치운다. 바뀐 모든 줄은 사용자 요청으로 이어져야 한다.
  4. **Goal-Driven Execution** — 성공 기준을 정하고 검증될 때까지 반복한다. "검증 추가"는 "잘못된 입력에 대한 테스트를 쓰고 통과시키기"로 바꾼다.
- 파일 머리말: 이 지침은 속도보다 신중함 쪽으로 기울어 있으며, 사소한 작업에는 판단을 쓰라고 적었다.
- 효과 수치("실수 41%→11%", "정확도 94%")는 블로그 주장일 뿐 측정 방법이 확인되지 않음 — 인용하지 않는다.
- 2026-06-28에는 검증·디버깅·의존성·소통·흔한 실패 유형을 더한 "10개 규칙" 판이 Karpathy 이름으로 돌았으나 Karpathy가 확인하지 않았다(TechTimes).

## 04_llm_traits와의 대응
| Karpathy의 함정 | 이 폴더의 행동 특성 | 지침 원칙 |
|---|---|---|
| 말없는 잘못된 가정, 반대하지 않음 | 아첨(01), 환각(03) | 1. Think Before Coding |
| 과잉 복잡화 | 과잉 열의(07) | 2. Simplicity First |
| 관련 없는 수정 | 과잉 열의·범위 확장(07) | 3. Surgical Changes |
| 검증 없는 완료 | 조기 완료(06), 보상 해킹(05) | 4. Goal-Driven Execution |

## 강연에 쓸 만한 포인트
- 메시지: 행동 특성은 막연한 경고가 아니라, **지침 파일 한 장으로 다룰 수 있는 대상**이다(컨텍스트 파트의 "쓰기(Write)", CLAUDE.md와 연결).
- 대학원생용 번역: 1 "모르면 묻게 하라", 2 "작게 만들게 하라", 3 "요청한 곳만 고치게 하라", 4 "끝의 기준을 먼저 정하라".
- 인용(1개): "Touch only what you must." (andrej-karpathy-skills CLAUDE.md)
