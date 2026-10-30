# 01. 영상 목록: Claude Code와 context engineering 관련 강연·발표

- 조사일: 2026-09-29
- 검증 방법: 모든 영상은 YouTube 영상 페이지의 메타데이터(제목, 채널, 게시일, 길이, 조회수, 설명란)를 직접 조회해 확인했다. 게시일은 YouTube 게시일(미국 태평양시 기준)이다. 행사 발표일이 다르면 따로 적었다.
- 조회수는 2026-09-29에 조회한 값이다. 참고용이며 시간이 지나면 바뀐다.
- "대상 청중"은 설명란과 트랜스크립트 도입부를 근거로 판단했다.
- 표기: 핵심 목록은 02 분석 문서에서 상세히 분석한 영상이다. 보조 목록은 목록만 기록한 참고 영상이다.

---

## A. 영어 영상: 핵심 12개

| # | 제목 | 연사 | 채널 / 행사 | 게시일 | 길이 | 언어 | URL | 한 줄 요약 | 대상 청중 | 조회수 |
|---|---|---|---|---|---|---|---|---|---|---|
| E1 | No Vibes Allowed: Solving Hard Problems in Complex Codebases | Dex Horthy (HumanLayer) | AI Engineer / AIE Code Summit 2025 | 2025-12-02 | 20:31 | 영어 | https://www.youtube.com/watch?v=rmvDxxNubIg | 컨텍스트 창을 약 40% 안쪽 "smart zone"에 유지하는 Research-Plan-Implement 흐름과 의도적 압축(intentional compaction) | Claude Code를 실무에 쓰는 개발자, 팀 리더 | 646,322 |
| E2 | Claude Code best practices \| Code w/ Claude | Cal Rueb (Anthropic) | Anthropic / Code w/ Claude 2025 | 2025-07-31 (발표 2025-05-22) | 25:53 | 영어 | https://www.youtube.com/watch?v=gv0WHhKelSE | Claude Code의 내부 구조(도구+루프, agentic search)를 먼저 설명한 뒤 CLAUDE.md, 권한, /clear·/compact, 계획 등 모범 사례 정리 | Claude Code 입문~중급 개발자 | 569,741 |
| E3 | Mastering Claude Code in 30 minutes | Boris Cherny (Anthropic) | Anthropic / Code w/ Claude 2025 | 2025-05-22 | 28:07 | 영어 | https://www.youtube.com/watch?v=6eBSHbLKuN0 | 제작자가 직접 소개하는 실전 팁. 코드베이스 Q&A로 시작해 편집, 도구 연결, 컨텍스트(CLAUDE.md 계층), SDK, 병렬 실행으로 확장 | Claude Code 입문~중급 개발자 | 1,626,500 |
| E4 | Andrej Karpathy: Software Is Changing (Again) | Andrej Karpathy | Y Combinator / AI Startup School | 2025-06-18 (발표 2025-06-17) | 39:31 | 영어 | https://www.youtube.com/watch?v=LCEmiRjPEtQ | Software 1.0/2.0/3.0 틀, LLM을 운영체제로 보는 비유, 컨텍스트 창을 작업 기억(working memory)으로 보는 관점, 부분 자율성(autonomy slider) | 학부·대학원생, 예비 창업자 (비전공자도 따라갈 수준) | 2,569,663 |
| E5 | Context Engineering for Engineers | Jeff Huber (Chroma) | YC Root Access / Context Engineering SF 밋업 | 2025-08-25 | 11:16 | 영어 | https://www.youtube.com/watch?v=3jN77Aw7Utk | Chroma의 context rot 기술 보고서를 근거로, 입력이 길수록 성능이 떨어지므로 정보를 모으고(gather) 걸러내야(glean) 한다는 주장 | AI 엔지니어 | 15,216 |
| E6 | 12-Factor Agents: Patterns of reliable LLM applications | Dex Horthy (HumanLayer) | AI Engineer / AIE 2025 | 2025-07-03 | 17:05 | 영어 | https://www.youtube.com/watch?v=8kMaTybvDUw | 실제 운영 중인 에이전트는 대부분 평범한 소프트웨어이며, 컨텍스트 창을 직접 소유하라는 등 12가지 원칙 제시 | 에이전트를 만드는 개발자 | 288,137 |
| E7 | Context Engineering for Agents - Lance Martin, LangChain | Lance Martin (당시 LangChain) | Latent Space 팟캐스트 | 2025-09-11 | 1:03:18 | 영어 | https://www.youtube.com/watch?v=_IlTcWciEC4 | 컨텍스트 전략(offload, reduce, retrieve, isolate 등)을 분류하고 Manus, Cognition, Anthropic 사례를 비교하는 대담. 슬라이드 공개 | AI 엔지니어 (중급 이상) | 44,007 |
| E8 | Claude Agent SDK [Full Workshop] | Thariq Shihipar (Anthropic) | AI Engineer / AIE Code Summit | 2026-01-05 | 1:52:25 | 영어 | https://www.youtube.com/watch?v=TqC1qOfiVcQ | 에이전트 정의부터 시작해 라이브 코딩으로 에이전트 루프를 구현하고, 파일시스템과 bash로 컨텍스트를 구성하는 방법을 청중과 대화하며 보여주는 워크숍 | 에이전트를 직접 만들려는 개발자 | 151,162 |
| E9 | Understanding is the new bottleneck | Geoffrey Litt (Notion) | AI Engineer / AIE World's Fair 2026 | 2026-07-10 | 19:33 | 영어 | https://www.youtube.com/watch?v=WkBPX-oDMnA | 에이전트가 만든 결과물을 사람이 이해하도록 돕는 방법(설명 문서, 퀴즈, 마이크로월드). 교육학·인지과학 아이디어를 가져옴 | 개발자·디자인 엔지니어. 연구자에게도 시사점 큼 | 147,702 |
| E10 | Building Great Agent Skills: The Missing Manual | Matt Pocock | AI Engineer / AIE World's Fair 2026 (사전 녹화 발표) | 2026-06-29 | 20:43 | 영어 | https://www.youtube.com/watch?v=UNzCG3lw6O0 | 스킬 점검표 4단계(trigger, structure, steering, pruning). SKILL.md를 작게 유지하고 참조 자료는 필요할 때 불러오도록 분리 | Skills를 만드는 개발자·팀 | 181,329 |
| E11 | Field Guide to Fable | Thariq Shihipar (Anthropic) | AI Engineer / AIE World's Fair 2026 | 2026-07-06 | 19:28 | 영어 | https://www.youtube.com/watch?v=9fubhllmsBU | 최신 모델 세대에서는 무거운 지시문이 오히려 모델을 묶는다는 관점. Claude Code 시스템 프롬프트 80% 삭제 사례 | Claude 사용자·개발자 | 179,968 |
| E12 | How I use LLMs | Andrej Karpathy | Andrej Karpathy 개인 채널 | 2025-02-27 | 2:11:12 | 영어 | https://www.youtube.com/watch?v=EWvNQjAaOHw | 일반 청중용 시리즈. 화면을 띄워 놓고 실제 사용 예시로 LLM 도구(검색, 딥리서치, 파일 업로드, 코드 실행, 메모리)를 하나씩 보여줌 | 일반인·비개발자 | 2,755,181 |

