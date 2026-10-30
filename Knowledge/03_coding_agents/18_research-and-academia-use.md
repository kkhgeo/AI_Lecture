# 연구자·대학원생의 코딩 에이전트 활용과 위험 (Research & academia use)

- **저자/기관**: Anthropic(Lyttelton·Massenkoff·Wilmers 사회과학자 설문; Mishra-Sharma 장기 실행 과학계산 사례); Nature Correspondence(Huiquan Zhang 외, University of Macau); Nature Machine Intelligence·Nature Methods 편집 기사; Harvard·Columbia·Cornell 대학 지침
- **발행일**: Anthropic 장기 실행 Claude 사례 2026-03-23; 사회과학자 설문 2026-05-27; Nature Correspondence 2026-05(정확한 일자 미확인); Claude Science 출시 2026-06-30 (2026-09-29 열람)
- **URL**:
  - https://www.anthropic.com/research/coding-agents-social-sciences
  - https://www.anthropic.com/research/long-running-Claude
  - https://www.nature.com/articles/d41586-026-01440-9 (Correspondence, 본문 유료벽 — 대학 보도자료로 요지 확인: https://www.um.edu.mo/news-and-press-releases/press-release/detail/64149/)
  - https://www.nature.com/articles/s42256-026-01219-7 (Nature Machine Intelligence, 재현성·코드 리뷰 가능성 — 본문 미열람)
  - https://www.nature.com/articles/s41592-026-03088-9 (Nature Methods "Call your AI agent" — 본문 미열람)
  - https://www.technologyreview.com/2026/06/30/1139987/claude-science-is-anthropics-newest-flagship-product/
  - https://www.huit.harvard.edu/ai/guidelines
  - https://provost.columbia.edu/content/office-senior-vice-provost/ai-policy
  - https://research-and-innovation.cornell.edu/generative-ai-in-academic-research/
  - https://arxiv.org/abs/2506.20463 (대학 AI 지침의 프라이버시·보안 분석)
- **자료 유형**: 보고서 | 기사 | 공식문서

## 핵심 요약
- **사회과학자 설문**(Anthropic, 2026-05-27; 계량 사회과학자 1,260명, 2026-02~03 조사): 81%가 AI 챗봇을 연구에 써봤지만, 코딩 에이전트를 주 1회 이상 쓰는 비율은 20%. 에이전트 사용자 중 86%가 Claude Code. 에이전트 사용자의 97%가 데이터 분석 코드 생성에 사용.
- 격차: 박사과정·포스닥 27% vs 정년 교수 13% 미만, 상위 25개 대학 소속은 40% 더 높고, 남성형 이름 연구자가 여성형 이름보다 2배 이상 사용. 에이전트 사용자는 워킹페이퍼 게시가 75% 많았으나 저널 투고에서는 아직 유의한 차이 없음. (저자 소속이 도구 개발사라는 이해상충 유의)
- **장기 실행 과학계산 사례**(Anthropic, 2026-03-23): Claude Opus 4.6이 며칠에 걸쳐 JAX 기반 미분가능 우주론 Boltzmann solver를 구현, 기준 코드(CLASS)와 sub-percent 수준 일치. 핵심 습관: CLAUDE.md(계획·설계결정), CHANGELOG.md(진행 기록·실패한 접근), 기준 구현을 test oracle로 사용, 작업 단위마다 git commit, HPC(SLURM) 실행. 저자는 결과물이 프로덕션 수준이 아니며 전문가라면 즉시 잡을 기초 실수도 있었다고 명시.
- **Nature Correspondence**(2026-05): 연구책임자가 에이전트로 문헌 검토·디버깅을 빠르게 처리하면서, 학생이 시행착오·방법 보정·오류 해결을 통해 배우던 **도제식 훈련(apprenticeship)**이 약화될 수 있다고 경고.
- **재현성**: Nature Machine Intelligence(2026) 등은 LLM 활용으로 논문·코드가 급증하는 상황에서 코드의 리뷰 가능성·문서화·공개가 더 중요해졌다고 지적(본문 미열람, 검색 요약 기준). 에이전트가 만든 코드는 의존성 누락 등으로 재현이 안 되는 경우가 보고됨.
- **대학 지침 공통점**(Harvard·Columbia·Cornell 등): 비공개 연구데이터·인간대상 연구의 식별 정보·학생/의료 기록을 기관 승인 없는 공개 AI 도구에 넣지 말 것; 기존 연구윤리·학문적 정직성 규정이 그대로 적용; 규칙은 과목·학과·연구실 단위로 달라질 수 있음.
- **Claude Science**(2026-06-30 출시, MIT Technology Review 보도): 연구자용 AI 워크벤치로, 계산생물학·문헌검색·원고 작성 도구를 통합했다고 소개. (제품 홍보 성격)

