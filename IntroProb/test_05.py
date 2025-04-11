from collections import deque
def check(start, end, visited, graph):
    visited[start] = 1
    visited[end] = 1
    q = deque()
    q.append(end)
    print(q)
    cnt = 1
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                cnt += 1
                q.append(next)
    return cnt

def solution(n, wires):
    answer = -1
    graph = [[] for _ in range(n+1)]
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    answer = float("inf")
    #print(answer)
    for s,e in wires:
        #print(s,e)
        visited = [0] * (n+1)
        res = check(s, e, visited, graph)
        alpha = abs(n - res)
        res = abs(res - alpha)
        answer = min(answer, res)
    return answer
print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))