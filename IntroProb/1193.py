import sys

n = int(sys.stdin.readline())

idx=1
i=0
while 1:
    idx+=i
    i+=1
    idx_next=idx+i

    if idx <= n < idx_next:
        break

#print(i)
#print(idx)
real_idx= n-idx
#print(real_idx)
if i %2 ==0:
    for k in range(0,real_idx+1):
        fraction = str(k+1)+'/'+str(i-k)
    print(fraction)
else:
    for k in range(0,real_idx+1):
        fraction = str(i-k)+'/'+str(k+1)
    print(fraction)
