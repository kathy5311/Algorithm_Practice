import sys
from collections import deque

max=10**5
dict=[0]*(max+1)
start, end = map(int, sys.stdin.readline().split())

def bfs():
    q = deque([])
    q.append(start)

    while q:
        v= q.popleft()

        if v ==end:
            print(dict[v])

        for i in (v+1, v-1, 2*v):
            if (0<= i <max) and not dict[i]:
                q.append(i)
                dict[i] = dict[v]+1 
bfs()
