# The Metacognitive Demands of GenAI · The Gulf of Envisioning · Why Johnny Can't Prompt (상호작용 자체가 왜 생각을 요구하는가)
- **저자/기관**:
  - Lev Tankelevitch, Viktor Kewenig, Auste Simkute, Ava Elizabeth Scott, Advait Sarkar, Abigail Sellen, Sean Rintel (Microsoft Research 외) — CHI 2024 (Best Paper)
  - Hariharan Subramonyam, Roy Pea, Christopher Lawrence Pondoc, Maneesh Agrawala (Stanford), Colleen Seifert (Univ. of Michigan) — CHI 2024
  - J.D. Zamfirescu-Pereira, Richmond Y. Wong, Bjoern Hartmann, Qian Yang (UC Berkeley, Georgia Tech, Cornell) — CHI 2023
  - 보조: James Prather 외 (Abilene Christian Univ., Univ. of Auckland 등), ACM TOCHI (arXiv 2023-04)
- **발행일**: Tankelevitch arXiv 2023-12 / CHI 2024-05; Subramonyam arXiv 2023-09(개정 2024-03) / CHI 2024-05; Zamfirescu-Pereira CHI 2023-04; Prather arXiv 2023-04 (2026-10-01 열람)
- **URL**:
  - Tankelevitch et al. — https://arxiv.org/abs/2312.10893 (HTML: https://arxiv.org/html/2312.10893)
  - Subramonyam et al. — https://arxiv.org/abs/2309.14459 (HTML: https://arxiv.org/html/2309.14459v2)
  - Zamfirescu-Pereira et al. — https://doi.org/10.1145/3544548.3581388 (저자 PDF: https://people.eecs.berkeley.edu/~bjoern/papers/zamfirescu-johnny-chi2023.pdf)
  - Prather et al. — https://arxiv.org/abs/2304.02491
- **자료 유형**: 논문 (Tankelevitch·Subramonyam: 이론/개념 틀 + 문헌 종합, Zamfirescu-Pereira·Prather: 관찰·인터뷰 연구)

