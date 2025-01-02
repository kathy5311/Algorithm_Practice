import sys

N = int(sys.stdin.readline())

s=1
e=1
count=1
sum=1
while e!=N:
    
    if sum == N:
        count+=1
        e+=1
        sum+=e

    elif sum <N:
        e+=1
        sum+=e

    elif sum > N:
        sum-=s
        s +=1

print(count)
