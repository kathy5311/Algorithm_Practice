import sys

v,e = map(int, input().split())
#부모 테이블 초기화
parent = [0]*(v+1)
for i in range(1,v+1):
    parent[i]=i

#find 연산
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

#union 연산
def union_parent(parent, a, b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

edges=[]
total_cost =0

for _ in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost, a, b))

edges.sort()

for i in range(e):
    cost, a,b = edges[i]
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent, a, b)
        total_cost += cost
print(total_cost)