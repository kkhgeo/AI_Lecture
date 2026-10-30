# 출력을 텍스트 밖으로 꺼내는 제품들: Generative UI, Artifacts, Canvas, NotebookLM, Claude Code 출력 스타일 (산업계 흐름)

여러 제품 발표를 시간순으로 묶었다. 각 항목은 공식 발표·문서에서 확인했고, 2차 기사로만 확인한 부분은 (2차 자료)로 표시했다.

---

## 0. 시간표 한눈에
| 날짜 | 회사 | 기능 | 출력 해석에 생긴 변화 |
|---|---|---|---|
| 2024-03-01 | Vercel | AI SDK 3.0 Generative UI | 답을 텍스트 대신 React 컴포넌트로 스트리밍 |
| 2024-06-21(페이지 표기) | Anthropic | Claude Artifacts | 코드·문서·앱을 대화와 분리된 옆 창에 띄움 |
| 2024-10-03 | OpenAI | ChatGPT Canvas | 결과물을 옆 창에 두고 부분 선택·인라인 수정 |
| 2025-03-19~ | Google | NotebookLM 마인드맵 | 자료 전체를 클릭 가능한 지도로 (2차 자료: 9to5google 등) |
| 2025-07-29 | Google | NotebookLM Video Overviews | 자료를 해설 슬라이드 영상으로 |
| 2025-08-14 | Anthropic | Claude Code 출력 스타일(Explanatory, Learning), v1.0.81 | 코드와 함께 "왜"를 설명하는 Insight 블록 (2차 자료: 릴리스 추적 사이트) |
| 2025-09-29 | Anthropic | Imagine with Claude(연구 프리뷰, Sonnet 4.5와 함께) | 화면을 즉석 생성 (2차 자료) |
| 2025-11-18 | Google Research | Generative UI (Gemini 앱 dynamic view·visual layout, Search AI Mode) | 질문마다 맞춤 인터랙티브 페이지 생성 |
| 2026-03-12 | Anthropic | Claude 채팅 인라인 시각화(베타) | 답 안에 차트·다이어그램을 그려 넣음 |

---

## 1. Google Research — Generative UI (생성형 UI)
- **저자/기관**: Yaniv Leviathan, Dani Valevski, Vishnu Natchu, Yossi Matias / Google Research
- **발행일**: 2025-11-18 (2026-10-01 열람)
- **URL**: https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/ (논문 "Generative UI: LLMs are Effective UI Generators"는 블로그에서 링크)
- **자료 유형**: 공식 블로그 + 논문

### 핵심 요약
- 프롬프트마다 웹페이지·게임·도구·시뮬레이션 같은 **인터랙티브 화면을 즉석에서 생성**하는 방식을 제안.
- 구현: 모델에 도구(이미지 생성, 웹 검색) 접근 + 정교한 시스템 지시문 + 후처리.
- 제품 적용: Gemini 앱의 **dynamic view**와 **visual layout** 실험, Google 검색 **AI Mode**(미국 Pro/Ultra 구독자부터).
- 평가: 사람 평가자가 ① 전문가가 직접 만든 페이지, ② 생성형 UI, ③ 상위 검색 결과, ④ 일반 텍스트, ⑤ 마크다운 답을 비교. 전문가 제작 페이지가 1위, 생성형 UI가 근소한 2위, 나머지(텍스트·마크다운 포함)와는 **큰 격차**. 비교용 전문가 제작 사이트 데이터셋 PAGEN을 공개 예정.
- 단서: 이 선호 결과는 **생성 속도를 무시한 조건**이다(생성에 시간이 걸림). 구체 퍼센트는 블로그에서 확인하지 못함.

## 2. Anthropic — Claude Artifacts (2024) → 인라인 시각화 (2026)
- **저자/기관**: Anthropic
- **발행일**: Artifacts 2024-06-21(Claude 3.5 Sonnet 발표 페이지 표기); 인라인 시각화 2026-03-12(2026-04-22 갱신) (2026-10-01 열람)
- **URL**: https://www.anthropic.com/news/claude-3-5-sonnet , https://claude.com/blog/claude-builds-visuals
- **자료 유형**: 공식 블로그

