import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

count=0
for k in range(N):
    find = num[k]
    s=0
    e=N-1
    while s<e:

        if num[s]+num[e] == find:
            if s != k and e != k:
                count+=1
                break
            elif s == k:
                s+=1
            elif e==k:
                e-=1
        elif num[s]+num[e] > find:
            e-=1
        else:
            s+=1
print(count)