costs = 	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n=4

def find_parent(parents, a):
    if parents[a] != a:
        parents[a] = find_parent(parents, parents[a])
    return parents[a]

def union_parent(parents, a, b):
    a = find_parent(parents,a)
    b = find_parent(parents,b)

    if a<b:
        parents[b]=a
    else:
        parents[a]=b


def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    #parents creation
    parents=[0 for _ in range(n)]
    for i in range(n):
        parents[i]=i
    #parents update
    for cost in costs:
        a,b,value = cost[0], cost[1], cost[2]
        if find_parent(parents,a) == find_parent(parents,b):
            continue
        else:
            answer+=value
        union_parent(parents,a,b)
    return answer

print(solution(n,costs))