### 핵심 요약
- Artifacts: 코드·문서·디자인을 **대화 옆 전용 창**에 띄워 보고·고치고·발전시키게 함. 대화형 AI에서 "협업 작업 공간"으로의 전환이라고 소개.
- 인라인 시각화(베타, 모든 요금제): 답 **안에** 차트·다이어그램·인터랙티브 시각화를 그리고, 대화가 진행되면 고치거나 사라지게 함. Artifacts가 공유·다운로드용 "완성물"이라면, 이것은 **이해를 돕는 일시적 칠판**.
- 사용자가 "다이어그램으로 그려 줘"처럼 요청할 수도 있고, 시각화가 이해에 도움이 된다고 판단하면 Claude가 스스로 그리기도 함. 예: 복리(곡선을 조작), 주기율표(클릭해 세부 보기).
- 그 사이 2025-09-29에 "Imagine with Claude" 연구 프리뷰(화면을 실시간 생성)가 있었고, 공식 블로그는 이를 인라인 시각화의 전신으로 언급.

## 3. OpenAI — ChatGPT Canvas
- **저자/기관**: OpenAI
- **발행일**: 2024-10-03 (2026-10-01 열람)
- **URL**: https://openai.com/index/introducing-canvas/
- **자료 유형**: 공식 블로그

### 핵심 요약
- 글쓰기·코딩을 위한 **별도 창**. 대화 스크롤 속에 묻히던 결과물을 한 곳에 고정.
- 사용자가 **특정 부분을 선택**해 그 부분만 묻거나 고치게 함(Graphologue 형성 연구의 "부분을 짚어 묻고 싶다"는 요구와 같은 방향).
- 코딩 단축 기능: 코드 리뷰, 로그 추가, 주석 추가, 버그 수정, 다른 언어로 포팅. 인라인 제안.

## 4. Google — NotebookLM 마인드맵·비디오 개요
- **저자/기관**: Google Labs
- **발행일**: 마인드맵 2025-03-19 배포 시작(2차 자료: 9to5google 2025-03-27 등); Video Overviews 2025-07-29 (2026-10-01 열람)
- **URL**: https://blog.google/technology/google-labs/notebooklm-video-overviews-studio-upgrades/ , https://9to5google.com/2025/03/27/notebooklm-mind-map/
- **자료 유형**: 공식 블로그 / 기사

### 핵심 요약
- 마인드맵: 올린 자료 전체의 주제 구조를 **클릭 가능한 지도**로 보여 주고, 노드를 누르면 그 주제에 대해 질문.
- Video Overviews: 노트·PDF·이미지를 **해설이 붙은 슬라이드 영상**으로 변환(첫 형식). 이전의 Audio Overviews(팟캐스트형)에 이어 "읽지 않고 보고 듣게" 하는 방향.

## 5. Anthropic — Claude Code 출력 스타일
- **저자/기관**: Anthropic
- **발행일**: Explanatory·Learning 도입 2025-08(v1.0.81, 2025-08-14 — 2차 자료); 현재 문서는 Default·Proactive·Concise·Explanatory·Learning 5종 (2026-10-01 열람)
- **URL**: https://code.claude.com/docs/en/output-styles
- **자료 유형**: 공식 문서

