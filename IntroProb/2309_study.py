import sys
from itertools import combinations
N = [int(sys.stdin.readline()) for _ in range(9)]
''' 1. combination 이용
comb = list(combinations(N,7))

checking=[]
for i in comb:
    if sum(i)==100:
        checking=list(i)
        break

checking.sort()
for i in checking:
    print(i)'''
N.sort()
sumN = sum(N)
for i in range(len(N)):
    for j in range(i+1,len(N)):
        
        if sumN-N[i]-N[j]==100:
            for k in range(len(N)):
                if k==i or k==j:
                    pass
                else:
                    print(N[k])
            exit()






