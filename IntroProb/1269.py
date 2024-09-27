import sys
import bisect
N,M = list(map(int, sys.stdin.readline().split()))

N_set = list(map(int,sys.stdin.readline().split()))
M_set = list(map(int,sys.stdin.readline().split()))

N_set = (sorted(N_set))
M_set = (sorted(M_set))

N_M=[]
for i in N_set:
    l = bisect.bisect_left(M_set, i)
    r = bisect.bisect_right(M_set, i)
    if r-l ==0:
        N_M.append(l-r)

M_N=[]
for i in M_set:
    l = bisect.bisect_left(N_set, i)
    r = bisect.bisect_right(N_set, i)
    if r-l ==0:
        M_N.append(l-r)
print(len(M_N)+len(N_M))





