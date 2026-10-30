# Autonomous chemical research with large language models (Coscientist: 실험까지 수행하는 LLM 화학 연구 에이전트)

- **저자/기관**: Daniil A. Boiko, Robert MacKnight, Ben Kline, Gabe Gomes / Carnegie Mellon University (미국)
- **발행일**: *Nature* 624(7992):570–578, 2023-12-20 (접수 2023-04-20, 게재승인 2023-10-27) (2026-10-23 열람)
- **URL**:
  - 학술지판: https://doi.org/10.1038/s41586-023-06792-0 (nature.com은 로그인 리다이렉트로 직접 열지 못함)
  - 전문(PMC, 실제로 확인한 본문): https://pmc.ncbi.nlm.nih.gov/articles/PMC10733136/
  - 간이 구현 코드: https://github.com/gomesgroup/coscientist (논문에 기재된 주소, 저장소 내용은 열어보지 않음)
- **자료 유형**: 논문 (학술지)

## 핵심 요약
- Coscientist는 여러 LLM 모듈로 구성된 에이전트로, 웹·문서 검색, 코드 실행, 실험 자동화 장비 제어를 묶어 화학 실험을 스스로 설계하고 수행한다.
- 구조의 중심은 **Planner**(GPT-4 채팅 어시스턴트)다. Planner는 사용자 요청과 각 명령의 출력을 받아 다음 행동으로 네 가지 명령 중 하나를 고른다.
  - GOOGLE: Web searcher 모듈(그 자체가 LLM)이 웹을 검색한다.
  - PYTHON: 격리된 Docker 컨테이너에서 코드를 실행한다(LLM 없음).
  - DOCUMENTATION: Docs searcher 모듈이 장비·API 문서를 찾아 요약한다.
  - EXPERIMENT: Automation 모듈이 생성된 코드를 실제 장비에서 실행하거나 수동 절차를 출력한다.
- 논문이 제시한 6개 과제: (1) 공개 데이터로 알려진 화합물의 합성 계획, (2) 방대한 하드웨어 문서 검색·탐색, (3) 문서를 이용해 클라우드 실험실에서 고수준 명령 실행, (4) 저수준 명령으로 액체 분주 장비 정밀 제어, (5) 여러 하드웨어 모듈과 데이터 출처를 동시에 쓰는 복합 과제, (6) 기존 실험 데이터를 분석하는 최적화 문제.
- 사용 장비: Opentrons OT-2 액체 분주기(Python API, heater–shaker 모듈 포함), Emerald Cloud Lab(문서로 Symbolic Lab Language를 학습해 HPLC 코드를 생성, 카페인 표준물질로 실행 성공), UV–Vis 플레이트 리더(식용 색소 식별 과제에 사용).
- Pd 촉매 교차결합 실험: Suzuki–Miyaura와 Sonogashira 반응을 대상으로, 에이전트가 반응 조건을 검색하고 결합 상대를 고르고 부피를 계산해 OT-2 프로토콜을 작성했다. 첫 스크립트에서 heater–shaker 메서드 이름을 잘못 썼지만 문서를 다시 찾아 고친 뒤 실행에 성공했다. 생성물은 GC–MS로 확인했다. 플레이트 이동은 사람이 했다.
- 최적화 과제: 모든 조건 조합의 수율이 알려진 두 데이터셋(Perera 등의 Suzuki 흐름 반응, Doyle의 Buchwald–Hartwig C–N 결합)에서 최대 20회 반복으로 고수율 조건을 찾게 했다. 정규화 지표(NMA)로 비교했을 때 두 GPT-4 설정(사전 정보 제공 여부) 모두 베이지안 최적화보다 높았다.
- 비교한 LLM: 합성 계획 과제(7개 화합물)에서 GPT-3.5, GPT-4, Claude 1.3, Falcon-40B-Instruct와 웹 검색 붙은 변형(search-gpt-4, search-gpt-3.5-turbo)을 비교했다. 검색 없는 GPT-4와 Claude 1.3이 기본 모델 중 비슷하게 가장 나았고, Falcon-40B는 대부분 실패했다. 웹 검색을 붙인 GPT-4가 가장 좋았다. Suzuki 최적화에서 GPT-3.5는 요구한 JSON 형식을 자주 어겨 쓸 만한 출력이 적었다.
- 안전·이중 용도: 저자들은 불법 활동·보안 위협 가능성을 언급하고, 간단한 이중 용도(dual-use) 검토를 보충자료에 넣었다(보충자료 자체는 열람하지 않음). 안전 우려 때문에 전체 데이터·코드·프롬프트는 과학 응용에 대한 미국 AI 규제가 마련된 뒤 공개하겠다고 밝혔고, 간이 구현만 GitHub에 공개했다.

