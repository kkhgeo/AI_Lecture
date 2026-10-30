# Equipping agents for the real world with Agent Skills (+ Claude Code Skills 문서)

- **저자/기관**: Barry Zhang, Keith Lazuka, Mahesh Murag (Anthropic)
- **발행일**: 2025-10-16 (2025-12-18 오픈 표준 공개 업데이트)
- **URL**: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills , 공식 문서 https://code.claude.com/docs/en/skills , 표준 https://agentskills.io
- **자료 유형**: 블로그 (Anthropic 공식) + 공식문서

## 핵심 요약

- Agent Skill은 에이전트가 발견해 필요할 때 불러 쓰는 **지시·스크립트·자료가 든 폴더**다. 핵심 파일은 `SKILL.md`이며, YAML 앞머리(frontmatter)에 `name`과 `description`을 둔다.
- 설계 원리는 **progressive disclosure(점진적 공개)** 3단계다.
  1. **메타데이터**(이름·설명)만 시스템 프롬프트에 미리 로드 → 관련성 판단용
  2. 관련 있다고 판단되면 **SKILL.md 본문** 로드
  3. 본문이 가리키는 **추가 파일**(reference.md, forms.md 등)은 특정 상황에서만 로드
- 따라서 스킬에 담을 수 있는 지식의 양은 사실상 제한이 없다. 컨텍스트에는 필요한 층만 올라가기 때문이다.
- 스킬에는 실행 가능한 스크립트를 포함할 수 있다. 정렬이나 양식 필드 추출처럼 결정적인 작업은 모델이 토큰으로 생성하는 대신 코드를 실행하게 해 신뢰성과 효율을 얻는다(스크립트 코드 자체는 컨텍스트에 올리지 않고 실행 결과만 받음).
- 보안: 신뢰할 수 있는 출처의 스킬만 설치하고, 코드 의존성과 외부 네트워크 연결을 감사하라고 권고한다.
- 2025-12-18 Agent Skills를 플랫폼 간 이식 가능한 **오픈 표준**으로 공개했다(agentskills.io).

## 핵심 개념·용어 정의

| 개념 | 설명 |
|---|---|
| Skill | 특정 과제용 절차 지식을 패키지한 폴더 (`SKILL.md` + 부속 파일 + 스크립트) |
| Progressive disclosure | 목차 → 장(章) → 부록처럼 필요한 깊이까지만 로드 |
| Reference skill vs Action skill | 참고 지식(예: API 스타일 가이드) vs 실행 워크플로(예: `/deploy`) |
| disable-model-invocation: true | 모델이 자동 호출하지 못하고 사용자만 `/이름`으로 호출. 설명도 컨텍스트에 올라가지 않아 비용 0 |
| context: fork | 스킬을 격리된 subagent 컨텍스트에서 실행 |
| Dynamic context injection | SKILL.md 안에 느낌표 접두 셸 명령을 적으면, 그 실행 결과(예: git diff)가 본문에 삽입된 채로 Claude에게 전달됨 |

- Claude Code 문서 기준 권장: `SKILL.md`는 500줄 이하, 상세 자료는 별도 파일로 분리. compaction 후 호출된 스킬 본문은 스킬당 5,000토큰, 합계 25,000토큰 한도로 재주입되며 앞부분이 남으므로 중요한 지시는 위에 둔다.

## 강연에 쓸 만한 포인트

- **"잘 정리된 매뉴얼" 비유**: 목차(메타데이터)만 책상에 두고, 필요한 장을 펴고, 더 필요하면 부록을 찾는다.
- **3층 깔때기 도식**: Level 1(수십 토큰, 항상) → Level 2(수천 토큰, 관련 시) → Level 3(사실상 무제한, 필요 시).
- **CLAUDE.md vs Skill 대비표**: 항상 로드 vs 필요 시 로드. "매 세션 필요한가?"라는 질문 하나로 배치 결정.
- **데모**: 강연자가 만든 스킬(예: 논문 요약 스킬)을 `~/.claude/skills/`에 두고, 관련 요청을 하면 Claude가 스스로 스킬을 로드하는 모습 시연. `/context`에서 스킬 설명만 차지하던 토큰이 호출 후 늘어나는 것 확인.
- 인용(1개): 스킬은 "organized folders of instructions, scripts, and resources" (Anthropic, 2025-10-16)

## Claude Code와의 연결점

- 위치: 개인 `~/.claude/skills/<이름>/SKILL.md`, 프로젝트 `.claude/skills/<이름>/SKILL.md`, 플러그인 스킬은 `/<plugin>:<이름>`.
- 호출: 사용자가 `/이름` 입력, 또는 Claude가 description과 과제를 대조해 자동 로드.
- 부작용 있는 작업(배포, 커밋, 메시지 발송)은 `disable-model-invocation: true`.
- 번들 스킬 예: `/code-review`, `/batch`, `/debug`, `/doctor`, `/verify`.
- 같은 절차를 세 번째 붙여넣고 있다면 스킬로 만들라는 공식 권장(18번 참조).
