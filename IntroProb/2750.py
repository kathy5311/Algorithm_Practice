import sys
N= int(sys.stdin.readline())

new_list=[]
for _ in range(N):
    a=int(sys.stdin.readline())
    new_list.append(a)

new_list.sort()
for i in new_list:
    print(i)