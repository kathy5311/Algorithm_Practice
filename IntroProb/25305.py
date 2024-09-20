import sys

N, C = list(map(int, sys.stdin.readline().split()))

a = list(map(int, sys.stdin.readline().split()))

a.sort()
a.reverse()
print(a[C-1])