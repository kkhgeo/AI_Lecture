# Open-source, model-agnostic coding agents (오픈소스 에이전트: OpenCode·Cline·Aider·Goose·OpenHands·Kilo)

- **저자/기관**: 각 프로젝트 GitHub 저장소·공식 문서 (anomalyco/OpenCode, Cline Bot Inc., Aider-AI, AAIF/goose, OpenHands(All Hands AI), Kilo-Org)
- **발행일**: 저장소 README 상시 갱신 (2026-09-29 열람; 스타 수는 열람 시점 값)
- **URL**:
  - https://github.com/sst/opencode (→ anomalyco/opencode), https://opencode.ai/docs/providers/
  - https://github.com/cline/cline
  - https://github.com/Aider-AI/aider, https://aider.chat
  - https://github.com/block/goose (→ aaif-goose/goose), https://goose-docs.ai/blog/2026/04/07/goose-moves-to-aaif/
  - https://github.com/All-Hands-AI/OpenHands
  - https://github.com/Kilo-Org/kilocode
- **자료 유형**: 공식문서 (GitHub README)

## 핵심 요약
- 벤더 제품(Claude Code, Codex, Copilot, Cursor)과 달리 이들은 **모델을 고를 수 있는(model-agnostic)** 오픈소스 에이전트다. API key만 바꾸면 Claude·GPT·Gemini·DeepSeek는 물론 **로컬 모델**(Ollama, LM Studio, llama.cpp)도 쓸 수 있다.
- **OpenCode**(MIT, 스타 약 21만): 터미널 TUI + 데스크톱 앱(베타). 75개+ provider, 로컬 모델 3종(Ollama, LM Studio, llama.cpp) 문서화. ChatGPT Plus/Pro, GitHub Copilot, Claude Pro/Max 등 **기존 구독으로 로그인** 가능(문서 기준). 기본 에이전트 `build`(전권)와 읽기 전용 `plan` 전환 — Claude Code의 plan mode와 같은 발상.
- **Cline**(Apache-2.0, 스타 약 7만): VS Code 확장으로 시작해 CLI(`npm i -g cline`)·JetBrains·데스크톱·SDK로 확장. **Plan/Act 모드**, 단계별 승인, `.clinerules` 지침, MCP, OpenRouter 경유 200+ provider와 로컬 모델 지원. 헤드리스 CLI로 CI/CD에도 사용.
- **Aider**(Apache-2.0, 스타 약 4.9만): 원조격 터미널 "AI pair programming". 저장소 전체를 요약한 **repo map**, 변경마다 **git 자동 커밋**(되돌리기 쉬움), 100+ 언어, 로컬 모델 지원. 월 약 680만 pip 설치(README 표기).
- **Goose**(Apache-2.0, 스타 약 5.5만): Block이 만든 로컬 우선 범용 에이전트(데스크톱+CLI+API). MCP 기반 확장 70+개. 15+ provider(Ollama 포함). 2025-12-09 AAIF 창립 프로젝트로 기증, 2026-04-07 저장소가 AAIF로 이전(aaif-goose/goose). 지침 파일 `.goosehints`와 AGENTS.md.
- **OpenHands**(MIT, 스타 약 9만, 구 OpenDevin): 연구 커뮤니티 출신 자율 에이전트 플랫폼. Docker 샌드박스, Python SDK/Agent Server, 클라우드. 현재 README는 "Agent Canvas"로 소개하며 OpenHands 자체 에이전트뿐 아니라 Claude Code·Codex·Gemini 등 ACP 호환 에이전트를 한 곳에서 돌리는 자체 호스팅 관제판을 표방.
- **Kilo Code**(MIT, 스타 약 2.7만): VS Code·JetBrains·CLI·웹 클라우드 에이전트. 500+ 모델을 provider 가격 그대로(무마진) 제공, Code/Plan/Ask/Debug 모드. README상 OpenCode에서 포크(초기에는 Roo Code·Cline 계보로 알려짐 — 계보는 교차확인 권장).
- 공통 추세: 벤더 도구와 똑같이 plan 모드·승인 게이트·MCP·서브에이전트·AGENTS.md를 갖추게 되어 **기능 격차는 작아지고, 차이는 모델 선택권과 비용 구조**에 남는다.

