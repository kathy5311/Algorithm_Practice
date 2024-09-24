import sys

N = int(sys.stdin.readline())

arr = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

sort_list=[]
for age in range(1,201):
    for i in arr:
        if int(i[0])==age:
            sort_list.append(i)
    


for i in sort_list:
    a,b=i
    print(a,b)