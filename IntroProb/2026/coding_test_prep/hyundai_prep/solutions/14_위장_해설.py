'''
[해설] 위장
========================================
핵심 아이디어:
  카테고리별로 (의상 수 + 1)을 곱한 뒤 1 빼기
  +1: "해당 카테고리 안 입는" 경우 포함
  -1: 모든 카테고리를 안 입는 경우(완전히 알몸) 제외

예: headgear 2개, eyewear 1개
  headgear: yellow_hat / green_turban / 안 입음  → 3가지
  eyewear:  blue_sunglasses / 안 입음           → 2가지
  전체: 3 * 2 = 6가지
  - 1 (둘 다 안 입는 경우) = 5가지
'''

from collections import Counter

def solution(clothes):
    cnt = Counter(c[1] for c in clothes)   # 카테고리별 개수
    result = 1
    for v in cnt.values():
        result *= (v + 1)
    return result - 1

'''
========================================
포인트 정리
========================================
1. Counter(c[1] for c in clothes): 두 번째 원소(카테고리)만 집계
   제너레이터 표현식으로 리스트 생성 없이 바로 Counter 생성

2. 곱셈 공식: (각 카테고리 개수 + 1)의 곱 - 1
   수학적 증명: 각 카테고리는 독립적 선택 → 경우의 수 곱셈 법칙

3. result = 1로 초기화 (곱셈의 항등원)
   result = 0으로 하면 항상 0이 됨 → 실수 주의

한 줄로:
  from functools import reduce
  return reduce(lambda x, y: x*(y+1), Counter(c[1] for c in clothes).values(), 1) - 1
'''

# 테스트
print(solution([["yellow_hat","headgear"],["blue_sunglasses","eyewear"],["green_turban","headgear"]]))  # 5
print(solution([["crow_mask","face"],["blue_sunglasses","face"],["smoky_makeup","face"]]))              # 3
