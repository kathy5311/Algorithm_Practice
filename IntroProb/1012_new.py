import sys
sys.setrecursionlimit(10000)

def dfs(i, j, visited, g):
    visited[i][j] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if x < 0 or y < 0 or x >= len(visited) or y >= len(visited[0]): 
            continue
        if visited[x][y]==False and g[x][y] == 1:
            dfs(x, y, visited, g)

turn = int(input())
for _ in range(turn):
    M, N, K = map(int, input().split())
    g = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        g[b][a] = 1

    visited = [[False] * M for _ in range(N)]
    key = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and g[i][j] == 1:
                dfs(i, j, visited, g)
                key += 1

    print(key)