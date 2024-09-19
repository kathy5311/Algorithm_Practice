import sys

a,b,c,d,e,f = list(map(int, sys.stdin.readline().split()))

print((((b*f)-(c*e))//((b*d)-(a*e))),(((c*d)-(a*f))//((b*d)-(a*e))))
