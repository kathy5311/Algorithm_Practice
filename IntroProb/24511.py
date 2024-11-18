import sys
from collections import deque

NQS = int(input())
QorS = list(map(int, sys.stdin.readline().split()))
Init = list(map(int, sys.stdin.readline().split()))
LenS = int(input())
InNum = list(map(int, sys.stdin.readline().split()))

res = deque()

for i in range(NQS):

    if QorS[i] == 0:
        res.appendleft(Init[i])
seq=[]
for j in range(LenS):
    res.append(InNum[j])
    k=res.popleft()
    seq.append(k)

for i in seq:
    print(i, end=' ')

