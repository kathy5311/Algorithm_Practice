'''
[해설] 오픈채팅방
========================================
핵심 아이디어:
  1회 순회로는 최종 닉네임을 알 수 없음 → 2회 순회 필요
  1회차: uid→nickname 딕셔너리 구축 + (uid, 액션) 이벤트 저장
  2회차: 이벤트를 순회하며 최종 닉네임으로 메시지 생성
'''

def solution(record):
    uid_nick = {}
    events = []

    for r in record:
        parts = r.split()
        action, uid = parts[0], parts[1]

        if action == 'Enter':
            uid_nick[uid] = parts[2]
            events.append((uid, '님이 들어왔습니다.'))
        elif action == 'Leave':
            events.append((uid, '님이 나갔습니다.'))
        else:                           # Change
            uid_nick[uid] = parts[2]   # 메시지 없음, 닉네임만 업데이트

    return [uid_nick[uid] + msg for uid, msg in events]

'''
========================================
포인트 정리
========================================
1. 2회 순회 패턴: "나중에 바뀌는 정보를 먼저 확정해야 할 때" 사용
   1회차에서 정보 수집 → 2회차에서 최종값으로 출력

2. Change는 events에 추가하지 않음 (메시지 없음)

3. list comprehension으로 최종 메시지 생성:
   uid_nick[uid] + msg → "Prodo님이 들어왔습니다."

잘못된 접근:
  ❌ 1회 순회로 바로 메시지 생성 → 이후 Change 반영 불가
  ✓ 이벤트(uid, 액션)만 저장 → 끝에서 최종 닉네임으로 치환
'''

# 테스트
record = ["Enter uid1234 Muzi","Enter uid4567 Prodo",
          "Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
# ["Prodo님이 들어왔습니다.","Ryan님이 나갔습니다.",
#  "Prodo님이 들어왔습니다.","Prodo님이 나갔습니다.","Prodo님이 들어왔습니다."]
