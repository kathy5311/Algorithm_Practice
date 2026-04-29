'''
[해설] 크레인 인형 뽑기 게임
========================================
핵심 아이디어:
  board 각 열을 위에서부터 탐색해 첫 번째 인형 뽑기
  바구니(스택)의 맨 위와 같은 인형이면 팝 + count+=2
  다르면 push

  스택의 top == 새 인형 → 터짐 (짝 맞추기 = 올바른 괄호와 동일 패턴)
'''

def solution(board, moves):
    N = len(board)
    basket = []
    count = 0

    for col in moves:
        col -= 1                         # 1-indexed → 0-indexed
        for row in range(N):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0      # 뽑은 자리는 빈 칸으로

                if basket and basket[-1] == doll:
                    basket.pop()
                    count += 2           # 두 개 터짐
                else:
                    basket.append(doll)
                break                   # 한 개만 뽑고 다음 move로

    return count

'''
========================================
포인트 정리
========================================
1. board[row][col] == 0: 빈 칸 → 건너뜀
   처음 0이 아닌 칸이 해당 열의 가장 위 인형

2. board[row][col] = 0: 뽑은 자리 비우기 (다음에 다시 그 열을 선택하면 아래 인형)

3. 스택 top 비교 후 pop or push:
   올바른 괄호 문제와 동일한 구조

4. break: 인형 하나 뽑으면 즉시 다음 move로
   break 없으면 같은 열에서 계속 뽑는 버그

5. count += 2: 두 개가 터지므로 +2
'''

# 테스트
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
print(solution(board, [1,5,3,5,1,2,1,4]))  # 4