## B. 영어 영상: 보조 7개

| # | 제목 | 연사 | 채널 / 행사 | 게시일 | 길이 | URL | 한 줄 요약 | 대상 청중 |
|---|---|---|---|---|---|---|---|---|
| E13 | Claude for Long-Horizon Tasks | Lance Martin (Anthropic) | AI Engineer / AIE World's Fair 2026 | 2026-07-22 | 25:18 | https://www.youtube.com/watch?v=9QebvrrY3KY | 장시간 작업용 하네스 설계: 두뇌와 손의 분리, 자기 검증, "dreaming"(오프라인 메모리 정리) | 에이전트 개발자 |
| E14 | Boris Cherny: We Cut 80% of Claude Code's Prompt | Boris Cherny, Diana Hu(진행) | Y Combinator / Startup School 2026 | 2026-07-27 | 35:51 | https://www.youtube.com/watch?v=qyPCVqFUyDo | 대담 형식. 시스템 프롬프트를 줄인 이유와 다시 설계하는 방법, 프롬프트 엔지니어링의 변화. 설명란에 공식 트랜스크립트 링크 있음 | 창업자·개발자 |
| E15 | Context Management in Claude Code | Anthropic (Claude 채널) | Claude 공식 채널 / Anthropic 강좌 일부 | 2026-05-18 | 3:30 | https://www.youtube.com/watch?v=eW3oTyfeWZ0 | 컨텍스트를 Claude의 작업 기억으로 설명하고 /compact와 /clear의 사용 시점을 안내하는 짧은 공식 강의 (설명란만 확인) | 입문자 |
| E16 | Claude Code for Non-Coders (6 Hour Course) | Nate Herk | Nate Herk \| AI Automation | 2026-07-11 | 5:58:59 | https://www.youtube.com/watch?v=jdbOVepEtUE | 비개발자 대상 장편 강좌. 모델=엔진, 하네스=자동차, 사람=운전자 비유와 인턴 온보딩 비유로 컨텍스트 개념 설명 | 비개발자 지식노동자 |
| E17 | Claude Code for Researchers | Research Solutions (scite) | Research Solutions 웨비나 | 2026-06-23 | 1:01:08 | https://www.youtube.com/watch?v=ydVB6Fke0VA | scite MCP를 Claude Code에 연결해 문헌 검증, 연구 공백 탐색, 대시보드 제작을 라이브로 시연 (벤더 웨비나. 설명란만 확인, 트랜스크립트 미확인) | 연구자 |
| E18 | Advanced Context Engineering for Agents | Dex Horthy | YC Root Access (같은 녹화가 Chroma 채널에도 있음: https://www.youtube.com/watch?v=VvkhYWFWaKI) | 2025-08-25 | 14:37 | https://www.youtube.com/watch?v=IS_y40zY-hc | E1의 앞선 버전. 12-factor에서 intentional compaction, subagent, RPI로 이어지는 흐름. 챕터 제공 | AI 엔지니어 |
| E19 | Code with Claude 2026: Opening Keynote | Ami Vora, Cat Wu, Boris Cherny 외 | Claude 공식 채널 / Code with Claude SF 2026 | 2026-05-06 | 47:29 | https://www.youtube.com/watch?v=GMIWm5y90xA | Anthropic 공식 행사 기조연설. 제품 발표 중심 | 개발자 전반 |

---

## C. 한국어 영상: 핵심 8개

| # | 제목 | 연사 | 채널 / 행사 | 게시일 | 길이 | 언어 | URL | 한 줄 요약 | 대상 청중 | 조회수 |
|---|---|---|---|---|---|---|---|---|---|---|
| K1 | (트랙2) Claude Code 기초 / 황민호 / 260429 | 황민호 (카카오, 소속은 K16 설명란 근거 추정) | 한국과학기술연구원(KIST) / 사내 AI 교육 트랙2 "바이브코딩 인텐시브" 1회차 | 2026-04-29 | 2:09:00 | 한국어 | https://www.youtube.com/watch?v=pHfDgZ7cll0 | 연구원 대상 실습형 기초 강의. 참석자가 함께 따라 하며 조사 보고서, 웹사이트, 논문 소개 사이트, 디자인 스킬을 만듦 | 연구기관 연구자·보직자·행정직 (비개발자 포함) | 19,911 |
| K2 | Claude Code Harness 심화 / 황민호 / 260527 | 황민호 (카카오, 추정) | KIST / 트랙2 3회차 | 2026-05-27 | 2:02:34 | 한국어 | https://www.youtube.com/watch?v=iqoPgoYBVaM | 하네스를 AI가 일하는 시스템의 설계로 정의. 청중에게 연구 주제를 받아 하네스 적용 전후를 라이브로 비교. 컨텍스트를 주방 작업대에 비유 | KIST 연구자 (K1 수강자) | 27,306 |
| K3 | (트랙2) Claude Code Skill 심화 / 김태영 / 260512 | 김태영 (인공지능팩토리, K16 진행자와 동일인 추정) | KIST / 트랙2 2회차 | 2026-05-12 | 2:24:12 | 한국어 | https://www.youtube.com/watch?v=Mw8SnA_xgQo | 스킬의 구조(메타데이터, 지침, 리소스)를 도서관 책 표지 비유로 설명. 기관 브랜드 가이드 스킬 설치 실습, 온라인 질문 응답 | KIST 연구자 | 10,932 |
| K4 | 하네스 엔지니어링, 9달러 vs 200달러의 비밀 (클로드 코드) | 짐코딩 | 짐코딩 (유튜브) | 2026-04-11 | 15:10 | 한국어 | https://www.youtube.com/watch?v=6cr4PeilKJk | 프롬프트, 컨텍스트, 하네스로 이어지는 개념 변화. Anthropic 실험 사례로 도입하고 Claude Code 설정 6가지(CLAUDE.md, 권한, 훅, MCP, 서브에이전트, 진화)로 정리 | Claude Code 입문~중급 | 36,753 |
| K5 | 메타 엔지니어의 클로드코드 완벽 가이드 [실전편] — 컨텍스트 관리, 실전 워크플로우 20분 총정리 | 실밸개발자 | 실밸개발자 (유튜브) | 2026-03-11 | 21:35 | 한국어 | https://www.youtube.com/watch?v=DCsv0rKKrN4 | 세컨드 브레인, lazy loading(CLAUDE.md에는 참조만), 한 세션에 기능 하나, MCP 토큰 관리 등 컨텍스트 관리 팁 모음. 노션 치트시트 제공 | Claude Code 사용 개발자 | 44,016 |
| K6 | Context Engineering에 대하여 (2025.7) | 안상진 (인제의대 약리학교실) | MahlerLab (유튜브) | 2025-07-01 | 15:57 | 한국어 | https://www.youtube.com/watch?v=5w9KiIbei1c | 의대 교수가 설명하는 컨텍스트 엔지니어링. 문맥 실패 4가지 유형과 대응, 마지막에 일반인을 위한 교훈(대화 편집, 요약 문서로 새 세션 시작) | 일반인·연구자 | 1,716 |
| K7 | 코딩 1도 모르는 직장인을 위한 Claude Code 시작 가이드 | 일잘러 장피엠 | 일잘러 장피엠 (유튜브) | 2026-02-13 | 43:34 | 한국어 | https://www.youtube.com/watch?v=C6xlOsQFyOQ | 비개발자가 "내 업무를 언어로 설명하는 능력"만으로 에이전트를 만드는 5단계. 논문 번역 에이전트와 블로그 작성 에이전트를 처음부터 만들어 보임 | 비개발자 직장인 | 197,788 |
| K8 | Anthropic이 시스템 프롬프트 80%를 지운 이유 (클로드 5세대의 새로운 컨텍스트 엔지니어링 규칙) | 김플립 | 김플립 - LLM 코딩 (유튜브) | 2026-08-11 | 9:28 | 한국어 | https://www.youtube.com/watch?v=TWo-lXNbcws | Anthropic 엔지니어 Thariq가 공개한 최신 컨텍스트 엔지니어링 규칙 6가지를 신입사원 매뉴얼 비유로 정리 | Claude 사용자 전반 | 17,443 |

## D. 한국어 영상: 보조 8개

| # | 제목 | 연사 | 채널 / 행사 | 게시일 | 길이 | URL | 한 줄 요약 | 대상 청중 |
|---|---|---|---|---|---|---|---|---|
| K9 | "Research X AI: Quick Talk Series" Claude를 활용한 논문 작성 사례 소개 | 윤종희 (아주대 물리학과 교수) | 아주대학교 에너지시스템학과 | 2026-05-27 | 9:03 | https://www.youtube.com/watch?v=ZMZFW2h3M4M | 연구실 대상 10분 발표. 논문 작성과 리비전(리뷰 코멘트 반영, 변경 부분 표시)에 Claude를 쓴 경험 | 대학원생·연구자 |
| K10 | 사람과 AI Agent를 위한 통합 Context Provider 구축 | 신동걸, 심효진 (네이버) | NAVER D2 / NAVER ENGINEERING DAY 2026 | 2026-06-21 | 13:26 | https://www.youtube.com/watch?v=0VdAZCYBwSU | 에이전트가 엉뚱한 답을 한 사례에서 시작해 팀 데이터 자산의 메타데이터를 에이전트에 공급하는 플랫폼 구축기. 데모 포함 | 사내 개발자 |
| K11 | 하네스 엔지니어링 40분 개념 정리 \| 클로드 코드 × 코덱스 | 전현준 | 패스트캠퍼스 | 2026-04-07 | 38:02 | https://www.youtube.com/watch?v=5buNm0pA1mg | 같은 모델인데 결과가 다른 이유를 환경(하네스)에서 찾음. 3가지 핵심 설계, Claude와 Codex 비교 | 개발자 |
| K12 | 하네스/루프/그래프 엔지니어링, 순서대로 이해하기 [with Noto] | sudoremove, Noto | sudoremove (유튜브) | 2026-08-05 | 41:28 | https://www.youtube.com/watch?v=lokHQ8_b5Rk | 2023년 Auto-GPT부터 context engineering, 하네스, 루프, 그래프까지 용어의 변천을 대담으로 정리. 발표자료 공개 | 개발자 (중급 이상) |
| K13 | Claude Code 왕초보 입문 튜토리얼 23가지 팁 | AI싱크클럽 | AI싱크클럽 (유튜브) | 2026-02-11 | 47:37 | https://www.youtube.com/watch?v=1_bRmkUvjHA | 23가지 팁을 3단계(기초, 중급, 고급 맛보기)로 나눈 체크리스트형 강의. /context, /compact, HANDOFF.md 포함 | 입문자·비개발자 |
| K14 | [전체강의 통합본] 클로드 코드 2시간 안에 마스터하기 | 실밸개발자 | 실밸개발자 (유튜브) | 2026-03-21 | 1:34:27 | https://www.youtube.com/watch?v=vxEvo2BLM6A | K5를 포함한 입문, 실전, 심화 3부작 통합본. 파트마다 하이라이트, 인트로, 요약 구조 | 입문~중급 |
| K15 | [강수진 X 테디노트] 2025 프롬프트 엔지니어링, Context Engineering & Agent Orchestration | 강수진 (더 프롬프트 컴퍼니), 테디노트 | 테디노트 TeddyNote (라이브) | 2026-03-11 | 3:32:25 | https://www.youtube.com/watch?v=b8GfaOVRqH8 | 국내 프롬프트 엔지니어의 3시간 라이브. 프롬프트에서 컨텍스트, 에이전트 오케스트레이션으로 확장 | 개발자·실무자 |
| K16 | AI Co-Scientist를 위한 가상 연구실(Lab) 구축: Claude Code로 끝내는 에이전트 인터페이스 | 황민호 (카카오) | 인공지능팩토리(AIFactory) / 2026 AI Co-Scientist Challenge Korea 연계 세미나 | 2025-12-31 | 1:19:19 | https://www.youtube.com/watch?v=Pz1rM5jjw1w | 과학 연구용 AI 동료(Co-Scientist)와 소통하는 웹 인터페이스를 Claude Code로 빠르게 만드는 과정 | 과학기술 연구자, 경진대회 참가자 |

---

## 확인하지 못했거나 제외한 것

- "Context Engineering for High-Leverage Coding Agents"(채널 Learn by Doing with Steven, https://www.youtube.com/watch?v=4Cr3CKuCUoA): Dex Horthy 강연을 다시 올린 것으로 보이고 조회수가 매우 적어 제외했다.
- "The Creator of Claude Code Teaches You How to Actually Use It"(채널 JawcoAI, https://www.youtube.com/watch?v=jsoKH4Pvld0): 설명란은 Boris Cherny 워크숍이라고 하지만 원 출처가 명시되지 않은 재게시물로 보여 뺐다.
- Code with Claude 2026의 개별 세션(19개): 키노트(E19)만 직접 확인했다. 나머지는 확인하지 않았다.
- 한국어 자동 자막은 고유명사 인식 오류가 많다(예: "클로드"가 다른 단어로 표기됨). 한국어 영상 분석은 자막의 흐름과 설명란 챕터를 근거로 했고, 세부 표현은 틀릴 수 있다.
