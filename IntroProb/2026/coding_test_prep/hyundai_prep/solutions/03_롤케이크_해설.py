'''
[해설] 롤케이크 자르기
========================================
핵심 아이디어:
  왼쪽에서 오른쪽으로 토핑을 하나씩 "왼쪽 조각"으로 이동시키며
  왼쪽/오른쪽의 토핑 종류 수가 같은 순간을 카운트

  left  = set()         ← 왼쪽 조각의 토핑 종류 (중복 무시)
  right = Counter()     ← 오른쪽 조각의 토핑 개수 추적

  매 단계:
    - left.add(t)
    - right[t] -= 1, 0이 되면 삭제 (종류 수 감소)
    - len(left) == len(right) → 공평한 분배 → count++
'''

from collections import Counter

def solution(topping):
    right = Counter(topping)
    left = set()
    answer = 0

    for t in topping:
        left.add(t)
        right[t] -= 1
        if right[t] == 0:
            del right[t]
        if len(left) == len(right):
            answer += 1

    return answer

'''
========================================
포인트 정리
========================================
1. left는 set: 종류만 셈 (중복 자동 제거)
2. right는 Counter: 개수가 0이 되면 del → 종류 수 감소 반영
3. O(N): 각 토핑을 정확히 한 번씩 처리

잘못된 접근:
  ❌ 매 자르는 위치마다 set(left), set(right) 새로 만들기 → O(N²) TLE
  ✓ Counter를 이동시키며 O(1)로 업데이트

del right[t] vs right[t] = 0:
  del right[t]: 키 완전 제거 → len(right)가 줄어듦 (정확)
  right[t] = 0: 키 남아있음 → len(right) 안 줄어 오답
'''

# 테스트
print(solution([1, 2, 1, 3, 1, 4, 1, 2]))  # 2
print(solution([1, 2, 3, 1, 4]))            # 0