## 핵심 개념·용어 정의
- **Model-agnostic**: 에이전트(harness)와 모델(LLM)을 분리해 아무 모델이나 끼워 쓰는 설계.
- **BYOK (Bring Your Own Key)**: 사용자가 자신의 API key를 넣고 토큰 원가만 지불하는 방식.
- **Local model**: 내 PC/연구실 GPU에서 도는 오픈 가중치 모델(Ollama, LM Studio, llama.cpp 서버). 코드가 외부로 나가지 않는다.
- **OpenAI-compatible endpoint**: `/v1/chat/completions` 형식의 API. 대부분의 로컬 서버가 이 형식을 흉내 내므로 에이전트가 바로 연결 가능.
- **Repo map (Aider)**: 저장소의 함수·클래스 시그니처를 압축한 지도. 작은 컨텍스트로 큰 코드베이스를 다루는 기법.
- **ACP (Agent Client Protocol)**: 편집기·관제 도구가 여러 코딩 에이전트를 같은 방식으로 구동하게 하는 프로토콜(OpenHands·Goose가 언급).

## 강연에 쓸 만한 포인트
- 대학원생이 신경 쓸 이유 3가지: (1) **비용** — 구독 없이 BYOK로 토큰 원가만, 혹은 로컬 모델로 0원; 이미 가진 구독(Copilot 학생 무료, ChatGPT)을 OpenCode에 연결. (2) **프라이버시·데이터 규정** — 미공개 연구 데이터·IRB 대상 자료·기관 보안 코드를 외부 API로 보내지 않고 로컬 모델로 처리. (3) **재현성·투명성** — 에이전트 코드와 프롬프트를 직접 열람·고정할 수 있어 연구 방법 기술에 유리.
- 현실적 주의: 로컬 모델은 대형 상용 모델보다 도구 호출·장기 작업 성능이 떨어지는 경우가 많다(일반적 관찰, 수치 근거는 별도 확인 필요). "민감 데이터는 로컬, 어려운 설계는 상용" 혼합 전략 제안.
- 도식 아이디어: "에이전트 = 하네스(harness) + 엔진(모델)" 그림. 벤더 도구는 하네스와 엔진이 용접되어 있고, 오픈소스는 엔진 교체형.
- 숫자(스타, 2026-09-29): OpenCode 21만, OpenHands 9만, Cline 7만, Goose 5.5만, Aider 4.9만, Kilo 2.7만.
- 인용(1개): Goose는 "goes beyond code suggestions" 하는 범용 에이전트 — goose README

## 원본 그림
- 이번 열람에서 각 README의 직접 이미지 URL은 확보하지 못함 — 없음. (Aider 스크린캐스트 `https://aider.chat/assets/screencast.svg`는 과거 README에 있던 것으로 기억되나 미확인)

## Claude Code와의 비교점
- **형태**: 대부분 CLI/TUI + IDE 확장 + 데스크톱, 일부 클라우드(OpenHands, Kilo). Claude Code와 표면 구성 유사.
- **모델**: 가장 큰 차이. 오픈소스는 어떤 모델이든(로컬 포함), Claude Code는 Claude 모델 전용(Bedrock/Vertex 등 경유는 가능하나 모델 자체는 Claude).
- **권한·샌드박스**: Cline 단계별 승인, OpenCode plan 에이전트, OpenHands Docker 샌드박스, Aider git 커밋 기반 되돌리기. Claude Code는 permission mode·hooks·sandbox로 더 세분화.
- **지침 파일**: `.clinerules`, `.goosehints`, Aider `CONVENTIONS.md`(설정으로 로드), 공통적으로 AGENTS.md 지원 확산. Claude Code는 CLAUDE.md(+AGENTS.md).
- **확장**: 모두 MCP 지원이 사실상 표준. 코드 자체를 포크·수정할 수 있다는 점이 벤더 도구와의 본질적 차이.
