import sys
import math

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

#partial sum
D = [0]*(N+1)
for i in range(1,N+1):
    D[i] = D[i-1]+num[i-1]
D = D[1:]

C = [0]*M
count=0
for i in range(len(D)):
    remainder=D[i]%M
    if remainder==0:
        count+=1
    C[remainder]+=1


for i in C:
    if i>1:
        count+= math.factorial(i)//math.factorial(2)
print(count)



'''
time out
count=0
for i in range(N+1):
    a = D[i]%M
    for j in range(i+1,N+1):
        if D[j]%M == a:
            count+=1

print(count)
'''









