import sys

A=[]
for _ in range(9):
    a = list(map(int,sys.stdin.readline().split()))
    A.append(a)

maximum=0
row=0
col=0

for i in range(9):
    for j in range(9):
        if maximum <= A[i][j]:
            maximum=A[i][j]
            row=i+1
            col=j+1
print(maximum)
print(row,col)

