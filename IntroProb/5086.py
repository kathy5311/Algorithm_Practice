import sys

while 1:
    a, b = list(map(int, sys.stdin.readline().split()))
    if a==0 and b==0: break

    if a>b and a%b==0:
        print('multiple')
    elif a<b and b%a==0:
        print('factor')
    else:
        print('neither')
