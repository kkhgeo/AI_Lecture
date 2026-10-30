# Ironies of Automation과 생성형 AI (자동화의 아이러니)
- **저자/기관**: Lisanne Bainbridge (University College London); Norman H. Mackworth (UK Medical Research Council); Raja Parasuraman & Dietrich H. Manzey (George Mason Univ. / TU Berlin); Auste Simkute, Lev Tankelevitch, Viktor Kewenig, Ava Elizabeth Scott, Abigail Sellen, Sean Rintel (Microsoft Research Cambridge 등)
- **발행일**: Bainbridge 1983; Mackworth 1948; Parasuraman & Manzey 2010; Simkute et al. arXiv 2024-02, *International Journal of Human–Computer Interaction* 2024-10 게재 (2026-10-01 열람)
- **URL**:
  - Bainbridge (1983) *Automatica* 19(6):775–779 — https://gwern.net/doc/sociology/technology/1983-bainbridge.pdf ; 해설 https://blog.acolyer.org/2020/01/08/ironies-of-automation/
  - Mackworth (1948) The breakdown of vigilance during prolonged visual search, *QJEP* 1:6–21 — https://en.wikipedia.org/wiki/Mackworth_Clock
  - Parasuraman & Manzey (2010) Complacency and bias in human use of automation, *Human Factors* 52(3):381–410 — https://depositonce.tu-berlin.de/handle/11303/8923
  - Simkute et al. (2024) Ironies of Generative AI — https://arxiv.org/abs/2402.11364 ; https://www.microsoft.com/en-us/research/?p=1095732
- **자료 유형**: 논문 (고전 + 리뷰)

## 핵심 요약
- **Bainbridge의 핵심 역설 (1983)**: 설계자는 사람을 오류의 원천으로 보고 없애려 하지만, 결국 자동화하지 못한 일, 즉 *가장 어렵고 드문 일*과 *자동화를 지켜보는 일*을 사람에게 남긴다.
- **기술 퇴화 + 최악의 인수 시점**: 평소 손으로 하지 않으니 기술이 녹슬고, 그런데도 사람은 자동화가 실패하는 가장 까다로운 순간에 개입해야 한다.
- **마지막 아이러니**: 거의 개입이 필요 없는 성공적 자동화일수록 사람 운전자 훈련에 가장 많이 투자해야 한다. 자동 제어는 변동을 상쇄하면서 고장을 "가려" 버릴 수도 있다.
- **Vigilance decrement (Mackworth 1948)**: 시계 바늘의 드문 '두 칸 점프'를 2시간 동안 찾는 과제에서 탐지율이 **처음 30분 동안 약 10–15% 떨어지고** 이후 완만히 계속 하락. 2차대전 레이더 병사가 30분쯤 지나면 잠수함 신호를 놓치던 관찰에서 출발. Bainbridge는 이를 근거로 "드물게 이상이 생기는 안정된 화면을 사람이 오래 감시할 수는 없다"고 했다.
- **Complacency와 automation bias (Parasuraman & Manzey 2010)**: 두 현상 모두 주의(attention) 배분 문제로 통합 설명. 다른 수동 과제와 주의를 다투는 *multi-task* 상황에서 자동화 감시가 소홀해진다. 초보자와 전문가 모두에게 나타나고, 단순 연습이나 지시만으로는 막기 어렵다.
- **Out-of-the-loop 문제**: 운영자가 직접 조작하지 않으면 상황 인식(situation awareness)이 떨어져 인수 시 무슨 일이 일어나는지 파악하는 데 시간이 걸린다 (Endsley & Kiris 1995, *Human Factors* 37(2) — 원문 미열람, 서지 정보만 확인 필요).
- **Ironies of Generative AI (Simkute et al. 2024)**: 항공·자율주행 연구의 교훈이 GenAI에도 그대로 재현된다며 네 가지 문제를 정리했다. ① production→evaluation 이동, ② 도움이 안 되는 workflow 재구성(프롬프트 작성이라는 새 과제, 출력 수정·조합), ③ 흐름을 끊는 interruption(Copilot 제안이 생각을 끊는다는 개발자 보고), ④ task-complexity polarization(쉬운 일은 더 쉬워지고 어려운 일은 더 어려워짐). 결과적으로 사용자가 cognitive load 증가와 과도한 검증 시간을 겪는다.
- **Simkute가 인용한 사례**: Copilot 사용자가 기존 autocomplete 사용자보다 과제 완수에 더 자주 실패한 연구가 있다는 정리 (원 연구의 수치는 이 리뷰에서 직접 확인하지 못함).
- **에이전트 시대로의 확장**: 2025년 Hugging Face 연구진(Mitchell 등)이 자율성 수준이 높아질수록 사람 감독이 형식화된다고 주장하며 Bainbridge를 인용했다는 보도가 있음 — approval fatigue, overreliance, 상황 인식 상실, 기술 퇴화를 언급. **원문 미확인, 강연 사용 전 확인 필요.**

