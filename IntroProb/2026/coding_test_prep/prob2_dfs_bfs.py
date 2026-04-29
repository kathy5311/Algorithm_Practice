'''
========================================
[유형 2] DFS / BFS
========================================
빈출 이유: 그래프·트리 탐색의 기본 중 기본
핵심 패턴:
  DFS → 재귀 or 스택 (경우의 수, 조합 탐색)
  BFS → deque (최단 거리, 최소 횟수)

----------------------------------------
[문제] 타겟 넘버 (프로그래머스 Lv.2) — DFS
----------------------------------------
n개의 음이 아닌 정수로 이루어진 배열 numbers에서
각 수에 +/- 를 붙여 합이 target이 되는 경우의 수를 구하세요.

예: numbers=[1,1,1,1,1], target=3
  → -1+1+1+1+1 = 3  ✓
     1-1+1+1+1 = 3  ✓
     ... 총 5가지

입출력 예:
numbers         | target | return
[1,1,1,1,1]    |   3    |   5
[4,1,2,1]      |   4    |   2

----------------------------------------
[내 풀이 시도 공간]
----------------------------------------
def solution(numbers, target):
    pass

----------------------------------------
[해설 & 정답]
----------------------------------------
핵심 아이디어:
  각 인덱스마다 +/- 두 갈래로 분기 → 이진 트리 탐색
  끝까지 가면 합이 target인지 체크

DFS 재귀 풀이:
'''

def solution(numbers, target):
    count = 0

    def dfs(idx, current_sum):
        nonlocal count
        if idx == len(numbers):        # 모든 수 사용 완료
            if current_sum == target:
                count += 1
            return
        dfs(idx + 1, current_sum + numbers[idx])  # + 붙이기
        dfs(idx + 1, current_sum - numbers[idx])  # - 붙이기

    dfs(0, 0)
    return count

'''
DFS 스택 풀이 (재귀 대신):
def solution(numbers, target):
    stack = [(0, 0)]   # (인덱스, 현재 합)
    count = 0
    while stack:
        idx, s = stack.pop()
        if idx == len(numbers):
            if s == target:
                count += 1
            continue
        stack.append((idx+1, s + numbers[idx]))
        stack.append((idx+1, s - numbers[idx]))
    return count

----------------------------------------
[문제 2] 게임 맵 최단거리 (프로그래머스 Lv.2) — BFS
----------------------------------------
n×m 격자에서 (0,0) → (n-1,m-1) 최단 거리 반환
이동 불가 칸=0, 이동 가능=1

입출력 예:
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
→ return 11

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,1,1,0,1],[1,1,1,0,0],[0,0,0,0,1]]
→ return -1 (도달 불가)
'''

from collections import deque

def solution_bfs(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    queue = deque([(0, 0, 1)])   # (행, 열, 거리)
    visited[0][0] = True
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        r, c, dist = queue.popleft()
        if r == n-1 and c == m-1:
            return dist
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maps[nr][nc] == 1:
                visited[nr][nc] = True
                queue.append((nr, nc, dist+1))
    return -1

'''
========================================
핵심 정리
========================================
DFS vs BFS 선택 기준:
  DFS → 가능한 경우의 수 전체 탐색, 조합/순열, 깊이 우선
  BFS → 최단 거리/최소 횟수, 레벨 단위 탐색

BFS 기본 템플릿:
  from collections import deque
  q = deque([시작])
  visited = set([시작])
  while q:
      curr = q.popleft()
      for next_node in neighbors(curr):
          if next_node not in visited:
              visited.add(next_node)
              q.append(next_node)

DFS 재귀 템플릿:
  def dfs(node):
      if 종료조건: ...
      for next_node in neighbors(node):
          if next_node not in visited:
              visited.add(next_node)
              dfs(next_node)
'''

# 테스트
print(solution([1,1,1,1,1], 3))   # 5
print(solution([4,1,2,1], 4))     # 2
maps1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution_bfs(maps1))        # 11
