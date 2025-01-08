import sys
from itertools import combinations_with_replacement
N = int(sys.stdin.readline())

T = [i*(i+1)//2 for i in range(1, 45)]
replacecomb = list(combinations_with_replacement(T,3))

for _ in range(N):
    K = int(sys.stdin.readline())

    
    for i in range(len(replacecomb)):
        if i!=(len(replacecomb)-1) and K == sum(replacecomb[i]):
            print(1)
            break
        elif i == len(replacecomb)-1:
            print(0)
            break
