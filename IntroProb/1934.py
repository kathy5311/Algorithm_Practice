import sys

N = int(sys.stdin.readline())

def min(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    
    if a>=b:
        return min(a%b,b)
    elif a<b:
        return min(a,b%a)

total=[]
for _ in range(N):
    a,b = list(map(int, sys.stdin.readline().split()))
    k=min(a,b)
    total.append(k*(a//k)*(b//k))

for i in total:
    print(i)