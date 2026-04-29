'''
[해설] 소수 찾기
========================================
핵심 아이디어:
  1. 1자리 ~ n자리 모든 순열 생성 (permutations)
  2. 각 순열을 숫자로 변환 → set에 저장 (중복 제거)
  3. set의 각 숫자에 대해 소수 판별
'''

from itertools import permutations

def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    candidates = set()
    for r in range(1, len(numbers) + 1):
        for perm in permutations(numbers, r):
            candidates.add(int(''.join(perm)))

    return sum(1 for n in candidates if is_prime(n))

'''
========================================
포인트 정리
========================================
1. permutations(iterable, r):
   - iterable: 문자열도 가능 ("17" → ['1','7'])
   - r개를 뽑는 모든 순열 반환 (튜플)
   - r=1부터 len(numbers)까지 모두 시도

2. set으로 중복 제거:
   "11"에서 permutations("11", 2) → ('1','1'), ('1','1')
   → int(''.join(...)) = 11 두 번 → set으로 1개로 합쳐짐

3. int(''.join(('0','1'))) = 1: 앞의 0 자동 제거

4. is_prime: O(√n) 소수 판별
   - n < 2: 0, 1은 소수 아님
   - 2부터 √n까지 나눠지면 소수 아님

combinations vs permutations:
  이 문제는 순서가 다르면 다른 수 → permutations
  ex) ('1','7') = 17, ('7','1') = 71 → 둘 다 포함
'''

# 테스트
print(solution("17"))   # 3  (소수: 7, 17, 71)
print(solution("011"))  # 2  (소수: 11, 101)
