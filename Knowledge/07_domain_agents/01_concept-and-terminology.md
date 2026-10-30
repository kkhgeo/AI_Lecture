# 도메인 특화 AI 에이전트: 개념과 용어 (domain specialization, specialized/scientific/vertical agents)

- **저자/기관**: 복수 출처 — Chen Ling 외 23명(서베이 논문), Shuo Ren 외 5명(서베이 논문), Anthropic(엔지니어링 블로그), Y Combinator Lightcone 팟캐스트(Garry Tan, Diana Hu, Harj Taggar, Jared Friedman)
- **발행일**: 출처별로 아래 표기 (2026-10-23 열람)
- **URL**:
  - Ling et al., "Domain Specialization as the Key to Make Large Language Models Disruptive: A Comprehensive Survey" — arXiv v1 2023-05-30, 최신 v7 2024-03-29: https://arxiv.org/abs/2305.18703
  - 같은 논문 학술지 게재판: ACM Computing Surveys 58(3), pp. 1–39, 온라인 2025-10-06 (인쇄판 2026-02-28), DOI 10.1145/3764579: https://doi.org/10.1145/3764579 (Crossref 메타데이터로 확인, ACM 페이지는 접근 차단으로 미열람)
  - Ren et al., "Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents" — arXiv v1 2025-03-31, v3 2026-02-02: https://arxiv.org/abs/2503.24047
  - Anthropic, "Equipping agents for the real world with Agent Skills" (Barry Zhang, Keith Lazuka, Mahesh Murag, 2025-10-16): https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
  - Anthropic, "Building agents with the Claude Agent SDK" (Thariq Shihipar, 2025-09-29): https://claude.com/blog/building-agents-with-the-claude-agent-sdk
  - Y Combinator Lightcone, "Vertical AI Agents Could Be 10X Bigger Than SaaS" (YouTube, Y Combinator 채널, 2024-11-22 게시): https://www.youtube.com/watch?v=ASABxNenD_U
  - (2차 보도) David Ramel, "The Future of AI: Follow the Money", Virtualization Review (2024-12-05): https://virtualizationreview.com/Articles/2024/12/05/The-Future-of-AI-Follow-the-Money.aspx
- **자료 유형**: 논문(서베이) 2편 + 엔지니어링 블로그 + 팟캐스트 영상(+ 2차 보도)

