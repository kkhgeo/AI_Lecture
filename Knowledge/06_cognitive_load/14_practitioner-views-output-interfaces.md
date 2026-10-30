# 실무자·디자이너들의 주장: "채팅 텍스트 말고 보이는 인터페이스로" (실무자 관점 모음)

사람별로 템플릿을 반복한다. 원문(영상·블로그)에서 직접 확인한 것과 2차 자료를 구분했다. 직접 인용은 파일 전체에서 1개.

---

## 1. Andrej Karpathy — "Software Is Changing (Again)" (YC AI Startup School 강연)
- **저자/기관**: Andrej Karpathy (전 Tesla AI 책임자, OpenAI 공동창업자)
- **발행일**: 2025-06-17 강연 (2026-10-01 열람)
- **URL**: https://www.youtube.com/watch?v=LCEmiRjPEtQ / 자동 전사본 https://cdn.billmill.org/static/yt-transcribe/karpathy/httpswwwyoutubecomwatchvLCEmiRjPEtQ.html / 정리 https://www.latent.space/p/s3
- **자료 유형**: 영상(전사본으로 확인; 자동 전사라 단어 일부 오류 가능)

### 핵심 요약
- LLM과 텍스트로 대화하는 것은 **터미널로 운영체제를 다루는 것** 같다고 비유. 모든 작업에 통하는 일반적 GUI는 아직 발명되지 않았다고 말함.
- 성공한 LLM 앱(Cursor 예)의 핵심 요소 중 하나로 **앱 전용 GUI**를 꼽음. 텍스트는 읽고 해석하고 이해하기 매우 어렵다는 취지로 말함.
- 코드 변경은 **빨강·초록 diff**로 보는 편이 훨씬 낫고, 단축키로 수락·거절하면 된다 → GUI가 사람이 오류 가능한 시스템의 작업을 **감사(audit)하고 더 빨리** 가게 해 준다.
- **자율성 슬라이더(autonomy slider)**: Cursor(탭 완성 → 선택 영역 수정 → 파일 → 저장소 전체), Perplexity(빠른 검색 → 리서치 → 딥 리서치)처럼 맡기는 정도를 사용자가 조절.
- 사람-AI 루프 = AI가 생성, 사람이 검증. 이 루프를 빠르게 돌리는 두 방법: ① **검증을 빠르게**(GUI는 머릿속 "시각 GPU"를 쓰므로 감사에 유용), ② **AI를 짧은 줄에 묶기**(1,000줄짜리 diff는 쓸모없다, 결국 내가 병목이므로 작은 단위로 진행).
- 결론 비유: 자율 로봇(아이언맨 로봇)보다 **아이언맨 슈트**(부분 자율 + 맞춤 GUI + 빠른 생성-검증 루프)를 만들라.

## 2. Andrej Karpathy — "2025 LLM Year in Review" (LLM GUI 절)
- **저자/기관**: Andrej Karpathy
- **발행일**: 2025-12-19 (2026-10-01 열람)
- **URL**: https://karpathy.bearblog.dev/year-in-review-2025/
- **자료 유형**: 블로그

### 핵심 요약
- LLM과의 "채팅"은 1980년대 콘솔에 명령을 입력하던 것과 비슷하다고 다시 정리.
- 사람들은 텍스트 읽기를 싫어한다(느리고 힘듦). 정보를 **시각적·공간적으로** 받아들이는 것을 좋아하며, 그래서 전통 컴퓨팅에서 GUI가 발명되었다는 논리.
- 따라서 LLM은 사람이 선호하는 형식(이미지, 인포그래픽, 슬라이드, 화이트보드, 애니메이션·영상, 웹앱)으로 말해야 한다고 주장. 이미지 모델(Nano Banana)을 그 초기 신호로 언급.

## 3. Amelia Wattenberger — "Why Chatbots Are Not the Future"
- **저자/기관**: Amelia Wattenberger (당시 GitHub Next 디자인 연구)
- **발행일**: 2023 (페이지에 날짜 표기 없음; Simon Willison이 2023-05-15에 링크) (2026-10-01 열람)
- **URL**: https://wattenberger.com/thoughts/boo-chatbots
- **자료 유형**: 블로그(인터랙티브 에세이)

### 핵심 요약
- 빈 채팅창은 무엇을 어떻게 물어야 하는지 알려 주지 않는다(어포던스 부족).
- 필요한 맥락을 매번 프롬프트에 직접 타이핑해야 한다.
- 답이 나온 뒤 고치기가 번거롭다: 여러 버전을 **스크롤하며 무엇이 바뀌었는지 직접 찾아야** 한다 → 출력 해석 부담과 직결.
- 생성-평가를 오가는 흐름이 대기와 모드 전환으로 끊긴다.
- 대안: 맥락을 슬라이더·토글 같은 **인터페이스 요소**로 넣고, 내용 생성기보다 **제안을 주는 도구**를 만들 것.

## 4. Simon Willison — Artifacts 활용기, 그리고 "인지 부채"를 갚는 설명 패턴
- **저자/기관**: Simon Willison (Datasette 개발자, Django 공동 창시자)
- **발행일**: "Everything I built with Claude Artifacts this week" 2024-10-21; Agentic Engineering Patterns 가이드 중 "Linear walkthroughs"(2026-02), "Interactive explanations"(2026) (2026-10-01 열람)
- **URL**: https://simonwillison.net/2024/Oct/21/claude-artifacts/ , https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/ , https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/
- **자료 유형**: 블로그

