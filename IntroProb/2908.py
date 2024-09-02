import sys

a,b = sys.stdin.readline().split()


b=''.join(reversed(b))
a=''.join(reversed(a))
if a>b:
    print(a)
elif a<b:
    print(b)

