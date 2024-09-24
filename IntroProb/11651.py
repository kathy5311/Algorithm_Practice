import sys

N = int(sys.stdin.readline())

a_list=[]
for _ in range(N):
    a= list(map(int, sys.stdin.readline().split()))
    a=list(reversed(a))
    a_list.append(a)

a_list.sort()
new_list=[]
for i in a_list:
    i=list(reversed(i))
    new_list.append(i)

for i in new_list:
    a,b = i
    print(a,b)