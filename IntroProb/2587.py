import sys
a=[]
for _ in range(5):
    a.append(int(sys.stdin.readline()))

a.sort()

print(sum(a)//5)
print(a[2])