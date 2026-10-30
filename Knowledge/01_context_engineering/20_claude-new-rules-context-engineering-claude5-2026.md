# The new rules of context engineering for Claude 5 generation models

- **저자/기관**: Thariq Shihipar (Anthropic, Member of Technical Staff)
- **발행일**: 2026-07-24
- **URL**: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models (접속 시 https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/ 로 리다이렉트)
- **자료 유형**: 블로그 (Anthropic/Claude 공식 블로그)

## 핵심 요약

- Anthropic은 Claude 5 세대 모델용으로 **Claude Code 시스템 프롬프트의 80% 이상을 제거**했는데, 코딩 평가에서 측정 가능한 성능 손실이 없었다.
- 이전 모델용으로 쌓아온 규칙들이 오히려 모델을 **과잉 제약(over-constraining)**하고 있었다. 예: 시스템 프롬프트는 "문서화는 적절히"라고 하는데 어떤 skill은 "주석 절대 금지"라고 해, 모델이 모순을 조정하는 데 부담을 졌다.
- 여섯 가지 규칙 전환을 제시한다.
  1. **규칙 주기 → 판단에 맡기기**: 세세한 금지 대신 "주변 코드처럼 읽히게 작성" 같은 원칙
  2. **예시 주기 → 인터페이스 설계**: 예시는 탐색을 좁힌다. 도구 파라미터·열거형을 표현력 있게 설계
  3. **전부 앞에 넣기 → progressive disclosure**: 세부 지침은 skills로, 도구는 지연 로드
  4. **반복 강조 → 간결한 도구 설명**: 시스템 프롬프트와 도구 정의의 중복 제거
  5. **CLAUDE.md에 기억 적기 → auto memory**: 기억은 Claude가 자동 저장
  6. **단순한 스펙 → 풍부한 참조**: 테스트 스위트, 코드 예, 루브릭, 목업 같은 고충실도 자료
- 층별 권장: CLAUDE.md는 가볍게(저장소 목적, 코드베이스 고유의 함정), 파일 시스템만 봐도 알 수 있는 뻔한 내용은 쓰지 말 것. Skills에는 팀 고유 의견을 담되 중요한 부분 외에는 과잉 제약 금지, 긴 skill은 여러 파일로 분할. 참조 자료는 가능하면 코드 형태로.
- 이를 자동으로 돕도록 Claude Code의 `/doctor`가 skills와 CLAUDE.md의 크기를 적정화하는 기능을 갖게 되었다.

## 핵심 개념·용어 정의

- **Over-constraining**: 모델의 판단력을 믿지 않고 규칙을 과도하게 쌓아, 모순·잡음·준수율 저하를 부르는 상태.
- **Scaffolding → Curation**: 모델을 붙잡아 주는 비계 대신, 좋은 자료를 골라 주는 큐레이션으로 무게중심 이동.
- **Rich references**: 말로 된 명세보다 테스트·코드·루브릭처럼 모호함이 적은 자료.

## 강연에 쓸 만한 포인트

- **"Then → Now" 6행 표**: 강연 후반부 "2026년의 context engineering" 슬라이드로 적합. 2025년 자료들(01~13번)과 대비해 "원칙(적게, 고신호로)은 같고, 모델이 좋아질수록 더 적게 넣는다"는 흐름.
- **80% 수치**: "시스템 프롬프트를 5분의 1로 줄여도 성능이 같았다"는 한 줄은 청중에게 강한 인상을 준다. 더 많이 쓰는 것이 더 잘 시키는 것이 아니라는 증거.
- **모순 규칙 예시**: 청중의 CLAUDE.md와 skills 사이에 충돌이 없는지 점검하는 과제로 연결(Drew Breunig의 context clash, 04번).
- **주의점**: 이 글은 Claude 5 세대 기준이다. 구형·소형 모델이나 다른 회사 모델에는 여전히 명시적 규칙이 필요할 수 있음을 함께 언급.
- 인용(1개): Claude Code 시스템 프롬프트의 "over 80%"를 제거 (Anthropic, 2026-07-24)

## Claude Code와의 연결점

- `/doctor`로 CLAUDE.md·skills 적정화 제안 받기.
- auto memory(`/memory`)로 "기억"을 CLAUDE.md에서 분리.
- MCP tool search(지연 로드)와 skills의 on-demand 로드가 규칙 3의 실제 구현.
- 규칙 6 실습: 말로 된 요구사항 대신 실패하는 테스트나 디자인 목업(`@mockup.png`)을 참조로 주고 구현시키기.
