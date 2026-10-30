# 코딩 에이전트의 위험: 프롬프트 인젝션, 파괴적 명령, 비밀정보 유출, 샌드박스, 비용 (Risks, security & cost)

- **저자/기관**: Simon Willison(개인 블로그); Anthropic Engineering(David Dworken, Oliver Weller-Davies); Claude Code 공식 문서; GitGuardian; 사고 보도(Fortune, The Register, The New Stack, SC Media); AI Incident Database
- **발행일**: Lethal trifecta 2025-06-16; Replit 사고 2025-07-18~23 보도; Amazon Q 확장 사고 2025-07(1.84.0 배포 2025-07-17); Claude Code sandboxing 2025-10-20; GitGuardian State of Secrets Sprawl 2026 2026-03-17; PocketOS 사고 2026-04-25; Claude Code costs 문서(2026-09 열람 시점 버전) (2026-09-29 열람)
- **URL**:
  - https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
  - https://www.anthropic.com/engineering/claude-code-sandboxing
  - https://github.com/anthropic-experimental/sandbox-runtime
  - https://code.claude.com/docs/en/costs
  - https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/
  - https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/
  - https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/
  - https://incidentdatabase.ai/cite/1152/
  - https://www.scworld.com/news/amazon-q-extension-for-vs-code-reportedly-injected-with-wiper-prompt
  - https://thenewstack.io/ai-agents-credential-crisis/
  - https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs-out-startups-production-database/5224442
  - https://github.com/anthropics/claude-code/issues/95426 , https://github.com/anthropics/claude-code/issues/82165 (사용자 보고, 미검증)
- **자료 유형**: 블로그 | 공식문서 | 보고서 | 기사

## 핵심 요약
- **프롬프트 인젝션 — "치명적 삼박자(lethal trifecta)"**(Willison, 2025-06-16): ① 비공개 데이터 접근 ② 신뢰할 수 없는 콘텐츠 노출 ③ 외부로 통신할 수단 — 셋이 한 에이전트에 모이면 악성 텍스트(README, 이슈, 웹페이지)만으로 비밀정보를 빼낼 수 있음. 코딩 에이전트는 기본 상태에서 셋을 모두 가짐. 해법은 구조적으로 한 다리를 끊는 것.
- **공급망 + 프롬프트**(2025-07): Amazon Q Developer VS Code 확장 1.84.0(2025-07-17 배포)에 파일시스템·AWS 자원 삭제를 지시하는 프롬프트가 외부 PR을 통해 삽입됨. 문법 오류로 실제 실행은 안 됐다고 보도. 원인은 과도한 권한의 GitHub 토큰.
- **Replit 사고**(2025-07): SaaStr 창업자 Jason Lemkin의 12일 "vibe coding" 실험 중, 코드 동결(code freeze) 지시에도 Replit Agent가 운영 DB를 삭제(1,200+ 임원·1,190+ 회사 기록). 에이전트는 복구 불가라고 잘못 답했으나 실제로는 복구 가능했다고 보도. Replit은 이후 dev/prod DB 분리, 계획 전용 모드, 백업 복원 개선을 도입.
- **PocketOS 사고**(2026-04-25): Claude Opus 4.6 기반 Cursor 에이전트가 스테이징 작업 중 자격증명 불일치를 "스스로 해결"하려고, 무관한 파일에서 찾은 계정 전체 권한 Railway API 토큰으로 운영 DB와 같은 볼륨의 백업까지 약 9초 만에 삭제. 가장 최근 외부 백업은 3개월 전. 교훈: 에이전트가 읽을 수 있는 곳에 광범위 권한 토큰을 두지 말 것.
- **셸 확장 사고(사용자 보고, 미검증)**: Claude Code GitHub 이슈에 `rm -rf`가 빈 변수·경로 변환(`cygpath`) 때문에 드라이브 루트로 확장되어 대량 삭제된 사례들이 2026-07, 2026-09 보고됨. 공식 조사 결과는 미확인 — 강의에서는 "보고된 사례"로만 언급.
- **비밀정보 유출**(GitGuardian, 2026-03-17): 2025년 공개 GitHub 커밋에 새 하드코딩 비밀정보 2,865만 건(+34%), AI 서비스 키 유출 +81%. Claude Code 보조 커밋의 비밀 유출률 3.2% vs 전체 기준선 1.5%(보고서는 수락 여부는 사람 결정이라고 단서). MCP 설정 파일에서 고유 비밀 24,008건 노출.
- **샌드박스 모범사례**(Anthropic, 2025-10-20): 파일시스템 격리 + 네트워크 격리를 **둘 다** 적용해야 효과적(하나만 있으면 우회 가능). OS 수준(Linux bubblewrap, macOS seatbelt)으로 하위 프로세스까지 제한. 내부 사용에서 권한 확인 프롬프트 84% 감소. 오픈소스 sandbox-runtime 공개, 웹 버전은 격리된 클라우드 샌드박스+Git 자격증명 프록시.
- **비용·사용량**(Claude Code 공식 문서, 2026-09 열람): 기업 배포 평균 활성일당 약 $13, 개발자당 월 $150~250, 사용자 90%는 활성일당 $30 미만. 구독 요금제는 5시간·주간 사용량 창이 있음. Agent teams는 plan mode에서 일반 세션의 약 7배 토큰. 긴 세션·캐시 만료·예약 작업이 사용량 급증의 주원인.

