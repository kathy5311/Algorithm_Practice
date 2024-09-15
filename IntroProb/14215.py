import sys

a = list(map(int, sys.stdin.readline().split()))

total=0
for i in a:
    total+=i

if total-max(a) <= max(a):
    k=max(a)
    a.remove(max(a))
    max_k=total-k-1
    a.append(max_k)

new_total=0
for i in a:
    new_total+=i
print(new_total)