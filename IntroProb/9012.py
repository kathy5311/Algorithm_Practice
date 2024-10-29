import sys

N = int(sys.stdin.readline())


for _ in range(N):
    check = input()
    stack = []
    for i in check:
        if i =='(':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

    if len(stack)==0:
        print('Yes')
    else:
        print('No')