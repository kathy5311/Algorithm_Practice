import sys

n,m = (map(int, sys.stdin.readline().split()))

a=[i for i in range(1,n+1)]
for _ in range(m):
    
    b,c = (map(int, sys.stdin.readline().split()))
    
    temp=a[b-1:c]
    temp.reverse()
    for i in range(0,c-b+1):
        a[b-1+i] = temp[i]

for i in a:
    print(i, end=' ')
