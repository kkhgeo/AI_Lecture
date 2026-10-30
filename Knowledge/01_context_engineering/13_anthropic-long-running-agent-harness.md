# Effective harnesses for long-running agents

- **저자/기관**: Justin Young (Anthropic), 기여자 다수 (David Hershey, Prithvi Rajasekaran, Jeremy Hadfield 외)
- **발행일**: 2025-11-26
- **URL**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **자료 유형**: 블로그 (Anthropic 공식 엔지니어링 블로그)

## 핵심 요약

- 여러 컨텍스트 창에 걸친 장기 과제에서 에이전트는 매 세션을 **기억 없이** 시작한다. 교대 근무 엔지니어가 이전 교대의 기억 없이 출근하는 상황과 같다.
- compaction이 있어도 충분하지 않았다. Opus 4.5조차 상위 수준 지시만으로는 완성도 높은 웹앱을 만들지 못했다. 실패 양상은 두 가지: ① 한 창에서 너무 많은 것을 하려다 반쯤 만든 상태로 끝남 ② 다음 세션이 진행 상황을 보고 "끝났다"고 오판.
- 해법은 두 종류의 에이전트 프롬프트다.
  - **Initializer agent**(첫 세션): 개발 서버 실행 스크립트 `init.sh`, 진행 기록 `claude-progress.txt`, 초기 git 커밋, 200개 이상의 기능을 담은 **JSON 기능 목록**(각 항목 `passes: false`)을 만든다.
  - **Coding agent**(이후 세션): 매번 git 로그와 진행 파일을 읽고, 가장 우선인 미완료 기능 **하나만** 구현·테스트·커밋하고 진행 파일을 갱신한다.
- 기능 목록을 마크다운이 아닌 JSON으로 둔 이유: 모델이 JSON을 부적절하게 고쳐 쓸 가능성이 더 낮았다.
- 브라우저 자동화(Puppeteer MCP)로 사용자처럼 끝단 테스트를 하게 하자 코드만 봐서는 안 보이는 버그를 잡았다.
- 결론: compaction은 기계적 압축일 뿐이고, **구조화된 외부 산출물(진행 파일, 기능 목록, git 기록)**이 세션 간 맥락의 연속성을 만든다.

## 핵심 개념·용어 정의

- **Harness**: 모델을 둘러싸고 도구·컨텍스트·세션을 관리하는 실행 틀(Claude Code, Agent SDK 등). Claude Code 문서도 자신을 "agentic harness"라고 부른다.
- **Initializer / Coding agent**: 같은 도구·하네스에 다른 초기 프롬프트만 준 두 역할.
- **Incremental progress**: 한 세션에 한 기능. 깨끗한 상태로 끝내기(clean state).
- **세션 시작 루틴**: 작업 디렉터리 확인 → git 로그·진행 파일 읽기 → 다음 기능 선택 → 기본 동작 테스트 후 새 작업 시작.

## 강연에 쓸 만한 포인트

- **"교대 근무 엔지니어" 비유**: 인수인계 노트(progress 파일), 업무 목록(feature list), 작업 일지(git log)가 없으면 매 교대가 처음부터 다시 파악해야 한다.
- **실패와 대응 표**: 조기 완료 선언 → 기능 목록 + 테스트 후에만 통과 표시 / 엉망인 상태 인계 → 시작 시 로그 확인, 끝날 때 커밋 / 실행 방법 모름 → `init.sh`.
- **도식**: 세션1(Initializer) → [파일: features.json, progress.txt, git] → 세션2, 3, 4…(Coding). 각 세션은 새 컨텍스트, 파일이 다리 역할.
- **메시지**: 장기 작업에서 컨텍스트의 진짜 저장소는 모델의 창이 아니라 **파일 시스템과 git**이다.
- 인용(1개): 새 교대 엔지니어는 "no memory of what happened on the previous shift" (Anthropic, 2025-11-26)

## Claude Code와의 연결점

- 그대로 실습 가능: 첫 세션에서 "기능 목록 JSON, `claude-progress.txt`, `init.sh`를 만들고 커밋해줘" → `/clear` → "진행 파일과 git log를 읽고 다음 기능 하나만 구현·테스트·커밋해줘"를 반복.
- `CLAUDE.md`에 "세션 시작 시 progress 파일과 git log를 먼저 읽을 것"을 넣어 루틴 고정.
- 검증 강제: Stop hook이나 `/goal`로 테스트 통과 전 종료를 막기, Claude in Chrome 또는 Playwright MCP로 끝단 테스트.
- 비대화형 반복: `claude -p`를 루프로 돌려 세션마다 새 컨텍스트로 한 기능씩 처리.
