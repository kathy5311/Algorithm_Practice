========================================
현대자동차 / 현대모비스 코딩테스트 가이드
========================================

[현대 계열 시험 특징]
--------------------------------------
- 플랫폼: 프로그래머스
- 문제 수: 보통 2~3문제 (60~90분)
- 난이도: Lv.1~2 중심, 간혹 Lv.3
- 특징: 알고리즘 < 구현 정확도
         → 문제 길고 조건 많음 → 꼼꼼히 읽기 필수

[빈출 유형 우선순위]
--------------------------------------
★★★★★  구현/시뮬레이션   type1_simulation.py
★★★★☆  스택/큐           type2_stack_queue.py  (+기존 stack_prog1~3.py)
★★★★☆  정렬             type3_sort.py
★★★☆☆  완전탐색          type4_bruteforce.py

[2일 학습 플랜]
--------------------------------------
D-2 오전: type1_simulation.py  (시뮬레이션 3문제 - 가장 중요)
D-2 오후: type2_stack_queue.py (다리 트럭 + 주식가격)
D-1 오전: type3_sort.py        (가장 큰 수 - cmp_to_key 암기)
D-1 오후: type4_bruteforce.py  (카펫 + 소수 찾기)
D-1 저녁: 전 유형 해설 없이 처음부터 재풀이

[시험 풀이 전략]
--------------------------------------
1. 문제 읽기 (5분)
   - 조건 밑줄 치며 읽기
   - 입출력 예 손으로 직접 추적

2. 풀이 설계 (3분)
   - 자료구조 결정 (dict? deque? list?)
   - 시간복잡도 어림 (N 크기 확인)

3. 코딩 (20분)
   - 엣지 케이스 먼저 메모: 빈 배열, 0, 최댓값

4. 검증 (5분)
   - 주어진 예제 통과 확인
   - 엣지 케이스 수동 대입

[자주 쓰는 코드 스니펫]
--------------------------------------
# 시간 → 분 변환
h, m = map(int, "HH:MM".split(':'))
minutes = h * 60 + m

# 다중 기준 정렬
arr.sort(key=lambda x: (-x[0], x[1]))   # 1순위 내림, 2순위 오름

# 커스텀 정렬 (cmp_to_key)
from functools import cmp_to_key
arr.sort(key=cmp_to_key(lambda a, b: -1 if a+b > b+a else 1))

# Counter 활용
from collections import Counter, defaultdict
cnt = Counter(arr)          # 빈도 계산
cnt.most_common(k)          # 상위 k개

# deque
from collections import deque
dq = deque([0] * n)
dq.popleft()   # O(1)
dq.append(x)   # O(1)

# 순열/조합
from itertools import permutations, combinations
list(permutations([1,2,3], 2))  # [(1,2),(1,3),(2,1),...]
list(combinations([1,2,3], 2))  # [(1,2),(1,3),(2,3)]

# 소수 판별
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

# 재귀 깊이 제한 해제 (DFS 쓸 때)
import sys
sys.setrecursionlimit(10**6)

[실수 TOP 5]
--------------------------------------
1. dict.get(key, 0) 대신 dict[key] → KeyError
2. BFS에서 큐에 넣기 전에 visited 체크해야 함
3. 정렬 기준 내림차순: reverse=True or 음수(-)
4. 나눗셈 올림: math.ceil() or -(-a//b)
5. 리스트 슬라이싱은 새 객체: a[1:3]은 복사본
