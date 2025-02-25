import sys

N,S,M= map(int,(sys.stdin.readline().split()))
vol = list(map(int, sys.stdin.readline().split()))
dp=[[-1] for _ in range(N+1)]
dp[0].append(S)
for i in range(1,len(vol)+1):
    for j in range(1,len(dp[i-1])):
        if 0<=vol[i-1]+dp[i-1][j]<=M:
            if vol[i-1]+dp[i-1][j] not in dp[i]:
                dp[i].append(vol[i-1]+dp[i-1][j])
        
        if 0<=-vol[i-1]+dp[i-1][j]<=M:
            if -vol[i-1]+dp[i-1][j] not in dp[i]:
                dp[i].append(-vol[i-1]+dp[i-1][j])
    
    if len(dp[i])==1 and dp[i][0]==-1:
        print(-1)
        exit()
  
print(max(dp[-1]))
#print(dp)
    
     





