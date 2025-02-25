import sys
from collections import deque

def solution(graph):
    ans=0

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))

        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx < 0 or nx >=len(graph) or ny<0 or ny>=len(graph[0]):
                    continue
                if graph[nx][ny]==1:
                    graph[nx][ny]=graph[x][y]+1
                    queue.append((nx,ny))

        return graph[len(graph)-1][len(graph[0])-1]
    ans = bfs(0,0)
    return -1 if ans==1 else ans

