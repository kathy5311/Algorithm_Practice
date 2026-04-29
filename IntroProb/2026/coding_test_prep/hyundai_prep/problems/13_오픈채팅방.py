'''
[유형] 해시
[난이도] 프로그래머스 Lv.2
[문제] 오픈채팅방
========================================

오픈채팅방에서 입장/퇴장/닉네임 변경 기록이 주어질 때
모든 기록이 처리된 후 최종 닉네임 기준으로 메시지를 반환하세요.

[기록 형식]
  Enter uid nickname  → 입장 (닉네임 설정)
  Leave uid           → 퇴장
  Change uid nickname → 닉네임 변경 (메시지 없음)

[반환 형식]
  "{최종 닉네임}님이 들어왔습니다."
  "{최종 닉네임}님이 나갔습니다."

[조건]
  - 닉네임은 Change 또는 재입장 시 바뀔 수 있음
  - 채팅방에 없는 사람이 나가거나 닉네임 변경 없음

[입출력 예]
record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]
→ ["Prodo님이 들어왔습니다.", "Ryan님이 나갔습니다.",
    "Prodo님이 들어왔습니다.", "Prodo님이 나갔습니다.",
    "Prodo님이 들어왔습니다."]
'''

def solution(record):
    pass


# 테스트
record = ["Enter uid1234 Muzi","Enter uid4567 Prodo",
          "Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
# ["Prodo님이 들어왔습니다.","Ryan님이 나갔습니다.",
#  "Prodo님이 들어왔습니다.","Prodo님이 나갔습니다.","Prodo님이 들어왔습니다."]
