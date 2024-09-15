import sys
#다시!
a, b = (map(int, sys.stdin.readline().split()))
c =int(sys.stdin.readline())
n_0 = int(sys.stdin.readline())


if ((a*n_0)+b) <= c*n_0 and (c>=a):
    print(1)
else:
    print(0)


        