## 핵심 요약
- **메타인지가 계속 켜져 있어야 한다 (Tankelevitch 2024)**: 메타인지는 자기 생각과 행동을 감시(monitoring)하고 조절(control)하는 능력이다. 저자들은 생성형 AI의 사용성 문제 상당수가 이 메타인지 요구에서 나온다고 본다. 원래 일을 하면 암묵적으로 처리되던 의도가, AI에게 맡기려면 명시적으로 드러나야 하기 때문이다. (원문 확인)
- **프롬프트 단계의 요구**: ① 내 목표를 스스로 알아차리기(self-awareness of goals), ② 과제를 전달 가능한 하위 과제로 쪼개기(task decomposition), ③ 그것을 말로 표현하기. 한 인용 연구의 참가자는 작업이 "서사를 생각하는 것"에서 "지시를 생각하는 것"으로 바뀌었다고 표현했다 — 즉 **일 자체를 생각하는 대신 일을 설명하는 방법을 생각**하게 된다. (원문 확인)
- **출력 평가 단계의 요구**: 내 확신이 실제 정확도와 맞아야 하고(calibration), 맞는 출력과 틀린 출력을 구별할 수 있어야 한다(resolution). 출력이 길고 새로울수록 평가 노력이 커진다. 비결정적이라 실패가 내 프롬프트 탓인지, 모델 한계인지, 우연인지 가리기 어렵다. AI는 사람이 안 하는 종류의 미묘한 오류를 낸다. (원문 확인)
- **작업 흐름 단계의 요구**: 이 일에 AI를 쓸지, 언제, 어떻게 쓸지를 계속 판단해야 한다. 직접 하는 것과 AI에 맡기는 것 사이의 확신 비교가 필요하다. 일부 사용자는 흐름을 깨뜨린다는 이유로 Copilot을 꺼버렸다. (원문 확인)
- **유창성 착각**: 결과가 빨리, 매끄럽게 나오면(processing fluency) 그 품질에 대한 확신이 근거 없이 올라갈 수 있다. (원문 확인)
- **구상의 간극 (Subramonyam 2024)**: Norman의 실행 간극·평가 간극에 앞서, **목표를 프롬프트로 바꾸기 전 단계**에 새 간극(gulf of envisioning)이 있다. 세 가지 정렬 실패로 구성된다 — 능력 간극(이 과제를 어떻게 풀지 내가 절차를 그릴 수 있는가), 지시 간극(그걸 어떤 말로 지시할 것인가; 표현을 조금 바꿔도 출력이 크게 달라짐), 의도 간극(직접 계획·실행하는 단계를 건너뛰고 바로 출력을 평가하니, 내가 원하는 게 무엇이었는지 충분히 발달하지 않아 평가 기준이 없음). 이 논문은 새 사용자 실험이 아니라 인지과학 문헌과 12개 LLM 도구 분석에 기반한 개념 틀이다. (원문 확인)
- **비전문가는 체계적이지 않게, 사람에게 말하듯 프롬프트한다 (Zamfirescu-Pereira 2023)**: AI 비전문가 10명이 챗봇 프롬프트를 고치는 과정을 관찰. 참가자들은 체계적으로 시험하지 않고 기회주의적으로(그때그때) 고쳤고, 한 번 성공하면 멈추고 한두 번 실패하면 "이건 못 하나 보다"라고 과잉 일반화했다. 사람에게 지시하던 습관(예시 대신 직접 지시, 공손한 말투, "~하지 마라" 형식)이 방해가 되었고, "ABC라고 말하지 마"라고 쓰면 챗봇이 ABC를 그대로 말하는 데 놀랐다. 모든 참가자가 한 번은 "왜 이렇게 했지?"라고 물었고, 연구자도 대부분 "모른다"고 답할 수밖에 없었다. (원문 확인)
- **제안이 생각을 끊는다 (Prather 외, CS1 학생 19명)**: Copilot의 계속되는 코드 제안이 학생들의 문제 해결을 방해했다. 대부분의 학생이 제안이 뜨면 일단 그것을 읽고 해독하려 했고, 큰 코드 블록은 해독에 상당한 시간과 노력을 썼다. 한 학생은 해법을 생각하려는데 화면이 제안으로 차서, 생각하는 대신 그것을 따라가고 싶어진다고 말했다. (원문 확인)

## 핵심 개념·용어 정의
- **메타인지(metacognition)**: 자기 인지를 감시하고 조절하는 능력. 감시 측면 = 자기 인식, 확신 조정 / 조절 측면 = 과제 분해, 메타인지 유연성(새 정보에 따라 전략을 바꾸는 능력).
- **확신 보정(confidence calibration)**: 내 확신 수준이 실제 정답률과 맞는 정도.
- **처리 유창성(processing fluency)**: 일이 쉽게 느껴지는 주관적 감각. AI의 빠른 생성은 이 감각을 높여 과신을 부를 수 있다.
- **구상의 간극(gulf of envisioning)**: 막연한 목표와 "좋은 출력을 끌어낼 프롬프트" 사이의 거리. 능력·지시·의도의 세 간극으로 구성.
- **Norman의 7단계 행동 모델**: 목표 → 의도 형성 → 행동 명세 → 실행 → 지각 → 해석 → 평가. Subramonyam은 LLM이 "실행 간극"은 줄였지만 그동안 덜 다뤄진 2단계 "의도 형성"을 새 병목으로 만들었다고 본다.
- **기회주의적 프롬프팅**: 계획·테스트 없이, 지금 보이는 문제 하나를 재시도 버튼으로 고치는 방식. 앞서 고친 오류가 다시 생겨도 알아채지 못한다.

