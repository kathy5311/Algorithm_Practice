'''
[유형] 스택/큐
[난이도] 프로그래머스 Lv.2
[문제] 다리를 지나는 트럭
========================================

트럭 여러 대가 일방통행 다리를 건너려 합니다.
모든 트럭이 다리를 건너는 데 걸리는 최소 시간을 반환하세요.

[조건]
  - 매 초마다 다리 위 모든 트럭은 1칸 전진
  - 다리에는 최대 bridge_length대 올라갈 수 있음
  - 다리 위 트럭 무게 합이 weight 초과 불가
  - 트럭은 순서대로 건너야 함
  - 대기 중인 트럭은 올라올 수 있으면 즉시 진입

[입출력 예]
bridge_length=2, weight=10, truck_weights=[7,4,5,6]  → 8
bridge_length=100, weight=100, truck_weights=[10]*10  → 110
bridge_length=2, weight=10, truck_weights=[10,10,10,10] → 8

설명 (bridge_length=2, weight=10, [7,4,5,6]):
  시간  다리         대기
  0초   [0,0]       [7,4,5,6]
  1초   [0,7]       [4,5,6]
  2초   [7,4]       [5,6]
  3초   [4,0]       [5,6]   ← 7이 나감, 5는 4+5=9≤10 이지만 4 아직 있음
  4초   [0,5]       [6]
  5초   [5,6]       []
  6초   [6,0]       []
  7초   [0,0]       []
  → 8초
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    pass


# 테스트
print(solution(2, 10, [7,4,5,6]))           # 8
print(solution(100, 100, [10]*10))          # 110
print(solution(2, 10, [10,10,10,10]))       # 8
