'''
[해설] H-Index
========================================
핵심 아이디어:
  내림차순 정렬 후 인덱스 i의 의미:
    "인용수 >= citations[i]인 논문이 (i+1)편 있다"

  citations[i] >= i+1 이면 H = i+1 이상 가능
  citations[i] <  i+1 이면 → 이 시점이 한계 → H = i

  i >= c 조건 (0-indexed):
    i = 현재 인덱스, c = 인용수
    i >= c → "순위(i)보다 인용수(c)가 작음" → H = i
  끝까지 조건 안 깨지면 → H = len(citations)
'''

def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i >= c:
            return i
    return len(citations)

'''
========================================
포인트 정리
========================================
직관적으로 이해하기:
  [6, 5, 3, 1, 0] (내림차순 정렬)
  i=0: c=6, 0 >= 6? No  → 적어도 1편이 1회 이상 → 계속
  i=1: c=5, 1 >= 5? No  → 적어도 2편이 2회 이상 → 계속
  i=2: c=3, 2 >= 3? No  → 적어도 3편이 3회 이상 → 계속
  i=3: c=1, 3 >= 1? Yes → 4편이 4회 이상? No → H = 3 반환

두 번째 return len(citations):
  [5, 5, 5, 5, 5]: 모두 조건 통과 → 5편 이상 5회 이상 → H = 5

잘못된 접근:
  ❌ citations.count(c) 방식 → O(N²)
  ✓ 정렬 후 인덱스 활용 → O(N log N)
'''

# 테스트
print(solution([3, 0, 6, 1, 5]))   # 3
print(solution([10, 8, 5, 4, 3]))  # 4
print(solution([25, 8, 5, 3, 3]))  # 3
print(solution([5, 5, 5, 5, 5]))   # 5
