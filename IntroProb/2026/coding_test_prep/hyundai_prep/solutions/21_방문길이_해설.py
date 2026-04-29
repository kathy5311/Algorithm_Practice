'''
[해설] 방문 길이
========================================
핵심 아이디어:
  간선(edge)을 (출발, 도착) 쌍으로 set에 저장
  양방향이므로 (r,c,nr,nc)와 (nr,nc,r,c) 둘 다 추가
  set의 크기 // 2 = 처음 걸어본 간선 수
'''

def solution(dirs):
    visited = set()
    r, c = 0, 0
    d_map = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

    for d in dirs:
        dr, dc = d_map[d]
        nr, nc = r+dr, c+dc

        if not (-5 <= nr <= 5 and -5 <= nc <= 5):
            continue                             # 경계 밖 → 무시

        visited.add((r, c, nr, nc))              # 정방향 간선
        visited.add((nr, nc, r, c))              # 역방향 간선 (양방향 처리)
        r, c = nr, nc

    return len(visited) // 2

'''
========================================
포인트 정리
========================================
1. 간선 = (출발점, 도착점) 쌍: 좌표가 아닌 이동 경로를 저장
   "처음 걷는 길" = set에 없는 간선

2. 양방향 처리:
   A→B와 B→A는 같은 도로 → 둘 다 추가 → len//2
   또는 (min(r,nr), min(c,nc), max(r,nr), max(c,nc))로 정규화해도 됨

3. 경계 처리:
   nr, nc 계산 후 범위 체크 → 벗어나면 r, c 업데이트하지 않음
   (r, c는 이동 전 값 유지)

4. 격자 좌표 방향 주의:
   U: 행 감소(-1, 0), D: 행 증가(1, 0)
   L: 열 감소(0, -1), R: 열 증가(0, 1)

잘못된 접근:
  ❌ visited에 좌표(r, c)만 저장 → 같은 좌표를 다른 경로로 가는 경우 구분 불가
  ✓ (출발, 도착) 간선 단위로 저장
'''

# 테스트
print(solution("ULURRDLLU"))  # 7
print(solution("LULLLLLLU"))  # 7
