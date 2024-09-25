import sys
import bisect
N,M = list(map(int, sys.stdin.readline().split()))

have_list=[sys.stdin.readline().split() for _ in range(N)]
check_list = [sys.stdin.readline().split() for _ in range(M)]

have_list.sort()
check_list.sort()
new_list=[]
for i in check_list:
    l = bisect.bisect_left(have_list, i)
    r = bisect.bisect_right(have_list,i)
    new_list.append(r-l)

print(sum(new_list))
idx=-1
for i in new_list:
    idx+=1
    if i==1:
        print(check_list[idx][0])