## 핵심 개념·용어 정의
- **Test oracle**: 정답을 알려주는 기준(예: 검증된 기존 구현, 해석해). 에이전트 산출물 검증의 핵심.
- **Hallucinated code**: 존재하지 않는 API·함수·패키지 인자나 잘못된 통계 절차를 그럴듯하게 생성하는 현상.
- **Slopsquatting**: AI가 환각한 패키지 이름을 공격자가 선점 등록해 악성 코드를 설치시키는 공급망 공격(개념 소개, 이 파일에서 별도 사례 수치 미확인).
- **Apprenticeship(도제 학습)**: 지도교수·선배 곁에서 실제 연구 과정을 반복하며 판단력을 익히는 학습 방식.
- **Data governance**: 데이터 분류(공개/내부/민감)에 따라 어떤 도구·계정·지역에서 처리할 수 있는지 정한 규칙.

## 강연에 쓸 만한 포인트
- 대학원생 체크리스트: ① 데이터 등급 확인(IRB·개인정보) ② 분석 코드엔 기준값·단위테스트(작은 합성데이터로 결과 검증) ③ 모든 변경 git 기록 ④ 논문 방법 섹션에 AI 사용 명시 ⑤ "내가 설명 못 하는 코드는 논문에 넣지 않는다".
- 숫자: "사회과학자 81% 챗봇 경험, 20%만 에이전트"(2026-02~03) — 강의 청중 대부분이 아직 초입 단계임을 보여줌.
- 사례 스토리: "몇 달 걸릴 수치 코드를 며칠에" + "그러나 전문가가 보면 초보적 실수" — 속도와 검증의 균형.
- 토론 질문: "에이전트가 대신 디버깅해주면, 나는 무엇을 배우는가?"(Nature Correspondence 논점)
- 인용(1개): Anthropic 사례는 CHANGELOG를 "portable long-term memory"로 표현(Anthropic, 2026-03-23).

## 원본 그림
- Anthropic 사회과학자 설문 페이지 그림 — 이미지 직접 URL 미확인(페이지 https://www.anthropic.com/research/coding-agents-social-sciences 에서 확인 필요)
- Anthropic 장기 실행 Claude 사례 그림(정확도 추이 등) — 이미지 직접 URL 미확인(페이지에서 확인 필요)
- Nature 기사 — 없음(유료벽)

## Claude Code와의 연결점
- 사회과학자 에이전트 사용자의 86%가 Claude Code → 강의 청중(대학원생)에게 가장 현실적인 도구.
- 장기 실행 사례의 CLAUDE.md·CHANGELOG·test oracle·git 습관은 Claude Code 기능(메모리 파일, 서브에이전트, hooks, 권한)으로 바로 실습 가능.
- 데이터 프라이버시: Claude Code는 로컬 파일을 읽어 모델 API로 전송하므로, 민감 데이터 폴더는 권한 설정(deny 규칙)·샌드박스로 제외하고 기관 계약(Enterprise/학교 라이선스) 여부를 확인해야 함(19번 파일).
