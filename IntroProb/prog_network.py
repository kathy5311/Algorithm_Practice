#dfs
n=3
computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def solution(n,computers):
    visited = [False for _ in range(n)]
    answer=0
    for com in range(len(computers)):
        if visited[com]==False:
            dfs(n,computers,com,visited)
            answer+=1
    return answer

def dfs(n,computers,com,visited):
    visited[com]=True

    for i in range(n):
        if i!=com and computers[i][com]==1 and visited[i]==False:
            dfs(n,computers,i,visited)

print(solution(n,computers))
