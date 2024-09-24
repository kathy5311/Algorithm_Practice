import sys

N, M = list(map(int, sys.stdin.readline().split()))

count=1
pocket_dict={}
for _ in range(N):
    a = input()
    if a not in pocket_dict:
        pocket_dict[a]=str(count)
    count+=1

inverse_pocket = {v:k for k,v in pocket_dict.items()}
check_list=[sys.stdin.readline().split() for _ in range(M)]

for i in check_list:
    if i[0] in pocket_dict:
        print(pocket_dict[i[0]])
    elif i[0] in inverse_pocket:
        print(inverse_pocket[i[0]])