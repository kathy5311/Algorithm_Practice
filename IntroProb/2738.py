import sys

N,M = (map(int,sys.stdin.readline().split()))

# Make matrix
A,B=[],[]

for _ in range(N):
    a = list(map(int,sys.stdin.readline().split()))
    A.append(a)

for _ in range(N):
    b= list(map(int, sys.stdin.readline().split()))
    B.append(b)

for i in range(N):
    row_list=[]
    for j in range(M):
        row_list.append(A[i][j]+B[i][j])
    for k in row_list:
        print(k, end=' ')
    print()



