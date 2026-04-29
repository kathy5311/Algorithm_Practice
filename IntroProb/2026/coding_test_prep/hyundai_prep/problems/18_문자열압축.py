'''
[유형] 문자열 처리
[난이도] 프로그래머스 Lv.2
[문제] 문자열 압축
========================================

문자열을 앞에서부터 일정 단위로 잘라 반복 횟수를 붙여 압축할 때
가장 짧은 압축 결과의 길이를 반환하세요.

[압축 규칙]
  - 1개 이상 단위로 잘라 같은 값이 연속되면 "횟수+단위"로 표현
  - 1회 반복이면 횟수 생략
  - 마지막 단위가 짧아도 그대로 사용

[입출력 예]
s = "aabbaccc"       → 7
  단위 1: "2a2ba3c"  = 7글자
  단위 2: "2aab2ac"  ... 등
  → 최솟값 7

s = "ababcdcdababcdcd" → 9
  단위 8: "2ababcdcd" = 9글자 → 최솟값

s = "xyzxyzxyzxyz" → 8
  단위 3: "4xyz"     = 4글자... wait
  → 4xyz = 4글자? No "4" + "xyz" = 4글자
  → 4글자... let me recalculate
  단위 3: xyzxyzxyzxyz → 4xyz → "4xyz" = 4글자

s = "a"              → 1
s = "aaaaaaaaaa"     → 2  (단위 5: "2aaaaa")
'''

def solution(s):
    pass


# 테스트
print(solution("aabbaccc"))         # 7
print(solution("ababcdcdababcdcd")) # 9
print(solution("xyzxyzxyzxyz"))    # 4
print(solution("a"))               # 1
print(solution("aaaaaaaaaa"))      # 2
