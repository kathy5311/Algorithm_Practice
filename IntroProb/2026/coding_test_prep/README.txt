========================================
코딩테스트 2일 전 집중 연습 가이드
========================================

[파일 목록 & 학습 순서]
--------------------------------------
prob1_hash.py          ★★★★★ 해시 (빈도 계산, 접두어 탐색)
prob2_dfs_bfs.py       ★★★★★ DFS/BFS (경우의 수, 최단 거리)
prob3_greedy.py        ★★★★☆ 탐욕법 (정렬 + 국소 최적)
prob4_dp.py            ★★★★☆ 동적 프로그래밍 (점화식)
prob5_bruteforce_twopter.py ★★★★☆ 완전탐색 + 투 포인터

[2일 스케줄]
--------------------------------------
D-2 (오늘):
  □ prob1_hash.py        → 해설 읽고 스스로 다시 짜보기
  □ prob2_dfs_bfs.py     → DFS 재귀 템플릿 암기, BFS deque 패턴 암기
  □ prob3_greedy.py      → 투 포인터 손으로 시뮬레이션

D-1 (내일):
  □ prob4_dp.py          → 점화식 찾는 연습 (코드 없이 점화식 먼저)
  □ prob5_bruteforce_twopter.py → 슬라이딩 윈도우 손으로 추적
  □ prob1~5 전체를 해설 안 보고 처음부터 다시 풀기

[시험 당일 체크리스트]
--------------------------------------
□ from collections import deque   (BFS용)
□ import heapq                    (우선순위 큐)
□ from collections import Counter (빈도 계산)
□ sys.setrecursionlimit(10**6)    (DFS 재귀 깊이 제한 해제)
□ 시간복잡도 계산: N=10^6 → O(N log N) 이하 필요

[자주 나오는 실수]
--------------------------------------
1. BFS에서 visited 표시를 큐에 넣기 전에 해야 함
   (넣은 후 하면 중복 방문 발생)
2. DFS 재귀에서 nonlocal 또는 리스트로 결과 전달
3. 그리디 정렬 기준 실수 → 반례 먼저 찾기
4. DP 배열 크기 인덱스 off-by-one 오류
5. 정수 나눗셈: // 사용 (/ 는 float)
