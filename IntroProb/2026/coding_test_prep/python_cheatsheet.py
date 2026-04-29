"""
========================================
파이썬 코딩테스트 치트시트
========================================
목차:
  ★ 1. collections 모듈         ← 필수 암기
  ★ 2. 정렬 패턴                 ← 필수 암기
  ★ 3. 실수 TOP 10              ← 필수 암기
  ─────────────────────────────────────
    4. 효율적인 코드 패턴          ← BFS/DFS 템플릿 암기용
    5. 문자열 (String)            ← 문자열 문제 + 파싱 필수
    6. 리스트 (List)              ← 거의 모든 문제 사용
    7. 딕셔너리 (Dictionary)      ← 해시 문제 핵심
    8. itertools 모듈             ← 완전탐색 필수
    9. 집합 (Set)                 ← 중복 제거, O(1) 탐색
   10. 자주 쓰는 한 줄 표현       ← 편의 문법
   11. 수학 / 숫자                ← 필요할 때 참고
   12. 입출력                     ← 거의 고정 패턴
========================================
"""

# ======================================
# ★ 1. collections 모듈
# ======================================

from collections import Counter, defaultdict, deque

# ---- Counter ----
cnt = Counter([1, 2, 2, 3, 3, 3])   # Counter({3:3, 2:2, 1:1})
cnt = Counter("aabbcc")              # Counter({'a':2,'b':2,'c':2})

cnt[3]              # 3  (없으면 0 반환, KeyError 없음)
cnt.most_common(2)  # 상위 2개: [(3,3), (2,2)]
cnt.most_common()   # 전체 빈도 내림차순

# Counter 연산
c1 + c2             # 합산
c1 - c2             # 차감 (0 이하 제거)
c1 & c2             # 각 키의 min
c1 | c2             # 각 키의 max

list(cnt.elements())  # [3,3,3,2,2,1] 원소 펼치기

# ---- defaultdict ----
d = defaultdict(int)    # 없는 키 → 0
d = defaultdict(list)   # 없는 키 → []
d = defaultdict(set)    # 없는 키 → set()

d["new"] += 1           # KeyError 없이 바로 사용
d["list"].append(5)     # KeyError 없이 바로 사용

# ---- deque ----
dq = deque([1, 2, 3])
dq.append(4)            # 오른쪽 추가  O(1)
dq.appendleft(0)        # 왼쪽 추가   O(1)
dq.pop()                # 오른쪽 제거 O(1)
dq.popleft()            # 왼쪽 제거   O(1)  ← list.pop(0)은 O(N)
dq.rotate(1)            # 오른쪽으로 1칸 회전

# deque 초기화
dq = deque([0] * n)     # n개 0으로 채움
dq = deque(maxlen=k)    # 최대 k개 유지 (초과 시 반대편 자동 제거)

# ======================================
# ★ 2. 정렬 패턴
# ======================================

# 기본
arr.sort()                              # 오름차순 (제자리)
arr.sort(reverse=True)                  # 내림차순 (제자리)
sorted(arr)                             # 오름차순 (새 리스트)

# key 함수
arr.sort(key=len)                       # 길이 기준
arr.sort(key=lambda x: x[1])           # 두 번째 원소 기준
arr.sort(key=lambda x: -x[1])          # 두 번째 원소 내림차순
arr.sort(key=lambda x: (x[1], -x[0]))  # 다중 기준 (1순위 오름, 2순위 내림)

# 커스텀 비교 함수 (cmp_to_key) ← "가장 큰 수" 유형 필수
from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a: return -1     # a 앞
    elif a + b < b + a: return 1    # b 앞
    return 0

arr.sort(key=cmp_to_key(compare))

# 안정 정렬: 파이썬 sort는 기본적으로 안정 정렬 (같은 값이면 원래 순서 유지)

