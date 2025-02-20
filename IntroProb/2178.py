import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y

            if 0<=nx<len(graph) and 0<=ny<len(graph[0]):
                
                if graph[nx][ny]==1:
                    graph[nx][ny] = graph[x][y]+1
                    queue.append((nx,ny))
    return graph[len(graph)-1][len(graph[0])-1]

N,M = map(int, sys.stdin.readline().split()) 
graph =[list(map(int, input().strip())) for _ in range(N)]

print(bfs(0,0))