# How Claude Code is used in practice / How Anthropic teams use Claude Code / Economic Index: AI's impact on software development / How scientists use Claude (코딩 밖의 활용과 연구 활용)

- **저자/기관**: Anthropic (Research팀, Economic Research팀, claude.com 블로그)
- **발행일**:
  - How Claude Code is used in practice — 2026-06-16 (Zoe Hitzig, Maxim Massenkoff, Eva Lyubich, Shaoyi Zhang, Ryan Heller, Peter McCrory)
  - How Anthropic teams use Claude Code — 2025-07-24
  - Anthropic Economic Index: AI's impact on software development — 2025-04-28
  - How scientists use Claude to accelerate research — 2026-01-15
  - Claude Science (beta) — 2026-06-30
  - (모두 2026-09-29 열람)
- **URL**:
  - https://www.anthropic.com/research/claude-code-expertise
  - https://claude.com/blog/how-anthropic-teams-use-claude-code (PDF: https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)
  - https://www.anthropic.com/research/impact-software-development
  - https://www.anthropic.com/news/accelerating-scientific-research
  - https://www.anthropic.com/news/claude-science-ai-workbench
  - 보조: https://code.claude.com/docs/en/how-claude-code-works (터미널에서 가능한 일이면 코딩 외에도 도움 가능하다고 명시)
- **자료 유형**: 블로그(연구 보고) + 공식문서

## 핵심 요약
- 공식 문서 스스로 Claude Code가 코딩에 강하지만 **명령줄에서 할 수 있는 일이면 무엇이든**(문서 작성, 빌드, 파일 검색, 주제 조사) 돕는다고 설명한다. 폴더·파일·셸이 있는 모든 작업이 대상이 된다.
- **실사용 분석(2026-06-16)**: 2025-10~2026-04, 약 23.5만 명 사용자의 약 40만 세션 분석. 56%가 코드 생성·유지·테스트, 17%가 소프트웨어 운영, **27%가 계획·분석·문서화** 같은 비(非)코드 작업. 9가지 작업 유형 중 "Analyzing(데이터 분석)"과 "Communicating(발표자료·문서 작성)"이 별도 범주로 존재.
- 같은 연구: 사람은 **계획 결정의 약 70%**, **실행 결정의 약 20%**만 내린다 → 사람이 목표를 정하고 Claude가 실행 방법을 정하는 분업. 전문성이 높은 사용자는 프롬프트당 약 2배 많은 행동(12 vs 5), 약 5배 많은 산출을 끌어낸다.
- 핵심 메시지: 성공을 가르는 것은 **코딩 능력보다 도메인 전문성**. 주요 직업군의 검증된 성공률이 소프트웨어 엔지니어와 7%p 이내(약 29~34%)에 모여 있다. 7개월간 작업 가치는 약 27% 상승, 디버깅 비중은 33% → 19%로 감소.
- **Anthropic 내부 사례(2025-07-24)**: 데이터 사이언스팀은 TypeScript를 몰라도 RL 성능 시각화 React 앱을 만들었고, 법무팀은 담당자 연결용 프로토타입을 만들었고, 그로스 마케팅은 수백 개 광고 CSV를 처리해 저성과 광고를 찾고 변형 문구를 생성하는 workflow와 광고 100개 변형을 만드는 Figma 플러그인을 만들었다. 추론(Inference)팀은 모델 관련 함수 이해에 드는 조사 시간을 약 80% 줄였다(1시간 → 10~20분). 보안팀은 장애 진단을 10~15분에서 약 3분으로 줄였다.
- **Economic Index(2025-04-28)**: 코딩 대화 50만 건 분석. Claude Code 대화의 **79%가 "자동화(automation)"**로 분류(Claude.ai는 49%). 사람이 결과를 확인하는 피드백 루프 패턴도 Claude Code에서 약 2배 자주 나타났다. JS/TS 31%, HTML/CSS 28% 등 웹·UI 작업 비중이 높았고, Claude Code 대화에서 스타트업 비중 32.9%, 대기업 23.9%.
- **과학 연구 사례(2026-01-15)**: Stanford Biomni(생의학 에이전트)가 GWAS를 20분에, 웨어러블 데이터 파일 450개 분석을 35분에 수행(원래 수개월·약 3주 추정). MIT Cheeseman Lab의 MozzareLLM은 CRISPR knockout 결과 해석을 자동화했다. 모두 Claude 기반이며, Claude Code 단독 사례인지는 글마다 다르므로 "Claude 활용 사례"로 소개해야 정확하다.
- **Claude Science(2026-06-30 beta)**: 과학자용 AI workbench. 문헌 분석, 다단계 연구 실행, 출판용 그림·원고 생성, 60개 이상의 사전 구성 skills(유전체학·단백질체학·구조생물학), UniProt·PDB·Ensembl 커넥터, 인용·계산을 점검하는 reviewer agent, HPC·GPU 연결을 지원한다. Pro/Max/Team/Enterprise, macOS·Linux. Claude Code와는 별도 제품.
- 대학원생에게 바로 적용 가능한 사용처(문서·사례에서 도출한 재구성, 공식 목록은 아님): ① 데이터 분석(CSV·Jupyter 노트북 편집은 `NotebookEdit` 도구, 그림 생성 스크립트), ② LaTeX 원고·BibTeX 정리와 컴파일 오류 수정, ③ 문헌 폴더 정리·요약(WebSearch/WebFetch, MCP로 Zotero·Drive 연결), ④ 반복 분석 파이프라인을 skill로 저장, `claude -p`와 Routines로 야간 자동 실행.

