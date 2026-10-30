# Create custom subagents (Claude Code Subagents)

- **저자/기관**: Anthropic (Claude Code 공식 문서)
- **발행일**: 상시 갱신 문서 (2026-09-29 열람)
- **URL**: https://code.claude.com/docs/en/sub-agents
- **자료 유형**: 공식문서

## 핵심 요약

- Subagent는 **자기만의 컨텍스트 창**, 사용자 정의 시스템 프롬프트, 제한된 도구, 독립 권한을 가진 특화 보조 에이전트다.
- 가장 큰 이점은 **context isolation**: 검색 결과·로그·파일 내용처럼 다시 볼 일 없는 대량 출력이 메인 대화를 채우는 대신, subagent가 자기 창에서 처리하고 **요약만** 돌려준다.
- 내장 subagent: **Explore**(읽기 전용 빠른 탐색), **Plan**(plan mode에서 계획 전 조사), **general-purpose**(탐색+수정이 필요한 복합 작업) 등.
- 사용자 정의: `.claude/agents/`(프로젝트) 또는 `~/.claude/agents/`(개인)에 마크다운 + YAML frontmatter(`name`, `description` 필수, `tools`, `model`, `permissionMode`, `skills`, `memory`, `isolation: worktree` 등 선택).
- **subagent가 시작할 때 받는 것**: 자기 시스템 프롬프트, 위임 메시지, (설정에 따라) CLAUDE.md와 git 상태, 미리 지정한 skills. **받지 않는 것**: 메인 대화 기록. 단, fork는 부모 대화를 복사해 시작.
- **언제 쓰나**: 장황한 출력, 도구 제한이 중요할 때, 요약으로 돌려줄 수 있는 자기완결적 작업, 병렬 조사. **언제 쓰지 않나**: 잦은 상호작용, 단계 간 맥락 공유가 큰 작업, 빠른 소규모 수정, 지연이 중요한 경우.
- subagent에도 영속 memory 디렉터리를 줄 수 있어 세션을 넘어 학습 가능.

## 핵심 개념·용어 정의

- **Context isolation**: 작업 과정은 격리, 결과 요약만 반환.
- **Delegation**: Claude가 `description`을 보고 자동 위임하거나, 사용자가 이름·`@agent-이름`으로 지정.
- **Fork**: 현재 대화를 복사해 분기한 subagent.
- **Foreground / Background**: 결과를 기다리는 실행 vs 동시에 도는 실행.
- **Adversarial review**: 구현 후 새 컨텍스트의 subagent가 diff만 보고 검토(작성자의 추론에 오염되지 않음).

## 강연에 쓸 만한 포인트

- **"리서치 조수" 비유**: 도서관에 조수를 보내 책 수십 권을 읽게 하고, 나는 한 쪽짜리 요약만 받는다. 내 책상(컨텍스트)은 깨끗하게 유지.
- **도식**: 메인 창(작게 유지) ← 요약 화살표 ← subagent 창(크게 부풀었다가 사라짐). 공식 context-window 시뮬레이션도 subagent 안에서 쓴 토큰은 메인에 0으로 표시.
- **사용/비사용 기준표**: Cognition(09번)·Anthropic(10번) 논쟁과 연결해 "읽기는 위임, 쓰기는 신중히".
- **예시 정의 파일**을 슬라이드에 보여주기(보안 리뷰어: Read, Grep, Glob, Bash만 허용).
- 인용(1개): 공식 권장 문구 "use subagents to investigate X" (Claude Code best practices)

## Claude Code와의 연결점

- 바로 쓰는 프롬프트: "subagent를 써서 우리 인증 시스템이 토큰 갱신을 어떻게 처리하는지 조사해줘", "subagent로 전체 테스트를 돌리고 실패 상위 5개만 보고해줘".
- `/agents`로 관리하거나 Claude에게 "읽기 전용 코드 개선 subagent를 `~/.claude/agents/`에 만들어줘"라고 요청.
- 스킬과 결합: skill frontmatter에 `context: fork`로 격리 실행, subagent의 `skills:`로 필요한 스킬 사전 로드.
- 병렬 쓰기가 필요하면 `isolation: worktree`, 대규모는 `/batch`나 dynamic workflow.
