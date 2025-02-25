from collections import deque

def DFS(g, v, visited):
    visited[v]=True
    print(v, end=' ')
    for i in g[v]:
        if not visited[i]:
            DFS(g,i,visited)

def BFS(g, start, visited):
    queue = deque([start])
    visited[start]=True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in g[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
