import sys
'''
N = int(sys.stdin.readline())
list_T=[]
list_P=[]
for _ in range(N):
    T,P = map(int,(sys.stdin.readline().split()))
    list_T.append(T)
    list_P.append(P)

profit =[]
for i in range(N):

    T=i
    P=0
    while T < N:
        if T == N-1 and list_T[T]==1:
            P += list_P[T]
        elif T!=N-1:
            P+=list_P[T]
        else:
            break
        T += list_T[T]
        if T + list_T[T] > N-1:
            break
    profit.append(P)
    
print(max(profit))'''
N = int(input())

timeTable = [list(map(int, input().split())) for _ in range(N)]

def solve(i):
    if i>=N:
        return 0
    ret = 0
    if i+timeTable[i][0]<=N :
        ret = solve(i+timeTable[i][0])+timeTable[i][1]
    ret = max(ret,solve(i+1))
    return ret

print(solve(0))

