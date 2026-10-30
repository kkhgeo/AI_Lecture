# RAG의 기원과 세 가지 패러다임 (Lewis et al. 2020의 원형에서 Gao et al. 서베이의 Naive·Advanced·Modular RAG까지)

- **저자/기관**:
  - Lewis et al. (2020): Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela / Facebook AI Research, University College London, New York University (논문 표지에 세 기관이 함께 표기됨. 저자별 소속 대응은 표지 텍스트에서 확인하지 못함)
  - Gao et al. (2023): Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang, Haofen Wang / Tongji University(Shanghai Research Institute for Intelligent Autonomous Systems; College of Design and Innovation), Fudan University(Shanghai Key Laboratory of Data Science). 교신저자 Haofen Wang
- **발행일**:
  - Lewis et al.: arXiv v1 2020-05-22, 최신 v4 2021-04-12. NeurIPS 2020 채택 (2026-10-23 열람)
  - Gao et al.: arXiv v1 2023-12-18, 최신 v5 2024-03-27 (2026-10-23 열람)
- **URL**:
  - https://arxiv.org/abs/2005.11401 (본문은 v4 PDF로 확인)
  - https://arxiv.org/abs/2312.10997 (본문은 v5 PDF와 arXiv HTML로 확인)
  - 저장소(서베이 자료 모음): https://github.com/Tongji-KGLLM/RAG-Survey (논문 각주에 표기, 직접 열어보지는 않음)
- **자료 유형**: 논문 (Lewis et al.: 학회 논문 NeurIPS 2020 / Gao et al.: 서베이 프리프린트, arXiv)

