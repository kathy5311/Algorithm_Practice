#0303 review
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    if x<0 or y<0 or x>=M or y>=N:
        return False 
    
    if graph[x][y]==1:
        graph[x][y]=0
        for i in range(4):
            X=x+dx[i]
            Y=y+dy[i]
            dfs(X,Y)
        return True
    return False

T=int(input())

for _ in range(T):
    count=0
    M,N,K=map(int, sys.stdin.readline().split())
    graph = [[0]*N for _ in range(M)]
    for _ in range(K):
        x,y = map(int,sys.stdin.readline().split())
        graph[x][y]=1

    for a in range(M):
        for b in range(N):
            if dfs(a,b):
                count+=1
    print(count)



