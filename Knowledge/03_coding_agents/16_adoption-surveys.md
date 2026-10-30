# 개발자 AI·코딩 에이전트 도입 현황: 설문·사용 데이터 (Adoption surveys)

- **저자/기관**: Stack Overflow / JetBrains / GitHub(Octoverse) / Google Cloud DORA / Anthropic(Economic Index) / The Pragmatic Engineer
- **발행일**: Stack Overflow 2025 설문 2025-07-29; JetBrains State of Developer Ecosystem 2025 2025-10; GitHub Octoverse 2025 2025-10-28 전후; DORA 2025 2025-09-23; Anthropic Economic Index — 소프트웨어 개발편 2025-04, 2026-01, 2026-03, 2026-06-26 보고서; Pragmatic Engineer 2026-03-03 (2026-09-29 열람)
- **URL**:
  - https://survey.stackoverflow.co/2025/ai
  - https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/
  - https://stackoverflow.blog/2026/06/23/the-2026-developer-survey-is-now-open-for-human-developers-only/
  - https://blog.jetbrains.com/research/2025/10/state-of-developer-ecosystem-2025/
  - https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
  - https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/
  - https://www.anthropic.com/research/impact-software-development
  - https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
  - https://www.anthropic.com/research/economic-index-june-2026-report
  - https://newsletter.pragmaticengineer.com/p/ai-tooling-2026
- **자료 유형**: 보고서

## 핵심 요약
- **Stack Overflow 2025**(2025-07-29, 응답 49,000+명, 177개국): 84%가 AI 도구를 사용 중이거나 사용 예정(2024년 76%). 전문 개발자의 약 51%가 매일 사용. 그러나 AI 정확성을 "불신" 46% > "신뢰" 33%, "매우 신뢰"는 3%. 불신 비율은 2024년 31%에서 급증.
- 같은 설문에서 **AI 에이전트**를 업무에 쓰는 비율은 31%(매일 14.1%), 38%는 도입 계획 없음. 최대 불만은 "거의 맞지만 딱 맞지는 않은 답"(66%), AI 코드 디버깅이 더 오래 걸린다 45%. 72%는 "vibe coding"을 업무에 쓰지 않음.
- **Stack Overflow 2026 설문**은 2026-06-23 개시; 공지에서 "에이전트 사용이 두 배로 늘었다"고 언급. 2026-09-29 현재 **2026 정식 결과는 확인하지 못함**(일부 블로그가 2025 결과를 "2026 설문"으로 잘못 표기 — 인용 주의).
- **JetBrains 2025**(2025-10, 24,534명, 194개국, 2025-04~06 조사): 85%가 AI를 정기적으로 사용, 62%가 최소 하나의 AI 코딩 어시스턴트·에이전트·AI 에디터에 의존. AI 사용자 10명 중 약 9명이 주 1시간 이상 절약, 5명 중 1명은 주 8시간 이상.
- **GitHub Octoverse 2025**: Copilot coding agent가 2025-05~09 사이 100만 건 이상의 PR을 작성. 2025-08 TypeScript가 GitHub 최다 사용 언어로 등극(AI 생성 코드에 타입 안정성이 유리하다는 해석). 병합 PR 5억 1,870만 건(+29%).
- **DORA 2025**(2025-09-23, 약 5,000명): 기술 전문가 90%가 업무에 AI 사용(전년 대비 +14%p), 80% 이상이 생산성 향상 체감, 그러나 30%는 AI 코드를 거의/전혀 신뢰하지 않음. 중앙값 하루 2시간 AI 사용.
- **Anthropic Economic Index**: (2025-04) 코딩 대화 50만 건 분석 — Claude Code 대화의 79%가 "자동화(automation)"로 분류, Claude.ai는 49%. 스타트업 작업 33% vs 기업 13%. (2026-01 보고서, 2025-11 데이터) Claude.ai 사용의 36%가 코딩. (2026-06-26 "Cadences") Claude Code 세션은 채팅보다 자율성 점수가 1~5 척도에서 0.37점 높고, Claude Code 세션의 54%가 Opus 모델 사용.
- **Pragmatic Engineer 2026**(906명, 2026-01~02): 95%가 주 1회 이상 AI 사용, 75%가 업무의 절반 이상을 AI로, 55%가 에이전트를 정기 사용, Claude Code가 사용량 1위.

## 핵심 개념·용어 정의
- **Adoption vs trust gap(도입-신뢰 격차)**: 사용률은 오르는데 결과물 신뢰는 떨어지는 현상.
- **Automation vs augmentation**: AI가 과제를 직접 수행(자동화)하느냐, 사람과 반복 협업하며 보조(증강)하느냐의 구분(Anthropic Economic Index 분류).
- **Vibe coding**: 코드를 읽지 않고 자연어 지시와 "모두 수락"으로 소프트웨어를 만드는 방식(Karpathy, 2025-02 명명).
- **AI agent (설문 정의)**: 단순 자동완성·채팅을 넘어 여러 단계를 자율 수행하는 도구.

## 강연에 쓸 만한 포인트
- 한 장 요약: "84% 사용, 33% 신뢰, 31% 에이전트"(Stack Overflow 2025) → 1년도 안 되어 "55% 에이전트 정기 사용"(Pragmatic Engineer 2026, 표본 성격이 다름에 유의).
- 막대 두 개 도식: 사용률(84~90%) vs 신뢰(24~33%) — 설문 3종(SO, DORA, JetBrains) 비교.
- 인용(1개): Stack Overflow CEO는 신뢰 저하를 "the key data point"라 표현(Stack Overflow 보도자료, 2025-07-29).
- 대학원생 맥락: 표본 차이 주의 — Pragmatic Engineer는 경력 11~15년 중앙값·유럽/미국 편중, Stack Overflow는 학습자 포함 대규모 자발 응답.

## 원본 그림
- Anthropic Economic Index 2026-06 Figure 1.1 — https://www-cdn.anthropic.com/images/4zrzovbb/website/153b647190951536f59f8051f4470c0b6216b2ad-1920x1075.png
- Anthropic Economic Index 2026-06 Figure 2.1 — https://www-cdn.anthropic.com/images/4zrzovbb/website/453f808bfc9df630e89bb55e79b8194eb6df5a71-1920x1078.png
- Anthropic Economic Index 2026-06 Figure 3.6 — https://www-cdn.anthropic.com/images/4zrzovbb/website/7cddf6cfaa30bf44395459f948b52233853a5dfe-1920x1030.png
  - (각 그림의 정확한 내용은 페이지에서 확인 필요 — 세부 캡션 미확인)
- Stack Overflow 2025 AI 섹션 차트 — https://survey.stackoverflow.co/2025/ai (인터랙티브, 이미지 직접 URL 없음)
- JetBrains 2025 AI 섹션 — https://devecosystem-2025.jetbrains.com/artificial-intelligence (인터랙티브)

## Claude Code와의 연결점
- Anthropic 데이터상 Claude Code는 채팅보다 "자동화" 비중이 뚜렷이 높음(79% vs 49%, 2025-04) → "대화형 조수"에서 "작업 위임형 에이전트"로의 전환을 보여주는 지표.
- Pragmatic Engineer·Thoughtworks 모두 Claude Code를 에이전트 도입의 대표 사례로 언급(14번 파일).
- 신뢰 격차 데이터는 Claude Code 사용 시 "테스트·diff 검토·권한 제한" 습관이 필요한 이유(19번 파일)로 연결.
