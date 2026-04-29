'''
[해설] 행렬 테두리 회전하기
========================================
핵심 아이디어:
  1. 사각형 테두리를 시계 방향으로 순서대로 1차원 리스트로 추출
  2. 1차원 리스트에서 최솟값 저장
  3. 리스트를 오른쪽으로 1칸 회전 (마지막 원소를 맨 앞으로)
  4. 다시 행렬에 채워 넣기

추출 순서 (시계 방향):
  위쪽 행   →  (r1, c1~c2)
  오른쪽 열 →  (r1+1~r2, c2)
  아래쪽 행 ←  (r2, c2-1~c1)
  왼쪽 열   ↑  (r2-1~r1+1, c1)
'''

def solution(rows, columns, queries):
    matrix = [[columns*(i-1)+j for j in range(1, columns+1)]
              for i in range(1, rows+1)]
    result = []

    for r1, c1, r2, c2 in queries:
        r1-=1; c1-=1; r2-=1; c2-=1    # 0-indexed 변환

        # 테두리 시계방향 추출
        top    = [matrix[r1][c]  for c in range(c1, c2+1)]
        right  = [matrix[r][c2]  for r in range(r1+1, r2+1)]
        bottom = [matrix[r2][c]  for c in range(c2-1, c1-1, -1)]
        left   = [matrix[r][c1]  for r in range(r2-1, r1, -1)]
        border = top + right + bottom + left

        result.append(min(border))

        # 오른쪽으로 1칸 회전 (마지막 → 맨 앞)
        border = [border[-1]] + border[:-1]

        # 다시 채워 넣기
        idx = 0
        for c in range(c1, c2+1):        matrix[r1][c]  = border[idx]; idx+=1
        for r in range(r1+1, r2+1):      matrix[r][c2]  = border[idx]; idx+=1
        for c in range(c2-1, c1-1, -1):  matrix[r2][c]  = border[idx]; idx+=1
        for r in range(r2-1, r1, -1):    matrix[r][c1]  = border[idx]; idx+=1

    return result

'''
========================================
포인트 정리
========================================
1. 1-indexed → 0-indexed 변환: r1-=1, c1-=1, r2-=1, c2-=1

2. 시계 방향 회전 = 1차원 리스트를 오른쪽으로 1칸 shift
   [a,b,c,d,e] → [e,a,b,c,d]
   border = [border[-1]] + border[:-1]

3. 테두리 추출 방향 주의:
   위: 왼→오   range(c1, c2+1)
   우: 위→아   range(r1+1, r2+1)
   아래: 오→왼 range(c2-1, c1-1, -1)   ← 역방향!
   좌: 아→위   range(r2-1, r1, -1)      ← 역방향!

4. min(border): 이동한 숫자의 최솟값 = 테두리 전체 최솟값
'''

# 테스트
print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))               # [8, 10, 25]
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))     # [1, 1, 5, 3]
