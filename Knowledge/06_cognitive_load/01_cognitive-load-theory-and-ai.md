# Cognitive Load Theory와 생성형 AI (인지 부하 이론의 적용)
- **저자/기관**: 이론 원전 — John Sweller (UNSW); Nelson Cowan (Univ. of Missouri); Evan F. Risko & Sam J. Gilbert (Waterloo / UCL). 적용 연구 — Bastani et al. (Wharton/Penn, PNAS 2025); Kosmyna et al. (MIT Media Lab, 2025 preprint); Gerlich (SBS Swiss Business School, 2025); Paul Kirschner (2026 에세이)
- **발행일**: Sweller 1988 / Sweller·van Merriënboer·Paas 1998·2019; Cowan 2001; Risko & Gilbert 2016; 적용 연구 2025–2026 (2026-10-01 열람)
- **URL**:
  - Risko & Gilbert (2016) Cognitive offloading, *Trends in Cognitive Sciences* 20(9):676–688 — https://discovery.ucl.ac.uk/id/eprint/1508770/
  - Bastani et al. (2025) Generative AI without guardrails can harm learning, *PNAS* 122(26) — https://papers.ssrn.com/abstract=4895486
  - Kosmyna et al. (2025) Your Brain on ChatGPT — https://www.media.mit.edu/publications/your-brain-on-chatgpt/ , https://www.brainonllm.com/
  - Gerlich (2025) AI Tools in Society, *Societies* 15(1) — https://doaj.org/article/d5c17dd91ce64775a065095d8af730ce
  - Kirschner (2026-01-13) Offloading, no outsourcing — https://paulkirschner173727.substack.com/p/offloading-no-outsourcing
  - Microsoft New Future of Work Report 2025 (MSR-TR-2025-58), p.50 — https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf
- **자료 유형**: 논문 (이론 + 실증) / 보고서 / 에세이

## 핵심 요약
- **CLT의 출발점**: working memory는 용량과 지속 시간이 제한되어 있고, long-term memory는 사실상 무제한이다. 학습이란 working memory의 처리를 거쳐 long-term memory에 schema를 쌓는 일이다 (Sweller 1988, *Cognitive Science* 12:257–285; 이후 Sweller, van Merriënboer & Paas 1998·2019 *Educ. Psych. Review*).
- **용량의 크기**: Miller(1956)의 "7±2" 대신, Cowan(2001, *Behavioral and Brain Sciences* 24:87–185)은 리허설·청킹을 막으면 동시에 유지되는 단위가 **약 3–5 chunk(대략 4개)** 라고 정리했다.
- **세 가지 부하**: intrinsic(과제 자체의 요소 상호작용), extraneous(나쁜 설계·불필요한 탐색에서 오는 부하), germane(schema 형성에 쓰이는 부하). 후기 CLT(2019)는 germane을 독립 부하라기보다 "intrinsic 처리에 배분된 working memory 자원"으로 재정의했다 — 강연에서는 3분류로 단순화해도 무방.
- **AI와 CLT의 기본 가설**: 생성형 AI는 검색·서식·보일러플레이트 같은 extraneous load를 크게 덜어 주지만, 사용자가 사고 과정 자체를 넘기면 germane 처리(=학습)도 함께 사라진다. 2025년 교육 분야 리뷰들이 이 구도를 반복해서 제시한다 (예: 2025 Open & Distance Learning 학회 통합 리뷰; 단, 이 계열 리뷰 다수는 소규모·자기보고 기반이므로 근거 강도는 중간).
- **실험 증거 1 (Bastani et al., PNAS 2025)**: 터키 고교생 약 1,000명 현장실험. GPT-4 접근 시 연습 문제 성적은 GPT Base +48%, GPT Tutor(정답을 바로 주지 않는 힌트형) +127%. 그러나 AI를 회수한 뒤 시험에서 GPT Base 집단은 **대조군보다 17% 낮았다**. 힌트형 Tutor는 이 손실을 대부분 상쇄.
- **실험 증거 2 (Kosmyna et al., MIT, 2025-06 preprint)**: 54명, 에세이 작성을 LLM / 검색엔진 / 도구 없음 세 조건으로 3회 수행, 4회차에 18명이 조건 교차. EEG 뇌 연결성은 도구 없음 > 검색 > LLM 순으로 약했고, LLM 집단은 방금 쓴 에세이를 인용하는 능력과 소유감이 낮았다. **저자 스스로 peer review 전이며 예비 결과라고 명시** — 강연에서 인용 시 이 단서를 붙일 것.
- **상관 증거 (Gerlich, Societies 2025)**: 666명 설문 + 50명 인터뷰. AI 사용 빈도와 critical thinking 점수 사이 음의 상관, cognitive offloading이 매개. 젊은 층에서 의존이 높음. 저자도 인과는 확립되지 않았다고 명시 (구체적 상관계수는 2차 기사에서 확인 못 함 — 원문 확인 필요).
- **Offloading의 정의 (Risko & Gilbert 2016)**: 과제의 정보처리 요구를 바꿔 인지적 부담을 줄이려고 신체 행위를 쓰는 것(예: 머리를 기울여 회전된 글자 보기, 휴대폰 알림 설정). 이 자체는 합리적인 전략이며, 사람은 자기 기억에 대한 메타인지적 확신이 낮을 때 더 많이 offload한다.
- **Microsoft NFW 2025 정리**: 생성형 AI는 노력의 위치를 '해 보면서 생각하기'에서 '산출물 중에서 고르기'로 옮기며, 업스킬링 없이는 deskilling 위험이 있다. 동시에 사람들은 무조건 최대한 offload하지 않고 상황별 비용-편익을 따진다(Grinschgl & Neubauer 2022 인용).

