'''
[해설] 다리를 지나는 트럭
========================================
핵심 아이디어:
  다리를 길이만큼의 deque로 표현 (초기값 0으로 채움)
  0 = 빈 칸, 양수 = 트럭 무게

  매 초마다:
    1. popleft() → 맨 앞 칸 나감 → current_weight 감소
    2. 다음 트럭이 올라올 수 있으면 append(무게), truck_idx++
       올라올 수 없으면 append(0)  ← 빈 칸으로 채워 시간 진행
  마지막 트럭 진입 후 bridge_length초 추가 (다리 끝까지 이동)
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    time = 0
    current_weight = 0
    truck_idx = 0

    while truck_idx < len(truck_weights):
        time += 1
        current_weight -= bridge.popleft()

        next_truck = truck_weights[truck_idx]
        if current_weight + next_truck <= weight:
            bridge.append(next_truck)
            current_weight += next_truck
            truck_idx += 1
        else:
            bridge.append(0)

    return time + bridge_length

'''
========================================
포인트 정리
========================================
1. deque([0]*bridge_length): 다리 위 상태를 큐로 표현
   - popleft(): 앞 칸 나감 O(1)
   - append(): 뒤 칸 추가 O(1)
   - list 쓰면 pop(0)이 O(N) → TLE 가능성

2. current_weight 변수: 다리 위 총 무게를 O(1)로 추적
   (매번 sum(bridge) 하면 O(bridge_length) → 느림)

3. return time + bridge_length:
   while문은 마지막 트럭이 "올라탄" 시점에 종료
   그 트럭이 반대편에 도달하려면 bridge_length초 더 필요

잘못된 접근:
  ❌ sum(bridge) > weight 체크 → O(N) 반복, 느림
  ❌ return time 만 하면 마지막 트럭 통과 시간 누락
'''

# 테스트
print(solution(2, 10, [7,4,5,6]))           # 8
print(solution(100, 100, [10]*10))          # 110
print(solution(2, 10, [10,10,10,10]))       # 8
