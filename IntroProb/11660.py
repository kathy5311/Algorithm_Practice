import sys

N,M = map(int, sys.stdin.readline().split())

#make matrix
mat=[[0]*(N+1)]
for _ in range(N):
    row = [0]+list(map(int, sys.stdin.readline().split()))
    mat.append(row)

#partial sum(D)
D = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        D[i][j] = D[i-1][j]+D[i][j-1]-D[i-1][j-1]+mat[i][j]

#total sum
for _ in range(M):
    s_row, s_col, e_row, e_col = list(map(int, sys.stdin.readline().split()))
    total = D[e_row][e_col]-D[e_row][s_col-1]-D[s_row-1][e_col]+D[s_row-1][s_col-1]

    print(total)