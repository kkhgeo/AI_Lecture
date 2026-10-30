# 숙련도별 이질적 효과: 누가 AI로 더 이득을 보는가 (Heterogeneous effects by skill)
- **저자/기관**: Brynjolfsson·Li·Raymond (Stanford/MIT, QJE); Dell'Acqua 외 (HBS·BCG); Noy & Zhang (MIT, Science); Otis·Clarke·Delecourt·Holtz·Koning (Berkeley·HBS, Management Science); Toner-Rodgers (MIT, 철회 요청); METR; Google DORA; Anthropic
- **발행일**: 2023-07 ~ 2026-01 (2026-09-30 열람)
- **URL**:
  - https://www.nber.org/papers/w31161 (Generative AI at Work → QJE 140(2), 2025)
  - https://papers.ssrn.com/abstract=4573321 (Jagged Frontier, HBS WP 24-013, 2023; 이후 Organization Science 게재)
  - https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1_0.pdf (Science 2023)
  - https://www.hks.harvard.edu/centers/cid/publications/uneven-impact-generative-ai-entrepreneurial-performance
  - https://economics.mit.edu/news/assuring-accurate-research-record (MIT의 Toner-Rodgers 논문 불신임 성명)
  - https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
  - https://dora.dev/research/2025/dora-report/
  - https://www.anthropic.com/research/economic-index-primitives (2026-01-15)
- **자료 유형**: 논문 + 보고서 + 기사

## 핵심 요약
- **Brynjolfsson·Li·Raymond, "Generative AI at Work" (NBER WP 2023-04, QJE 2025)**: 고객상담원 5,179명(QJE 본문 표기 약 5,172명). 시간당 해결 건수 **평균 +14%**(QJE판 요약은 약 15%로 보도됨), **신입·저숙련 +34%**, 숙련·고숙련자는 효과 미미(속도 소폭↑, 품질 소폭↓). AI가 우수 상담원의 노하우를 확산시키고 "학습"을 일으켰을 가능성을 제시.
- **Dell'Acqua 외, "Navigating the Jagged Technological Frontier" (HBS WP 2023-09)**: BCG 컨설턴트 758명 사전등록 실험. 프런티어 **안쪽** 과업에서 과업 12.2%↑, 속도 25.1%↑, 품질 40% 이상↑. **평균 이하 집단 +43%, 평균 이상 집단 +17%**. 프런티어 **바깥** 과업에서는 AI 사용자가 정답을 낼 확률이 **19%p 낮음**.
- **Noy & Zhang (Science, 2023-07)**: 대졸 전문직 453명 글쓰기 과제. 소요 시간 −40%, 품질 +18%, **작업자 간 격차 축소**(저성과자가 더 많이 개선).
- **Otis 외 (케냐 창업자 640명, WhatsApp GPT-4 멘토, Management Science)**: 평균 효과는 거의 0이지만 **고성과자 약 +15%(일부 보도 15–20%), 저성과자 약 −8%**. 저성과자는 더 어려운 문제를 AI에 물었고 조언을 실행으로 연결하지 못함 → **AI가 격차를 벌림**.
- **Toner-Rodgers (재료과학 R&D, arXiv 2024-11)**: "상위 과학자가 가장 큰 이득, 하위 1/3은 거의 이득 없음"을 보고해 "AI는 전문가를 증폭한다"의 대표 근거로 쓰였음. 그러나 **MIT가 2025-05-16 성명에서 데이터의 출처·신뢰성·타당성을 신뢰할 수 없다고 밝히고 arXiv 철회를 요청**, QJE 투고도 철회됨. **강연에서 근거로 사용 금지**, 쓴다면 "철회된 연구의 교훈"으로만.
- **METR (2025-07)**: 숙련 오픈소스 개발자 16명·246개 과업 RCT. AI 사용 시 **19% 더 느림**, 본인들은 24% 빨라질 것으로 예측했고 사후에도 약 20% 빨라졌다고 믿음. 2025년 말 후속 실험에서 복귀 개발자는 약 18% 속도 향상 추정(CI −38%~+9%), 신규 개발자 약 4%(−15%~+9%)로 개선됐으나, AI 없이 일하기를 거부하는 참가자 이탈로 측정 자체가 편향 → METR는 설계 변경 발표. **"전문가가 AI로 항상 더 이득"도 아님**.
- **Google DORA 2025 보고서 (약 5,000명 기술 전문가)**: 핵심 결론은 **"AI는 증폭기(amplifier)"** — 고성과 조직의 강점과 부진 조직의 기능 장애를 모두 증폭. 조직 수준 결과이지 개인 숙련도 실험은 아님.
- **Anthropic Economic Index (2026-01-15)**: 대화 100만 건 분석. 과업 요구 교육 연수가 높을수록 AI 속도 향상은 커지고(대졸 수준 약 12배 vs 고졸 수준 약 9배) 성공률은 다소 낮아짐(약 66% vs 70%). 사용자 전문성과 결과 간 인과 계수는 제시되지 않음.
- **Anthropic 코딩 기술 형성 RCT (2026-01)**: 같은 AI를 써도 "개념 질문형" 사용자는 퀴즈 65% 이상, "전면 위임형"은 40% 미만. 숙련도보다 **사용 방식**이 학습 결과를 가름(04·06 파일 참조).

