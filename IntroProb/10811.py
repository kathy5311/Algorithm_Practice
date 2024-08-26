import sys

n,m = (map(int, sys.stdin.readline().split()))

a=[i for i in range(1,n+1)]
copy_a = a[:]
for _ in range(m):
    b,c = (map(int, sys.stdin.readline().split()))
    copy_a.reverse()
    a[b-1:c]=copy_a[b-1:c]
    copy_a=a[:]

for i in a:
    print(i, end=' ')
