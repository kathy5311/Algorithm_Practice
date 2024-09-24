import sys

N = int(sys.stdin.readline())

str_list=[input() for _ in range(N)]

len_list=[]
for length in range(1,51):
    alpha_list=[]
    for i in str_list:
        if len(i)==length:
            alpha_list.append(i)
    alpha_list.sort()
    for j in alpha_list:
        if j not in len_list:
            len_list.append(j)

for i in len_list:
    print(i)        




