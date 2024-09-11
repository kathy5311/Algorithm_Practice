import sys

#ascii A:65, python ord('A')
def changer(n,B):
    total=0
    n=n[::-1]
    for i in range(len(n)):
        
        if n[i].isalpha():
            numN=ord(n[i])-55
        else:
            numN=int(n[i])

        total+=numN*(int(B)**i)
    return total

n,B = list(map(str, sys.stdin.readline().split()))

print(changer(n,B))


