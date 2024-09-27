import sys

N = sys.stdin.readline().split()
N=N[0]
new_set=set()

for i in range(len(N)):
    for j in range(i,len(N)+1):
        new_set.add(N[i:j+1])
print(len(new_set))