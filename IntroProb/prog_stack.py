# 올바른 괄호
s="((()))"
def solution(s):
    stack=[]
    for i in s:
        if len(stack)==0:
            stack.append(i)
        elif stack[-1]=='(' and i == ')':
            stack.pop(-1)
        else:
            stack.append(i)
    if stack:
        return False

    return True
print(solution(s))