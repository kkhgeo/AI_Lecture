# 도메인 특화 AI 에이전트 종합: 정의, 범용 에이전트와의 차이, 만드는 법, 주의점 (01~06 종합, 슬라이드용)

- **저자/기관**: 강연자 정리 (01~06번 노트 종합)
- **발행일**: 2026-10-23
- **URL**: 각 근거는 01~06번 노트의 URL 참조
- **자료 유형**: 종합 노트 (강연자 해석 포함, 해석은 따로 표시)

## 핵심 요약
- **개념은 있다. 이름은 하나로 정해져 있지 않다.** 학계 모델 수준은 "domain specialization"(Ling et al., ACM Computing Surveys 2025), 과학 분야 에이전트는 "scientific agents"(Ren et al. 2025), Anthropic은 "specialized agents", 업계는 "vertical AI agents"(YC Lightcone 2024-11-22)를 쓴다. "domain-specific agents"를 정식 용어로 정의한 대표 1차 출처는 찾지 못했다(01, 06).
- **정의(강연용, 강연자 종합)**: 범용 에이전트의 루프(계획 → 도구 실행 → 관찰·검증)에 특정 분야의 지식, 전문 도구, 데이터, 검증 절차를 결합해, 그 분야의 결과를 그 분야의 기준으로 확인하며 일하는 LLM 에이전트. 근거는 Ren et al.의 범용 에이전트 대비 네 가지 차이(도메인 지식 통합, 전문 도구·장비를 통한 행동, 이질적 과학 데이터, 검증 메커니즘)(06).
- **만드는 법은 대부분 "모델을 새로 만들기"가 아니라 "하네스 쪽을 바꿔 끼우기"다.**
  - ChemCrow: GPT-4 + 화학 도구 18개(학술지판) + ReAct 루프(03).
  - Coscientist: GPT-4 Planner + 웹·문서 검색, 코드 실행, 실험 장비 제어 모듈(04).
  - Biomni: LLM + 문헌에서 캐낸 도구 150·소프트웨어 105·DB 59 + 코드 실행(05).
  - Anthropic 금융 템플릿 10종: Claude + skill(업무 지식) + connector(데이터 접근) + subagent(02). GitHub에 markdown·YAML·JSON 파일만으로 공개.
  - Ling et al.의 기법 분류로는 외부 보강(black box) → 프롬프트 설계(grey box) → 미세조정(white box) 중 앞쪽 두 단계에 해당한다(01). 미세조정 없이도 도메인 특화가 된다는 점이 강의의 핵심 메시지가 될 수 있다.
- **AI 에이전트 그림(8번 슬라이드)과의 연결 (강연자 해석)**: 첫째 칸(LLM + Harness)은 그대로 두고, 둘째 칸(Memory·Skills·Tools)을 도메인 것으로 바꾸면 도메인 특화 에이전트가 된다. 셋째 칸(계획 → 실행 → 검증)에서 검증이 그 분야의 기준(실험, 시뮬레이터, 전문가)으로 바뀐다.

## 핵심 개념·용어 정의
- **범용 vs 도메인 특화 비교표 (Ren et al. 근거, 마지막 행은 강연자 묶음)**:
  | 구분 | 범용 에이전트 (Claude Code, Codex) | 도메인 특화 에이전트 |
  |---|---|---|
  | 지식(Memory) | 일반 지식 + 프로젝트 지침 파일 | 도메인 지식베이스, 문헌, 표준·규정 |
  | 절차(Skills) | 일반 작업 절차 | 분야 표준 절차(예: scRNA-seq QC, AML 규칙) |
  | 도구(Tools) | 파일, 셸, 웹 검색 | 전문 소프트웨어, DB, 시뮬레이터, 실험 장비 |
  | 데이터 | 텍스트, 코드 | 분자 구조, 서열, 지리공간, 관측 자료 |
  | 검증(Verify) | 테스트, 사람 리뷰 | 분야 기준: 실험·시뮬레이터·계산 확인, 전문가 |
  | 제약 | 권한·샌드박스 | 안전 목록(화학무기), 개인정보, 규제, 이중 용도 |
