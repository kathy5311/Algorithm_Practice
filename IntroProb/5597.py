import sys

a = [i for i in range(1,31)]
for i in range(28):
    b = int(sys.stdin.readline())
    
    if b in a:
        a.remove(b)
    
a.sort()
for i in a:
    print(i)