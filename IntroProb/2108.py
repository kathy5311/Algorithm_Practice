import sys
from collections import Counter
N = int(sys.stdin.readline().strip())

num_list=[]
for _ in range(N):
    a = int(sys.stdin.readline().strip())
    num_list.append(a)

num_list.sort()
sum_num = sum(num_list)
len_num = len(num_list)

print(round((sum_num/len_num)))
print(num_list[len(num_list)//2])
#최빈값
cnt = Counter(num_list)
_,b=max(cnt.items())
bin_list=[]
for i,j in cnt.items():
    if j == b:
        bin_list.append(i)
bin_list.sort()
print(bin_list)
if len(bin_list)>=2:
    print(bin_list[1])
else:
    print(bin_list[0])
#범위
print(max(num_list)-min(num_list))
