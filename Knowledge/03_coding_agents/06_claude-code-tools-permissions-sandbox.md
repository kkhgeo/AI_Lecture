# Tools reference / Choose a permission mode / Sandboxing / Checkpointing / Security + How we built Claude Code auto mode (도구·권한·샌드박스)

- **저자/기관**: Anthropic (Claude Code 공식 문서, Anthropic Engineering 블로그)
- **발행일**: 공식 문서 상시 갱신(2026-09-29 열람). 엔지니어링 블로그: sandboxing 2025-10-20, auto mode 2026-03-25. 제품 블로그 auto mode 2026-03-24(2026-07-10 GA)
- **URL**:
  - https://code.claude.com/docs/en/tools-reference
  - https://code.claude.com/docs/en/permission-modes
  - https://code.claude.com/docs/en/sandboxing
  - https://code.claude.com/docs/en/checkpointing
  - https://code.claude.com/docs/en/security
  - https://www.anthropic.com/engineering/claude-code-sandboxing
  - https://www.anthropic.com/engineering/claude-code-auto-mode
  - https://claude.com/blog/auto-mode
- **자료 유형**: 공식문서 + 엔지니어링 블로그

## 핵심 요약
- **내장 도구(built-in tools)**는 다섯 범주로 정리된다: 파일 조작(`Read`, `Edit`, `Write`, `NotebookEdit`), 검색(`Grep`, `Glob`), 실행(`Bash`, `PowerShell`, `Monitor`), 웹(`WebSearch`, `WebFetch`), 코드 인텔리전스(`LSP`). 그 밖에 오케스트레이션 도구(`Agent`=subagent 생성, `AskUserQuestion`, `EnterPlanMode`/`ExitPlanMode`, `TaskCreate` 등 작업목록, `Skill`, `Workflow`, `EnterWorktree`, `CronCreate` 등)가 있다. 문서 표 기준 약 40여 개(2026-09 시점).
- 도구별 권한 필요 여부: `Read`·`Grep`·`Glob`·`LSP`는 작업 디렉터리 안에서는 묻지 않음. `Edit`·`Write`·`Bash`·`WebFetch`·`WebSearch`·`Skill`은 Manual 모드에서 승인 필요. 단 `Bash`도 `ls`, `cat`, `git status` 같은 읽기 전용 명령은 바로 실행.
- **Permission mode 6종**(Shift+Tab으로 순환): `default`(=Manual, 읽기만 자동) / `acceptEdits`(파일 편집 + mkdir·mv 등 기본 파일 명령 자동) / `plan`(읽고 조사해 계획만 제시, 승인 전 편집 금지) / `auto`(별도 classifier 모델이 사람 대신 검토) / `dontAsk`(미리 허용한 도구만, 나머지는 거부 — CI용) / `bypassPermissions`(전부 허용, 격리된 컨테이너·VM 전용, `--dangerously-skip-permissions`).
- 모드 위에 **permission rules**(allow/ask/deny)를 겹친다. 예: `Bash(npm run *)`, `Read(~/secrets/**)`, `WebFetch(domain:example.com)`. deny 규칙은 bypass 모드에서도 적용된다. `rm -rf /`, `rm -rf ~` 같은 critical path 삭제는 어떤 모드에서도 자동 승인되지 않는다.
- **Auto mode**(2026-03-24 preview, 2026-07-10 GA): 입력 쪽에서는 서버 측 prompt-injection 탐지기가 도구 출력을 검사하고, 출력 쪽에서는 transcript classifier(Sonnet 4.6)가 각 행동을 실행 전에 판정한다. 2단계 구조: 빠른 1-token 필터 → 걸린 것만 chain-of-thought 재검토. classifier에게는 사용자 메시지와 도구 호출만 보여 주고 Claude의 설명문·도구 출력은 제거해 조작을 막는다. v2.1.283 이상에서는 터미널·VS Code 대화형 세션의 기본 시작 모드.
- **Sandboxing**(2025-10-20): OS 수준에서 Bash 명령과 자식 프로세스를 가둔다. 파일시스템 격리는 macOS Seatbelt, Linux/WSL2 bubblewrap, 네트워크 격리는 샌드박스 밖 프록시가 허용 도메인만 통과시킨다. `/sandbox`로 설정. 네이티브 Windows는 미지원(WSL2 필요). 런타임은 오픈소스(`anthropic-experimental/sandbox-runtime`, npm `@anthropic-ai/sandbox-runtime`). 최신 문서에는 자격증명을 가짜값(sentinel)으로 가리고 허용 호스트로 나갈 때만 프록시가 진짜 값으로 바꿔 주는 masking 기능도 있다.
- 클라우드(웹) 세션은 세션마다 격리 VM에서 돌며, GitHub 자격증명은 VM 안에 들어가지 않고 Anthropic 프록시가 서버 측에서 붙인다. push는 현재 작업 브랜치로 제한된다.
- **Checkpoints / rewind**(2025-09-29 도입): 사용자 프롬프트마다 파일 상태를 자동 스냅숏(세션당 최근 100개). `Esc` 두 번 또는 `/rewind`로 "코드+대화 / 대화만 / 코드만" 복원, 또는 특정 지점부터 요약(context 절약). 한계: Bash로 바꾼 파일(rm, mv, cp), 대부분의 subagent 편집, 외부 변경, DB·배포 같은 원격 부작용은 되돌릴 수 없다. git을 대체하지 않는다.
- 보안 권고: 제안된 명령을 검토하고, 신뢰할 수 없는 콘텐츠를 그대로 파이프하지 말고, 외부 웹과 상호작용할 때는 VM·dev container를 쓰라. 처음 여는 코드베이스와 새 MCP 서버는 trust 확인을 거친다(`-p` 비대화형에서는 생략). `WebFetch`는 별도 context window로 가져와 prompt injection 확산을 줄인다. 취약점은 HackerOne으로 제보.

