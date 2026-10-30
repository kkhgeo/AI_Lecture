# Instruction Drift in Long Sessions & Lost in the Middle (긴 세션에서 지시 망각·표류)

- **저자/기관**: Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang / Kenneth Li, Tianle Liu, Bashkansky, Bau, Viégas, Pfister, Wattenberg / Laban, Hayashi, Zhou, Neville (소속은 원문 확인 필요) / Kelly Hong, Anton Troynikov, Jeff Huber (Chroma) / Anthropic Applied AI 팀 / Anthropic Claude Code Docs
- **발행일**: 2023-07-06 (Lost in the Middle arXiv 초판, 2023-11-20 최종 수정, TACL 게재) / 2024-02-16경 (Instruction Stability, arXiv 2402.10962, COLM 2024 — 정확한 제출일 미확인) / 2025-05-09 (LLMs Get Lost in Multi-Turn Conversation) / 2025-07-14 (Chroma Context Rot) / 2025-09-29 (Anthropic context engineering) / Claude Code best practices는 상시 갱신 (2026-09-30 열람)
- **URL**:
  - https://arxiv.org/abs/2307.03172
  - https://arxiv.org/abs/2402.10962
  - https://arxiv.org/abs/2505.06120
  - https://www.trychroma.com/research/context-rot
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://code.claude.com/docs/en/best-practices
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- **자료 유형**: 논문 | 공식 블로그 | 공식 문서

## 핵심 요약
- **Lost in the Middle (Liu et al., 2023; TACL 2024)**: 다중 문서 QA와 key-value 검색에서, 관련 정보가 입력의 처음이나 끝에 있을 때 성능이 가장 높고 중간에 있을 때 크게 떨어지는 U자형 곡선. long-context용 모델도 마찬가지.
- **Instruction drift (Li et al., COLM 2024)**: LLaMA2-chat-70B·GPT-3.5 등에서 시스템 프롬프트로 준 persona·지시가 8라운드 대화 안에 유의미하게 흐트러짐. 원인으로 대화가 길어질수록 초기 지시에 대한 attention이 감소(attention decay)하는 현상을 지목, split-softmax라는 경량 완화법 제안.
- **Multi-turn 성능 저하 (Laban et al., 2025-05-09)**: 20만 건 이상 시뮬레이션 대화에서, 같은 과제를 한 번에 주지 않고 여러 턴에 나눠 주면 6개 생성 과제 평균 39% 성능 하락. 능력 저하는 작고 비일관성(unreliability)이 크게 증가. 모델은 초반에 섣부른 가정을 하고 해법을 서둘러 내놓은 뒤, 잘못 들어선 길에서 회복하지 못함.
- **Context rot (Chroma, 2025-07-14)**: GPT-4.1·Claude 4·Gemini 2.5·Qwen3 등 18개 모델 모두 입력이 길어질수록 단순 과제에서도 성능이 불안정해짐. 질문과 정답의 어휘가 다를 때, 주제가 비슷한 distractor가 있을 때 저하가 커짐.
- **Anthropic context engineering (2025-09-29)**: 토큰이 늘수록 context에서 정보를 정확히 떠올리는 능력이 떨어지는 context rot을 인정하고, context를 한정된 "attention budget"으로 다루라고 권고. 장기 과제 기법으로 compaction(요약), 구조화된 외부 노트(NOTES.md 등), subagent 분리를 제시.
- **Claude Code 문서 (2026-09 열람)**: context가 차면 Claude가 초기 지시를 "잊거나" 실수가 늘 수 있다고 명시. CLAUDE.md가 너무 길면 중요한 규칙이 묻혀 절반을 무시한다고 경고. 같은 문제를 두 번 넘게 교정했다면 `/clear` 후 더 나은 첫 프롬프트로 새로 시작하는 편이 낫다고 권고. compaction 시 보존할 항목(수정 파일 목록, 테스트 명령 등)을 CLAUDE.md에 지정 가능.
- **최신 모델의 변화 (Opus 5 문서, 2026)**: Anthropic은 Claude Opus 5가 1M 토큰 전체에서 지시 따르기·도구 호출·추론이 일관되게 유지된다고 주장. 벤더 자체 주장이며 독립 검증은 본 자료에서 확인하지 못함 — 긴 세션에서 규칙이 흐트러지는 현상은 여전히 실무에서 전제하는 편이 안전.

