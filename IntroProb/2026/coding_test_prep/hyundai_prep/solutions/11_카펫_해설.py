'''
[해설] 카펫
========================================
핵심 아이디어:
  total = brown + yellow = width * height
  테두리 공식: 2*(width + height) - 4 = brown

  height를 3부터 순서대로 완전탐색:
    total의 약수인 height 찾기
    width = total // height
    가로 >= 세로 조건 (width >= height) 확인
    테두리 공식 만족하면 반환
'''

def solution(brown, yellow):
    total = brown + yellow

    for height in range(3, total + 1):
        if total % height != 0:
            continue
        width = total // height
        if width < height:          # 가로 >= 세로 위반 → 이후 없음
            break
        if 2 * (width + height) - 4 == brown:
            return [width, height]

'''
========================================
포인트 정리
========================================
테두리 공식 유도:
  가로 위 칸: width개
  가로 아래 칸: width개
  세로 왼쪽: (height-2)개  ← 모서리 제외
  세로 오른쪽: (height-2)개
  합계: 2*width + 2*(height-2) = 2*(width+height) - 4

탐색 범위 최적화:
  height <= sqrt(total) 까지만 탐색해도 됨
  width < height가 되는 순간 break (이후는 의미 없음)

잘못된 접근:
  ❌ width, height 모두 이중 for → O(total²)
  ✓ height만 탐색, width = total // height → O(sqrt(total))
'''

# 테스트
print(solution(10, 2))   # [4, 3]
print(solution(8, 1))    # [3, 3]
print(solution(24, 24))  # [8, 6]
