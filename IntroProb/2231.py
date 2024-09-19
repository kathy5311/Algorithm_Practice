import sys

a = int(sys.stdin.readline())

for i in range(1,a+1):
    sum = i
    i_str=str(i)
    for j in i_str:
        #print(j)
        sum+=int(j)

    if sum == a:
        print(i_str)
        break
    elif i == a:
        print(0)
        break


