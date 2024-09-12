import sys

A, B, V = list(map(int, sys.stdin.readline().split()))

n=(V-A)/(A-B)
if (V-A)%(A-B)!=0:
    n=int(n)+1
print(int(n+1))