## 강연자의 경험("AI와 상호작용할 때 생각하기 어렵다")과의 연결
- 강연자가 겪는 "주고받는 도중에 생각이 안 된다"는 느낌은 이 세 논문이 말하는 **이중 작업** 상태로 설명된다. 머리는 (a) 원래 문제를 생각하면서 동시에 (b) 그 생각을 AI가 알아들을 말로 바꾸고, (c) 나온 결과를 믿어도 되는지 판단하고, (d) 다음 턴에 무엇을 시킬지 정해야 한다. (b)~(d)는 모두 메타인지 작업이며, 원래 문제에 쓸 작업기억을 나눠 쓴다(작업기억 한계는 01 파일 참고).
- **의도 간극**이 특히 잘 맞는다. 직접 했다면 쓰고 고치는 동안 서서히 "내가 원하는 것"이 분명해졌을 텐데, AI에 바로 맡기면 그 과정을 건너뛰어 출력을 봐도 좋은지 나쁜지 판단할 기준이 머릿속에 아직 없다. 그래서 출력을 읽을 때 생각이 멈춘 듯 느껴진다.
- 출력의 비결정성 때문에 "내 지시가 잘못됐나, 모델이 못하나, 운이 나빴나"를 매 턴 따져야 한다 — Zamfirescu-Pereira 연구의 "왜 이렇게 했지?"가 그 순간이다.
- 03 파일(Lee 외 CHI 2025)이 말한 "생산 → 검증으로의 노력 이동"이 결과 쪽이라면, 이 파일은 **상호작용 순간 자체의 부하**를 다룬다.

## 강연에 쓸 만한 포인트
- **인용(1개)**: 메타인지는 "the psychological ability to monitor and control one's thoughts and behavior" — Tankelevitch et al., CHI 2024.
- **비유**: "AI와 일하는 것은 일을 하면서 동시에 그 일을 남에게 설명하는 것이다." 운전하면서 옆 사람에게 길을 설명하는 상황 — 둘 다 하면 운전도 설명도 서툴러진다.
- **예시 (청중 참여용)**: Subramonyam 논문의 "땅콩버터 샌드위치 만들기 지시문" — 매일 하는 일도 정확한 지시문으로 쓰려면 막힌다. 은퇴 축사 예시: "Taylor를 위한 축사를 써줘"는 평범한 결과를 낳고, 따뜻한 톤·5분·골프 농담 등 의도를 먼저 구체화해야 좋은 결과가 나온다.
- **예시 ("하지 마라"의 함정)**: "~라고 말하지 마"를 추가했더니 효과가 없었고, "하지 마" 문장을 지우고 "~해라"로 바꾸자 해결됐다(Zamfirescu-Pereira 2023, 참가자 P4 사례).
- **그림 아이디어**: Norman의 7단계 원형 다이어그램에 "의도 형성" 칸을 빨갛게 강조하고, 그 앞에 "구상의 간극" 골짜기를 그린다. 각 단계 옆에 사람이 해야 하는 메타인지 작업(목표 자각·분해·보정·유연성)을 붙인다.

## 원본 그림
- Tankelevitch Figure 2 — 단순화된 작업 흐름의 각 지점(프롬프트 작성, 반복, 평가, 자동화 전략, 흐름 조정)에서 생기는 메타인지 요구 (a)~(e) — https://arxiv.org/html/2312.10893v3/MC_design_figure_2.png
- Tankelevitch Figure 1 — 메타인지 지식·경험 → 감시 → 조절 → 수행의 틀 — https://arxiv.org/html/2312.10893v3/MC_design_figure_1.png
- Subramonyam Figure 2 — Norman 7단계 모델 확장, "의도 형성" 단계 강조 — https://arxiv.org/html/2309.14459v2/normanmodel.png
- Subramonyam Figure 3 — 사람-LLM 상호작용에서 빠진 단계와 세 경로(바로 목표 말하기 / 의도를 다듬어 프롬프트 / 전용 도구로 넘어가기) — https://arxiv.org/html/2309.14459v2/llmModel.png
- Subramonyam Figure 1 — 의도 구체성·기능 유연성·출력 결정성 3축 개념도 — https://arxiv.org/html/2309.14459v2/figures/new_teaser.png
- (모두 HTTP 200 확인. 슬라이드 사용 시 arXiv 라이선스 확인 필요)
