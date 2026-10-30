# Biomni: A General-Purpose Biomedical AI Agent (문헌에서 도구를 캐내 만든 범용 생의학 에이전트)

- **저자/기관**: Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu, Yusuf Roohani, Ryan Li, Lin Qiu, Gavin Li, Junze Zhang, Di Yin, Shruti Marwaha, Jennefer N. Carter, Xin Zhou, Matthew Wheeler, Jonathan A. Bernstein, Mengdi Wang, Peng He, Jingtian Zhou, Michael Snyder, Le Cong, Aviv Regev, Jure Leskovec (프리프린트 저자 23명) / Stanford University 중심. 학술지판 보도자료는 Kexin Huang의 소속을 Stanford 및 Phylo, Inc.로 표기
- **발행일**: bioRxiv 프리프린트 2025-06-02 게시 (DOI 10.1101/2025.05.30.656746). 이후 *Science*에 "Autonomous biomedical research with an artificial intelligence agent"라는 제목으로 2026-07-09 출판 (DOI 10.1126/science.adz4351) (2026-10-23 열람)
- **URL**:
  - 프리프린트: https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1
  - 프리프린트 전문(PMC, 실제로 확인한 본문): https://pmc.ncbi.nlm.nih.gov/articles/PMC12157518/
  - 학술지판: https://www.science.org/doi/10.1126/science.adz4351 (403 응답으로 열지 못함)
  - AAAS 보도자료: https://www.eurekalert.org/news-releases/1134718
  - 코드: https://github.com/snap-stanford/biomni (주소만 확인)
- **자료 유형**: 논문 (프리프린트 → 학술지 게재)
- **주의**: 아래 수치는 모두 bioRxiv v1(PMC 전문) 기준이다. *Science* 게재판은 본문을 열지 못했고, 게재 사실·제목·DOI·날짜는 AAAS 보도자료(EurekAlert)와 Stanford 보도 기사(Tech Xplore)로만 확인했다. 게재판에서 수치나 구성이 바뀌었을 수 있다.

## 핵심 요약
- Biomni는 특정 과제용이 아닌 "범용" 생의학 에이전트를 목표로 한다. 두 부분으로 구성된다. **Biomni-E1**은 도구·소프트웨어·데이터베이스를 모은 환경(action space)이고, **Biomni-A1**은 이 환경을 쓰는 에이전트다.
- 환경 구축 방법(action discovery): LLM 에이전트가 bioRxiv의 25개 생의학 분야 논문에서 과제, 소프트웨어, 데이터베이스를 추출하고 사람 전문가가 이를 정리·검증했다. 문헌 규모는 원문 안에서도 표기가 엇갈린다. 초록은 "수만 편", Fig. 1과 Results는 2,500편(분야당 100편), Methods는 2024년 논문 100편이라고 쓴다.
- 환경 규모(Biomni-E1): 전문 도구 150개, 소프트웨어 패키지 105개, 데이터베이스 59개. 도구는 전문가가 테스트 케이스로 검증했고, 소프트웨어는 Python·R·Bash를 지원하는 컨테이너 환경에 설치된다. 대형 웹 API 데이터베이스는 자연어 질의 함수 하나로 감싸고, 나머지는 로컬 표(pandas DataFrame)로 전처리했다.
- 에이전트 구조(Biomni-A1): LLM 추론 + 검색 증강 계획(retrieval-augmented planning) + 코드 기반 실행. CodeAct 방식으로 LLM이 Python/R/Bash 코드를 써서 실행하고 결과를 관찰한다. 별도 LLM이 질의마다 필요한 함수·데이터·소프트웨어를 골라 컨텍스트에 넣고, 에이전트는 번호 붙은 계획을 세운 뒤 실행하면서 고친다.
- 구동 LLM: 확인한 본문 범위에서는 Biomni 자체의 기본 모델을 명확히 확인하지 못했다. 비교 기준선(base LLM)으로 Claude 3.7 Sonnet이 쓰였다.
- 벤치마크(프리프린트 기준):
  - Humanity's Last Exam 생의학 52문항: Biomni 17.3%, 기본 LLM 6.0%, 코딩 에이전트 12.8%, 문헌 에이전트 12.2%.
  - LAB-Bench DbQA: Biomni 74.4%, 인간 전문가 74.7%(API 비용 때문에 12.5% 부분집합으로 평가).
  - LAB-Bench SeqQA: Biomni 81.9%, 인간 78.8%.
  - 새로 만든 실제 과제 8종(변이 우선순위화, GWAS 원인 유전자 탐지, CRISPR 스크린 설계, 희귀질환 진단, 약물 재창출, scRNA-seq 세포 주석, 마이크로바이옴 분석, 환자 유전자 우선순위화): 기본 LLM 대비 평균 상대 향상 402.3%, 코딩 에이전트 대비 43.0%, Biomni-ReAct 대비 20.4%.
