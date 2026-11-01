# 프로젝트 진행 지침

이 문서는 `yunkio/project-orchestrator`의 시작점이다. 사용자가 이 문서를 작업 지침으로 지정하면, 메인 에이전트가 **orchestrator**가 되어 아래 순서로 실제 작업을 시작한다. 스킬을 읽거나 내려받았다는 안내만 하고 끝내지 않는다. 사용자가 설명·검토만 요청했거나 수행 범위를 한정했다면 그 범위를 지킨다.

## 1. 스킬 전체를 확보하고 읽는다

저장소: **https://github.com/yunkio/project-orchestrator**. 공개 HTTPS 주소로 가져오며 GitHub 로그인·토큰·SSH 키는 필요하지 않다.

1. 아직 로컬에 없으면, 쓰기 가능한 도구용 새 폴더에 저장소를 `git clone --depth 1`로 가져온다. 기존 폴더를 덮어쓰지 않는다. 이 위치는 스킬 보관 위치이며 사용자의 프로젝트 작업·기록 경로를 확정한 것이 아니다.
2. 이미 있다면 저장소 주소와 파일을 확인해 재사용한다. 사용자의 변경을 강제로 초기화하거나 덮어쓰지 않는다. `inst.md`, `SKILL.md`, 참조·양식은 같은 체크아웃에서 읽고, 실제 사용한 경로와 커밋을 이후 WORKLOG에 기록한다.
3. 아래 문서를 실제로 읽는다. 이 문서의 요약만으로 절차를 대신하지 않는다.
   - [전체 운영 절차 — SKILL.md](skills/project-orchestrator/SKILL.md)
   - [질문과 의도 보존](skills/project-orchestrator/references/qna-and-intent.md)
   - [소통·명세·계획](skills/project-orchestrator/references/spec-and-plan.md)
   - [지속 체크리스트 운영](skills/project-orchestrator/references/checklist-and-gates.md)
4. 별도 스킬 설치나 도구 버전 변경은 시작 조건이 아니다. 내려받은 `SKILL.md`를 직접 적용하고, 그 문서가 연결하는 참조와 양식을 단계에 맞춰 읽는다. 스킬 저장소의 README·테스트는 사용자가 해결할 프로젝트의 요구사항이 아니다.

이 문서의 링크는 저장소 최상위를 기준으로 한다. 스킬 안의 상대 경로는 그 문서가 있는 폴더를 기준으로 해석한다. 파일을 가져오거나 읽을 수 없으면 그 한계를 알리고, 읽지 않은 절차를 수행했다고 기록하지 않는다.

## 2. 시작에 필요한 값만 확인한다

현재 대화에서 이미 제공한 **작업 경로, 요구사항 자료, 현업 자료 또는 질의 채널, 기록 경로, 시간·산출물·도구 제약**을 확인한다. 과거 프로젝트의 경로나 요구를 자동으로 가져오지 않는다.

- 기록 경로가 없으면, 이미 알려진 쓰기 가능한 현재 작업 폴더 아래 고유한 임시 폴더에 `QNA.md`만 만들고 빠진 경로를 묻는다. 이 임시 위치를 최종 경로로 간주하지 않는다. 쓸 수 있는 위치조차 없으면 그 사실과 필요한 경로를 알린다.
- 경로가 정해지면 실제 원자료와 기존 기록부터 읽는다. 기존 작업이면 QNA 답변·의도·명세·진행 상태를 읽어 이어가며, 초기화로 덮어쓰지 않는다.
- 기록 경로에 별도 [CHECKLIST.md](skills/project-orchestrator/assets/CHECKLIST.md)를 만들거나 기존 파일을 읽는다. 기존 작업에 이 파일만 없으면 기존 근거를 확인해 보완하며, 다른 기록을 재초기화하지 않는다.
- 사용자에게 QNA의 **실제 파일 링크와 질문 ID**, 이미 확인한 내용, 답을 기다리는 작업과 진행 가능한 일을 알려준다. 답변 칸은 비워 둔다. 파일 편집 뒤 “QNA 수정했어”라고 알려주면 실제 내용을 다시 읽고 이어간다고 안내한다.
- 사용자가 목표를 따로 정리하지 않았어도 원자료를 읽은 뒤 좋은 결과의 기준·우선순위·중요한 절충을 스스로 질문으로 도출한다. 원문이나 사용자가 이미 확정한 값은 다시 선택시키지 않는다.

경로가 빠졌다고 설치 방법만 설명하고 끝내거나, 불확실한 목적을 임의로 정해 제품 구현부터 시작하지 않는다. 답을 기다리는 동안 독립적인 자료 확인·검토는 진행한다.

## 3. 네 단계를 계속 조율한다

세부 행동과 통과 기준은 `SKILL.md`를 따른다. 다음 표는 필요한 문서를 제때 읽기 위한 연결표다. 사용자에게 다음 단계를 별도로 호출하게 하지 않는다.