## 핵심 개념·용어 정의
- **Built-in tool**: Claude Code가 기본 제공하는 행동 단위. 이름(`Read`, `Bash` 등)이 권한 규칙·hook matcher·subagent 도구 목록에서 그대로 쓰인다.
- **Permission mode**: 세션에서 "묻지 않고 해도 되는 범위"의 기본값.
- **Permission rule**: 특정 도구·명령·경로·도메인에 대한 allow / ask / deny 규칙. 모드 위에 겹쳐 적용.
- **Classifier (auto mode)**: 사람 승인자를 대신해 각 행동의 위험도를 판정하는 두 번째 모델.
- **Prompt injection**: 에이전트가 읽은 파일·웹페이지 속 악성 문장이 지시를 가로채려는 공격.
- **Sandbox**: OS가 강제하는 파일·네트워크 경계. 권한 모드는 "묻느냐"를 정하고, 샌드박스는 실행된 명령이 "어디까지 닿느냐"를 정한다.
- **Checkpoint / Rewind**: 세션 단위의 되돌리기 지점과 복원 기능.
- **Protected/critical path**: 어떤 모드에서도 자동 승인되지 않는 민감 경로·삭제 대상.

## 강연에 쓸 만한 포인트
- 숫자: 사용자는 권한 프롬프트의 **93%를 승인**한다 → 승인 피로(approval fatigue)가 실제 위험. 샌드박싱은 권한 프롬프트를 **84% 줄였다**(Anthropic 내부 사용 기준). Auto mode 전체 파이프라인의 오탐(무해한 행동 차단)은 **0.4%**, 실제 과잉 행동(overeager)의 약 **17%는 통과**(=약 83% 차단). → "완벽하지 않다, 그래서 샌드박스와 겹쳐 쓴다".
- 비유: permission mode는 "결재 규정", sandbox는 "출입 통제 구역", checkpoint는 "문서의 실행 취소(Ctrl+Z)". 셋은 독립적이며 겹쳐 쓸수록 안전(defense in depth).
- 도식 아이디어: 가로축 자율성, 세로축 보안으로 default·acceptEdits·plan·auto·bypass를 배치한 2D 그림(auto mode 엔지니어링 블로그 Figure 1과 같은 발상).
- 대학원생 실습 팁: 처음엔 `plan` 모드로 "무엇을 할지"만 보게 하고, 연구 데이터가 있는 폴더에서는 `bypassPermissions`를 쓰지 말 것. rewind는 Bash로 지운 파일을 되살리지 못하므로 git 커밋을 습관화.
- 인용(1개): "sandboxing safely reduces permission prompts by 84%" (Anthropic Engineering, 2025-10-20)

## 원본 그림
- Auto mode Figure 1: 권한 모드들을 자율성×보안 평면에 배치(유지보수 부담 표시) — https://www-cdn.anthropic.com/images/4zrzovbb/website/d6b34bdb92808fd5739e4d14340a1752d5607dda-1920x1920.png
- Auto mode Figure 2: 시스템 구조(prompt-injection probe + transcript classifier) — https://www-cdn.anthropic.com/images/4zrzovbb/website/05f268391243c60c3f725c26151eed7b0b531e86-1920x2002.png
- Auto mode Figure 3: classifier가 보는 "벗겨진(stripped)" transcript 예시 — https://www-cdn.anthropic.com/images/4zrzovbb/website/411b97a06450b27b11f1f9a952ab03d37d8ca3a3-1920x1679.png
- Auto mode Figure 4: 2단계 분류 파이프라인 — https://www-cdn.anthropic.com/images/4zrzovbb/website/58a83df591dc5a2344a65216d4f8eaee3c071d935.png (URL 형식이 다른 그림과 달라 불완전할 수 있음. 원문 페이지에서 확인 필요)
- Sandboxing 엔지니어링 글의 다이어그램 — 추출 도구가 이미지 URL을 반환하지 않음(원문 https://www.anthropic.com/engineering/claude-code-sandboxing 에서 직접 확인 필요)

## 다른 도구와의 비교점
- **OpenAI Codex CLI**도 승인 정책(approval mode)과 OS 샌드박스(macOS Seatbelt, Linux Landlock/seccomp 계열)를 조합하는 설계다. "권한 모드 + OS 샌드박스" 이중 구조는 업계 공통 패턴이 되었다(Codex 쪽 세부는 해당 파일에서 확인, 여기서는 미검증).
- Claude Code의 차별점: ① 사람 대신 **모델 classifier가 승인**하는 auto mode, ② 샌드박스 런타임을 **오픈소스로 공개**해 다른 에이전트도 쓰도록 한 점, ③ 대화와 코드를 따로 되돌리는 **checkpoint/rewind**.
- IDE 기반 도구(Cursor 등)는 편집을 diff로 보여 주고 사람이 수락하는 흐름이 중심이다. Claude Code는 셸 실행까지 포함하므로 권한 체계가 더 세분화되어 있다.
