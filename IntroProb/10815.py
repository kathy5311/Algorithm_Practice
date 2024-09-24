import sys
import bisect

N = int(sys.stdin.readline())
have_list= list(map(int, sys.stdin.readline().split()))
have_list.sort()
M = int(sys.stdin.readline())
check_list= list(map(int, sys.stdin.readline().split()))
new_list=[0]*M

for o in check_list:
    l = bisect.bisect_left(have_list,o)
    r = bisect.bisect_right(have_list,o)

    print(r-l, end=' ')


