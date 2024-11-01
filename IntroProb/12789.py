import sys

N = input()
line = list(map(int, sys.stdin.readline().split()))

stack =[]
now_turn = min(line)
for value in line:
    stack.append(value)
    while stack and stack[-1] == now_turn:
        stack.pop()
        now_turn+=1

if stack:
    print("Sad")
else:
    print("Nice")

    
