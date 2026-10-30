# 12-Factor Agents: Principles for building reliable LLM applications

- **저자/기관**: Dex Horthy (HumanLayer)
- **발행일**: 2025 (GitHub 저장소, 2025년 봄 공개 후 지속 갱신. 정확한 최초 공개일은 저장소에서 확인하지 못함)
- **URL**: https://github.com/humanlayer/12-factor-agents (Factor 3: https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md)
- **자료 유형**: 공개 문서 (GitHub 원칙 모음, 웹앱 설계의 "12-Factor App"을 패러디)

## 핵심 요약

- 실제 프로덕션에 들어간 "AI 에이전트" 대부분은 거창한 자율 에이전트가 아니라, 결정적 코드 사이에 LLM 단계를 적절히 끼워 넣은 소프트웨어라는 관찰에서 출발한다.
- 무거운 프레임워크를 통째로 쓰기보다 작은 모듈식 원칙을 기존 제품에 녹이는 것이 품질 기준을 넘는 가장 빠른 길이라고 주장한다.
- 12개 원칙 중 context engineering의 중심은 **Factor 3: Own your context window**다. LLM은 입력을 출력으로 바꾸는 상태 없는(stateless) 함수이므로, 입력(컨텍스트)을 최적화하는 것이 성능을 올리는 유일하고 가장 큰 지렛대라는 논리다.
- 표준 채팅 메시지 형식(system/user/assistant/tool)에만 의존하지 말고, 이벤트 기록을 XML 등 밀도 높은 사용자 정의 형식으로 직접 직렬화해 토큰·주의 효율을 높이라고 제안한다.
- 저자는 이 저장소를 통해 "context engineering" 용어 확산에 앞장선 인물 중 하나다.

## 핵심 개념·용어 정의

**12개 원칙 목록**

1. Natural Language to Tool Calls (자연어를 도구 호출로)
2. Own your prompts (프롬프트를 직접 소유)
3. **Own your context window (컨텍스트 창을 직접 소유)**
4. Tools are just structured outputs (도구는 구조화 출력일 뿐)
5. Unify execution state and business state (실행 상태와 비즈니스 상태 통합)
6. Launch/Pause/Resume with simple APIs
7. Contact humans with tool calls (사람 호출도 도구 호출로)
8. Own your control flow (제어 흐름 소유)
9. **Compact Errors into Context Window (에러를 압축해 컨텍스트에)**
10. **Small, Focused Agents (작고 집중된 에이전트)**
11. Trigger from anywhere
12. Make your agent a stateless reducer (에이전트를 상태 없는 reducer로)

- **Factor 3이 말하는 컨텍스트 구성요소**: 프롬프트와 지시, 검색 문서(RAG), 과거 상태·도구 호출·결과, 관련 대화의 과거 메시지·이벤트, 구조화 출력 지시.
- **Factor 10**: 에이전트를 작게 유지해야 컨텍스트가 관리 가능한 크기로 남는다 → context isolation과 같은 맥락.

## 강연에 쓸 만한 포인트

- **"LLM = 상태 없는 함수" 도식**: `output = LLM(context)`. 모델을 바꾸지 못한다면 바꿀 수 있는 건 context뿐이다 → context engineering이 유일한 레버라는 메시지를 한 줄 수식으로.
- **표준 메시지 vs 사용자 정의 형식 비교**: 같은 이벤트 기록을 JSON 메시지 배열로 줄 때와 XML 태그 묶음 하나로 줄 때 토큰 수 비교(직접 세어 보여주기).
- **12-Factor App 패러디**라는 점은 개발자 청중에게 친숙한 도입부.
- 인용(1개): Factor 3 제목 "Own your context window" (HumanLayer, 12-factor-agents)

## Claude Code와의 연결점

- Claude Code 사용자가 "컨텍스트를 소유"하는 방법: `CLAUDE.md`·rules로 상시 컨텍스트 설계, `/context`로 구성 점검, `/compact <지시>`로 요약 내용 통제, CLAUDE.md의 "Compact Instructions" 절로 압축 시 보존 항목 지정.
- Factor 9(에러 압축): 긴 테스트 로그 전체 대신 핵심 실패만 요약해 넣도록 subagent에게 "실패 테스트 상위 5개만 보고"라고 위임.
- Factor 10(작은 에이전트): `.claude/agents/`에 역할이 좁은 custom subagent 정의(도구 제한, 짧은 시스템 프롬프트).
- Claude Agent SDK로 직접 에이전트를 만들 때는 시스템 프롬프트와 컨텍스트 형식을 "소유"하는 실습 가능.
