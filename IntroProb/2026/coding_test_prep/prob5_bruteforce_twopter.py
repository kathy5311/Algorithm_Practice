'''
========================================
[유형 5] 완전탐색 + 투 포인터 / 슬라이딩 윈도우
========================================
빈출 이유: 범위 내 최적 조합 탐색, 연속 구간 문제
핵심 패턴: 정렬 후 포인터 이동, 윈도우 유지

----------------------------------------
[문제] 두 수의 합 / 세 수의 합 (카카오 변형 기본기)
----------------------------------------
정렬된 배열에서 합이 target이 되는 쌍의 개수를 구하세요.

예: arr=[1,2,3,4,5], target=5
  → (1,4), (2,3) → 2쌍

입출력 예:
arr=[1,2,3,4,5], target=5  → 2
arr=[1,1,2,3,4], target=5  → 2  (인덱스 기준 (1,4), (2,3))

----------------------------------------
[내 풀이 시도 공간]
----------------------------------------
def count_pairs(arr, target):
    pass

----------------------------------------
[해설 & 정답]
----------------------------------------
핵심 아이디어:
  정렬 후 left/right 포인터
  합이 target보다 작으면 left++, 크면 right--
  같으면 카운트 후 둘 다 이동
'''

def count_pairs(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    count = 0

    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            count += 1
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1

    return count

'''
----------------------------------------
[문제] 연속된 부분 배열의 합 (슬라이딩 윈도우)
----------------------------------------
양수 배열에서 연속 부분 배열의 합이 target 이상인
가장 짧은 구간의 길이를 구하세요.
(없으면 0 반환)

예: arr=[2,3,1,2,4,3], target=7
  → [4,3] (길이 2)

입출력 예:
arr=[2,3,1,2,4,3], target=7  → 2
arr=[1,1,1,1,1],   target=11 → 0
'''

def min_subarray_len(arr, target):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target:          # 조건 만족하는 동안
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return 0 if min_len == float('inf') else min_len

'''
----------------------------------------
[문제] 카펫 (프로그래머스 Lv.2) — 완전탐색
----------------------------------------
갈색 격자 수 brown, 노란색 격자 수 yellow가 주어질 때
카펫의 가로, 세로 크기를 [가로, 세로] 형태로 반환
(가로 >= 세로, 노란 격자는 안쪽, 갈색은 테두리)

예: brown=10, yellow=2 → [4,3]
     _ _ _ _
    |_ _ _ _|
    |_ Y Y _|
    |_ _ _ _|

입출력 예:
brown=10, yellow=2   → [4,3]
brown=8,  yellow=1   → [3,3]
brown=24, yellow=24  → [8,6]
'''

def solution_carpet(brown, yellow):
    total = brown + yellow

    # 가로 >= 세로, 최소 크기: 세로 3 (노란 격자 보장)
    for height in range(3, total + 1):
        if total % height != 0:
            continue
        width = total // height
        if width < height:
            break
        # 테두리 = 2*(width + height) - 4 == brown
        if 2 * (width + height) - 4 == brown:
            return [width, height]

'''
========================================
핵심 정리
========================================
투 포인터 조건:
  - 배열이 정렬되어 있거나 단조(monotone) 성질이 있을 때
  - "두 수의 합", "가장 가까운 쌍", "구간 길이 최소/최대"

슬라이딩 윈도우 조건:
  - 연속 구간에서 합/최대/최소 탐색
  - 윈도우 크기가 고정 또는 조건부 가변

완전탐색 효율화:
  - 가능한 범위를 줄이기 (약수, 범위 제한)
  - 정렬 후 탐색 (불필요한 경우 건너뜀)
  - 비트마스크로 부분집합 열거: for mask in range(1 << n)
'''

# 테스트
print(count_pairs([1,2,3,4,5], 5))         # 2
print(count_pairs([1,1,2,3,4], 5))         # 2
print(min_subarray_len([2,3,1,2,4,3], 7)) # 2
print(min_subarray_len([1,1,1,1,1], 11))  # 0
print(solution_carpet(10, 2))              # [4,3]
print(solution_carpet(24, 24))             # [8,6]
