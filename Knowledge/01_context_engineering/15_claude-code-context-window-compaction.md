# Explore the context window / How Claude Code works (컨텍스트 창과 compaction)

- **저자/기관**: Anthropic (Claude Code 공식 문서)
- **발행일**: 상시 갱신 문서 (2026-09-29 열람)
- **URL**: https://code.claude.com/docs/en/context-window , https://code.claude.com/docs/en/how-claude-code-works
- **자료 유형**: 공식문서 (인터랙티브 시뮬레이션 포함)

## 핵심 요약

- Claude Code는 **agentic loop**(맥락 수집 → 행동 → 결과 검증)를 돈다. 모델을 둘러싸고 도구를 제공하고 모델이 볼 컨텍스트를 관리하는 층을 **agentic harness**라 부른다.
- "Explore the context window" 페이지는 한 세션에서 창이 어떻게 차는지 타임라인으로 시뮬레이션한다(대표 수치 예시):
  - **입력 전 자동 로드**: 시스템 프롬프트(약 4,200), auto memory(약 680), 환경 정보(약 280), MCP 도구 이름(지연 로드, 약 120), 스킬 설명(약 450), 사용자 CLAUDE.md(약 320), 프로젝트 CLAUDE.md(약 1,800 토큰)
  - **작업 중**: 파일 읽기마다 1,000~2,400 토큰, 해당 경로의 path-scoped rule 자동 로드, 편집 후 PostToolUse hook 출력 추가
  - **subagent 위임**: 대량 파일 읽기는 subagent 창에 머물고 요약만 돌아옴
  - **/compact**: 대화가 구조화된 요약으로 대체됨
- **compaction 후 남는 것**: 시스템 프롬프트·output style 유지, 루트 CLAUDE.md·비범위 rules·auto memory·plan mode 계획은 디스크에서 재주입, git 상태 새로 읽기, 최근 수정 파일 최대 5개 재읽기(5,000토큰 넘는 파일은 경로만), 호출된 스킬 본문은 스킬당 5,000·합계 25,000토큰 한도로 재주입, path-scoped rule과 하위 디렉터리 CLAUDE.md는 해당 파일을 다시 읽을 때 재로드.
- 요약에 남는 것: 사용자 요청과 의도, 핵심 기술 개념, 살펴본·수정한 파일과 중요한 코드 조각, 오류와 해결, 남은 작업, 현재 작업. 도구 출력 전문과 중간 추론은 사라진다.
- 자동 관리 순서: 한계에 가까워지면 **오래된 도구 출력부터 지우고**, 필요하면 대화를 요약한다. 초기의 세부 지시는 잃을 수 있으므로 지속 규칙은 CLAUDE.md에 두라.

## 핵심 개념·용어 정의

- **Auto-compaction**: 한계 접근 시 자동 요약. 임계값은 모델·설정에 따라 다르며 `/autocompact`로 조정 가능.
- **/compact [focus]**: 수동 요약. 초점을 주면 자동 요약이 추측하는 대신 사용자가 고른 것을 남김.
- **Summarize from here / up to here**: `/rewind`에서 대화 일부만 요약.
- **Compact Instructions**: CLAUDE.md에 두는 압축 시 보존 지시 절.
- **SessionStart hook(compact)**: 압축 직후 실행되어 필요한 맥락을 다시 주입.
- **Thrashing**: 거대한 파일·출력 때문에 요약 직후 다시 차는 상황. 몇 번 시도 후 자동 압축 중단.
- **1M context**: 일부 모델은 100만 토큰 창을 지원하나, compaction은 동일하게 작동.

## 강연에 쓸 만한 포인트

- **가장 강력한 시각 자료**: 공식 인터랙티브 타임라인 자체를 강연에서 띄워 보여주기. "아무것도 치기 전에 이미 약 8천 토큰이 차 있다"는 사실이 인상적.
- **막대 도식**: 200k 창을 가로 막대로 그리고 [시스템 | 메모리 | 도구 | 스킬 설명 | CLAUDE.md | 대화 | 파일 읽기 | 여유] 구간 색칠.
- **"압축 후 무엇이 살아남나" 표**: 디스크에 있는 것(CLAUDE.md, memory, plan)은 살아남고, 대화 중에만 있던 것은 요약된다 → "중요한 건 파일로 써라"는 메시지의 근거.
- **팁**: 중요한 스킬 지시는 SKILL.md 위쪽에, 압축 후에도 필요한 규칙은 `paths:` 없이 루트에.
- 인용(1개): 문서는 compaction이 "Replaces the conversation with a structured summary"라고 설명 (Claude Code 문서)

## Claude Code와의 연결점

- `/context`: 범주별 실시간 사용량과 최적화 제안. `/context all`: MCP 도구별 토큰.
- `/compact focus on the auth bug fix` 식 초점 압축, `/clear`, `/autocompact <토큰수>`, `/rewind`.
- 상태 표시줄(statusline)에 컨텍스트 사용률을 상시 표시.
- 데모 순서: 새 세션 `/context` → 큰 파일 몇 개 읽기 → `/context` → subagent로 같은 조사 → `/context` → `/compact` → `/context`. 네 번의 수치 변화를 한 슬라이드로.
