'''
[유형] 문자열 처리
[난이도] 프로그래머스 Lv.1
[문제] 숫자 문자열과 영단어
========================================

숫자와 영단어가 섞인 문자열 s를 숫자로만 이루어진 문자열로 바꿔 정수로 반환하세요.

[영단어 → 숫자 매핑]
  zero=0, one=1, two=2, three=3, four=4
  five=5, six=6, seven=7, eight=8, nine=9

[입출력 예]
s = "one4seveneight"  → 1478
s = "23four5six7"     → 234567
s = "2three45sixseven" → 234567
s = "123"             → 123
'''

def solution(s):
    pass


# 테스트
print(solution("one4seveneight"))   # 1478
print(solution("23four5six7"))      # 234567
print(solution("2three45sixseven")) # 234567
print(solution("123"))              # 123
