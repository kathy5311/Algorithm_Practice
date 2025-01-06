import sys

N = int(sys.stdin.readline())

for i in range(N):
    strnum = str(i)
    listnum = list(strnum)

    sumup=0
    for j in listnum:
        sumup+=int(j)
    sumup+=i

    if i == N-1:
        print(0)
        break

    if sumup==N:
        print(i)
        break

    










