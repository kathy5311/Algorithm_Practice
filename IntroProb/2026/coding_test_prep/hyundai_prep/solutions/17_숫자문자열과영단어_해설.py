'''
[해설] 숫자 문자열과 영단어
========================================
핵심 아이디어:
  영단어 목록을 순서대로 정의하고
  str.replace(word, str(i))를 반복 적용
  → 모두 치환된 문자열을 int()로 변환
'''

def solution(s):
    words = ["zero","one","two","three","four",
             "five","six","seven","eight","nine"]
    for i, word in enumerate(words):
        s = s.replace(word, str(i))
    return int(s)

'''
========================================
포인트 정리
========================================
1. str.replace(old, new): 모든 출현을 new로 치환
   → 원본 문자열 변경 없이 새 문자열 반환
   → s = s.replace(...)로 재할당 필요

2. enumerate(words): (인덱스, 단어) → 인덱스가 곧 숫자값

3. 순서 상관없음: 각 단어가 겹치지 않으므로 어떤 순서든 동일

한 줄 버전:
  from functools import reduce
  words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
  return int(reduce(lambda s, t: s.replace(t[1], str(t[0])), enumerate(words), s))

re.sub 버전:
  import re
  table = {"zero":"0","one":"1",...}
  return int(re.sub('|'.join(table), lambda m: table[m.group()], s))
'''

# 테스트
print(solution("one4seveneight"))   # 1478
print(solution("23four5six7"))      # 234567
print(solution("2three45sixseven")) # 234567
print(solution("123"))              # 123
