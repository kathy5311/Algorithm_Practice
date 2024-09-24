import sys

N = int(sys.stdin.readline())

a_list=[]
for _ in range(N):
    a= list(map(int, sys.stdin.readline().split()))
    a_list.append(a)

a_list.sort()
for i in a_list:
    a,b = i
    print(a,b)