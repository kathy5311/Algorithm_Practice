import sys

n = int(sys.stdin.readline())


a = list(map(int, sys.stdin.readline().split()))

count=0
for i in a:
    if i ==1 or i==0: continue
    elif i==2:
        count+=1
    else:
        for j in range(2,(i+1)):
            if i==j: 
                count+=1
                break
            elif i%j==0: break
print(count)