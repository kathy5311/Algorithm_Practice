import sys

N = int(sys.stdin.readline())
list_tp=[[0,0]]
#list_tp[0]=T, list_tp[1]=P
for _ in range(N):
    list_tp.append(list(map(int,sys.stdin.readline().split())))
dp=[0 for _ in range(N+1)]

for i in range(1,N+1):
    dp[i] = max(dp[i-1], dp[i])
    fin_date = i+list_tp[i][0]-1
    if fin_date <=N:
        dp[fin_date] = max(dp[fin_date],dp[i-1]+list_tp[i][1])
print(dp[-1])

