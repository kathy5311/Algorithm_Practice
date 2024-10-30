import sys

while True:
    N = (input())

    if N=='.':
        break

    stack =[]
    for checker in N:
    
        if checker == '(' or checker == '[':
            stack.append(checker)
        elif checker == ')' or checker == ']':
            if stack:
                if  checker == ')' and stack[-1]=='(':
                    stack.pop()
                elif checker == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(checker)
                    break
            else:
                stack.append(checker)

    if stack:
        print('no')
    else:
        print('yes')
