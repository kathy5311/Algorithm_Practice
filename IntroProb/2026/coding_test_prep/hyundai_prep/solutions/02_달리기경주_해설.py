'''
[해설] 달리기 경주
========================================
핵심 아이디어:
  리스트만 쓰면 O(N*M) → TLE (players 5만, callings 100만)
  dict {이름: 인덱스} 를 함께 관리 → 이름으로 O(1) 위치 조회

  추월 시:
    1. rank[called]로 현재 위치 O(1) 조회
    2. 바로 앞 선수(front = players[idx-1]) 확인
    3. players 배열에서 두 선수 swap
    4. rank 딕셔너리도 동기화 (두 선수 인덱스 교환)
'''

def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}

    for called in callings:
        idx = rank[called]
        front = players[idx - 1]

        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        rank[called] = idx - 1
        rank[front] = idx

    return players

'''
========================================
포인트 정리
========================================
1. 리스트 + 딕셔너리 동시 유지: 핵심 패턴
   - players: 실제 순위 배열 (인덱스 → 이름)
   - rank: 빠른 탐색용 (이름 → 인덱스)
   - 두 자료구조를 항상 동기화해야 함

2. a, b = b, a: 파이썬 swap (임시 변수 불필요)

3. 시간복잡도:
   순진한 풀이: players.index(called) → O(N) → 전체 O(N*M) TLE
   dict 활용:   rank[called]          → O(1) → 전체 O(M) 통과

응용: 순위 변동, 리더보드 업데이트 등 동일 패턴
'''

# 테스트
print(solution(["mumu","soe","poe","kai","mine"], ["kai","kai","mine","kai"]))
# ["mumu","kai","mine","soe","poe"]
