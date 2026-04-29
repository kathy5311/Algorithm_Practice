'''
[해설] 게임 맵 최단거리
========================================
핵심 아이디어:
  BFS = 최단 거리 보장 (레벨 단위 탐색)
  queue에 (행, 열, 현재 거리)를 함께 저장
  목적지 도달 시 즉시 반환 → 처음 도달한 경로가 최단

  BFS 기본 흐름:
    1. 시작점 큐 삽입, visited 표시
    2. 꺼낸 칸의 4방향 탐색
    3. 유효하고 미방문이고 벽이 아니면 큐 삽입
    4. 목적지 도달 시 거리 반환
'''

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        r, c, dist = queue.popleft()
        if r == n-1 and c == m-1:
            return dist
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maps[nr][nc] == 1:
                visited[nr][nc] = True   # 큐에 넣기 전 방문 표시!
                queue.append((nr, nc, dist+1))

    return -1   # 목적지 도달 불가

'''
========================================
포인트 정리
========================================
1. visited 표시 타이밍: 큐에 넣기 전
   ❌ 꺼낼 때 표시 → 같은 칸이 큐에 여러 번 들어감 → TLE

2. 거리를 큐에 함께 저장 vs 별도 배열:
   함께 저장: (r, c, dist) → 간단하지만 메모리 조금 더 사용
   별도 배열: dist[r][c] 초기화 후 업데이트 → 더 일반적

   별도 배열 버전:
   dist = [[-1]*m for _ in range(n)]
   dist[0][0] = 1
   ...
   dist[nr][nc] = dist[r][c] + 1
   return dist[n-1][m-1]

3. return -1: while 루프가 끝날 때까지 목적지 미도달 → 불가능

BFS vs DFS 선택:
  최단 거리/최소 횟수 → BFS
  모든 경우의 수/경로 탐색 → DFS
'''

# 테스트
maps1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps2 = [[1,0,1,1,1],[1,0,1,0,1],[1,1,1,0,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps1))  # 11
print(solution(maps2))  # -1
