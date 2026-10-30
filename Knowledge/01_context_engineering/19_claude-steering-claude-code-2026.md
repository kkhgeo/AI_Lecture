# Steering Claude Code: when to use CLAUDE.md, skills, hooks, rules, subagents, and more

- **저자/기관**: Michael Segner (Anthropic)
- **발행일**: 2026-06-18
- **URL**: https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
- **자료 유형**: 블로그 (Anthropic/Claude 공식 블로그)

## 핵심 요약

- Claude Code에 지시를 넣을 수 있는 자리 일곱 곳(CLAUDE.md, rules, skills, subagents, hooks, output styles, system prompt append)을 **로드 시점, compaction 후 지속성, 컨텍스트 비용, 권위(강제력)** 기준으로 비교해 "어디에 둘지" 결정하는 틀을 제시한다.
- 핵심 논리: 루트 CLAUDE.md의 모든 줄은 저장소에서 일하는 모든 엔지니어의 모든 세션에 로드된다. 관련 없는 작업에도 토큰을 쓰고, 정말 중요한 지시의 준수율을 희석한다.
- 권장: 루트 CLAUDE.md는 200줄 이하, 모노레포는 팀별 하위 CLAUDE.md, 특정 경로 규칙은 `paths:` rules, 절차는 skills, 결과만 필요한 곁가지 작업은 subagents, 반드시 지켜야 할 것은 hooks.
- Output style은 기본 시스템 프롬프트를 통째로 대체하므로 보안·테스트 관련 기본 지시가 사라질 수 있어, 큰 역할 전환에만 쓰라고 한다.

## 핵심 개념·용어 정의

| 방법 | 로드 | compaction 후 | 비용 | 적합 |
|---|---|---|---|---|
| CLAUDE.md(루트) | 세션 시작 | 재로드 | 높음 | 빌드 명령, 규약, 팀 규범 |
| CLAUDE.md(하위) | 필요 시 | 해당 폴더 접근 전까지 소실 | 낮음 | 하위 폴더 전용 규약 |
| Rules | 시작(비범위) / 필요 시(범위) | 재주입 | 중간 | 특정 제약, 경로 한정 |
| Skills | 설명은 시작, 본문은 호출 시 | 예산 내 재주입 | 낮음 | 절차(체크리스트, 배포) |
| Subagents | 설명은 시작, 본문은 격리 | 요약만 반환 | 낮음 | 검색·감사 등 곁가지 작업 |
| Hooks | 생명주기 이벤트 | compaction과 무관 | 낮음 | 결정적 자동화, 차단 |
| Output styles | 세션 시작 | 유지 | 높음 | 큰 역할 전환 |

**피해야 할 안티패턴**
1. CLAUDE.md에 "X할 때마다 Y해라" → hook으로
2. "절대 하지 마라" 지시 → hook 또는 managed settings로 실제 강제
3. 30줄짜리 절차를 CLAUDE.md에 → skill로
4. 범위 없는 rules → `paths:` 추가
5. 개인 선호를 프로젝트 파일에 → 사용자·로컬 설정으로

## 강연에 쓸 만한 포인트

- **결정 트리 도식**: "매 세션 필요한가?" → 예: CLAUDE.md / 아니오 → "특정 경로에만?" → rules(paths) / "절차인가?" → skill / "결과만 필요한가?" → subagent / "예외 없이 반드시?" → hook.
- **비용 vs 권위 2축 그림**: x축 컨텍스트 비용, y축 강제력. hook은 비용 낮고 강제력 최고, CLAUDE.md는 비용 높고 강제력은 권고 수준.
- **안티패턴 5개**: 청중 자신의 CLAUDE.md를 점검하게 하는 셀프 체크리스트로 활용.
- 인용(1개): "Every line loads into every session for every engineer" (Michael Segner, 2026-06-18) — 9단어

## Claude Code와의 연결점

- 강연 실습 "CLAUDE.md 다이어트": 기존 CLAUDE.md를 읽고 ① 절차는 `.claude/skills/`로 ② 경로 한정 규칙은 `.claude/rules/`(paths)로 ③ 강제 규칙은 `.claude/settings.json` hooks로 옮기고 ④ 남은 핵심만 200줄 이내로.
- `/doctor`로 비대해진 CLAUDE.md·skills 정리 제안 받기.
- 팀 배포는 skills·subagents·hooks를 plugin으로 묶어 공유.
