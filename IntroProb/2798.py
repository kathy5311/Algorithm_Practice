#브루트포스 공부
import sys

N, M = list(map(int, sys.stdin.readline().split()))


a = list(map(int, sys.stdin.readline().split()))

a.sort()
a.reverse()
print(a)
new_list=[]
for i in range(N):
    total=0
    if i == len(a)-2:
        break
    for j in range(i,i+2):
        for k in range(j,len(a)):
            total+=a[j]
    print(total)
    if total <= M:
        new_list.append(total)

print(new_list)