- 사례 연구: 웨어러블 데이터(30명, 458개 파일) 분석, 골격 조직 multi-omics 약 33.6만 개 핵에 대한 유전자 조절 네트워크 분석(약 5시간), 분자 클로닝 프로토콜 설계와 실제 습식 실험 검증(B2M guide RNA를 lentiCRISPR v2 Blast에 클로닝, 시험한 두 콜로니에서 Sanger 시퀀싱으로 삽입 확인). 클로닝 과제 수는 Results 10개, Methods 20개로 원문 내에서 다르다.
- 공개: 코드 GitHub 공개, 웹 인터페이스(biomni.stanford.edu), 데이터 Harvard Dataverse. 저자들은 공개 웹 도구에 보호 대상 건강정보(PHI)를 넣지 말라고 명시한다.
- 한계(저자 명시): 평가 과제가 분야 일부만 다룬다. 모든 과제에서 전문가 수준은 아니며, 미묘한 임상 판단과 새로운 실험 추론에 약하다. action discovery가 최근 문헌에 치우쳐 오래된 기초 방법을 놓칠 수 있다.
- 사용 규모 주장(미검증): Stanford 보도 기사(Tech Xplore 게재)는 시제품을 1만 개 이상 연구실이 쓴다고 전하고, 분석 예시에서 사람이 60시간 넘게 걸릴 작업을 약 40분에 했다고 쓴다. 둘 다 개발진 발언 기반이며 독립 검증되지 않았다. 슬라이드에 쓰지 않거나 "개발진 주장"으로 표기할 것.

## 핵심 개념·용어 정의
- **Action space (행동 공간)**: 에이전트가 쓸 수 있는 도구·소프트웨어·데이터베이스 전체. Biomni는 이를 Biomni-E1이라는 통합 환경으로 만들었다.
- **Action discovery agent**: 논문을 읽고 그 분야 연구자가 실제로 쓰는 과제·도구·데이터베이스를 뽑아내는 에이전트. 환경 구축을 자동화하는 부분.
- **Retrieval-augmented planning**: 수백 개 자원을 모두 컨텍스트에 넣지 않고, 질의에 맞는 것만 검색해 계획에 쓰는 방식.
- **CodeAct**: 도구 호출을 JSON 대신 실행 가능한 코드로 표현하는 에이전트 방식. 여러 도구를 한 스크립트에서 조합할 수 있다.
- **LAB-Bench**: 생물학 연구 실무 능력을 재는 벤치마크. DbQA(데이터베이스 질의), SeqQA(서열 분석) 등 하위 세트가 있다.

## 강연에 쓸 만한 포인트
- ChemCrow·Coscientist와의 차이: 앞의 두 시스템은 사람이 도구를 골라 붙였다. Biomni는 "도구 목록 자체를 문헌에서 캐낸다"는 단계가 추가되었다. 도메인 에이전트를 만드는 비용의 상당 부분이 환경 구축이라는 점을 보여준다.
- 규모 비교 한 줄: ChemCrow 도구 18개 vs Biomni 도구 150 + 소프트웨어 105 + DB 59. 자원이 많아지면 "필요한 것만 골라 넣는 검색 단계"가 필수가 된다.
- 인간 대비 점수(DbQA 74.4% vs 74.7%)는 인상적이지만 12.5% 부분집합 결과라는 단서를 함께 적어야 한다.
- 원문 내부 불일치(문헌 수, 클로닝 과제 수)는 "프리프린트 수치는 게재판에서 확인하라"는 연구 관행 메시지로 쓸 수 있다.
- 프리프린트(2025-06) → *Science* 게재(2026-07): 약 13개월. 제목이 "general-purpose agent"에서 "autonomous biomedical research"로 바뀐 점도 눈여겨볼 만하다.
- 인용(1개): "25 biomedical domains" — Huang et al., bioRxiv 2025.05.30.656746 초록

