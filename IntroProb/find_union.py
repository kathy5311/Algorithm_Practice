import sys
v,e = map(int, input().split())
parent = [0]*(v)
for i in range(v):
    parent[i]=i
#print(parent)

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] =a
    else:
        parent[a] =b

cycle = False

for _ in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent,b):
        cycle =True
        continue
    else:
        union_parent(parent, a,b)

print(parent)
