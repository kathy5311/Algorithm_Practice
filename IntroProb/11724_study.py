import sys
sys.setrecursionlimit(5000)
def DFS(g, v, visited,node_list):

    visited[v]=True
    node_list.remove(v)
    for i in g[v]:
        if not visited[i]:
            DFS(g,i,visited,node_list)
    return node_list


N,M = map(int, sys.stdin.readline().split())

g=[[] for _ in range(N+1)]
for i in range(M+1):
    if i ==0:
        continue
    else:
        a,b = map(int, sys.stdin.readline().split())
        g[a].append(b)
        g[b].append(a)

#for i in g:
#    i.sort()
visited = [False]*(N+1)
node_list=[i for i in range(1,N+1)]

count=0
while len(node_list)>0:
    node_list=DFS(g,node_list[0],visited,node_list)
    count+=1
print(count)

