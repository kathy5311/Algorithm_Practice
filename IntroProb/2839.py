import sys

N =int(sys.stdin.readline())

num_bag=[]
# 5kg로만 구성

if N%5==0:
    num_bag.append(N//5)
if N%3==0:
    num_bag.append(N//3)

count=0
while 1:
    N=N-5
    count+=1
    if N <0:
        break
    if N % 3 == 0:
        num_bag.append(count+(N//3))

if len(num_bag)==0:
    print(-1)      
else:
    print(min(num_bag))