import sys

input = int(sys.stdin.readline())

for _ in range(input):
    a = sys.stdin.readline()
    if len(a) < 2:
        print(a*2)
    else:
        print(a[0]+a[-2])