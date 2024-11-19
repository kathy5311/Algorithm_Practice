import sys

N = int(sys.stdin.readline().strip())

name = set()
count=1
for _ in range(N):
    a,b = sys.stdin.readline().split()

    if a=='ChongChong' or b=='ChongChong':
        name.add(a)
        name.add(b)
    
    if a in name or b in name:
        name.add(a)
        name.add(b)
    

print(len(name))