import sys

N,M = (map(int, sys.stdin.readline().split()))
mat = [list((input())) for _ in range(N)]
step = min(N,M)-1

while step>=0:

    for i in range(N-step):
        for j in range(M-step):

            if (mat[i][j]==mat[i+step][j]) and (mat[i][j]==mat[i][j+step]) and (mat[i][j]==mat[i+step][j+step]):
                print((step+1)**2)
                exit()
    step-=1
