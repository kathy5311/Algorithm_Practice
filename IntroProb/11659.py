import sys

N,M = (map(int, sys.stdin.readline().split()))
num = list(map(int, sys.stdin.readline().split()))

partial_sum=[0]
count=0
for i in num:
    count= i+count
    partial_sum.append(count)

for _ in range(M):
    i,j = map(int, sys.stdin.readline().split())
    total= partial_sum[j]-partial_sum[i-1]
    print(total)
    

