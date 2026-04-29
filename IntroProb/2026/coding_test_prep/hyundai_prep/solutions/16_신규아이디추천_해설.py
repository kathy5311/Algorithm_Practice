'''
[해설] 신규 아이디 추천
========================================
핵심 아이디어:
  7단계를 순서대로 그대로 구현
  re 모듈로 정규식 활용 → 코드를 짧게

  정규식 필수:
    [^a-z0-9\-_.] : 허용되지 않는 문자
    \.{2,}         : 연속된 마침표 2개 이상
'''

import re

def solution(new_id):
    s = new_id.lower()                        # 1단계: 소문자 변환
    s = re.sub(r'[^a-z0-9\-_.]', '', s)      # 2단계: 허용 외 문자 제거
    s = re.sub(r'\.{2,}', '.', s)            # 3단계: 연속 마침표 → 하나
    s = s.strip('.')                          # 4단계: 앞뒤 마침표 제거
    if not s:
        s = 'a'                               # 5단계: 빈 문자열 → "a"
    if len(s) > 15:
        s = s[:15].rstrip('.')               # 6단계: 15자 초과 → 자르고 끝 . 제거
    while len(s) < 3:
        s += s[-1]                            # 7단계: 3자 미만 → 마지막 문자 반복
    return s

'''
========================================
포인트 정리
========================================
정규식 기본:
  re.sub(pattern, replace, string): 패턴에 맞는 부분 치환
  [^abc]: a, b, c 제외한 모든 문자
  {2,}: 2개 이상 반복
  \.: 마침표 (그냥 .은 임의의 문자)

각 단계 대응 코드:
  1단계: .lower()
  2단계: re.sub(r'[^a-z0-9\-_.]', '', s)
  3단계: re.sub(r'\.{2,}', '.', s)
  4단계: .strip('.')
  5단계: if not s
  6단계: s[:15].rstrip('.')
  7단계: while len(s) < 3: s += s[-1]

정규식 없이 2단계 구현:
  allowed = set('abcdefghijklmnopqrstuvwxyz0123456789-_.')
  s = ''.join(c for c in s if c in allowed)

6단계에서 rstrip('.') 중요:
  "abcde." → 15자 자르면 마지막이 . 일 수 있음 → 제거
'''

# 테스트
print(solution("...!@BaT#*..y.abcdefghijklm"))  # "bat.y.abcdefghi"
print(solution("z-+.^."))                        # "z--"
print(solution("=.="))                           # "aaa"
print(solution("123_.def"))                      # "123_.def"
print(solution("abcdefghijklmn.p"))             # "abcdefghijklmn"