### 핵심 요약
- 출력 스타일 = 세션 전체의 역할·어조·**응답 형식**을 바꾸는 지시문 묶음. `/output-style <이름>`으로 전환.
- **Concise**: 첫 문장에 결과·답을 놓고 서두·과정 중계·마무리 요약을 뺀다(오류·보안 경고는 그대로 다 보여 줌). → **결론 먼저** 원칙을 제품 기능으로 만든 것.
- **Explanatory**: 작업은 같게 하되 코드 앞뒤에 2~3개 요점의 `Insight` 블록으로 "왜 이렇게 했는지"를 설명. 코드베이스를 알아 가는 중일 때 권장.
- **Learning**: Insight에 더해 설계 판단이 필요한 몇 줄을 `TODO(human)`으로 남겨 사용자가 직접 쓰게 함.
- 공식 문서의 커스텀 스타일 예시가 **"Diagrams first"**: 코드·구조·데이터 흐름 설명을 Mermaid 다이어그램으로 시작하고(노드 15개 이하), 그다음 산문. → 시각 우선 출력을 사용자가 직접 설정할 수 있음.
- 주의: 스타일은 지시일 뿐 보장이 아니며, Explanatory·Learning은 출력이 길어져 토큰이 늘어난다(문서 명시).

## 6. Vercel — AI SDK 3.0 Generative UI
- **저자/기관**: Vercel
- **발행일**: 2024-03-01 (2026-10-01 열람)
- **URL**: https://vercel.com/blog/ai-sdk-3-generative-ui
- **자료 유형**: 공식 블로그

### 핵심 요약
- v0에서 쓰던 생성형 UI 기술을 오픈소스로 공개. LLM 응답에 **React 서버 컴포넌트**를 연결해 스트리밍.
- 개발자가 "평문·마크다운 챗봇"을 넘어 날씨 카드·주식 차트 같은 **컴포넌트형 답**을 만들 수 있게 함.

---

## 강연자의 경험("AI 출력을 이해·해석하기 어렵다")과의 연결
- 2024~2026년 주요 회사 세 곳이 모두 같은 방향으로 움직였다: **텍스트 → 옆 창의 작업물(Artifacts·Canvas) → 답 안의 시각화·생성형 UI**. "출력이 읽기 어렵다"는 문제를 회사들도 인정하고 제품으로 대응하고 있다는 증거.
- 해석을 돕는 장치가 세 갈래로 나뉜다: ① **분리**(결과물을 대화에서 떼어 한 곳에 고정: Artifacts, Canvas), ② **변환**(텍스트를 그림·지도·영상으로: 인라인 시각화, 마인드맵, Video Overviews, Generative UI), ③ **형식 규칙**(결론 먼저·설명 블록: Claude Code Concise/Explanatory).
- 코딩 에이전트 사용자에게 가장 바로 쓸 수 있는 것은 ③이다. 출력 스타일이나 CLAUDE.md로 "결론 먼저, 다이어그램 먼저"를 기본값으로 만들 수 있다.
- 단서: Google 평가는 생성 시간을 빼고 비교한 것이고, 시각 출력은 만드는 데 시간·토큰이 더 든다. 빠른 확인에는 짧은 텍스트가 나을 수 있다.

## 강연에 쓸 만한 포인트
- 인용: 이 파일에서는 직접 인용 없음(공식 문서 내용은 재서술).
- 슬라이드 한 줄: "2024 옆 창(Artifacts·Canvas) → 2025 생성형 UI → 2026 답 속의 그림" — 업계는 '읽는 출력'에서 '보는 출력'으로 이동 중.
- 데모 아이디어: Claude Code에서 `/output-style concise`와 `/output-style explanatory`를 같은 질문에 적용해 출력 길이·구조 비교.
- 그림 아이디어: 위 시간표를 가로 타임라인으로, 각 점에 제품 스크린샷 썸네일.

## 원본 그림
- Google Generative UI 대표 이미지(생성된 인터랙티브 화면 예시) — https://storage.googleapis.com/gweb-research2023-media/images/GenUI-0b-Hero.width-1250.png (200 확인)
- Google Generative UI 시스템 개요(도구 + 시스템 지시 + 후처리) — https://storage.googleapis.com/gweb-research2023-media/images/GenUI-4-Overview.width-1250.png (200 확인)
- Google Generative UI 결과 예시 — https://storage.googleapis.com/gweb-research2023-media/images/GenUI-0-Hero.width-1250.png (200 확인)
- Claude 인라인 시각화 — 블로그에 GIF·PNG가 있으나 이미지 URL은 확인하지 못함(없음)