## 핵심 개념·용어 정의
- **평준화(leveling / compression) 효과**: AI가 저숙련자의 산출을 더 크게 끌어올려 격차를 줄이는 현상 (Brynjolfsson, Noy & Zhang, Dell'Acqua).
- **증폭(amplification) 효과**: 기존 역량·조직 역량이 높은 쪽이 AI로 더 큰 이득을 보는 현상 (Otis, DORA).
- **들쭉날쭉한 프런티어(jagged frontier)**: 비슷해 보이는 과업도 AI가 잘하는 쪽과 못하는 쪽으로 불규칙하게 나뉜다는 개념. 프런티어 밖에서 AI를 믿으면 성과가 떨어짐.
- **산출(output) 효과 vs 역량(skill) 효과**: 대부분의 평준화 연구는 "AI를 켠 상태의 산출"을 측정. AI를 끈 뒤의 역량 변화는 별개 문제.

## 비판론(skeptic)과 반론의 대응
- **강연자 믿음에 불리한 점**: 가장 견고한 대규모 연구들(QJE, Science, BCG)은 **산출 기준으로 저숙련자가 더 많이 이득**을 본다. "상위 집단이 더 얻는다"를 가장 강하게 보여준 재료과학 연구는 **MIT가 불신임**했다. METR은 숙련 개발자가 오히려 느려진 경우를 보였다.
- **강연자 믿음에 유리한 점**: (1) Otis 케냐 연구 — 고성과자만 이득, 저성과자는 손해. (2) Dell'Acqua — 프런티어 바깥에서 AI를 맹신하면 손해, 즉 **과업이 AI 경계 밖인지 판단하는 역량**이 필요하고 이것은 전문성에 가깝다. (3) DORA — 조직 수준에서 증폭. (4) Brynjolfsson — 고숙련자는 산출이 거의 안 늘었지만 **품질이 소폭 떨어짐**. 이는 "상위 집단은 AI를 써도 떨어지지 않는다"는 주장도 제약한다.
- **정리**: 증거는 **혼재(mixed)**. 정형화된 과업의 산출에서는 평준화, 비정형·복잡·판단이 필요한 과업과 학습(역량 형성)에서는 기초 역량과 사용 방식이 좋은 쪽이 유리하다는 신호가 있다. "상위 집단의 **능력 자체가 증가**한다"를 직접 보여준 견고한 인과 연구는 현재 찾기 어렵다.

## 강연에 쓸 만한 포인트
- 인용(Dell'Acqua 외 개념어): "jagged technological frontier" — AI 능력의 경계는 매끈하지 않다.
- 그림 아이디어: 2×2 매트릭스 — 가로축 "과업이 정형적 ↔ 비정형·판단 필요", 세로축 "산출 측정 ↔ 역량(학습) 측정". 왼쪽 위(정형·산출): 평준화(Brynjolfsson +34% vs 미미, Noy&Zhang, BCG +43% vs +17%). 오른쪽(비정형): 증폭·역효과(Otis +15% vs −8%, BCG 프런티어 밖 −19%p, METR −19%).
- 슬라이드 노트 경고: Toner-Rodgers는 MIT 불신임(2025-05) — 인용하지 말 것.

## 원본 그림
- Dell'Acqua 외 숙련도별 성과 분포 그림 — 이미지 URL 없음(HBS WP 원문 참조)
- Brynjolfsson 외 경력별 생산성 효과 그래프 — 이미지 URL 없음(NBER w31161 원문 참조)
- DORA 2025 "AI as amplifier" 인포그래픽 — 없음(https://dora.dev/research/2025/dora-report/ 참조)