## 핵심 요약
- **RAG라는 이름의 출발점은 Lewis et al. (2020)이다.** 사전학습 언어모델은 지식을 파라미터 안에 저장하지만, 그 지식을 정확히 꺼내 쓰는 능력이 제한적이고, 답의 근거(provenance)를 보여주거나 세계 지식을 갱신하기가 어렵다는 것이 논문의 문제의식이다. 서론은 이런 모델이 기억을 쉽게 확장·수정하지 못하고 "hallucination"을 낼 수 있다고 적는다.
- **해법은 두 종류의 기억을 결합하는 것.** 파라미터 기억(parametric memory)은 사전학습된 seq2seq 생성기인 BART-large(약 4억 개 파라미터)이고, 비파라미터 기억(non-parametric memory)은 Wikipedia 전체를 밀집 벡터(dense vector)로 색인한 문서 인덱스다. 둘을 잇는 검색기(retriever)는 DPR(Dense Passage Retriever)이며, BERT-base 기반의 질의 인코더와 문서 인코더로 이뤄진 bi-encoder 구조다.
- **인덱스 규모**: 2018년 12월 Wikipedia 덤프를 겹치지 않는 100단어 단위로 잘라 약 2,100만(21M) 개 문서로 만들고, FAISS로 HNSW 근사 MIPS(Maximum Inner Product Search) 인덱스를 구축했다. 학습 때는 질의마다 상위 k개(k는 5 또는 10)를 검색한다.
- **학습 방식**: 어떤 문서를 가져와야 하는지에 대한 직접 지도 없이 검색기와 생성기를 end-to-end로 함께 미세조정한다. 검색된 문서를 잠재변수(latent variable)로 보고 상위 K개에 대해 확률을 합산(marginalize)한다. 문서 인코더와 인덱스는 고정하고 질의 인코더와 BART만 미세조정한다.
- **두 가지 변형**: RAG-Sequence는 답 전체를 하나의 같은 문서에 기대어 생성하고, RAG-Token은 토큰마다 다른 문서를 참고할 수 있다. 분류 과제(출력 길이 1)에서는 둘이 같아진다.
- **대표 결과(Table 1, Exact Match)**: Natural Questions에서 RAG-Seq. 44.5 / RAG-Token 44.1 (DPR 41.5, REALM 40.4, T5-11B+SSM 36.6), WebQuestions에서 RAG-Token 45.5 / RAG-Seq. 45.2, CuratedTrec에서 RAG-Seq. 52.2, TriviaQA(Wiki 테스트셋)에서 RAG-Seq. 68.0. 논문은 네 개 open-domain QA 과제에서 새 최고 성능을 냈다고 쓰되, TriviaQA는 T5와 비교 가능한 분할에서만 그렇다고 단서를 단다. 정답이 검색 문서 어디에도 없는 NQ 사례에서도 11.8%를 맞혔다(추출형 모델이라면 0%).
- **생성 과제**: Jeopardy 질문 생성 사람 평가(452쌍)에서 RAG가 더 사실적이라는 판정이 42.7%, BART가 더 사실적이라는 판정이 7.1%였다. MS-MARCO에서는 RAG-Sequence가 BART보다 BLEU·ROUGE-L 모두 2.6점 높았다. FEVER 3-way 분류에서는 검색 지도(retrieval supervision)를 쓰는 최고 파이프라인과 4.3% 이내 차이였다.
- **지식 갱신 실험(index hot-swapping)**: 2016년 덤프 인덱스와 2018년 덤프 인덱스를 바꿔 끼우며 세계 지도자 82명에 대해 질문했다. 시점이 맞는 인덱스에서는 70%(2016)·68%(2018)를 맞혔고, 시점이 어긋나면 12%·4%로 떨어졌다. 재학습 없이 비파라미터 기억만 교체해 지식을 갱신할 수 있다는 근거로 제시된다.
- **Gao et al. (2023)의 서베이는 LLM 시대의 RAG를 세 패러다임으로 정리한다.** 100편 이상의 RAG 연구를 Naive RAG → Advanced RAG → Modular RAG로 묶고, 검색(Retrieval)·생성(Generation)·증강(Augmentation) 세 축과 평가 체계를 정리했다. 26개 과제, 약 50개 데이터셋을 다룬다고 밝힌다.
- **Naive RAG**: ChatGPT 확산 직후 자리 잡은 가장 단순한 형태. 색인(indexing: 문서 정제 → 청크 분할 → 임베딩 → 벡터 DB 저장) → 검색(retrieval: 질의 임베딩과 유사도가 높은 상위 K개 청크) → 생성(generation: 질의와 청크를 프롬프트로 합쳐 LLM이 답함)의 사슬. "Retrieve-Read" 구조라고도 부른다. 한계로 (1) 검색의 정밀도·재현율 부족, (2) 검색 문맥에 근거하지 않은 내용을 만드는 환각, (3) 검색 정보와 과제를 엮을 때의 중복·비일관성, (4) 원 질의 한 번의 검색으로는 복잡한 문제에 필요한 문맥을 얻기 어렵다는 점을 든다.
- **Advanced RAG**: Naive RAG의 사슬 구조는 유지하면서 검색 전후를 다듬는다. 검색 전(pre-retrieval)에는 색인 품질(데이터 세분화, 색인 구조 최적화, 메타데이터, 정렬 최적화, 혼합 검색)과 질의(query rewriting, transformation, expansion)를 개선한다. 검색 후(post-retrieval)에는 재순위화(rerank)와 문맥 압축(context compressing)으로 LLM에 들어갈 정보를 고른다.
- **Modular RAG**: 앞의 둘을 계승하되 기능 모듈을 추가·교체하고 모듈 간 흐름을 재배치할 수 있게 한 형태. 새 모듈로 Search, RAG-Fusion, Memory, Routing, Predict, Task Adapter를, 새 패턴으로 Rewrite-Retrieve-Read, Generate-Read, Recite-Read, DSP, ITER-RETGEN 등을 든다. 서베이는 FLARE와 Self-RAG를 Modular RAG의 유연한 흐름이 가져온 "적응형 검색(adaptive retrieval)"의 예로 들며, 상황에 따라 검색이 필요한지부터 판단한다는 점에서 고정된 검색 절차를 넘어선다고 설명한다.
- **증강 과정(Section V)이 agentic RAG로 넘어가는 다리다.** 서베이는 "한 번 검색하고 생성"하는 기본형이 다단계 추론이 필요한 복잡한 문제에 부족하다고 보고, 세 가지 대안을 정리한다.
  - 반복 검색(iterative retrieval): 원 질의와 지금까지 생성한 텍스트를 바탕으로 지식 베이스를 되풀이해 검색. 예: ITER-RETGEN. 의미 단절과 무관한 정보 누적이 약점.
  - 재귀 검색(recursive retrieval): 이전 검색 결과를 보고 질의를 점점 다듬거나 문제를 하위 문제로 쪼갬. 예: IRCoT(chain-of-thought로 검색을 이끌고 검색 결과로 CoT를 고침), ToC(모호한 질의를 명확화 트리로 정리). 계층적 색인 탐색, 그래프 데이터의 multi-hop 검색과 함께 쓰임.
  - 적응형 검색(adaptive retrieval): LLM이 검색할 시점과 내용을 스스로 정함. FLARE는 생성 중인 토큰의 확률(신뢰도)이 임계값 아래로 떨어지면 검색을 발동하고, Self-RAG는 "retrieve"와 "critic" 두 종류의 반성 토큰(reflection token)으로 검색 여부를 정하고 출력을 스스로 평가한다. WebGPT는 강화학습으로 GPT-3가 검색엔진 질의·결과 탐색·인용을 특수 토큰으로 수행하게 했다.
