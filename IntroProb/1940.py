import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
s=0
e=N-1
print(num)
count=0
while s<e:
    sum = int(num[s])+int(num[e])

    if sum < M:
        s+=1
    elif sum ==M:
        count+=1
        s+=1
    elif sum > M:
        e-=1

print(count)


'''
num.sort(reverse=True)
s=0
e=1
count=0

while True:
    sum = num[s]+num[e]

    if sum > M:
        e+=1
    elif sum == M:
        count+=1
        s+=1
        e=s+1
    else:
        break
print(count)
# 1 2 3 4 5 7'''
    

