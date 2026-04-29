'''
[유형] 해시
[난이도] 프로그래머스 Lv.2
[문제] 위장
========================================

스파이는 여러 종류의 옷을 갖고 있으며 매일 다른 조합으로 위장합니다.
각 종류에서 최대 1개만 착용 가능하고, 최소 1가지는 입어야 합니다.
서로 다른 옷의 조합 수를 반환하세요.

[조건]
  - clothes[i] = [의상 이름, 의상 종류]
  - 같은 이름의 의상은 없음
  - 의상 종류는 여러 개 가능

[핵심 수식]
  각 카테고리에서 "안 입는 경우"를 포함한 선택지: (개수 + 1)
  전체 경우의 수 = 모든 카테고리의 (개수+1)을 곱한 값 - 1(아무것도 안 입는 경우)

[입출력 예]
clothes = [["yellow_hat","headgear"],["blue_sunglasses","eyewear"],["green_turban","headgear"]]
→ 5

  headgear: yellow_hat, green_turban (2개) → 3가지 선택 (안 입기 포함)
  eyewear:  blue_sunglasses (1개)          → 2가지 선택 (안 입기 포함)
  3 * 2 - 1 = 5

clothes = [["crow_mask","face"],["blue_sunglasses","face"],["smoky_makeup","face"]]
→ 3
'''

def solution(clothes):
    pass


# 테스트
print(solution([["yellow_hat","headgear"],["blue_sunglasses","eyewear"],["green_turban","headgear"]]))  # 5
print(solution([["crow_mask","face"],["blue_sunglasses","face"],["smoky_makeup","face"]]))              # 3