## 핵심 개념·용어 정의
- **Working memory**: 지금 의식적으로 붙잡고 조작하는 정보의 작업대. 용량 약 4 chunk (Cowan 2001), 리허설 없이는 수십 초 안에 소실.
- **Chunk**: 경험으로 하나로 묶인 정보 단위. 전문가는 같은 코드를 더 큰 chunk로 본다 → 같은 4칸에 더 많이 담는다.
- **Intrinsic load**: 과제 고유의 복잡도(동시에 고려해야 할 요소 간 상호작용 수). 설계로는 줄일 수 없고, 학습자의 schema가 늘어야 줄어든다.
- **Extraneous load**: 학습·문제해결에 기여하지 않는 부하(문서 찾기, 문법 실수, 환경 설정, 산만한 화면).
- **Germane load**: schema를 만들고 자동화하는 데 쓰이는 "좋은" 노력.
- **Cognitive offloading (Risko & Gilbert 2016)**: 외부 도구·행위로 내부 인지 요구를 줄이는 것. 메모, 계산기, 알림 등.
- **Offloading vs outsourcing (Kirschner 2026 등 교육계 구분)**: offloading은 중간 결과를 밖에 적어 두고 *생각은 내가 계속하는* 것, outsourcing은 *생각 자체*를 외부 행위자에게 넘기는 것. 비슷한 구분으로 "autonomous vs dependent offloading", "cognitive surrender"(최소한의 검토로 AI 답을 자기 답으로 채택) 같은 용어가 2025–2026 문헌에 등장한다. 이 구분은 Risko & Gilbert 원 논문의 용어가 아니라 후속 논자들의 정리임에 유의.
- **Cognitive debt (Kosmyna et al. 2025)**: 당장 정신적 노력을 아낀 대가로 이해·기억·소유감이 나중에 부족해지는 현상을 기술 부채에 빗댄 말(예비 연구).

## 코딩 에이전트 사용과의 연결점
- **줄어드는 곳 (extraneous ↓)**: API 문서 찾기, 보일러플레이트, 문법·빌드 설정, 정규식 작성, 낯선 라이브러리 탐색. 이 영역은 offloading으로 보는 것이 타당하고 실제 이득이 크다.
- **옮겨 가는 곳 (intrinsic의 재배치)**: 문제를 쪼개 지시문·CLAUDE.md/AGENTS.md로 명세하는 일, 에이전트의 계획을 읽고 판단하는 일. 과제의 본질적 복잡도는 사라지지 않고 "명세와 검토" 단계로 이동한다.
- **사라질 위험이 있는 곳 (germane ↓)**: 대학원생이 자기 분석 코드의 논리를 직접 짜 보는 경험. 에이전트에 통째로 맡기면(outsourcing) 결과는 나오지만 schema가 쌓이지 않아, Bastani 실험처럼 도구를 뺐을 때 실력이 오히려 낮을 수 있다.
- **늘어나는 곳**: 에이전트가 만든 수백 줄 diff를 working memory 4칸으로 따라가야 하는 검토 부하 (02, 03 파일 참고).
- **실천 원칙(강연용 제안)**: (1) 내가 이미 할 줄 아는 일은 맡긴다(offload), (2) 지금 배워야 하는 일은 AI를 튜터·힌트 모드로 쓴다(Bastani의 GPT Tutor처럼), (3) 결과를 받으면 "설명할 수 있는가"로 outsourcing 여부를 자가 점검한다.

## 강연에 쓸 만한 포인트
- **비유**: working memory는 "손바닥 위 4개의 공". AI가 저글링 공 일부를 대신 들어 주면(offloading) 좋지만, 저글링 연습 자체를 대신하면(outsourcing) 손은 영영 늘지 않는다.
- **그림 아이디어**: 세 칸 막대(intrinsic / extraneous / germane)를 AI 사용 전후로 비교 — extraneous는 줄고, germane은 "맡기는 방식"에 따라 늘거나 0이 되는 두 갈래 화살표.
- **그림 아이디어 2**: Bastani 결과 막대 — 연습 성적(+48%, +127%) vs 시험 성적(−17%, ≈0). "연습장에선 날았는데 시험장에선 떨어졌다."
- **인용 후보(1개)**: Kirschner — "A notebook stores what you write. AI decides what to write." (Kirschner, 2026, Substack)

## 원본 그림
- Cowan(2001) / Sweller CLT 공식 도식 — 없음 (직접 그리기 권장)
- Bastani et al. PNAS 2025 결과 막대그래프 — 이미지 URL 확인 못 함 (논문 Fig. 참조: https://papers.ssrn.com/abstract=4895486)
- Microsoft NFW 2025 p.50 "Transversal Skills and Competences model" — PDF 내 그림 (https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf , p.50)