- **자율성 3단계 (Zheng et al., EMNLP 2025)**: Tool(사람이 과제 배정, 한 단계 자동화) → Analyst(사람이 문제 정의·결과 검증, 에이전트가 분석 수행) → Scientist(사람 개입 최소, 가설부터 결론까지)(06). 대학원 연구에서 현실적인 위치는 Analyst 단계(강연자 해석).
- **Ren et al.의 4요소**: Planner, Memory, Action Space, Verifier. 8번 그림의 계획·실행·검증 + 기억과 대응한다(강연자 대응).

## 강연에 쓸 만한 포인트
- **환경·지구과학 사례**: Ren et al.이 지구·환경·기후 영역 예로 GeoAgent, GeoMap-Agent, MineAgent, LLM-Find, PANGAEA GPT, Earth-Agent, ClimateGPT를 든다(06). 개별 논문은 아직 열람하지 않았다. 수문·기후 모델링 에이전트 논문은 이번 조사에서 확인하지 못했다(05).
- **주의점 1, 평가**: ChemCrow에서 GPT-4 평가자는 유창한 GPT-4 단독 답을 선호했지만 화학 전문가는 ChemCrow를 높게 평가했다. 도메인 결과는 LLM 평가로 대신할 수 없다(03).
- **주의점 2, 정확도**: Anthropic도 금융 벤치마크 64.37%를 "업계 최고"로 내세우면서 사람 검토를 전제한다(02). 도메인 특화가 곧 신뢰는 아니다.
- **주의점 3, 안전·이중 용도**: ChemCrow는 화학무기 목록 대조 도구를 넣었고, Coscientist는 안전 우려로 전체 코드·프롬프트를 공개하지 않았다(03, 04).
- **주의점 4, 재현성**: 폐쇄형 API 모델이라 재현이 제한되고(03), 논문 안에서도 수치가 엇갈린다(ChemCrow 도구 13/18/19개, Biomni 문헌 규모 세 가지 표기)(03, 05). 연구에 쓸 때는 실행 기록을 남겨야 한다는 Ren et al.의 윤리 권고와 연결.
- **슬라이드 구성안 (강연자 제안)**:
  1. 정의 슬라이드: 위 정의 + 8번 그림 둘째 칸을 도메인 것으로 바꾼 그림.
  2. 사례 슬라이드: ChemCrow·Coscientist·Biomni를 "LLM + 도메인 도구 + 검증" 표로.
  3. 만들기 슬라이드: 내 분야 에이전트 = 지침 파일 + 스킬 + MCP 연결 (Claude Code로 바로 가능).
  4. 주의 슬라이드: 평가·정확도·안전·재현성.

## 원본 그림
- Ren et al. Fig. 1 (Planner–Memory–Action Space–Verifier 구조): https://arxiv.org/html/2503.24047v3/architecture.png (06)
- Zheng et al. Fig. 2 (자율성 단계 분류): https://arxiv.org/html/2505.13259v3/survey_new.svg (06)
- ChemCrow·Coscientist·Biomni 구조도는 각 노트(03~05) 참조.

## Claude Code와의 연결점
- Claude Code 자체가 범용 하네스이고, 도메인 특화는 사용자가 직접 할 수 있다 (강연자 해석): CLAUDE.md = 분야 지식·규칙(Memory), `.claude/skills/` = 분야 표준 절차(Skills), MCP 서버 = 분야 DB·도구 연결(Tools), 테스트·기준 결과·전문가 리뷰 = 분야 검증(Verify).
- Anthropic의 금융 템플릿과 생명과학 패키지가 정확히 이 구조(skill + connector + subagent)를 Claude Code 플러그인으로 배포한다(02). 연구실 단위로 같은 방식의 "우리 분야 플러그인"을 만들 수 있다는 메시지로 이어진다.
