# 업계의 도메인 특화 에이전트: Anthropic 도메인 패키지와 vertical 제품 사례 (skills + connectors + subagents)

- **저자/기관**: Anthropic(뉴스·엔지니어링 블로그, GitHub), Thomas Claburn / The Register(보도), Harvey·Abridge(회사 웹사이트)
- **발행일**: 출처별로 아래 표기 (2026-10-23 열람)
- **URL**:
  - Anthropic, "Agents for financial services" (2026-05-05): https://www.anthropic.com/news/finance-agents
  - Thomas Claburn, "Anthropic wants Claude to play with money, unleashes finance agents", The Register (2026-05-05): https://www.theregister.com/2026/05/05/anthropic_unleashes_finance_agents_claude/
  - GitHub anthropics/financial-services (Apache-2.0, 열람 시점 기준): https://github.com/anthropics/financial-services
  - Anthropic, "Claude for Financial Services" (2025-07-15, 2026-04-10 각주 갱신): https://www.anthropic.com/news/claude-for-financial-services
  - Anthropic, "Claude for Life Sciences" (2025-10-20): https://www.anthropic.com/news/claude-for-life-sciences
  - Anthropic, "Equipping agents for the real world with Agent Skills" (2025-10-16): https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
  - Anthropic, "Building agents with the Claude Agent SDK" (2025-09-29): https://claude.com/blog/building-agents-with-the-claude-agent-sdk (구 주소 anthropic.com/engineering/building-agents-with-the-claude-agent-sdk 에서 리다이렉트)
  - Harvey 회사 웹사이트 (발행일 없음): https://www.harvey.ai/
  - Abridge 회사 웹사이트 (발행일 없음): https://www.abridge.com/
- **자료 유형**: 공식 발표·블로그 + 보도 + GitHub 저장소 + 회사 웹사이트

## 핵심 요약
- **Anthropic 금융 에이전트 템플릿(2026-05-05)**: Anthropic 원문과 The Register 보도 모두에서 확인했다. 템플릿은 10종이며, 각각을 "reference architecture"로 부른다. 한 템플릿은 세 가지를 묶는다: **skill**(작업 지시와 도메인 지식), **connector**(작업에 필요한 데이터·외부 서비스에 대한 통제된 접근), **subagent**(비교 기업 선정, 방법론 점검 같은 하위 작업을 맡는 추가 Claude 호출).
  - 리서치·고객 대응 5종: Pitch builder, Meeting preparer, Earnings reviewer, Model builder, Market researcher.
  - 재무·운영 5종: Valuation reviewer, General ledger reconciler, Month-end closer, Statement auditor, KYC screener. The Register는 KYC screener가 kyc-rules라는 skill로 자금세탁방지(AML) 규칙을 적용하고 위험 등급과 처리 결정을 구조화된 JSON으로 낸다고 소개했다.
  - 배포 경로: Claude Cowork와 Claude Code의 **플러그인**(유료 플랜), Claude Managed Agents용 **cookbook**(Claude Platform 공개 베타). Microsoft 365 add-in(Excel, PowerPoint, Word 정식, Outlook 예정)도 함께 발표됐다.
  - 수치: Anthropic은 Claude Opus 4.7이 Vals AI Finance Agent 벤치마크에서 64.37%로 업계 최고라고 밝혔다. The Register는 이 실패율이면 사람 직원은 해고될 것이라고 꼬집었고, Anthropic도 사람이 검토 과정에 남아 있어야 한다고 썼다.