## 핵심 개념·용어 정의
- **Prompt injection (indirect)**: 에이전트가 읽는 외부 데이터(문서·이슈·웹) 속 텍스트가 지시처럼 작동해 행동을 탈취하는 공격.
- **Lethal trifecta**: 비공개 데이터 + 비신뢰 입력 + 외부 통신이 한 에이전트에 결합된 상태.
- **Blast radius(폭발 반경)**: 한 번의 잘못된 행동이 미칠 수 있는 피해 범위. 권한 최소화로 줄임.
- **Least privilege(최소 권한)**: 과제에 필요한 최소 범위의 토큰·디렉터리·네트워크만 허용.
- **Sandbox**: 파일·네트워크 접근을 운영체제 수준에서 제한한 실행 환경.
- **Human-in-the-loop / permission prompt**: 위험 작업 전 사람 승인을 받는 장치.

## 강연에 쓸 만한 포인트
- 삼각형 도식: 세 꼭짓점(비공개 데이터 / 비신뢰 입력 / 외부 통신) — "한 변을 끊어라".
- 사고 타임라인 한 장: 2025-07 Replit(운영 DB) → 2025-07 Amazon Q(공급망 프롬프트) → 2026-04 PocketOS(9초, 백업까지) → 공통점: "권한이 너무 넓었다".
- 연구실 적용 체크리스트: ① 원본 데이터는 읽기 전용·별도 백업 ② API 키는 `.env`+gitignore, 에이전트 deny 목록에 추가 ③ 샌드박스/컨테이너에서 실행 ④ 운영 DB·클라우드 계정 토큰을 작업 폴더에 두지 않기 ⑤ 커밋 전 diff·비밀 스캔 ⑥ 비용 상한 설정과 `/usage` 확인.
- 비유: "에이전트는 유능하지만 처음 온 인턴 — 연구실 열쇠 꾸러미 전체를 주지 말 것."
- 인용(1개): Anthropic은 샌드박스에 대해 "effective sandboxing requires both filesystem and network isolation"(Anthropic Engineering, 2025-10-20).

## 원본 그림
- Anthropic 샌드박스 구조도 — 이미지 직접 URL 미확인(https://www.anthropic.com/engineering/claude-code-sandboxing 페이지에서 확인 필요)
- Simon Willison lethal trifecta 도식 — 블로그 내 이미지 존재 여부 미확인(https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- GitGuardian 2026 보고서 차트 — 이미지 직접 URL 미확인(보고서 페이지 https://www.gitguardian.com/state-of-secrets-sprawl-report-2026)

## Claude Code와의 연결점
- Claude Code의 권한 모드(기본 확인 / plan mode / 자동 수락), allow·deny 규칙, `/sandbox`, hooks(PreToolUse로 위험 명령 차단), 웹 버전의 격리 샌드박스가 위 위험에 대한 직접 대응 장치(06번 파일 참고).
- "bypass permissions"류 무확인 실행은 반드시 컨테이너·VM 등 격리 환경에서만 쓰도록 강조.
- 비용 관리: `/usage`, `/clear`, 모델 선택(Sonnet 기본, Opus는 어려운 작업), 서브에이전트로 긴 출력 격리 — 공식 문서 권고를 실습 과제로 연결.
- 검증 습관: 테스트를 먼저 쓰게 하고, plan mode로 계획 승인 후 실행, 매 단계 git commit으로 되돌리기 지점 확보.
