import sys

num=[]
for _ in range(10):
    b = int(sys.stdin.readline())
    b = b%42
    if b not in num:
        num.append(b)

print(len(num))
        