### 핵심 요약
- 2024: 일주일 동안 Artifacts로 만든 작은 인터랙티브 앱들을 기록. 즉석에서 단일 페이지 앱을 띄워 보는 것이 설명용 시제품이자 실제 문제 해결 도구로 유용하다고 평가.
- 2026: 에이전트가 쓴 코드가 어떻게 동작하는지 놓치면 **인지 부채(cognitive debt)**가 쌓인다고 정의(10번 파일의 인지 부채와 연결).
- 처방 ① **선형 워크스루**: 에이전트에게 소스를 읽고 순서대로 설명하는 문서를 만들게 함. 코드 조각은 손으로 베끼지 않고 명령으로 추출하게 해(Showboat 도구) 환각을 줄임.
- 처방 ② **인터랙티브 설명**: 이해 안 되는 알고리즘을 에이전트에게 **애니메이션 HTML**로 만들게 함. 예: 워드 클라우드 배치 알고리즘(나선형으로 자리 찾기, 충돌 검사)을 단계별로 재생·정지할 수 있는 페이지.
- 의미: 코딩 에이전트 출력의 해석 문제를 **에이전트 자신에게 시각 설명을 만들게 해서** 푸는 실무 사례.

## 5. Maggie Appleton — "Language Model Sketchbook, or Why I Hate Chatbots"
- **저자/기관**: Maggie Appleton (디자이너, 당시 Elicit)
- **발행일**: 2023 추정(페이지 표기 "3년여 전"; 정확한 날짜 미확인) (2026-10-01 열람)
- **URL**: https://maggieappleton.com/lm-sketchbook
- **자료 유형**: 블로그(디지털 가든)

### 핵심 요약
- 챗봇은 LLM 인터페이스 중 "게으른 해법"이며 가능성의 표면만 긁는다는 주장.
- 대안 스케치: 글 옆에서 성격이 다른 조언자들이 제안하는 **Daemons**, 원인·결과 사슬을 시각적으로 펼치는 **Branches**, 우클릭 메뉴로 문장 단위 비판·근거 찾기를 하는 **Epi**.
- 출력은 검증 대상이지 정답이 아니라는 입장 → 출력을 **비판적으로 읽도록 돕는 구조**를 설계하자는 쪽.

## 6. Linus Lee (thesephist) — "Imagining better interfaces to language models"
- **저자/기관**: Linus Lee (당시 독립 연구자, 이후 Notion AI)
- **발행일**: 2022-05-07 (2022-07-24 갱신 표기) (2026-10-01 열람)
- **URL**: https://thesephist.com/posts/latent/
- **자료 유형**: 블로그

### 핵심 요약
- ChatGPT 이전부터, 대화형 인터페이스는 텍스트 완성 능력을 그대로 노출한 것일 뿐이라고 지적.
- 대화는 정보를 추적하기에 나쁜 방식이며, 쓸모 있는 일 대부분은 정보를 작업 기억에 붙잡아 두어야 한다고 설명 → 출력이 대화 속으로 흘러가 버리는 문제.
- 대안: 사람과 AI가 함께 쓰는 **공유 문서**, 어조·길이 같은 방향을 손잡이로 끌어 조절하는 **잠재 공간 직접 조작**.

---

## 강연자의 경험("AI 출력을 이해·해석하기 어렵다")과의 연결
- Karpathy는 강연자의 경험을 거의 그대로 말한다: 텍스트는 읽고 해석하기 어렵고, 그래서 diff·GUI가 필요하며, 큰 출력(1,000줄 diff)은 검증 병목을 만든다.
- 해법이 두 갈래로 겹친다: **표현을 바꾸기**(GUI, diff, 시각 설명: Karpathy·Willison·Wattenberger) + **출력 단위를 줄이기**(짧은 줄, 작은 덩어리: Karpathy).
- Willison은 코딩 에이전트 사용자에게 바로 옮길 수 있는 처방을 준다: 이해가 안 되면 "설명 문서"나 "애니메이션 설명 페이지"를 에이전트에게 시켜라.
- Wattenberger·Appleton·Lee(2022~2023)는 ChatGPT 초기부터 "채팅은 최종 형태가 아니다"라고 말했고, 2024~2026 제품(13번 파일)이 그 방향을 따랐다.

## 강연에 쓸 만한 포인트
- 인용(1개): "Reading text is effortful and it's not fun, but looking at stuff is fun" — Andrej Karpathy, YC AI Startup School, 2025-06-17 (자동 전사본 기준)
- 슬라이드 한 줄: "검증을 빠르게(GUI·diff), AI는 짧은 줄로(작은 diff)" — Karpathy의 생성-검증 루프.
- 그림 아이디어: Karpathy 생성-검증 루프 원(AI 생성 → 사람 검증), 검증 화살표 위에 "diff·다이어그램", 생성 화살표 위에 "작은 단위".
- 데모 아이디어: Willison 방식 — 강연자가 이해 못 한 코드 하나를 골라 Claude Code에게 "이 알고리즘을 단계별 애니메이션 HTML로 설명해 줘"라고 시킨 결과를 보여 주기.

## 원본 그림
- Willison 인터랙티브 설명 데모(워드 클라우드 배치 애니메이션) — https://static.simonwillison.net/static/2026/animated-word-cloud-demo.gif (200 확인)
- Karpathy 강연 슬라이드 — 공개 Google Slides 링크가 있다는 2차 보도만 확인, 이미지 URL은 없음