## 핵심 개념·용어 정의
- **Automation vs Augmentation**(Economic Index): AI가 과업을 직접 수행하느냐(자동화), 사람과 반복 협업하며 보조하느냐(증강)의 구분.
- **Feedback loop**(Economic Index): AI가 대부분 수행하되 사람이 오류·결과를 되먹여 주는 자동화의 하위 유형.
- **Planning vs execution decisions**: 무엇을 할지(목표·범위) vs 어떻게 할지(구현 방법)에 관한 결정. 실사용 분석에서 사람은 전자를, Claude는 후자를 주로 담당.
- **Work modes(9종)**: Building, Fixing, Testing, Orchestrating, Operating, Understanding, Planning, Analyzing, Communicating.
- **Verified success**: 테스트 통과 등 객관적 신호로 확인된 세션 성공(연구의 분류 기준).
- **AI for Science program**: 연구자에게 API 크레딧을 무상 지원하는 Anthropic 프로그램.

## 강연에 쓸 만한 포인트
- 핵심 숫자 3개: **27%**(Claude Code 세션 중 비코드 작업), **70% vs 20%**(사람이 내리는 계획 결정 vs 실행 결정), **79%**(Claude Code 대화 중 자동화 비율, Claude.ai는 49%).
- 메시지: "코딩을 몰라도 되는 게 아니라, **자기 분야를 아는 사람이 더 잘 쓴다**" → 대학원생의 도메인 지식이 곧 경쟁력. 전문가는 같은 프롬프트로 약 5배 산출.
- 비유: Claude Code는 "코딩 도구"라기보다 **폴더와 터미널을 다룰 줄 아는 연구 조교**. 논문 폴더, 데이터 폴더, LaTeX 폴더 모두 "코드베이스"처럼 다룰 수 있다.
- 시연 아이디어: ① `data/` 폴더의 CSV로 탐색적 분석 → 그림 → 결과 요약 markdown, ② `paper/` LaTeX 컴파일 오류를 Claude Code가 고치게 하기, ③ 반복 분석을 skill로 저장해 `/analyze-run`으로 재실행.
- 주의점: 과학 사례 수치(20분 GWAS 등)는 특정 연구팀 보고이므로 일반화 금지. 결과 검증과 재현성 책임은 연구자에게 있다.
- 인용(1개): "People make about 70% of the planning decisions" (Anthropic, How Claude Code is used in practice, 2026-06-16)

## 원본 그림
- (claude-code-expertise) 대표 일러스트 "Agentic coding and persistent returns to expertise" — https://www-cdn.anthropic.com/images/4zrzovbb/website/f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg
- Figure 1: 9가지 작업 유형 — https://www-cdn.anthropic.com/images/4zrzovbb/website/b0c229bb9765b65716dfdf1cd0bedc2713037288-1920x1080.png
- Figure 2: 계획·실행 결정 중 Claude의 비중 — https://www-cdn.anthropic.com/images/4zrzovbb/website/c8c039a010b96ad191a3a9b7dfe6ad01adb410bf-1920x1080.png
- Figure 3: 전문성이 높을수록 프롬프트당 Claude가 더 많이 수행 — https://www-cdn.anthropic.com/images/4zrzovbb/website/a72b63aceab4eadb0baa5799a69cc3ff211e7462-1920x1080.png
- Figure 4: 2025-10~2026-04 작업 구성과 가치 변화 — https://www-cdn.anthropic.com/images/4zrzovbb/website/c72f140ee2d30cdf1385e425098fb698b7c5d74c-1920x1080.png
- Figure 5: 전문성과 세션 종료 양상 — https://www-cdn.anthropic.com/images/4zrzovbb/website/140578bc2523d4945c016d72e69628d2692228c8-1920x1080.png
- Figure 6: 직업별 검증·판정 성공률 — https://www-cdn.anthropic.com/images/4zrzovbb/website/3d2d5df2052152c1a010a139deadab4a7e593a39-1920x1080.png
- Table 1(전문성 분류기), Table 2(성공·실패 정의) — https://www-cdn.anthropic.com/images/4zrzovbb/website/fffb14937444e81d40e38d7b085438b61d5ea46ff-1850x1830.png , https://www-cdn.anthropic.com/images/4zrzovbb/website/54cae744dadf523561ef80b448161fef13991420-1850x1487.png
- Economic Index(2025-04-28) 그림(Claude Code vs Claude.ai 자동화 비율 막대 등) — 이번 추출에서 이미지 URL 미확인. 원문 페이지에서 직접 확인 필요
- How Anthropic teams use Claude Code — 팀별 사례 PDF(그림 아닌 문서): https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf

## 다른 도구와의 비교점
- Anthropic은 Economic Index·실사용 분석으로 **자사 코딩 에이전트의 사용 데이터를 연구 보고서로 공개**한다. 다른 코딩 에이전트 업체의 유사한 공개 통계가 있는지는 이 파일에서 확인하지 않음.
- 비개발자용 경로 분화: Anthropic은 같은 agent 구조를 비개발자용으로 옮긴 **Cowork**(데스크톱에서 폴더를 맡겨 문서·스프레드시트 작업, 2026년 초 research preview로 시작, 정확한 날짜 미확인)와 과학자용 **Claude Science**를 따로 내놓았다. "코딩 에이전트 → 범용 지식노동 에이전트"로 확장되는 흐름의 사례.
- ChatGPT·Claude.ai 같은 채팅 인터페이스와 비교: 채팅은 파일을 업로드해 답을 받는 구조, Claude Code는 **내 폴더 안에서 직접 실행·저장·재실행**하는 구조라 재현 가능한 분석 파이프라인을 만들기 쉽다(Economic Index의 자동화 79% vs 49%가 이 차이를 뒷받침).