| 흐름 | 적용할 자료 | 이어가기 위한 결과 |
|---|---|---|
| **① 파악** — G0·G1 원문 분석 | [요구사항·독립 감사](skills/project-orchestrator/references/requirements-and-audit.md) | 원자료·현업 요구를 출처별로 파악하고 필수 조건·모르는 점을 설명 |
| **② 확인** — G1 QnA | [질문과 의도 보존](skills/project-orchestrator/references/qna-and-intent.md) | 사용자·현업 질문, 선택지·절충, 답변 재독, 의도 보존. 중요한 모호함은 의존 작업 전에 해결 |
| **③ 명세·계획** — G2 | [명세·계획](skills/project-orchestrator/references/spec-and-plan.md), [실행·검증](skills/project-orchestrator/references/execution-and-evidence.md), [에이전트 운영](skills/project-orchestrator/references/agents-and-resume.md), [SPEC 양식](skills/project-orchestrator/assets/SPEC.md) | 명세·통과 조건·작업 의존성과 역할을 작성하고 독립 요구 대조의 중요한 차이를 해결 |
| **④ 구현·테스트** — G3·G4 | [실행·검증](skills/project-orchestrator/references/execution-and-evidence.md), [에이전트 운영](skills/project-orchestrator/references/agents-and-resume.md) | 명세 기반 병렬 구현·통합, 독립 검사, 실제 실패 재현·수정·재검사 |
| **최종 대조** — G5 | [요구사항·독립 감사](skills/project-orchestrator/references/requirements-and-audit.md) | 원자료부터 시작한 새 맥락 검토로 누락·불일치와 최신 실행 근거 확인 |
| **설명·인계** — G6 | [인수인계](skills/project-orchestrator/references/review-and-handoff.md), [그래프 설명·검증](skills/project-orchestrator/references/graph-handoff.md), [HANDOFF 양식](skills/project-orchestrator/assets/HANDOFF.md) | 실제 코드·근거와 연결된 그래프, 독립 읽기·사실 대조, 사용자 설명·이해 QnA·재현 안내 |

메인은 모든 단계에서 진행 상황과 판단 이유를 설명한다. 결정이 필요한 질문은 `QNA.md`, 답변의 목적과 이유는 별도 `USER_INTENT.md`에 유지한다. 명확한 답은 반영해 진행하며 형식적인 재승인을 반복하지 않는다. 답변이 바뀌면 관련 명세·계획·구현·검사·설명을 함께 갱신한다.

독립 작업은 실제 가용 도구와 자원 범위에서 하위 에이전트에 병렬 배정한다. 배정 전에 [단계별 역할과 독립성 기준](skills/project-orchestrator/references/agents-and-resume.md)을 읽고 파일 소유권·입출력·관련 체크 ID·완료 검사를 정한다. 독립 감사자는 부모의 결론이나 채운 체크리스트를 받기 전에 원자료와 답변 당시 질문·선택지 문맥에서 요구를 도출한다. 메인은 보고를 확인해 통합·판정하며, 가용하지 않은 독립 검토를 수행했다고 표시하지 않는다.

## 4. 단계가 빠진 채 끝내지 않는다

WORKLOG의 G0~G6 상태와 실제 근거를 유지한다. **시작·재개, 각 단계 진입·종료, 위임, 주요 쓰기·반환·통합, 답변/자료/명세 변경, 결함 수정, 최종 전달 전마다 CHECKLIST의 관련 항목을 확인**하고 최근 확인 이력을 남긴다. 단계별 절차뿐 아니라 모든 필수 요구·프로젝트 지시가 연결됐는지 확인한다. 오래된 근거는 재검토로 바꾸고 중요한 미해결 항목에 의존하는 작업은 보류한다. 시간이 부족해도 단계를 조용히 지우거나 미실행을 완료로 바꾸지 않는다. 다 끝낼 수 없다면 수행한 범위·남은 영향·재개 지점을 남긴다.

마지막 HANDOFF는 **선택과 절충 / 요청의 데이터·상태 흐름 / 검증의 신뢰 경계 / 실패·데이터 변경 / 품질 근거와 한계 / 실제 AI 협업 판단**을 설명한다. 단순한 작업 순서 그림으로 대신하지 않는다. 그래프의 노드와 코드·실행 근거를 연결하고, 독립 검토자가 먼저 그림을 읽고 설명한 뒤 실제 자료와 대조하게 한다.

완성한 자료는 사용자에게 전달하고 핵심 그래프를 설명한다. 실제 이해 답변이 없으면 **산출물 준비 상태와 이해 확인 답변 대기**를 구분한다. 프로젝트 자료나 기록을 이 공개 스킬 저장소로 업로드하지 않는다. 공개·배포·외부 연락은 해당 작업에서 허용된 범위만 따른다.
