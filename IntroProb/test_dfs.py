def dfs(node, visited, graph):
    visited[node] = True
    count = 1  # 현재 노드 포함
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(neighbor, visited, graph)
    return count

def solution(n, wires):
    answer = float('inf')
    
    for i in range(len(wires)):
        # i번째 전선을 끊는다
        temp = wires[:i] + wires[i+1:]
        print(temp)
        # 그래프 초기화
        graph = [[] for _ in range(n+1)]
        for a, b in temp:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * (n+1)
        
        # 끊고 난 후, 하나의 컴포넌트 개수 세기
        count = dfs(1, visited, graph)
        
        # 다른 컴포넌트는 전체 - count
        diff = abs(n - count - count)
        answer = min(answer, diff)
        
    return answer
print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))