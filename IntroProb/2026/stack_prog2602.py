#2026
def solution(s):
    stack=[]
    for i in s:
        stack.append(i)
    tmp=[stack.pop(-1)] #[)]

    while stack:
        curr = stack.pop()
        if tmp:
            if curr == "(" and tmp[0]==")":
                tmp.pop()
            else:
                tmp.append(curr)
        else:
            tmp.append(curr)
        
    if tmp:
        return False
    else:
        return True