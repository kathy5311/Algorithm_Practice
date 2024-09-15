import sys

def yak(a,b):
    yak_list=[]
    for i in range(1,(a)+1):
        if a%i==0:
            yak_list.append(i)
    if len(yak_list) < b:
        return 0
   
    return yak_list[b-1]

a, b = list(map(int, sys.stdin.readline().split()))
print(yak(a,b))