## 핵심 개념·용어 정의
- **Lost in the middle**: 긴 입력의 중간에 놓인 정보를 잘 활용하지 못하는 위치 편향(U자형 곡선).
- **Context rot**: 입력 토큰이 늘수록 모델의 정보 회수·추론 신뢰도가 떨어지는 현상 (Chroma가 명명, Anthropic도 채택).
- **Instruction / persona drift**: 대화가 길어지며 시스템 프롬프트의 규칙·역할에서 점점 벗어나는 현상.
- **Attention decay**: 새 토큰이 쌓일수록 초기 지시 토큰에 배분되는 attention이 줄어드는 것 (Li et al.의 원인 가설).
- **Compaction**: context 한계에 가까워지면 대화를 요약해 새 context로 이어가는 기법. 요약 과정에서 제약 조건이 빠질 수 있음.
- **Attention budget**: context를 무한 저장소가 아니라 소모되는 주의 자원으로 보는 관점.

## 강연에 쓸 만한 포인트
- **비유**: "회의 3시간째, 처음에 합의한 규칙을 아무도 기억하지 못한다." 또는 "책상 위 서류가 쌓일수록 맨 위와 맨 아래만 보인다"(lost in the middle).
- **숫자**: 8라운드 안에 지시 표류(Li et al., 2024) / 멀티턴 분할 시 평균 39% 하락(Laban et al., 2025-05) / 18개 모델 모두 길이에 따라 저하(Chroma, 2025-07).
- **도식 아이디어**: 가로축 "세션 길이(토큰)", 세로축 "초기 지시 준수율"의 하강 곡선 + compaction 지점에서 계단식 하락(요약 손실) + `/clear`로 리셋. 옆에 U자형 lost-in-the-middle 곡선.
- **실천 규칙 3개**: ① 과제가 바뀌면 `/clear` ② 핵심 규칙은 짧게, 중요한 것만 CLAUDE.md/AGENTS.md에(파일 맨 위·맨 끝 배치 고려) ③ 반드시 지켜야 할 것은 지시가 아니라 hook·권한으로.
- **인용**: "they get lost and do not recover" — Laban et al. (2025-05), 멀티턴에서 한 번 잘못 든 길을 설명하며.

## 원본 그림
- Chroma Context Rot 대표 그래프(입력 길이 증가에 따른 모델별 성능 저하) — https://www.trychroma.com/img/context_rot/hero_plot.png
- Chroma 헤더 이미지 — https://www.trychroma.com/img/context_rot/header_plot.jpg
- Chroma LongMemEval: Claude 계열의 집중(focused) vs 전체(full) 입력 성능 비교 — https://www.trychroma.com/img/context_rot/longmemeval/claude_comparison.png
- Laban et al. Figure 1(teaser: 단일 턴 vs 분할 멀티턴에서 성능·비일관성 변화) — https://arxiv.org/html/2505.06120v1/LIC_Teaser.png
- Li et al. Figure 1(대화 라운드에 따른 instruction drift) — https://arxiv.org/html/2402.10962v1/fig1.png ; attention decay 그래프 — https://arxiv.org/html/2402.10962v1/figs/decay.png
- Lost in the Middle Figure 1(관련 문서 위치에 따른 U자형 정확도 곡선): arXiv PDF p.1에 있으며 HTML 버전·직접 이미지 URL 없음 — https://arxiv.org/pdf/2307.03172 에서 캡처 필요.
- Anthropic context engineering 글: prompt engineering vs context engineering 비교 도식 — https://www-cdn.anthropic.com/images/4zrzovbb/website/faa261102e46c7f090a2402a49000ffae18c5dd6-2292x1290.png

## 코딩 에이전트 사용과의 연결점
- **어떻게 나타나나**: 세션 초반에 "테스트 파일 건드리지 마", "pnpm 써", "한국어 주석" 같은 제약을 줬는데, 수십 번의 파일 읽기·로그 출력 뒤나 auto-compaction 뒤에 슬그머니 어긴다. 긴 디버깅 끝에 원래 목표 대신 곁가지 문제를 풀고 있기도 하다(goal drift).
- **context 위생**: 무관한 작업 사이엔 `/clear`, 대량 탐색은 subagent에 맡겨 메인 context를 깨끗이. 두 번 교정해도 안 되면 새 세션 + 개선된 프롬프트.
- **지속 규칙은 파일로**: 반복 적용할 제약은 CLAUDE.md(Claude Code)·AGENTS.md(Codex)에 짧게 — 길면 묻힌다. compaction 때 보존할 항목도 명시.
- **결정적 강제**: 반드시 지켜야 할 제약(테스트 디렉터리 쓰기 금지, 포맷터 실행 등)은 자연어 지시가 아니라 hook·permission·CI로. 지시는 "권고", hook은 "보장"(Claude Code 문서).
- **장기 과제 설계**: spec·progress 파일·git log를 세션 간 "외부 기억"으로 쓰고, 새 context에서 이를 읽고 시작하게 한다(06번 파일의 long-running harness와 연결).
- **관련 파일**: context rot 자체의 상세는 context engineering 관련 지식 파일(다른 번호)과 연결해서 다룰 것.
