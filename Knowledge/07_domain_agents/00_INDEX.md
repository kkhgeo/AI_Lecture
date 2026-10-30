# 07_domain_agents 자료 색인

- 수집일: 2026-10-23
- 주제: 도메인 특화 AI 에이전트 — 개념과 용어, 업계 패키지, 과학 분야 사례, 서베이, 종합 (AI 에이전트 장 다음에 이어질 내용)
- 수록: 7개 파일
- 저작권: 요약·재서술 중심, 직접 인용은 파일당 1개(15단어 미만)

## 1. 자료 목록

### A. 개념과 업계
| 파일 | 한 줄 설명 |
|---|---|
| 01_concept-and-terminology.md | 개념은 있고 이름은 여럿: domain specialization(Ling et al., ACM CSUR 2025, DOI 10.1145/3764579), scientific/specialized/vertical agents, YC Lightcone(2024-11-22), 범용 vs 특화 |
| 02_vertical-agents-industry.md | Anthropic 금융 템플릿 10종(skill + connector + subagent, 2026-05-05), Claude for Financial Services·Life Sciences, Agent Skills, Harvey·Abridge(자기소개 기준) |

### B. 과학 분야 사례
| 파일 | 한 줄 설명 |
|---|---|
| 03_chemcrow.md | 화학: GPT-4 + 도구 18개 + ReAct, RoboRXN 실합성 4건, GPT-4 평가자는 유창성에 속음, 화학무기 목록 대조 |
| 04_coscientist.md | 화학 실험: GPT-4 Planner + 검색·코드·장비 제어, OT-2 교차결합, 베이지안 최적화보다 우수, 코드 비공개(안전) |
| 05_biomni.md | 생의학: 문헌에서 캐낸 도구 150·소프트웨어 105·DB 59, CodeAct, 벤치마크, Science 게재(2026-07-09, 보도로 확인), 지구·GIS 에이전트 짧은 목록 |

### C. 서베이와 종합
| 파일 | 한 줄 설명 |
|---|---|
| 06_scientific-agent-surveys.md | Ren et al. 4요소(Planner·Memory·Action Space·Verifier)와 범용 대비 네 가지 차이, 지구·환경·기후 사례 목록, Zheng et al. 자율성 3단계(Tool·Analyst·Scientist) |
| 07_synthesis.md | 강연용 정의, 범용 vs 특화 비교표, "하네스 쪽을 바꿔 끼우기", 8번 그림과의 연결, 주의점 4가지, 슬라이드 구성안 |

## 2. 슬라이드 연결
- 뼈대: 07번 종합. 정의 → 사례 → 만들기(Claude Code: CLAUDE.md·skills·MCP) → 주의점.
- 8번 AI 에이전트 그림의 둘째 칸(Memory·Skills·Tools)을 도메인 것으로 바꾸는 그림으로 이어 붙인다.

## 3. 확인하지 못한 것
- YC Lightcone 영상 본편(10배 발언·발언자는 2차 보도로만 확인), Wang et al. "Hitchhiker's Guide"의 Assistant·Partner·Avatar 단계(원문 403).
- Biomni Science 게재본의 최종 수치(모든 수치는 프리프린트 기준), Biomni 자체 구동 LLM.
- Ren et al.이 든 지구·환경 에이전트 개별 논문(GeoAgent, ClimateGPT 등)은 미열람.
