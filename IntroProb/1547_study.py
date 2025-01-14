import sys

cup = [1,2,3]
N = int(input())

for _ in range(N):
    a,b = map(int, sys.stdin.readline().split())
    tmp = cup.index(a)
    tmp1 = cup.index(b)
    cup[tmp] = b
    cup[tmp1] = a

if cup[0]:
    print(cup[0])
else:
    print(-1)

