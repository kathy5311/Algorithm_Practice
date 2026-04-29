'''
[유형] 문자열 처리
[난이도] 프로그래머스 Lv.1
[문제] 신규 아이디 추천
========================================

카카오 서비스 아이디 규칙에 맞도록 new_id를 변환해 반환하세요.

[7단계 변환 규칙]
  1단계: 대문자 → 소문자
  2단계: 알파벳, 숫자, -, _, . 을 제외한 문자 제거
  3단계: 연속된 마침표(..) → 마침표 하나(.)
  4단계: 앞뒤 마침표 제거
  5단계: 빈 문자열이면 "a"
  6단계: 길이 16 이상이면 앞 15자로 자르고, 끝이 .이면 제거
  7단계: 길이 2 이하이면 마지막 문자를 길이 3이 될 때까지 반복

[입출력 예]
new_id = "...!@BaT#*..y.abcdefghijklm"  → "bat.y.abcdefghi"
new_id = "z-+.^."                        → "z--"
new_id = "=.="                           → "aaa"
new_id = "123_.def"                      → "123_.def"
new_id = "abcdefghijklmn.p"             → "abcdefghijklmn"
'''

def solution(new_id):
    pass


# 테스트
print(solution("...!@BaT#*..y.abcdefghijklm"))  # "bat.y.abcdefghi"
print(solution("z-+.^."))                        # "z--"
print(solution("=.="))                           # "aaa"
print(solution("123_.def"))                      # "123_.def"
print(solution("abcdefghijklmn.p"))             # "abcdefghijklmn"
