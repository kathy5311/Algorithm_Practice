import sys
from collections import deque

def DFS(g, v, visited):
    visited[v]=True
    print(v, end=' ')
    for i in g[v]:
        if not visited[i]:
            DFS(g,i,visited)

def BFS(g,start,visited):
    queue = deque([start])
    visited[start]=True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in g[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, sys.stdin.readline().split())

visited = [False]*(N+1)
visited_bfs = [False]*(N+1)
g = [[] for _ in range(N+1)]

for i in range(M+1):
    if i ==0:
        continue
    else:
        a,b = map(int, sys.stdin.readline().split())
        g[a].append(b)
        g[b].append(a)
for i in g:
    i.sort()


DFS(g,V,visited)
print()
BFS(g,V,visited_bfs)