- **GitHub anthropics/financial-services**: 같은 구조가 파일로 공개되어 있다. 에이전트 플러그인(시스템 프롬프트 agents/*.md + skills 폴더), 업종별 skill·명령 묶음(vertical-plugins), MCP connector 선언(.mcp.json), Managed Agent용 agent.yaml과 subagent 정의(managed-agent-cookbooks)로 나뉜다. 빌드 단계 없이 markdown·YAML·JSON 파일만으로 구성된다. README는 결과물이 사람 검토용 초안이며 투자·법률·세무 자문이 아니라고 명시한다.
- **Claude for Financial Services (2025-07-15)**: 앞선 단계의 도메인 패키지다. Claude 모델 + Claude Code·Claude for Enterprise(사용량 확대) + 금융 데이터 제공사 MCP connector(Box, Daloopa, Databricks, FactSet, Morningstar, Palantir, PitchBook, S&P Global, Snowflake) + 구축 지원으로 구성된다. 고객 사례로 Bridgewater AIA Labs, Commonwealth Bank of Australia, AIG를 든다(AIG 수치는 고객 자체 보고).
- **Claude for Life Sciences (2025-10-20)**: 생명과학 연구용 패키지. 신규 connector로 Benchling, BioRender, PubMed, Scholar Gateway(Wiley), Synapse.org, 10x Genomics를 들고, 첫 과학 분야 Agent Skill로 single-cell RNA-seq 품질관리(`single-cell-rna-qc`, scverse 권장 절차 기반)를 공개했다. Protocol QA 벤치마크에서 Sonnet 4.5가 0.83(사람 기준선 0.79)을 기록했다고 회사가 밝혔다.
- **Agent Skills = 도메인 지식의 포장 단위(2025-10-16)**: skill은 SKILL.md(이름·설명을 담은 YAML 머리말 + 본문)와 스크립트·자료 파일을 담은 폴더다. 에이전트는 시작 시 이름과 설명만 읽고, 관련 있을 때 본문을, 필요할 때 부속 파일을 읽는다(progressive disclosure). Anthropic은 이를 범용 에이전트를 특화 에이전트로 바꾸는 방법으로 제시한다. 위 금융·생명과학 패키지가 모두 skill을 도메인 지식 단위로 쓴다.
- **Claude Agent SDK 글(2025-09-29)**: Claude Code를 만든 harness를 Claude Agent SDK로 일반화하면서, 이걸로 만들 수 있는 에이전트 예로 금융 에이전트(포트폴리오 이해·투자 평가), 개인비서, 고객지원, 심층 리서치 에이전트를 들었다. 즉 "범용 harness + 도메인 도구·데이터 = 도메인 에이전트"가 Anthropic의 공식 설명이다.
- **Vertical 제품 사례(회사 자기소개 기준, 독립 검증 아님)**:
  - Harvey(법률): 스스로를 법률·전문 서비스용 AI 소프트웨어로 소개한다. 법률 업무를 처음부터 끝까지 수행하는 목적 특화 agent, 업무 배분·검토를 관리하는 Legal Work Orchestration, 문서 저장·대량 분석용 Vault 등을 제품으로 둔다. 회사 웹사이트는 3,500곳 이상의 법률 조직, 20만 명 이상의 사용자, 85개국 이상을 내세운다.
  - Abridge(임상 기록): 진료 대화를 실시간으로 받아 임상 문서를 만드는 AI를 핵심 제품으로 소개하며, 300곳 이상의 의료 시스템이 쓴다고 밝힌다.
  - 위 수치는 모두 회사 웹사이트의 자기 주장이며, 열람 시점 값이라 바뀔 수 있다.

## 핵심 개념·용어 정의
- **Agent template / reference architecture (Anthropic)**: 특정 직무를 위한 skill + connector + subagent의 묶음. 사용자는 이를 출발점으로 받아 자기 조직에 맞게 고친다.
- **Skill**: 도메인 절차와 지식을 담은 폴더(SKILL.md + 스크립트·자료). 필요할 때만 context에 들어온다.
- **Connector (MCP 서버)**: 외부 데이터·서비스에 대한 통제된 연결. 금융 패키지에서는 FactSet, S&P Capital IQ, PitchBook, Morningstar 등 데이터 제공사가 해당한다.
- **Subagent**: 주 에이전트가 하위 작업을 맡기는 별도 Claude 호출. 자기 context에서 일하고 결과만 돌려준다.
- **Plugin**: Claude Code·Cowork에 설치하는 배포 단위. skill, 명령, subagent, connector 설정을 한 번에 담는다.
- **Vertical AI product**: 특정 산업의 특정 직무를 겨냥한 AI 제품(예: 법률의 Harvey, 임상 기록의 Abridge). 01번 파일의 "vertical AI agents" 참조.

## 강연에 쓸 만한 포인트
- 공식 하나: **도메인 에이전트 = 범용 에이전트(LLM + harness) + skill(지식·절차) + connector(데이터) + subagent(분업)**. Anthropic 금융 템플릿이 바로 이 구조라서, 범용 vs 특화의 차이를 추상론이 아니라 실제 제품으로 보여 줄 수 있다.
- 같은 템플릿이 Claude Code 플러그인과 Managed Agent(서버에서 자율 실행) 두 형태로 나온다는 점: 사람 옆에서 돕는 모드와 혼자 도는 모드가 같은 부품으로 만들어진다.
- 64.37%라는 벤치마크 점수는 "최고 수준이어도 사람 검토가 필수"라는 메시지에 쓰기 좋다. Anthropic 자신과 공개 저장소 README가 모두 사람 검토를 요구한다.
- 연구소 적용 상상(강연자 아이디어): 금융의 "Month-end closer" 자리에 "월간 대기질 자료 QA", "KYC screener" 자리에 "환경영향평가 서류 기준 대조"를 넣어 보면 skill(기준·절차), connector(측정망 DB), subagent(이상치 점검)로 같은 틀을 짤 수 있다.
- 생명과학 패키지의 single-cell RNA-seq QC skill은 "과학 분석 절차를 skill로 만든 사례"로, 환경 분야의 표준 분석 절차(예: 결측·이상치 처리 규칙)를 skill로 만드는 일과 바로 대응한다(대응은 강연자 해석).
- 인용(1개): "reference architecture" — Anthropic이 금융 에이전트 템플릿을 부른 말 (2026-05-05)

## 원본 그림
- Anthropic "Agents for financial services": 구조도는 없음. 영상 썸네일 https://img.youtube.com/vi/foxeK2AXfHQ/maxresdefault.jpg 과 고객사 로고 이미지뿐이라 슬라이드용 원본 다이어그램은 없음.
- Anthropic Agent Skills 글의 그림(페이지에서는 `/_next/image?url=...`로 감싸져 있어 URL 인코딩을 푼 주소. 개별 접근은 확인하지 않음):
  - SKILL.md 구조 — https://www-cdn.anthropic.com/images/4zrzovbb/website/6f22d8913dbc6228e7f11a41e0b3c124d817b6d2-1650x929.jpg
  - 추가 파일 묶기 — https://www-cdn.anthropic.com/images/4zrzovbb/website/191bf5dd4b6f8cfe6f1ebafe6243dd1641ed231c-1650x1069.jpg
  - Progressive disclosure — https://www-cdn.anthropic.com/images/4zrzovbb/website/a3bca2763d7892982a59c28aa4df7993aaae55ae-2292x673.jpg
  - Skill과 context window — https://www-cdn.anthropic.com/images/4zrzovbb/website/441b9f6cc0d2337913c1f41b05357f16f51f702e-1650x929.jpg
- The Register, Claude for Financial Services, Claude for Life Sciences, Harvey, Abridge: 슬라이드용 원본 그림 없음(확인 범위 내).
- "범용 에이전트 + skill + connector + subagent" 구조도는 직접 그려야 함.

## Claude Code와의 연결점 (또는 다른 도구와의 비교점)
- 금융 템플릿은 Claude Code 플러그인으로 직접 설치된다. 즉 Claude Code는 범용 coding agent이면서 동시에 도메인 패키지를 얹는 "받침대" 역할을 한다.
- 공개 저장소 구조(agents/*.md, skills/, .mcp.json, commands/)는 Claude Code 사용자가 자기 프로젝트에 쓰는 .claude/agents, skills, MCP 설정과 같은 형식이다. 연구자가 자기 분야 템플릿을 같은 방식으로 만들 수 있다는 점을 보여 주는 실물 예시다(형식이 같다는 판단은 저장소 구조를 근거로 한 강연자 해석).
- Harvey, Abridge 같은 vertical 제품은 사용자가 harness를 직접 만지지 않는 완성품이라는 점에서 Claude Code 위에 skill을 얹는 방식과 다르다. 완성품은 도입이 쉽지만 고치기 어렵고, 범용 에이전트 + skill은 손이 더 가지만 연구 절차에 맞춰 바꿀 수 있다(강연자 정리).
