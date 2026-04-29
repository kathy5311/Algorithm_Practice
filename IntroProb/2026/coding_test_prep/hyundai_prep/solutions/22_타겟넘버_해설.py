'''
[해설] 타겟 넘버
========================================
핵심 아이디어:
  각 숫자마다 +/-를 붙이는 두 갈래 선택 → 이진 트리
  DFS로 모든 경우 탐색, 마지막 인덱스에서 합 == target이면 count++

  재귀 구조:
    dfs(idx, 현재 합)
    종료 조건: idx == len(numbers)
    두 갈래: dfs(idx+1, s+numbers[idx])  / dfs(idx+1, s-numbers[idx])
'''

def solution(numbers, target):
    count = 0

    def dfs(idx, s):
        nonlocal count
        if idx == len(numbers):
            if s == target:
                count += 1
            return
        dfs(idx + 1, s + numbers[idx])   # + 붙이기
        dfs(idx + 1, s - numbers[idx])   # - 붙이기

    dfs(0, 0)
    return count

'''
========================================
포인트 정리
========================================
1. nonlocal count: 중첩 함수에서 외부 변수 수정 시 필수
   ❌ count += 1 만 쓰면 UnboundLocalError

2. 대안: 리스트로 우회 (nonlocal 없이)
   count = [0]
   count[0] += 1
   → 리스트는 참조라서 nonlocal 없이 수정 가능

3. 스택 방식 (재귀 없이):
   stack = [(0, 0)]  # (인덱스, 현재 합)
   while stack:
       idx, s = stack.pop()
       if idx == len(numbers):
           if s == target: count += 1
           continue
       stack.append((idx+1, s+numbers[idx]))
       stack.append((idx+1, s-numbers[idx]))

4. 시간복잡도: O(2^N) → numbers 최대 20개 → 2^20 = 약 100만 → 충분

DFS vs BFS:
  이 문제는 최단 거리가 아닌 모든 경우의 수 → DFS가 더 자연스러움
  BFS도 가능하지만 메모리 더 사용
'''

# 테스트
print(solution([1,1,1,1,1], 3))  # 5
print(solution([4,1,2,1], 4))    # 2
