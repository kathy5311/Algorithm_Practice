import sys

A,B = map(int,sys.stdin.readline().split())

total = 18*17/2
ans=0

if A==B:
    ans = total-(10-A)

else:
    mypoint = (A+B)%10

    for i in range(1,11):
        for j in range(i+1,11):
            if mypoint > (i+j)%10:
                if i==A and j==B:
                    continue
                elif i==A or i==B or j==A or j==B:
                    ans+=2
                else:
                    ans+=4
print('%.3f'% (ans/total))
