'''
[해설] 올바른 괄호
========================================
핵심 아이디어:
  '('를 스택에 push
  ')'를 만나면:
    - 스택이 비어있으면 → 닫을 짝이 없음 → False
    - 스택에 있으면 → pop (짝 맞춤)
  끝까지 순회 후 스택이 비어있으면 True, 아니면 False
'''

def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

'''
========================================
최적화: 카운터 방식 (스택 없이)
========================================
저장할 게 '('뿐이므로 개수만 세도 됨 → 메모리 O(1)
'''

def solution_v2(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        else:
            count -= 1
            if count < 0:   # 닫는 게 여는 것보다 많아짐
                return False
    return count == 0

'''
========================================
포인트 정리
========================================
1. return len(stack) == 0: 마지막 체크 절대 빠뜨리지 말 것
   "((" → 스택에 2개 남음 → False 반환해야 함

2. if not stack: return False
   → ")(" 케이스: 첫 문자가 ')' → 스택 비어있음 → 즉시 False

3. 두 조건 모두 필요:
   ① ')'인데 스택 비어있음 → 즉시 False
   ② 끝까지 갔는데 스택 비어있지 않음 → False

카운터 vs 스택:
  괄호 종류가 1가지일 때 → 카운터로 충분
  괄호 종류가 여러 가지({}, [], ()) → 스택 필수
'''

# 테스트
print(solution("()()"))    # True
print(solution("(())()"))  # True
print(solution(")()("))    # False
print(solution("(()"))     # False
