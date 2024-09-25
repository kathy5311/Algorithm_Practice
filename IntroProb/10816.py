import sys
import bisect

N = int(sys.stdin.readline())
have_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
chekc_list = list(map(int, sys.stdin.readline().split()))

have_list.sort()

new_list=[0]*M
count=0
for i in chekc_list:
    r = bisect.bisect_right(have_list, i)
    l = bisect.bisect_left(have_list, i)
    new_list[count]=r-l
    count+=1

for i in new_list:
    print(i, end=' ')
    


