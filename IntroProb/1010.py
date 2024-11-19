import sys
import math

N = int(sys.stdin.readline())

for _ in range(N):
    J,M = list(map(int, sys.stdin.readline().split()))

    a=1
    for i in range(J):
        a*=(M-i)
    a=a/(math.factorial(J))

    print(int(a))

