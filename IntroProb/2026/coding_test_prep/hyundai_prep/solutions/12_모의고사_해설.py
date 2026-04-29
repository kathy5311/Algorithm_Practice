'''
[해설] 모의고사
========================================
핵심 아이디어:
  각 수포자의 패턴을 배열로 정의
  i % len(pattern)으로 패턴 순환
  answers를 순회하며 각 수포자 점수 집계
  max_score와 같은 점수의 수포자 번호 반환
'''

def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0, 0, 0]

    for i, ans in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if pattern[i % len(pattern)] == ans:
                scores[j] += 1

    max_score = max(scores)
    return [i + 1 for i, s in enumerate(scores) if s == max_score]

'''
========================================
포인트 정리
========================================
1. i % len(pattern): 패턴 순환의 핵심
   i=0: pattern[0]
   i=5: pattern[5 % 5] = pattern[0]  → 처음으로 돌아옴

2. 반환 조건:
   - 1명 이상일 수 있음 (동점)
   - 번호는 1-indexed → i+1
   - 오름차순: enumerate는 순서대로 → 자동 정렬됨

3. max_score = max(scores): 먼저 최고점 구하고
   list comprehension으로 같은 점수 필터링

완전탐색 성격:
  3명 × 10,000문제 = 30,000번 비교 → O(N), 충분히 빠름
  패턴 길이가 다르지만 % 연산으로 균일하게 처리
'''

# 테스트
print(solution([1, 2, 3, 4, 5]))  # [1]
print(solution([1, 3, 2, 4, 2]))  # [1, 2, 3]
