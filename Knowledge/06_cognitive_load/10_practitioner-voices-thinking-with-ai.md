# Practitioner Voices: Thinking While Working with AI (실무자·연구자 1인칭 증언 모음)
- **저자/기관**: 개발자·연구자·작가 다수 (아래 표에 개별 표기)
- **발행일**: 2023-04 ~ 2026-08 (2026-10-01 열람)
- **URL**: 각 항목에 표기
- **자료 유형**: 블로그 / 팟캐스트 / 논문 속 참가자 발화 / 기사

> 표기 규칙: **[원문]** = 원 글·원 자료에서 직접 확인, **[원문-정리본]** = 저자 본인 블로그의 요약·발췌로 확인, **(2차 자료)** = 다른 사람의 인용·보도로만 확인. 모든 내용은 재서술이며, 직접 인용은 파일 전체에서 1개.
> 이미 04 파일에 정리된 "병렬 에이전트 감독" 증언(Willison 2025-10, Yegge, Karpathy 2026-01 등)은 중복을 피해 짧게만 다룬다.

## 핵심 요약
- 증언들은 네 갈래로 모인다: **생각이 끊긴다**(제안·알림·대기가 사고를 자른다), **내 생각을 잃는다**(쓰기를 맡기면 생각도, 시스템 이해도 사라진다), **판단할 게 너무 많다**(작업이 '만들기'에서 '결정하기'로 바뀜), **끝나고 나면 지친다**(짧은 시간에 고갈, 중독적 과몰입).
- 공통 원인: 사람의 사고·이해·판단은 **직렬이고 느린데**, AI 루프는 빠르고 끊임없이 사람에게 판단을 요구한다.
- 숙련자일수록 대응책도 구체적이다: 알림 끄기, 생각을 먼저 쓰기, 작은 단위로 시키기, 하루 사용량 제한.

## 1. 생각이 끊긴다
| 누구 | 언제·어디 | 무엇을 말했나(재서술) | 확인 |
|---|---|---|---|
| CS1 수강생 P13 (Prather 외 연구 참가자) | arXiv 2023-04, ACM TOCHI — https://arxiv.org/abs/2304.02491 | 해법을 생각하려는데 Copilot 제안이 화면을 채워서, 스스로 생각하는 대신 제안을 따라가고 싶어진다. 다른 학생들도 필요 없을 때 제안이 계속 떠서 자기가 치는 코드를 읽기 어렵다고 함. | [원문] |
| Mitchell Hashimoto (HashiCorp 공동창업자, Ghostty) | 2026-02-05, *My AI Adoption Journey* — https://mitchellh.com/writing/my-ai-adoption-journey | 에이전트 알림을 꺼야 한다. 맥락 전환이 매우 비싸기 때문에, 에이전트가 나를 부르는 게 아니라 내가 쉬는 틈에 에이전트를 확인해야 한다. 에이전트가 도는 동안 자신은 SNS·영상이 아니라 원래의 깊은 사고 모드로 다른 일을 했다. | [원문] |
| Prasad Rane (개발자) | dev.to, 9월 7일(연도 표기 없음, 2025년 추정) — https://dev.to/prasad_rane_dev/the-part-of-ai-coding-agents-i-didnt-expect-to-care-about-latency-44ak | 에이전트 행동 사이 1~2분 대기 때 다른 탭으로 새고, 돌아오면 문제에 대한 머릿속 모델을 잃는다. 몇 초 단위 루프가 집중을 지키는 데 더 낫다. | [원문, WebFetch 요약] |
| Andrej Karpathy | 2025-06-17 YC AI Startup School 강연 — 정리본 https://www.latent.space/p/s3 | 생성-검증 루프는 빠를수록 좋다. 검증을 쉽게 만들고, AI를 짧은 목줄에 묶어 작은 단위로 시켜라(큰 diff는 사람이 따라갈 수 없다). | (2차 자료: Latent Space 정리본) |

