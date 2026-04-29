'''
[해설] 주식가격
========================================
핵심 아이디어: 단조 스택 (Monotonic Stack)
  스택에 인덱스를 저장
  현재 가격 < 스택 top의 가격 → 가격 하락 발견
    → 스택에서 꺼내 answer[j] = 현재 인덱스 - j
  스택에 남은 인덱스 → 끝까지 가격 안 떨어짐
    → answer[j] = (마지막 인덱스) - j
'''

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []   # 인덱스 저장

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:   # 하락 발생
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:                                     # 끝까지 하락 없음
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer

'''
========================================
포인트 정리
========================================
1. 스택에 값이 아닌 인덱스를 저장: 거리 계산을 위해
2. 하락 조건: prices[stack[-1]] > price (같은 건 하락 아님)
3. 남은 인덱스 처리 잊지 않기: while stack 후처리 필수

단조 스택 패턴:
  "오른쪽에서 나보다 작은 첫 번째 원소까지 거리" 문제에 적용
  → O(N): 각 원소가 push/pop 각각 한 번씩만

순진한 풀이 O(N²) vs 단조 스택 O(N):
  이중 for문: prices가 100,000개 → 10^10 연산 TLE
  단조 스택: 10^5 연산 → 통과
'''

# 테스트
print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]