## 원본 그림
- Fig. 1 통합 생의학 행동 공간과 에이전트 환경 개요(a: 행동 공간 구축 과정, b: 분야별 도구·데이터베이스, c: 생물학 질문에 대한 추론과 코드 작성 예시) — https://cdn.ncbi.nlm.nih.gov/pmc/blobs/ab2b/12157518/ca9ba6c995f5/nihpp-2025.05.30.656746v1-f0001.jpg
- 참고: 프리프린트(CC BY 4.0) 그림이며 이미지 URL은 PMC 본문에서 추출. 개별 파일 직접 접근은 확인하지 않음. *Science* 게재판 그림은 확인하지 못함.

## Claude Code와의 연결점
- 강연 틀(AI 에이전트 = LLM + 하네스)에 가장 잘 맞는 사례다. LLM은 그대로 두고, 하네스 쪽에 도구(150개)·소프트웨어(105개)·데이터(59개)를 채워 넣어 생의학 에이전트를 만들었다. (이 대응은 정리자 해석이며 논문은 "harness"라는 용어를 쓰지 않는다.)
- Claude Code 구성 요소와의 대응(정리자 해석): 검증된 도구 함수와 노하우 ↔ 스킬(skills), 컨테이너 안 Python/R/Bash 실행 ↔ Bash 도구, 웹 API 데이터베이스 ↔ MCP 서버, 질의별 자원 검색 ↔ 스킬 설명만 먼저 읽고 필요할 때 본문을 불러오는 점진적 로딩(progressive disclosure).
- 기억 측면은 프리프린트에서 뚜렷하지 않다. 확인한 범위에서는 세션 간 장기 기억보다 "환경(도구·데이터)"을 키우는 데 초점이 있다.
- 환경 연구소에 주는 시사점(정리자 해석): 분야 문헌에서 자주 쓰는 데이터(대기·수질 측정망, 위성자료), 소프트웨어(GIS, 수치모델), 분석 절차를 목록화하는 작업이 곧 도메인 에이전트의 하네스를 만드는 작업이다.

## 참고: 지구·환경과학 분야의 유사 시스템
아래는 초록 수준으로만 확인한 자료다. 본문 수치는 검증하지 않았다.
- **Autonomous GIS / LLM-Geo** — Zhenlong Li, Huan Ning. arXiv 2305.06453 (v1 2023-05-10, v4 2023-05-29). GPT-4를 추론 핵심으로 써서 공간 데이터 수집·분석·시각화를 수행하는 시제품 LLM-Geo를 제시. 자율 GIS의 목표로 자기 생성·자기 조직·자기 검증·자기 실행·자기 성장의 5가지를 든다. 사례 연구 3건. 주의: arXiv 초록만 확인. arXiv 페이지에 학술지 정보가 없어 게재 여부는 확인하지 않음.
- **LLM-Find (An Autonomous GIS Agent Framework for Geospatial Data Retrieval)** — arXiv 2407.21024 (2024-07). LLM이 미리 정한 데이터 출처 목록에서 출처를 고르고, 출처별 "handbook"을 참고해 데이터 수집 코드를 생성·실행·디버깅한다. 새 출처를 플러그인처럼 추가할 수 있다. 주의: 검색 결과 요약으로만 확인했고 초록 페이지는 열지 않음. 저자명 미확인. 프리프린트.
- **GISclaw** — Jinzhen Han, JinByeong Lee, Yuri Shim, Jisung Kim, Jae-Joon Lee. arXiv 2603.26845 (v1 2026-03-27, v2 2026-05-03). 순수 Python 오픈소스 지리공간 분석 에이전트. LLM 추론 핵심 + 지속형 Python 샌드박스 + 프롬프트 규칙 3개 + 오류 기억 모듈로 구성되며, 로컬 오픈 가중치 모델로도 돌아간다. GeoAnalystBench 50개 과제(평균 5.8단계)에서 반복 3회 평균 성공률 97%. 단일 ReAct 루프가 클라우드 모델에서는 계획-실행 이중 에이전트보다 나았고, 로컬 14B 모델에서만 다중 에이전트 설계가 도움이 되었다고 보고. 주의: arXiv 초록만 확인, 프리프린트.
- 수문(hydrology)·기후 모델링 전용 에이전트는 이번 조사에서 실제 논문을 확인하지 못해 싣지 않았다.
