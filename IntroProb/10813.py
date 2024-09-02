#리스트 크기 정해주기
#다시 해보기
import sys
n,m = map(int,sys.stdin.readline().split())
a=[i for i in range(1,n+1)]
'''
copy_a=a[:]
for j in range(m):
    b,c = map(int,sys.stdin.readline().split())
    a[b-1]=copy_a[c-1]
    a[c-1]=copy_a[b-1]
    copy_a=a[:]
    #print(copy_a) 
for i in a:
    print(i, end=' ')'''
'''
a,b,c,d,e = [i for i in a]
print(a,b,c,d,e)
'''
'---------Another Solution-------'
for j in range(m):
    b,c = list(map(int, sys.stdin.readline().split()))
    temp = a[b]
    a[b] = a[c]
    a[c] = temp

print(a)