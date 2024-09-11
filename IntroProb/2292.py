import sys

a = int(sys.stdin.readline())

count_idx=1
i=1
while 1:
    current_idx=count_idx
    count_idx += (i-1)*6

    if count_idx >= a:
        print(i)
        break
    i+=1

