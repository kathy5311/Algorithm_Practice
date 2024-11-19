import sys
import math

N = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

b=1
if len(a)%2!=0:
    a.append(a[len(a)//2])
for i in a:
    b*=i
print(round(math.pow(b,1/(len(a)//2))))