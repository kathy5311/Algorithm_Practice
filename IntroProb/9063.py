import sys

n = int(sys.stdin.readline())

comp_x=[]
comp_y=[]
for _ in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))

    comp_x.append(a)
    comp_y.append(b)

comp_x.sort()
comp_y.sort()

if len(comp_x)==1 or comp_x[0]==comp_x[-1] or comp_y[0]==comp_y[-1]:
    print(0)

else:
    k = comp_x[-1]-comp_x[0]
    j = comp_y[-1]-comp_y[0]
    print(k*j)
