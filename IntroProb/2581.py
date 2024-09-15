import sys

m = int(sys.stdin.readline())
M = int(sys.stdin.readline())

new_list = [i for i in range(m,M+1)]

so_list=[]
for i in new_list:
    for j in range(2,i+1):
        if i==j:
            so_list.append(i)
        elif i%j==0: break
total=0

if len(so_list)==0:
    print(-1)
else:
    for i in so_list:
        total+=i
    print(total)
    print(so_list[0])