## 핵심 요약
- **개념은 존재하고, 학계 용어는 "domain specialization(도메인 특화)"이다.** Ling et al.의 서베이는 도메인 특화를 범용 LLM을 특정 도메인의 맥락 데이터에 맞춰 맞춤화하는 일로 설명하고, 이 맞춤화가 도메인 지식을 반영하고, 도메인 목표에 맞게 최적화되며, 도메인 제약을 따라야 한다고 본다(서론, arXiv HTML v7 확인).
- 같은 논문은 범용 LLM이 특정 분야에서 막히는 이유를 네 가지로 든다: 도메인 **데이터**의 이질성, 도메인 **지식**의 정교함, 도메인 **목표**의 고유성, **제약**(사회 규범, 문화, 종교, 윤리 기준)의 다양성. 초록은 이 네 가지를 "정의"라기보다 도메인 특화가 넘어야 할 장애물로 제시한다.
- 기법 분류는 모델 접근 수준에 따라 3단계다: 외부 보강(external augmentation, black box: 입출력만 사용, 외부 지식·도구 연결) → 프롬프트 설계(prompt crafting, grey box) → 모델 미세조정(fine-tuning, white box: 파라미터 직접 수정). 응용 분야로 생명의학, **지구과학(Earth Science)**, 금융·법, HCI·소프트웨어공학을 다룬다.
- **게재 정보 정정**: 이 서베이는 ACM Computing Surveys 58권 3호에 실렸고 DOI는 **10.1145/3764579**다(Crossref 확인). 사전 메모에 있던 DOI 10.1145/3735632는 Crossref 조회 결과 다른 논문(Li et al., "Fundamental Capabilities and Applications of Large Language Models: A Survey", ACM Comput. Surv. 58(2))이다.
- **에이전트 쪽 용어는 출처마다 다르다.** AI for Science 학계는 "scientific agents"(Ren et al.), Anthropic은 "specialized agents"(범용 에이전트를 특화 에이전트로 바꾼다는 맥락), 벤처·스타트업 업계는 "vertical AI agents"(YC Lightcone)를 쓴다. "domain-specific agents"는 논문들에서 서술어로 널리 쓰이지만, 이를 정식 용어로 정의한 대표 1차 출처는 이번 조사에서 찾지 못했다.
- **업계 담론(YC Lightcone, 2024-11-22)**: YouTube 원본에서 제목, 채널, 게시일, 영상 설명과 챕터 목록을 확인했다. 설명문은 vertical AI agents를 새로 보이는 비즈니스 모델로 소개하고, 기존 SaaS 기업에 미칠 영향, 적합한 사용 사례, 이 범주에서만 3,000억 달러 규모 기업이 나올 가능성을 다룬다고 쓴다. 핵심 주장(vertical 버전이 대체 대상 SaaS 기업보다 10배 커질 수 있다, 발언자 Jared Friedman)은 **주의: 영상 본편은 시청하지 못했고, 2차 보도(Virtualization Review)로만 확인**했다. 시장 규모 수치는 진행자의 전망이며 측정값이 아니다.
- **범용 vs 도메인 특화**: Claude Code·Codex는 범용 LLM + 범용 harness(파일, shell, 웹 도구)로 여러 일을 시도하는 에이전트다. 도메인 특화 에이전트는 같은 뼈대 위에 도메인 데이터 연결(connector), 도메인 절차·지식(skill), 도메인 검증·제약을 얹은 것이다. Anthropic은 Claude Code SDK를 Claude Agent SDK로 개명하면서 같은 harness가 금융, 개인비서, 고객지원, 심층 리서치 에이전트에 쓰일 수 있다고 설명했다(2025-09-29).

## 핵심 개념·용어 정의
- **Domain specialization (도메인 특화, Ling et al.)**: 범용 LLM을 특정 도메인의 데이터·지식·목표·제약에 맞추는 일. 대상은 원래 "LLM"이며 "에이전트"가 아니다.
- **External augmentation / Prompt crafting / Model fine-tuning**: Ling et al.의 3분류(black / grey / white box). 연구소 연구자에게 현실적인 것은 대부분 black box 단계인 외부 보강(검색, 도메인 도구 호출)이다.
- **Scientific agents (Ren et al., 2025)**: 가설 생성, 실험 설계, 데이터 분석, 시뮬레이션을 자동화하는 LLM 기반 에이전트. 초록은 이를 범용 LLM과 대비해 도메인 지식, 전문 도구, 검증 장치를 통합한 "specialized agents"로 설명하며, 재현성 지원을 장점으로 든다.
- **Specialized agents (Anthropic, 2025-10-16)**: Agent Skills 글은 skill(지시문·스크립트·자료를 담은 폴더, SKILL.md)을 범용 에이전트에 붙여 특화 에이전트로 만드는 방식을 제시한다. 사용 사례마다 맞춤 에이전트를 새로 만들 필요를 줄인다는 것이 동기다.
- **Vertical AI agents (YC Lightcone, 2024-11)**: 특정 산업(vertical)의 특정 직무를 수행하는 에이전트를 가리키는 업계·투자 용어. 소프트웨어(SaaS)뿐 아니라 그 소프트웨어를 다루던 사람의 노동까지 대체한다는 논리가 붙는다(2차 보도 기준). 대비어는 "horizontal"(여러 산업에 공통으로 쓰는 범용 도구).
- **General-purpose agent (범용 에이전트)**: 범용 LLM + 범용 harness. 예: Claude Code, Codex. 도메인 지식은 사용자가 대화나 파일(CLAUDE.md, skill)로 넣어 준다.

