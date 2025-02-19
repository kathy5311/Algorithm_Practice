
def DFS(numbers, target):
    ans=0
    leaves=[0]

    for num in numbers:
        tmp = []
        for leaf in leaves:
            tmp.append(num+leaf)
            tmp.append(((-1)*num)+leaf)
        leaves=tmp
    for pent in tmp:
        if pent==target:
            ans+=1
    return ans
numbers=[1,1,1,1,1]
target=3
print(DFS(numbers,target))
