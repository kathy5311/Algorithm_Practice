'''
[해설] 네트워크
========================================
핵심 아이디어:
  방문하지 않은 노드에서 DFS/BFS 시작 시마다 네트워크 +1
  한 번 DFS를 시작하면 연결된 모든 노드를 visited 처리

  전체 흐름:
    for 모든 노드:
        if 아직 미방문:
            DFS 시작 (연결된 전체 탐색)
            count += 1
'''

def solution(n, computers):
    visited = [False] * n

    def dfs(node):
        visited[node] = True
        for next_node in range(n):
            if computers[node][next_node] == 1 and not visited[next_node]:
                dfs(next_node)

    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count

'''
========================================
BFS 버전
========================================
'''

from collections import deque

def solution_bfs(n, computers):
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            while queue:
                node = queue.popleft()
                for next_node in range(n):
                    if computers[node][next_node] == 1 and not visited[next_node]:
                        visited[next_node] = True
                        queue.append(next_node)
            count += 1

    return count

'''
========================================
포인트 정리
========================================
1. "연결 요소 개수" = 그래프에서 가장 기본적인 DFS/BFS 활용

2. 인접 행렬 탐색: for next_node in range(n)
   → computers[node][next_node] == 1 이면 연결

3. 인접 리스트였다면: for next_node in graph[node]

4. computers[i][i] = 1 (자기 자신) → visited 체크로 자연스럽게 처리됨

DFS vs BFS 둘 다 가능:
  연결 요소 개수 문제는 DFS가 코드 더 짧음
  재귀 깊이 제한 걱정 없으면 DFS 재귀 추천

재귀 깊이 주의:
  n이 크면 sys.setrecursionlimit(10**6) 추가
'''

# 테스트
print(solution(3, [[1,1,0],[1,1,0],[0,0,1]]))  # 2
print(solution(3, [[1,1,0],[1,1,1],[0,1,1]]))  # 1
