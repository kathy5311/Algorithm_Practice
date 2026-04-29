'''
[해설] 가장 큰 수
========================================
핵심 아이디어:
  두 수 a, b를 문자열로 이어 붙인 결과를 비교
  "ab" > "ba" 이면 a가 앞에 와야 함

  예: 3과 30 비교
    "330" vs "303" → 330 > 303 → 3이 앞

  cmp_to_key로 이 비교 로직을 sort에 적용
'''

from functools import cmp_to_key

def solution(numbers):
    nums = list(map(str, numbers))

    def compare(a, b):
        if a + b > b + a:
            return -1   # a가 앞 (내림차순)
        elif a + b < b + a:
            return 1    # b가 앞
        return 0

    nums.sort(key=cmp_to_key(compare))
    result = ''.join(nums)
    return '0' if result[0] == '0' else result

'''
========================================
포인트 정리
========================================
1. cmp_to_key: 비교 함수(a, b)를 key 함수로 변환
   compare(a, b) 반환값:
     음수(-1): a가 b보다 앞
     양수(+1): b가 a보다 앞
     0: 동일

2. [0, 0, 0] 예외 처리:
   정렬 후 ''.join → "000"
   result[0] == '0' 이면 "0" 반환

3. int로 비교하면 안 되는 이유:
   3 vs 30: 수 크기는 30이 크지만 "3" + "30" = "330" > "303"
   → 문자열 연결 후 비교만이 정확

lambda 한 줄 버전 (숫자 최대 4자리인 경우):
  nums.sort(key=lambda x: x*4, reverse=True)
  → x를 반복해 비교 자릿수를 맞춤
  → 단, cmp_to_key가 더 정확하고 범용적
'''

# 테스트
print(solution([6, 10, 2]))            # "6210"
print(solution([3, 30, 34, 5, 9]))     # "9534330"
print(solution([0, 0, 0]))             # "0"
print(solution([10, 2]))               # "210"