- **Gao et al.이 직접 말하는 "agent"와의 연결**: 서베이는 적응형 검색을 LLM이 스스로 능동적 판단을 내리는 더 넓은 흐름의 일부로 놓고, 그 예로 AutoGPT, Toolformer, Graph-Toolformer를 든다. LLM이 언제 검색할지 스스로 정하는 모습을 에이전트가 도구를 쓰는 방식에 빗댄다. 또 향후 과제 절에서 CRAG가 가벼운 검색 평가기로 검색 문서 품질을 판정하고 신뢰도에 따라 다른 검색 행동을 촉발한다고 소개한다. 다만 서베이는 "agentic RAG"라는 용어를 쓰지 않으며, 이를 독립된 네 번째 패러다임으로 제시하지도 않는다.
- **평가(Section VI)**: 평가 대상은 검색 품질(Hit Rate, MRR, NDCG 등)과 생성 품질. 품질 점수 3가지(context relevance, answer faithfulness, answer relevance)와 필요 능력 4가지(noise robustness, negative rejection, information integration, counterfactual robustness)를 정리한다. 벤치마크로 RGB, RECALL, CRUD를, LLM을 심판으로 쓰는 자동 평가 도구로 RAGAS, ARES, TruLens를 든다(Table IV). 서베이는 이 지표들이 아직 성숙하거나 표준화된 방식은 아니라고 단서를 단다.
- **향후 과제(Section VII)**: 긴 문맥(long context)과의 관계(20만 토큰 이상을 다루는 LLM이 등장해도 속도와 근거 추적성 면에서 RAG의 역할이 남는다는 주장), 노이즈·반사실 정보에 대한 견고성, RAG와 미세조정의 결합, RAG의 스케일링 법칙, 실서비스용 RAG, 멀티모달 RAG.

## 핵심 개념·용어 정의
- **Parametric memory (파라미터 기억)**: Lewis et al.에서 BART 생성기의 파라미터 자체. 사전학습 중 모델 가중치에 암묵적으로 저장된 지식.
- **Non-parametric memory (비파라미터 기억)**: Lewis et al.에서 DPR로 만든 Wikipedia 밀집 벡터 인덱스. 재학습 없이 내용을 교체·확장할 수 있고 어떤 문서를 참고했는지 들여다볼 수 있다.
- **DPR (Dense Passage Retriever)**: BERT-base 질의 인코더와 문서 인코더가 각각 벡터를 만들고 내적으로 관련도를 매기는 bi-encoder 검색기. RAG의 검색기 초기값으로 쓰였고, 이 초기 검색기는 NQ와 TriviaQA 정답 문서 검색으로 학습된 것이다.
- **MIPS (Maximum Inner Product Search)**: 질의 벡터와 내적이 가장 큰 문서 k개를 찾는 문제. FAISS로 근사해 빠르게 푼다.
- **RAG-Sequence / RAG-Token**: 답 전체에 같은 문서를 쓰는지(Sequence), 토큰마다 다른 문서를 섞어 쓸 수 있는지(Token)의 차이.
- **Index hot-swapping**: 비파라미터 기억(인덱스)만 갈아 끼워 모델 지식을 갱신하는 것.
- **Naive / Advanced / Modular RAG**: Gao et al.의 세 패러다임. 순서대로 단순 사슬(색인-검색-생성), 검색 전후 최적화가 붙은 사슬, 모듈을 교체·재배치할 수 있는 유연한 구조.
- **Pre-retrieval / Post-retrieval**: 검색 전 단계(색인 구조, 질의 재작성·확장)와 검색 후 단계(재순위화, 문맥 압축)의 최적화.
- **Iterative / Recursive / Adaptive retrieval**: 반복해서 검색, 질의를 다듬거나 쪼개며 검색, 모델이 검색 여부와 시점을 스스로 결정. 뒤로 갈수록 모델의 자율 판단이 커진다.
- **Reflection token (Self-RAG)**: 모델이 "지금 검색이 필요한가", "이 출력이 적절한가"를 스스로 표시하는 특수 토큰.
- **RAG 품질 점수 3종**: context relevance(가져온 문맥이 관련 있는가), answer faithfulness(답이 문맥에 충실한가), answer relevance(답이 질문에 맞는가).