# ======================================
# ★ 3. 실수 TOP 10
# ======================================
"""
1. 2D 리스트 잘못된 초기화
   ❌ dp = [[0]*m]*n        → 모든 행이 같은 객체 참조
   ✓  dp = [[0]*m for _ in range(n)]

2. list.pop(0) 대신 deque.popleft()
   ❌ arr.pop(0)            → O(N)
   ✓  dq.popleft()         → O(1)

3. BFS visited 타이밍
   ❌ 꺼낼 때 visited 체크  → 중복 삽입 → TLE
   ✓  큐에 넣기 전에 visited 처리

4. dict 없는 키 접근
   ❌ d[key] += 1           → KeyError
   ✓  d[key] = d.get(key, 0) + 1
   ✓  defaultdict(int) 사용

5. 정렬 내림차순
   ❌ arr.sort(reverse=True) key와 동시 사용 시 착각
   ✓  key=lambda x: -x  (숫자인 경우)

6. 나눗셈 올림
   ❌ int(a / b) + 1       → 나머지 없을 때 1 더해지는 버그
   ✓  math.ceil(a / b)
   ✓  (a + b - 1) // b

7. 문자열 비교 vs 숫자 비교
   "10" > "9"  → False  (문자열: "1" < "9")
   10  > 9     → True   (숫자)

8. 리스트 복사
   ❌ b = a                → 같은 객체 참조
   ✓  b = a[:]             → 얕은 복사
   ✓  b = a.copy()         → 얕은 복사
   ✓  import copy; b = copy.deepcopy(a)  → 깊은 복사 (2D 이상)

9. range 범위
   range(n)      → 0 ~ n-1
   range(1, n)   → 1 ~ n-1
   range(n, 0, -1) → n ~ 1  (역방향)

10. 전역 변수 수정 (재귀/중첩 함수)
    ❌ count += 1               → UnboundLocalError
    ✓  nonlocal count; count += 1  (중첩 함수)
    ✓  global count; count += 1   (전역 함수)
    ✓  count = [0]; count[0] += 1 (리스트로 우회)
"""

# ======================================
# 4. 효율적인 코드 패턴
# ======================================

# ---- BFS 템플릿 ----
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)      # 큐에 넣기 전에 방문 표시!
                queue.append(next_node)

# 격자 BFS (상하좌우 이동)
def bfs_grid(grid, start_r, start_c):
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    queue = deque([(start_r, start_c, 0)])  # (행, 열, 거리)
    visited[start_r][start_c] = True
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] != 0:
                visited[nr][nc] = True
                queue.append((nr, nc, dist+1))

# ---- DFS 템플릿 (재귀) ----
def dfs(node, visited, graph):
    visited.add(node)
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node, visited, graph)