## 핵심 개념·용어 정의
- **Ironies of automation**: 자동화가 사람의 일을 줄이려다 오히려 더 어려운 감독·개입 역할을 남기는 역설.
- **Vigilance decrement**: 드문 신호를 장시간 감시할 때 시간이 갈수록 탐지 성능이 떨어지는 현상.
- **Automation complacency**: 자동화가 잘 돌아간다고 믿어 감시·교차확인을 덜 하는 상태. 특히 다른 일을 같이 할 때 생김.
- **Automation bias**: 자동화의 제안을 경험적 지름길로 받아들여, 틀린 제안을 따르거나(commission error) 자동화가 놓친 문제를 못 보는(omission error) 판단 편향.
- **Out-of-the-loop performance problem**: 수동 조작에서 멀어져 상황 인식과 기술이 떨어지고, 인수 시 성능이 저하되는 문제.
- **Production-to-evaluation shift (Simkute 2024)**: 사용자의 역할이 만들어 내는 사람에서 판정하는 사람으로 바뀌는 것.
- **Task-complexity polarization**: GenAI가 쉬운 과제는 더 쉽게, 어려운 과제(분해·디버깅 필요)는 더 어렵게 만드는 현상.

## 코딩 에이전트 사용과의 연결점
- **줄어드는 곳**: 타이핑, 보일러플레이트, 반복 리팩터링 — Bainbridge의 "쉬운 부분"이 자동화된다.
- **옮겨 가는 곳**: 직접 짜기 → 에이전트 diff·로그·계획 감시. Claude Code/Codex가 20분간 수십 개 파일을 고치는 동안 사람은 "안정된 화면을 보며 드문 이상을 찾는" Mackworth 시계 과제와 비슷한 상황에 놓인다.
- **늘어나는 곳**:
  - *해석 부하*: 내가 쓰지 않은 코드를 읽고 의도를 재구성해야 함 (out-of-the-loop).
  - *승인 피로*: 권한 요청을 계속 "Yes"로 넘기다 보면 complacency/automation bias가 생긴다. 여러 에이전트를 병렬로 돌리면 Parasuraman & Manzey가 말한 multi-task 조건이 그대로 성립.
  - *어려운 일만 남음*: 에이전트가 풀지 못한 버그는 대개 가장 까다로운 것이고, 사람은 그 코드베이스를 직접 만지지 않아 맥락이 없다 (task-complexity polarization).
- **관리 전략 (Bainbridge·Simkute 처방을 에이전트에 번역)**:
  - 감시 대신 *검증 자동화*: 테스트·린터·타입체크를 "알람"으로 두어 사람의 vigilance 의존을 줄인다 (단, Bainbridge가 경고한 '알람의 알람' 문제 — 테스트 자체를 검토해야 함).
  - 작업 단위를 잘게(Simkute: 긴 제안을 논리적 chunk로 분할) — 30분 이상 무감독 장시간 실행 후 한 번에 큰 diff 검토는 피한다.
  - 명확한 task allocation: 에이전트에 맡길 일과 내가 할 일을 미리 정한다.
  - 정기적인 "수동 비행": 핵심 로직은 가끔 직접 짜서 기술 퇴화를 막는다(Bainbridge의 hands-on practice 처방).

## 강연에 쓸 만한 포인트
- **비유**: 자동조종 비행기의 조종사. 순항은 자동조종이 하고, 조종사는 지루한 감시 끝에 가장 위험한 순간에만 조종간을 넘겨받는다. 코딩 에이전트 사용자도 같은 자리에 앉게 된다.
- **그림 아이디어**: 왼쪽 1983년 공장 제어실 / 오른쪽 2026년 터미널 속 Claude Code — 같은 구도의 "감시하는 사람". 가운데 Mackworth 시계 곡선(30분 내 탐지율 하락).
- **그림 아이디어 2**: Simkute의 4가지 아이러니를 2×2 아이콘으로.
- **인용 후보(1개)**: Bainbridge — "the most successful automated systems ... may need the greatest investment in human operator training" (Bainbridge, 1983, Automatica; 생략 포함 15단어 미만으로 줄여 사용)

## 원본 그림
- Simkute et al. Figure 1: GenAI의 네 가지 생산성 문제 도식 — https://arxiv.org/html/2402.11364v1/figure_challenges.png
- Mackworth Clock 실험 화면(PsychToolkit/PEBL 재현) — https://upload.wikimedia.org/wikipedia/commons/4/4b/Clocktest.pbl.png
- Bainbridge 1983 원문 — 그림 없음 (텍스트 논문)
