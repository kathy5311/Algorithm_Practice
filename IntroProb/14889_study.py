import sys
from itertools import combinations

N = int(sys.stdin.readline())

#combination list
comb = list(combinations([i for i in range(1,N+1)], N//2))

#power list
power = [list(map(int,(sys.stdin.readline().split()))) for _ in range(N)]

result=[]
i=0
j=len(comb)-1
while i<j:
    sum_1=0
    for n,m in combinations(list(comb[i]),2):
        sum_1 += power[n-1][m-1]+power[m-1][n-1]
    
    sum_2=0
    for n,m in combinations(list(comb[j]),2):
        sum_2 += power[n-1][m-1] + power[m-1][n-1]
    
    result.append(abs(sum_1-sum_2))

    i+=1
    j-=1

print(min(result))
