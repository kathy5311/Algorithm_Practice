import sys

a,b,w,h = list(map(int, sys.stdin.readline().split()))


left=a
below=b
right = w-a
up = h-b
len_list=[left,below,right,up]
print(min(len_list))
