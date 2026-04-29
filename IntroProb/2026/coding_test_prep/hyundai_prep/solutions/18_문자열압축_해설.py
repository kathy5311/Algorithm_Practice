'''
[해설] 문자열 압축
========================================
핵심 아이디어:
  압축 단위 1 ~ len(s)//2 를 완전탐색
  각 단위로 잘라 연속 반복 횟수 세어 압축 문자열 생성
  최소 길이 반환

  단위 unit으로 자를 때:
    prev = s[:unit]  (이전 조각)
    count = 1
    unit 간격으로 순회하며 prev와 같으면 count++, 다르면 압축 후 갱신
'''

def solution(s):
    if len(s) == 1:
        return 1

    min_len = len(s)   # 압축 안 하는 경우

    for unit in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:unit]
        count = 1

        for i in range(unit, len(s), unit):
            chunk = s[i:i + unit]
            if chunk == prev:
                count += 1
            else:
                compressed += (str(count) if count > 1 else '') + prev
                prev = chunk
                count = 1

        compressed += (str(count) if count > 1 else '') + prev   # 마지막 조각
        min_len = min(min_len, len(compressed))

    return min_len

'''
========================================
포인트 정리
========================================
1. 탐색 범위: range(1, len(s)//2 + 1)
   - 단위가 len(s)//2 초과면 반복 불가 → 의미 없음
   - 단위 = len(s)이면 압축 불가 → 원본 길이

2. 마지막 조각 처리 필수 (for문 종료 후 마지막 prev 남음)

3. count > 1 일 때만 숫자 붙임
   count=1이면 숫자 생략: "1abc" → "abc"

4. len(compressed)만 비교하므로 실제 문자열 생성 불필요
   → 최적화: 길이만 추적하면 되지만 가독성상 문자열로

잘못된 접근:
  ❌ unit = len(s)까지 탐색 → 불필요
  ❌ 마지막 조각 누락 → 오답
  ❌ count=1일 때 "1" 붙임 → 길이가 오히려 늘어나는 버그
'''

# 테스트
print(solution("aabbaccc"))         # 7
print(solution("ababcdcdababcdcd")) # 9
print(solution("xyzxyzxyzxyz"))    # 4
print(solution("a"))               # 1
print(solution("aaaaaaaaaa"))      # 2