## 2. 내 생각을 잃는다
| 누구 | 언제·어디 | 무엇을 말했나(재서술) | 확인 |
|---|---|---|---|
| Paul Graham (Y Combinator) | 2024-10, *Writes and Write-Nots* — https://paulgraham.com/writes.html | 쓰기는 곧 생각이다. AI가 쓰기의 압박을 없애면 대부분이 쓰기를 그만두고, 결과적으로 생각하는 사람과 못 하는 사람으로 갈린다. (이 파일의 유일한 인용은 아래 "강연 포인트"에) | [원문] |
| Ted Chiang (SF 작가) | 2024-08-31, *The New Yorker*, "Why A.I. Isn't Going to Make Art" | 글쓰기·예술은 수많은 작은 선택의 연속인데, 짧은 프롬프트로 LLM에 맡기면 그 선택 대부분을 기계가 대신(평균값으로) 한다. | (2차 자료: 유료벽으로 원문 미확인) |
| Simon Willison (Django 공동 제작자) | 2026-02-15, 블로그 — https://simonwillison.net/2026/Feb/15/cognitive-debt/ | 세부를 리뷰하지 않고 AI로 기능을 만든 자기 프로젝트들에 대해, 이제는 그것들이 무엇을 할 수 있고 어떻게 동작하는지 확고한 머릿속 모델이 없다고 고백. 그래서 다음 기능을 어떻게 더할지 추론하기 어려워졌다. | [원문] |
| Margaret-Anne Storey (Univ. of Victoria 교수) | 2026-02-09, "How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt" — https://margaretstorey.com/blog/2026/02/09/cognitive-debt/ | '인지 부채' 개념 제안: 빚은 코드가 아니라 사람 머릿속 이해에 쌓인다. 학생 팀이 코드 품질이 아니라 "왜 이렇게 설계했는지" 공유된 이해를 잃어서 변경을 못 하게 된 사례. 이해 없는 속도는 지속 불가능하다. | [원문] |
| Geoffrey Litt (HCI 연구자·개발자) | 2026-07, AI Engineer World's Fair 발표 / X 게시물 — Willison 정리 https://simonwillison.net/2026/Jul/2/understand-to-participate/ | 에이전트와 창의적으로 협업하려면 머릿속에 풍부한 개념이 있어야 한다. 이해해야 참여할 수 있다. | (2차 자료: Willison 경유) |
| Mario Zechner (pi 에이전트 제작자) | 2026-03, "Thoughts on slowing the fuck down" — Willison 정리 https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/ | 에이전트 군단에는 병목이 없어서 사람이 무엇이 일어나는지 모르게 된다. 하루 생성량 제한, 꼼꼼한 리뷰, 아키텍처는 손으로 쓰기를 제안. Willison은 이제 병목은 타이핑이 아니라 이해라고 덧붙임. | (2차 자료: Willison 경유) |
| Armin Ronacher (Flask 제작자) | 2026-01-18, "Agent Psychosis: Are We Going Insane?" — https://lucumr.pocoo.org/2026/1/18/agent-psychosis/ | 메모리 있는 에이전트에 의존하게 되고, AI는 진짜 협업자가 아니라 내 생각과 충동을 강화해 주는 존재가 되기 쉽다. 비판적 사고 없이 AI를 한 방향으로 밀어붙이는 세션을 자주 본다고 함. 자신에게도 그런 경향이 있다고 인정. | [원문] |
| Ethan Mollick (Wharton) | 2025-07-07, "Against 'Brain Damage'" — https://www.oneusefulthing.org/p/against-brain-damage | AI가 뇌를 망가뜨리는 게 아니라 생각하는 방식을 바꾼다. 처방: 먼저 생각하고 먼저 써라, 그 다음 AI에게 다듬기·피드백을 받아라. AI 제안은 아이디어를 예측 가능한 쪽으로 고정(anchoring)할 수 있다. | [원문, WebFetch 요약] |
| Florian Herrengt (개발자) | 2026-08, 블로그 — Willison 정리 https://simonwillison.net/2026/Aug/12/florian-herrengt/ (원문 https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) | 버그가 안 잡히는 팀에서, 데이터 출처를 물으니 아무도 모르고 "Claude에게 물어보자"고 답하는 장면. 아무도 시스템을 이해하지 못하는데 AI의 답만 자신만만하다. | (2차 자료: Willison 경유) |

## 3. 판단할 게 너무 많다
| 누구 | 언제·어디 | 무엇을 말했나(재서술) | 확인 |
|---|---|---|---|
| Ryan Donovan (Stack Overflow 블로그), 인터뷰: Pratima Arora (Smartsheet CPTO), Carol Lee (Intuit) | 2026-05-21, "Coding agents are giving everyone decision fatigue" — https://stackoverflow.blog/2026/05/21/coding-agents-are-giving-everyone-decision-fatigue/ | 일의 중심이 코드 작성에서 결정·리뷰로 옮겨가 하루가 더 '빽빽해졌다'. Arora: 근무 시간은 같은데 일의 밀도가 달라졌다. Lee: 리뷰에서 놓치면 내 책임이라는 압박. 처방: 판단 관문을 시작(명세)과 끝(결과·보안)으로 옮겨라. | [원문, WebFetch 요약] |
| Addy Osmani (Google) | 2026-04-07, "Your parallel Agent limit" — https://addyosmani.com/blog/cognitive-parallel-agents/ | 에이전트는 병렬이지만 사람의 감독·판단·이해는 단일 스레드다. 보지 않는 스레드에서 뭔가 어긋나고 있을지 모른다는 배경 불안, 스레드마다 다른 신뢰 보정이 부담. 편하다고 느끼는 수보다 적게 시작하라. | [원문, WebFetch 요약] |
| BotDesigner 연구 참가자들 (Zamfirescu-Pereira 외) | CHI 2023 — https://doi.org/10.1145/3544548.3581388 | 모든 참가자가 한 번은 "왜 이렇게 했지?"라고 물었다. 결과가 왜 나왔는지 모르는 채 다음 수를 결정해야 한다. (08 파일 참고) | [원문] |