## 핵심 개념·용어 정의
- **Planner**: 전체 작업을 조율하는 GPT-4 모듈. 어떤 명령을 쓸지 매 단계 결정한다.
- **Web searcher / Docs searcher**: 검색 결과나 문서를 읽고 요약해 Planner에 넘기는 하위 LLM 모듈.
- **Cloud lab (Emerald Cloud Lab)**: 원격으로 실험을 주문·실행하는 상용 실험 시설. 전용 언어 SLL로 실험을 기술한다.
- **Liquid handler (Opentrons OT-2)**: 피펫 작업을 자동화하는 장비. Python API로 제어한다.
- **NMA (normalized maximum advantage)**: 지금까지 찾은 최고 수율이 평균 대비 얼마나 나은지를 최대치로 나눈 값. 1이면 최고 수율 도달, 0이면 무작위 수준.
- **Dual-use**: 연구 목적의 기술이 유해 목적(예: 위험 물질 합성)에도 쓰일 수 있는 성질.

## 강연에 쓸 만한 포인트
- ChemCrow와의 대비: ChemCrow는 "화학 도구를 많이 붙인 에이전트", Coscientist는 "문서를 읽고 장비 코드를 짜서 실제 실험을 돌리는 에이전트"다. 같은 시기(2023) 같은 분야에서 나온 두 설계 방향이라 한 슬라이드에 나란히 두기 좋다.
- 자기 수정 장면: 장비 메서드 이름 오류 → 문서 검색 → 코드 수정 → 재실행 성공. 코딩 에이전트의 "실행 결과를 보고 고친다"는 루프가 실험실에서도 똑같이 작동한다는 예시다.
- "문서가 곧 도구 설명서"라는 점: 장비 API 문서를 검색해 읽는 능력이 있으면 새 장비에도 적응한다. 연구소의 분석 장비·모델 코드 문서화가 에이전트 활용의 전제 조건이 된다는 메시지로 연결할 수 있다(정리자 해석).
- 안전과 공개 범위: 연구진이 코드·프롬프트 전체 공개를 미룬 사례는 "도메인 에이전트는 공개 범위도 설계 대상"이라는 논점으로 쓸 수 있다.
- 인용(1개): "using documentation to execute high-level commands in a cloud laboratory" — Boiko et al., Nature (2023), 과제 3 설명

## 원본 그림
- Fig. 1 시스템 구조(Planner와 GOOGLE·PYTHON·DOCUMENTATION·EXPERIMENT 명령, 하위 모듈이 메시지를 주고받는 구성. 파란 상자는 LLM 모듈, 초록은 Planner, 흰 상자는 LLM을 쓰지 않는 모듈) — https://cdn.ncbi.nlm.nih.gov/pmc/blobs/a882/10733136/f7c6716d86f0/41586_2023_6792_Fig1_HTML.jpg
- 참고: 이미지 URL은 PMC 본문에서 추출한 것이며 개별 파일을 직접 열어 확인하지는 않음.

## Claude Code와의 연결점
- 강연 틀(AI 에이전트 = LLM + 하네스)로 보면, LLM은 GPT-4 Planner이고 하네스는 네 가지 명령과 그 뒤의 모듈(검색, 문서, 코드 실행 샌드박스, 장비 자동화)이다. (이 대응은 정리자 해석이며 논문은 "harness"라는 용어를 쓰지 않는다.)
- Claude Code와의 구조적 대응(정리자 해석): GOOGLE ↔ WebSearch/WebFetch, PYTHON(Docker 격리 실행) ↔ Bash 도구와 샌드박스, DOCUMENTATION ↔ 문서 검색 MCP 또는 스킬에 넣어둔 참고 문서, EXPERIMENT ↔ 외부 장비·서비스를 호출하는 MCP 서버. Web searcher·Docs searcher가 별도 LLM인 점은 Claude Code가 하위 작업을 subagent에 맡겨 요약만 돌려받는 방식과 닮았다.
- 하네스의 세 요소 중 Coscientist는 "도구"와 "문서 기반 지식"이 강하다. 장비 문서를 검색해 쓰는 부분은 스킬(절차·참고자료 묶음)에 가깝게 볼 수 있다. 장기 기억 기능은 논문에 뚜렷하게 나오지 않는다.
- 도메인 에이전트로 옮기려면 모델이 아니라 명령 목록과 문서·장비 연결을 바꾸면 된다는 것이 이 논문 구조가 주는 시사점이다. 예컨대 환경 연구에서는 EXPERIMENT 자리에 측정망 데이터 API나 수치모델 실행 스크립트를 둘 수 있다(정리자 해석, 논문에 없는 응용).