## 강연에 쓸 만한 포인트
- 도식 아이디어: "닫힌 책 시험 vs 열린 책 시험". 파라미터 기억만 쓰는 LLM은 외운 것으로 답하고, RAG는 시험장에 참고서(Wikipedia 2,100만 조각)를 들고 들어간다. Lewis et al.의 Table 1 자체가 closed-book(T5)과 open-book(REALM, DPR, RAG)으로 행을 나눠 놓아 이 비유를 그대로 뒷받침한다.
- 환경연구원 청중용 연결(강연자 해석): 인덱스 교체 실험(2016 vs 2018 인덱스, 시점 일치 시 약 70%, 불일치 시 4~12%)은 "법령·기준·통계가 바뀌면 모델을 다시 학습시키지 않고 문서 창고만 바꾸면 된다"는 메시지로 쓸 수 있다. 다만 원 실험은 세계 지도자 82명이라는 작은 사례다.
- Gao et al. Figure 3(세 패러다임 비교도)은 한 장으로 "사슬에서 모듈로"의 흐름을 보여준다. 캡션 끝에서 Modular RAG가 반복·적응형 검색을 포함한다고 밝히는 점이 다음 슬라이드(agentic RAG)로 넘어가는 연결고리가 된다.
- Gao et al. Figure 5(반복·재귀·적응형 검색)는 "검색을 한 번 하는 파이프라인"에서 "검색할지 말지를 모델이 정하는 루프"로 넘어가는 장면이다. 강연에서 agentic RAG의 직전 단계로 쓰기 좋다.
- 메시지(강연자 해석): RAG 연구의 흐름은 "누가 검색을 결정하는가"가 개발자의 고정 파이프라인에서 모델 자신에게로 옮겨가는 과정으로 읽을 수 있다. Naive RAG는 사람이 짠 절차대로 항상 한 번 검색하고, 적응형 검색은 모델이 검색 시점을 정한다. 이 해석은 Anthropic의 workflow vs agent 구분(03_coding_agents/01번 노트)과 겹친다. Gao et al.이 이 구분을 직접 쓰지는 않는다.
- 주의할 점: Gao et al.은 "agentic RAG"라는 용어도, 네 번째 패러다임도 제시하지 않는다. 이 서베이를 근거로 "agentic RAG가 여기서 시작됐다"고 말하면 과장이다. 서베이가 말하는 범위는 "적응형 검색은 LLM이 능동적으로 판단하는 흐름의 일부이며, 에이전트의 도구 사용과 닮았다"까지다.
- 인용(1개): "akin to how an agent utilizes tools" — Gao et al. (2023), Section V-C Adaptive Retrieval

## 원본 그림
- Lewis et al. Figure 1: RAG 전체 구조(질의 인코더 → MIPS로 문서 인덱스에서 top-K 검색 → BART 생성기, end-to-end 역전파). 강연용으로 가장 유용 — https://arxiv.org/html/2005.11401v4/RAG-Architecture.svg
- Lewis et al. Figure 2: RAG-Token이 "Hemingway" 입력으로 Jeopardy 질문을 생성할 때 토큰별 문서 사후확률(posterior) — https://arxiv.org/html/2005.11401v4/posterior_plot.png
- Gao et al. Fig. 1: RAG 연구 기술 계통도(technology tree; 사전학습·미세조정·추론 단계별) — https://arxiv.org/html/2312.10997v5/images/rag_tech_tree.png
- Gao et al. Fig. 2: 질의응답에 적용된 RAG 과정 예시(색인 → 검색 → 생성 3단계) — https://arxiv.org/html/2312.10997v5/images/RAG_case.png
- Gao et al. Fig. 3: Naive / Advanced / Modular RAG 세 패러다임 비교도. 강연용 핵심 그림 — https://arxiv.org/html/2312.10997v5/images/RAG_FrameCompre_eng.png
- Gao et al. Fig. 4: RAG·미세조정·프롬프트 엔지니어링 비교(외부 지식 필요도 × 모델 적응 필요도 사분면) — https://arxiv.org/html/2312.10997v5/images/rag_FT.png
- Gao et al. Fig. 5: 반복(iterative)·재귀(recursive)·적응형(adaptive) 검색 비교. agentic RAG로 넘어가는 다리 — https://arxiv.org/html/2312.10997v5/images/aug_process.png
- Gao et al. Fig. 6: RAG 생태계 요약 — https://arxiv.org/html/2312.10997v5/images/rag_summary.png
- 참고: 위 URL은 arXiv HTML 페이지의 img src를 절대경로로 바꾼 것이며, 모두 HTTP 200 응답을 확인함(2026-10-23). 그림과 번호의 대응은 HTML figcaption과 PDF 캡션으로 확인했고, 이미지 내용 자체는 열어보지 않음.