## 4. 끝나고 나면 지친다
| 누구 | 언제·어디 | 무엇을 말했나(재서술) | 확인 |
|---|---|---|---|
| Simon Willison | 2026-04-03, Lenny's Podcast 클립(자기 블로그에 자막 게시) — https://simonwillison.net/2026/Apr/3/cognitive-cost/ | 코딩 에이전트를 잘 쓰는 데 25년 경력을 전부 쏟아야 하고, 정신적으로 소모적이다. 에이전트 4개를 병렬로 돌리면 오전 11시면 하루치가 바닥난다. 모든 걸 리뷰하지 않아도, 한 번에 머리에 담을 수 있는 양에 한계가 있다. 새로운 한계를 찾는 것도 배워야 할 기술. | [원문: 자막 파일 https://static.simonwillison.net/static/2026/cognitive-cost.vtt] |
| Steve Yegge | 2026-02, "The AI Vampire" (Medium) — Willison 정리 https://simonwillison.net/2026/Feb/15/the-ai-vampire/ | AI 코딩은 중독적이고, 강도 높게 하면 갑자기 졸음이 쏟아져 낮잠을 자게 된다. 최대 속도의 바이브 코딩이라면 하루 3시간 정도만 기대하라. (04 파일과 중복) | (2차 자료: Medium 403, Willison·언론 경유) |
| Armin Ronacher | 2026-01-18 (위와 같은 글) | 많은 사람이 에이전트 코딩 중독에 걸려 잠을 거의 자지 않고 무언가를 만든다. 다른 사람과 부딪힐 때에야 과했다는 걸 깨닫는다. | [원문] |
| BCG / HBR "AI brain fry" | 2026-03 | 여러 AI 도구 감독 시 정신적 피로 보고. 세부 수치는 06 파일 참조(유료 원문 미확인). | (2차 자료) |

## 핵심 개념·용어 정의
- **인지 부채(cognitive debt)**: Storey(2026)의 용어. 기술 부채가 코드에 쌓이듯, AI로 빠르게 만들면서 팀원들 머릿속의 시스템 이해("왜 이렇게 됐는가")가 쪼개지고 사라지는 것.
- **쓰기 = 생각**: Graham의 주장. 생각을 글로 옮기는 과정에서 생각이 완성된다. 쓰기를 넘기면 생각의 기회도 넘어간다.
- **결정 피로(decision fatigue)**: 판단을 연속해서 내릴수록 판단의 질이 떨어지는 현상. 에이전트 작업에서는 승인·리뷰·방향 선택이 그 판단들이다.
- **의사(擬似) 협업**: Ronacher의 관점. AI가 내 생각을 반박하기보다 강화해 주므로, 협업처럼 보이지만 사실상 혼잣말의 증폭이 될 수 있다.

## 강연자의 경험("AI와 상호작용할 때 생각하기 어렵다")과의 연결
- 강연자의 경험은 혼자만의 것이 아니다. 숙련 개발자(Willison, Hashimoto, Ronacher), 연구자(Storey), 초보 학생(Prather 연구의 P13)까지 **같은 현상을 각자의 말로** 묘사한다.
- 네 갈래는 강연자의 경험을 쪼개 보는 틀로 쓸 수 있다: ① 대화 중에 생각이 잘린다(끊김) ② 생각을 AI 문장에 맡기다 보니 내 생각의 줄기가 사라진다(상실) ③ 매 턴 "이거 맞나, 다음엔 뭘 시키지"를 판단해야 한다(판단 과부하) ④ 그래서 짧은 시간에 지친다(고갈).
- 학생 청중에게: 초보일수록 ①이 크고(Prather), 숙련자일수록 ③·④가 크다(Willison, Osmani). 둘 다 겪는 것이 ②.

## 강연에 쓸 만한 포인트
- **인용(1개)**: "If you're thinking without writing, you only think you're thinking." — Paul Graham, *Writes and Write-Nots* (2024-10).
- **장면 묘사(재서술)**: "생각하려는데 화면이 제안으로 가득 차서 따라가고 싶어진다" — 초보 학생(Prather 외 2023). "에이전트 넷을 돌리면 오전 11시에 하루치가 끝난다" — Willison(2026). 두 장면을 나란히 놓으면 초보와 고수가 같은 벽에 부딪힌다는 메시지가 된다.
- **비유**: 인지 부채 = 신용카드. 지금은 빨리 사지만(빠른 생성), 이해라는 이자를 나중에 한꺼번에 낸다.
- **질문 슬라이드**: "AI와 30분 대화한 뒤, 방금 내린 결정을 AI 없이 설명할 수 있나요?"
- **그림 아이디어**: 2×2 격자(네 갈래 제목) 각 칸에 사람 아이콘 하나와 한 줄 재서술, 출처는 발표자 노트로.

## 원본 그림
- Ronacher 글 소셜 이미지 — https://lucumr.pocoo.org/social/2026-01-18-agent-psychosis-social.png (제목 카드, 내용 그림 아님)
- 그 외 없음
