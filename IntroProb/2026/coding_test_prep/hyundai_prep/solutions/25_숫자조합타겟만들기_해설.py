'''
[해설] 숫자 조합 타겟 만들기
========================================
핵심 아이디어:
  각 숫자마다 + 또는 - 를 붙이는 두 갈래 선택 → 이진 트리 구조
  재귀로 모든 경우를 탐색하고, 마지막 인덱스에서 합 == target이면 count++

  재귀 구조:
    dfs(idx, 현재 합)
    종료 조건: idx == len(numbers)
    두 갈래:
      dfs(idx+1, s + numbers[idx])   # + 붙이기
      dfs(idx+1, s - numbers[idx])   # - 붙이기
'''

def solution(numbers, target):
    count = 0

    def dfs(idx, s):
        nonlocal count
        if idx == len(numbers):
            if s == target:
                count += 1
            return
        dfs(idx + 1, s + numbers[idx])
        dfs(idx + 1, s - numbers[idx])

    dfs(0, 0)
    return count

'''
========================================
포인트 정리
========================================
1. nonlocal count: 중첩 함수에서 외부 변수 수정 시 필수
   ❌ count += 1 만 쓰면 UnboundLocalError 발생

2. 대안: 리스트로 우회 (nonlocal 없이)
   count = [0]
   count[0] += 1
   → 리스트는 참조라서 nonlocal 없이 수정 가능

3. 반환값으로 누적하는 방식 (nonlocal 없이):
   def dfs(idx, s):
       if idx == len(numbers):
           return 1 if s == target else 0
       return dfs(idx+1, s+numbers[idx]) + dfs(idx+1, s-numbers[idx])
   return dfs(0, 0)

4. 시간복잡도: O(2^N) → numbers 최대 20개 → 2^20 ≈ 100만 → 충분

※ 22번 타겟넘버와 동일한 구조 — 재귀 DFS 백트래킹의 가장 기본형
'''

# 테스트
print(solution([1,1,1,1,1], 3))  # 5
print(solution([4,1,2,1], 4))    # 2
