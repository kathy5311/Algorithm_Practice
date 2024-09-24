import sys

N,M = list(map(int, sys.stdin.readline().split()))

setting = [sys.stdin.readline() for _ in range(N)]
checker = [sys.stdin.readline() for _ in range(M)]

count=0
for i in checker:
    if i in setting:
        count+=1

print(count)