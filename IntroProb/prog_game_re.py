#게임 최단거리
from collections import deque

maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

def solution(maps):
    answer=0
    def bfs(x,y):
        dx=[0,0,-1,1]
        dy=[1,-1,0,0]

        queue = deque()
        queue.append((x,y))

        while queue:
            x,y = queue.popleft()


            for i in range(4):
                X=x+dx[i]
                Y=y+dy[i]
                if X>=len(maps) or Y>=len(maps) or X<0 or Y<0:
                    continue
                if maps[X][Y]==0:
                    continue
                if maps[X][Y]==1:
                    maps[X][Y]=maps[x][y]+1
                    queue.append((X,Y))
        return maps[len(maps)-1][len(maps)-1]
    answer=bfs(0,0)

    return -1 if answer==1 else answer


print(solution(maps))
