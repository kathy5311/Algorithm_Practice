import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))

queue = deque([i for i in range(1,N+1)])
seq=[]

while len(queue) >0:
    for _ in range(K-1):
        queue.append(queue.popleft())
    seq.append(str(queue.popleft()))

a = ", ".join(seq)
print("<",end="")
print(a,end="")
print(">")