## Claude Code와의 연결점
- **강연 틀과의 대응(강연자 해석)**: "AI 에이전트 = LLM + 하네스" 틀로 보면 Lewis et al.의 RAG는 파라미터 기억(LLM) 바깥에 비파라미터 기억(외부 문서 인덱스)을 붙인 초기 사례다. 하네스가 기억·스킬·도구를 준다는 관점에서 RAG는 그중 "기억" 하나를 고정 파이프라인으로 붙인 형태라고 볼 수 있다.
- **검색 주체의 이동(강연자 해석)**: Naive·Advanced RAG에서는 검색이 매번 정해진 단계로 일어나고, 적응형 검색에서 모델이 검색 시점을 고르기 시작한다. Claude Code의 agentic loop(gather context → take action → verify results)는 이 흐름의 끝에 있다. 공식 문서(https://code.claude.com/docs/en/how-claude-code-works)는 Claude가 앞 단계에서 배운 것을 보고 다음에 어떤 도구를 쓸지 정한다고 설명한다. 즉 "검색"이 파이프라인의 고정 단계가 아니라 루프 안에서 모델이 고르는 도구 중 하나가 된다.
- **Claude Code의 파일 탐색 방식(공식 문서로 확인)**: Claude Code 도구 문서(https://code.claude.com/docs/en/tools-reference)는 이름 패턴으로 파일을 찾는 Glob과 ripgrep 기반으로 파일 내용을 정규식 검색하는 Grep을 내장 도구로 든다. 단 2026-10-23 열람 기준으로 Glob·Grep은 Windows에서만 기본 도구 세트에 들어가고, macOS·Linux·WSL에서는 Bash 도구 안의 find·grep(내장 bfs·ugrep)으로 검색한다고 적혀 있다. 어느 쪽이든 문자열·패턴 검색이며, 이 문서에서 벡터 인덱스나 임베딩 검색 도구는 찾지 못했다.
- **"벡터 인덱스 대신 agentic search"라는 설계 판단의 근거(부분 확인)**: Claude Code를 만든 Boris Cherny(Anthropic)가 초기에 RAG 방식을 시도했다가 agentic search로 정착했고, 성능이 훨씬 좋았지만 근거는 체계적 벤치마크가 아닌 내부 체감이었다고 말했다는 보도가 있다. 이는 2차 보도(OfficeChai, 2025-05-27, https://officechai.com/ai/claude-researcher-explains-how-agentic-search-performed-better-than-rag-for-code-generation/)로만 확인했다. 그 보도가 출처로 단 YouTube 영상(https://www.youtube.com/watch?v=zDmW5hJPsvQ&t=2083s)은 직접 보지 않았고, "로컬 벡터 DB"라는 구체적 표현도 1차 출처로 확인하지 못했다. 강연에서는 "Claude Code 개발자의 발언(2차 보도 기준)"으로 표기할 것.
- **대비 포인트(강연자 해석)**: Lewis et al.은 2,100만 개 문서를 미리 임베딩해 색인했고, Claude Code는 미리 만든 색인 없이 필요할 때 패턴 검색으로 찾고 파일을 열어 읽는다. 코드처럼 자주 바뀌는 대상에서는 미리 만든 색인이 금방 낡을 수 있는데, 이는 Lewis et al.이 내세운 "인덱스 교체로 지식 갱신"의 이면(색인을 늘 최신으로 유지해야 하는 부담)이다. 반대로 환경 분야의 대규모 보고서·논문 코퍼스처럼 표현이 제각각인 개념을 찾아야 하는 경우에는 벡터 검색이 여전히 유효할 수 있다.