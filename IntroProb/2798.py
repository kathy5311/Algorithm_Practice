from itertools import combinations
import sys

N,M = list(map(int, sys.stdin.readline().split()))

a = list(map(int, sys.stdin.readline().split()))

com=(list(combinations(a,3)))

new_list=[]
for i in com:
    total=0
    for j in range(3):
        total+=i[j]
    if total <= M:
        new_list.append(total)
new_list.sort()
print(new_list[-1])


