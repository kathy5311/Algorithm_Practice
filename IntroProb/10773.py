import sys

N = int(sys.stdin.readline())
stack=[]
for _ in range(N):
    c = int(sys.stdin.readline())
    if c == 0:
        stack.pop(-1)
    else:
        stack.append(c)
    
print(sum(stack))