# ---- 투 포인터 ----
def two_sum(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1
    return False

# ---- 슬라이딩 윈도우 ----
def max_sum_window(arr, k):
    window = sum(arr[:k])
    result = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        result = max(result, window)
    return result

# ---- 누적 합 (Prefix Sum) ----
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i, v in enumerate(arr):
        prefix[i+1] = prefix[i] + v
    return prefix

# 구간 합: prefix[r+1] - prefix[l]

# ---- 우선순위 큐 (heapq) ----
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappop(heap)             # 최솟값 꺼내기

heapq.heappush(heap, -5)        # 최댓값 큐: 음수로 저장
-heapq.heappop(heap)            # 꺼낼 때 다시 음수로

heapq.heapify(arr)              # 리스트 → 힙 변환 O(N)
heapq.heappush(heap, (priority, value))  # (우선순위, 값) 쌍

# ---- 이진 탐색 ----
from bisect import bisect_left, bisect_right

arr = [1, 2, 3, 3, 5]
bisect_left(arr, 3)             # 2  (3이 들어갈 왼쪽 위치)
bisect_right(arr, 3)            # 4  (3이 들어갈 오른쪽 위치)
bisect_right(arr, 3) - bisect_left(arr, 3)  # 3의 개수: 2

# ======================================
# 5. 문자열 (String)
# ======================================

s = "Hello, World!"

# 기본 조작
s.upper()               # 대문자
s.lower()               # 소문자
s.strip()               # 양쪽 공백 제거
s.lstrip()              # 왼쪽 공백 제거
s.rstrip()              # 오른쪽 공백 제거
s.replace("l", "r")     # 치환
s.split()               # 공백 기준 분리 → 리스트
s.split(",")            # 쉼표 기준 분리
",".join(["a","b","c"]) # 리스트 → 문자열: "a,b,c"
"".join(["a","b","c"])  # 리스트 → 문자열: "abc"

# 탐색
s.find("o")             # 첫 번째 "o" 인덱스 (없으면 -1)
s.index("o")            # 첫 번째 "o" 인덱스 (없으면 ValueError)
s.count("l")            # "l" 개수
s.startswith("He")      # True/False
s.endswith("!")         # True/False

# 판별
s.isdigit()             # 모두 숫자?
s.isalpha()             # 모두 알파벳?
s.isalnum()             # 모두 알파벳+숫자?

# 포맷
f"Hello {name}"         # f-string (권장)
"Hello {}".format(name) # format

# 문자 ↔ 숫자
ord('A')                # 65  (문자 → ASCII)
chr(65)                 # 'A' (ASCII → 문자)
ord('a') - ord('a')     # 0  (a=0, b=1, ... z=25)

# 문자열은 불변 → 수정 시 리스트로 변환
s = list("hello")
s[0] = 'H'
s = "".join(s)          # 다시 문자열로

# ======================================
# 6. 리스트 (List)
# ======================================

arr = [1, 2, 3, 4, 5]

# 기본 조작
arr.append(6)           # 끝에 추가
arr.insert(0, 0)        # 인덱스 0에 삽입
arr.pop()               # 끝 제거 & 반환
arr.pop(0)              # 인덱스 0 제거 & 반환 ← O(N), 느림
arr.remove(3)           # 값 3 첫 번째 제거
arr.index(2)            # 값 2의 인덱스 반환
arr.count(2)            # 값 2의 개수
arr.reverse()           # 제자리 뒤집기
arr[::-1]               # 뒤집은 새 리스트

# 슬라이싱
arr[1:4]                # 인덱스 1~3
arr[:3]                 # 처음~2
arr[2:]                 # 2~끝
arr[::2]                # 짝수 인덱스만
arr[::-1]               # 전체 뒤집기

# 리스트 생성
zeros = [0] * 5                          # [0, 0, 0, 0, 0]
matrix = [[0]*m for _ in range(n)]       # n×m 2차원 배열
                                         # ❌ [[0]*m]*n 은 같은 행 참조!

# 자주 쓰는 함수
len(arr)                # 길이
sum(arr)                # 합계
max(arr)                # 최댓값
min(arr)                # 최솟값
sorted(arr)             # 정렬된 새 리스트 (원본 유지)
arr.sort()              # 제자리 정렬 (원본 변경)

# 리스트 합치기
a + b                   # 두 리스트 연결
a.extend(b)             # a에 b를 이어붙임 (제자리)

# 특정 값 존재 여부
3 in arr                # True/False  ← O(N)
3 not in arr

# 최댓값/최솟값 인덱스
arr.index(max(arr))
arr.index(min(arr))

# ======================================
# 7. 딕셔너리 (Dictionary)
# ======================================

d = {}
d = {"a": 1, "b": 2}

# 기본 조작
d["c"] = 3              # 추가/수정
d.get("x", 0)           # 없으면 0 반환 (KeyError 없음)
d.pop("a")              # 꺼내면서 삭제
"a" in d                # 키 존재 여부
del d["b"]              # 삭제

# 순회
for k in d:             # 키만
for k, v in d.items():  # 키, 값
for v in d.values():    # 값만
for k in d.keys():      # 키만

# 빈도 계산 패턴
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

# 정렬
sorted(d.items(), key=lambda x: x[1])           # 값 기준 오름차순
sorted(d.items(), key=lambda x: -x[1])          # 값 기준 내림차순
sorted(d.items(), key=lambda x: (-x[1], x[0]))  # 값 내림, 키 오름

# ======================================
# 8. itertools 모듈
# ======================================

from itertools import permutations, combinations, combinations_with_replacement, product

arr = [1, 2, 3]

# 순열 (순서 있음)
list(permutations(arr, 2))
# [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# 조합 (순서 없음)
list(combinations(arr, 2))
# [(1,2),(1,3),(2,3)]

# 중복 조합
list(combinations_with_replacement(arr, 2))
# [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]

# 곱집합 (카테시안 곱)
list(product([0,1], repeat=3))
# 000, 001, 010, ... 111  ← 비트마스크 대신 쓰기 좋음

list(product(arr, [4, 5]))
# [(1,4),(1,5),(2,4),(2,5),(3,4),(3,5)]

# ======================================
# 9. 집합 (Set)
# ======================================

s = {1, 2, 3}
s = set([1, 2, 3])      # 리스트 → 집합 (중복 제거)
s = set()               # 빈 집합 ({} 는 dict!)

s.add(4)                # 추가
s.remove(3)             # 삭제 (없으면 KeyError)
s.discard(3)            # 삭제 (없어도 에러 없음)
3 in s                  # 존재 여부 O(1)

# 집합 연산
a | b                   # 합집합
a & b                   # 교집합
a - b                   # 차집합 (a에만 있는 것)
a ^ b                   # 대칭 차집합 (한쪽에만 있는 것)

# ======================================
# 10. 자주 쓰는 한 줄 표현
# ======================================

# 리스트 컴프리헨션
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
flat    = [x for row in matrix for x in row]     # 2D → 1D 평탄화

# 딕셔너리 컴프리헨션
d = {k: v for k, v in zip(keys, values)}
freq = {x: arr.count(x) for x in set(arr)}

# 집합 컴프리헨션
unique_squares = {x**2 for x in arr}

# 조건부 표현식 (삼항 연산자)
result = a if condition else b

# enumerate: 인덱스 + 값
for i, v in enumerate(arr):
    pass
for i, v in enumerate(arr, start=1):   # 1부터 시작
    pass

# zip: 두 리스트 동시 순회
for a, b in zip(arr1, arr2):
    pass

# any / all
any(x > 0 for x in arr)    # 하나라도 양수면 True
all(x > 0 for x in arr)    # 모두 양수면 True

# 최댓값/최솟값 + 조건
max(arr, key=lambda x: abs(x))          # 절댓값 기준 최대
min(enumerate(arr), key=lambda x: x[1]) # (인덱스, 최솟값)

# 두 변수 swap
a, b = b, a

# 문자열 → 정수 리스트
digits = list(map(int, str(n)))          # 1234 → [1,2,3,4]
n = int("".join(map(str, digits)))       # [1,2,3,4] → 1234

# 리스트 중복 제거 (순서 유지)
seen = set()
result = [x for x in arr if not (x in seen or seen.add(x))]

# 리스트 평탄화
import itertools
flat = list(itertools.chain.from_iterable(matrix))

# ======================================
# 11. 수학 / 숫자
# ======================================

import math

math.ceil(2.3)          # 3  (올림)
math.floor(2.7)         # 2  (내림)
math.sqrt(16)           # 4.0 (제곱근)
math.gcd(12, 8)         # 4  (최대공약수)
math.lcm(4, 6)          # 12 (최소공배수, Python 3.9+)
math.inf                # 무한대
math.log(8, 2)          # 3.0 (log₂8)

# 나눗셈
7 // 2                  # 3  (몫, 내림)
7 % 2                   # 1  (나머지)
divmod(7, 2)            # (3, 1) (몫, 나머지 동시에)

# 올림 나눗셈
math.ceil(7 / 2)        # 4
-(-7 // 2)              # 4  (음수 이용 트릭)

# 거듭제곱
2 ** 10                 # 1024
pow(2, 10, 1000)        # 2^10 % 1000 (모듈러 거듭제곱, 빠름)

# 절댓값
abs(-5)                 # 5

# 무한대 표현
INF = float('inf')
INF = 10**9             # 정수 무한대 (비교 목적)

# 소수 판별
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# 에라토스테네스의 체 (범위 내 소수 전체)
def sieve(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            for j in range(i*i, n+1, i):
                is_p[j] = False
    return [i for i in range(2, n+1) if is_p[i]]

# ======================================
# 12. 입출력
# ======================================

# 기본 입력
n = int(input())
a, b = map(int, input().split())
arr = list(map(int, input().split()))

# 여러 줄 입력 받기
import sys
input = sys.stdin.readline   # input()보다 빠름 (대량 입력 시 필수)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 재귀 깊이 제한 해제 (DFS 재귀 쓸 때)
sys.setrecursionlimit(10**6)
