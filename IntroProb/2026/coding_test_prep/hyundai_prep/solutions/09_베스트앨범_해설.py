'''
[해설] 베스트앨범
========================================
핵심 아이디어:
  1. 장르별 총 재생수 집계 → 정렬 기준
  2. 장르별 (재생수, 인덱스) 리스트 구성
  3. 총 재생수 내림차순으로 장르 순회
  4. 각 장르에서 상위 2곡 추출 (재생수 내림, 인덱스 오름)
'''

from collections import defaultdict

def solution(genres, plays):
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)

    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] += p
        genre_songs[g].append((p, i))   # (재생수, 고유번호)

    result = []
    for genre in sorted(genre_total, key=lambda g: -genre_total[g]):
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        for p, idx in songs[:2]:
            result.append(idx)

    return result

'''
========================================
포인트 정리
========================================
1. defaultdict(int) : 없는 키 → 0으로 자동 초기화
   defaultdict(list): 없는 키 → []으로 자동 초기화

2. zip(genres, plays): 두 리스트 동시 순회
   enumerate(zip(...)): 인덱스 + 두 값 동시에

3. 다중 기준 정렬:
   key=lambda x: (-x[0], x[1])
   → 재생수 내림차순(-), 인덱스 오름차순

4. songs[:2]: 최대 2곡 (1곡뿐이면 자동으로 1곡만)

장르 정렬:
   sorted(genre_total, key=lambda g: -genre_total[g])
   → dict를 정렬하면 키(장르 이름)를 기준으로 반복
   → key에 총 재생수 음수 → 내림차순
'''

# 테스트
print(solution(
    ["classic","pop","classic","classic","pop"],
    [500, 600, 150, 800, 2500]
))  # [4, 1, 3, 0]
