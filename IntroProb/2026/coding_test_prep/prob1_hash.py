'''
========================================
[유형 1] 해시 (Hash / Dictionary)
========================================
빈출 이유: 탐색 O(1), 중복 제거, 빈도 계산에 필수
핵심 패턴: collections.Counter, dict.get(), set 연산

----------------------------------------
[문제] 전화번호 목록 (프로그래머스 Lv.2)
----------------------------------------
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하세요.

예: ["119", "97674223", "1195524421"]
  → "119"가 "1195524421"의 접두어이므로 False 반환

제약: 전화번호 개수 1 ≤ N ≤ 1,000,000

입출력 예:
phone_book              | return
["119","97674223","1195524421"] | False
["123","456","789"]     | True
["12","123","1235","567","88"]  | False

----------------------------------------
[내 풀이 시도 공간]
----------------------------------------
def solution(phone_book):
    pass

----------------------------------------
[해설 & 정답]
----------------------------------------
핵심 아이디어:
  정렬 후 인접한 번호만 비교 → O(N log N)
  또는 해시셋으로 모든 접두어를 O(N*L)에 검사

방법 1: 정렬 이용 (추천 - 간결)
  - 정렬하면 접두어 관계인 번호는 반드시 인접
  - ex) ["119", "1195524421", "97674223"] 정렬 후
    → "119"와 "1195524421" 인접, startswith로 체크
'''

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

'''
방법 2: 해시셋 이용
  - 모든 번호를 set에 저장
  - 각 번호의 부분 문자열이 set에 있으면 False

def solution(phone_book):
    phone_set = set(phone_book)
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in phone_set:
                return False
    return True

시간복잡도: O(N * L)  (L = 최대 번호 길이)

========================================
핵심 정리
========================================
1. 정렬 후 인접 비교 → 접두어/접미어 문제의 왕도
2. set/dict 조회는 O(1) → 빈도·존재 여부 체크에 필수
3. startswith(prefix) / endswith(suffix) 꼭 기억

자주 쓰는 해시 패턴:
  from collections import Counter
  cnt = Counter(arr)          # {값: 개수}
  cnt.most_common(k)          # 상위 k개
  cnt[key]                    # 없으면 0 반환 (KeyError 없음)
'''

# 테스트
print(solution(["119", "97674223", "1195524421"]))  # False
print(solution(["123", "456", "789"]))              # True
print(solution(["12", "123", "1235", "567", "88"])) # False
