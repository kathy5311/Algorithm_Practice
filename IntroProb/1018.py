import sys

N, M = list(map(int, sys.stdin.readline().split()))

board=[]
result=[]
for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        draw_0=0 #WB
        draw_1=0 #BW

        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    #print(a,b)
                    if board[a][b]=='B':
                        draw_1+=1
                    if board[a][b] == 'W':
                        draw_0+=1
                elif (a+b)%2==1:
                    if board[a][b]=='W':
                        draw_1+=1
                    if board[a][b]=='B':
                        draw_0+=1
        result.append(draw_0)
        result.append(draw_1)
print(min(result))


        