## 강연에 쓸 만한 포인트
- 용어 지도 슬라이드(강연자 정리):
  | 용어 | 주로 쓰는 쪽 | 출처 예 | 강조점 |
  |---|---|---|---|
  | Domain specialization | 학계(NLP) | Ling et al. 2023/2025 | LLM을 도메인 데이터·지식·목표·제약에 맞춤 |
  | Scientific agents | 학계(AI for Science) | Ren et al. 2025 | 과학 연구 과정 자동화 + 검증·재현성 |
  | Specialized agents | 모델 회사 | Anthropic Agent Skills 2025 | 범용 에이전트 + skill로 특화 |
  | Vertical AI agents | 벤처·스타트업 | YC Lightcone 2024 | 산업별 직무 대체, 사업 모델 |
- "도메인 특화가 어려운 4가지 이유"(데이터·지식·목표·제약)는 환경 연구에 바로 대입할 수 있다. 예: 관측자료 형식이 제각각(데이터), 대기화학·수문 모델 지식(지식), 정책 판단에 쓸 정확도 요구(목표), 법정 기준·자료 공개 규정(제약). 이 대입은 강연자 해석이다.
- Ling et al. 서베이가 응용 분야로 **지구과학**을 따로 다룬다는 점은 환경 연구소 청중과의 연결 고리다.
- "범용 → 특화" 3단 사다리: (1) 범용 에이전트를 그대로 쓴다 → (2) skill·connector로 도메인 지식과 데이터를 붙인다 → (3) 도메인 전용 제품·모델을 만든다. Ling et al.의 black/grey/white box 분류와 나란히 놓고 설명할 수 있다(대응 관계는 강연자 해석).
- 업계 수치(10배, 3,000억 달러)는 투자자의 전망으로만 소개하고 사실처럼 쓰지 않는다.
- 인용(1개): "transforming general-purpose agents into specialized agents that fit your needs" — Anthropic, Agent Skills (2025-10-16)

## 원본 그림
- Ling et al. arXiv HTML v7의 그림(페이지의 상대경로를 절대경로로 바꾼 것, 개별 파일 접근은 확인하지 않음):
  - Fig. 2 범용 LLM / 외부 지식 검색 / 도메인 지시문 / 내부 지식 갱신 4가지 비교 — https://arxiv.org/html/2305.18703v7/LLM_survey_example.png
  - Fig. 3 LLM이 도메인 도구를 호출하는 예 — https://arxiv.org/html/2305.18703v7/domain_tool_augmentation.png
  - Fig. 7 adapter 기반 vs task 지향 미세조정 — https://arxiv.org/html/2305.18703v7/knowledge_update.png
  - Fig. 1 기법 분류도(taxonomy)는 HTML에서 이미지 경로를 얻지 못함. PDF에서 캡처 필요.
- Anthropic Agent Skills 글의 progressive disclosure 그림 — https://www-cdn.anthropic.com/images/4zrzovbb/website/a3bca2763d7892982a59c28aa4df7993aaae55ae-2292x673.jpg (02번 파일 참조)
- YC Lightcone: 그림 없음(영상).
- 용어 지도와 범용→특화 사다리는 직접 그려야 함.

## Claude Code와의 연결점 (또는 다른 도구와의 비교점)
- Claude Code와 Codex는 "범용 LLM + 범용 harness"다. 도메인 특화 에이전트는 이 구조를 버리기보다 위에 도메인 층을 얹는 경우가 많다. Anthropic이 Claude Code의 harness를 Claude Agent SDK로 일반화하고, 금융 에이전트 템플릿을 Claude Code 플러그인으로도 배포한 것이 그 예다(02번 파일).
- Claude Code 사용자가 CLAUDE.md, skill, MCP 서버를 연구실 자료와 절차로 채우면, Ling et al.의 분류로는 black box 단계의 외부 보강을 직접 하는 셈이다(강연자 해석).
- 대조점: Ren et al.이 강조한 검증과 재현성은 범용 에이전트가 자동으로 보장하지 않는다. 도메인 검증 규칙(단위, 물리적 범위, 기준값)을 skill이나 테스트로 명시해야 한다는 메시지로 연결할 수 있다.
