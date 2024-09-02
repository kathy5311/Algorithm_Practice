import sys

n = int(sys.stdin.readline())

for _ in range(n):
    S=''
    a,b = (sys.stdin.readline().split(" "))

    for i in range(len(b)):
        S+=(b[i]*int(a))
    
    print(S.strip("\n"))