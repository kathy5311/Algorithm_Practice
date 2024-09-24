import sys

N = int(sys.stdin.readline())

a = list(map(int,(sys.stdin.readline().split())))
print(a)
idx_dict={}
num = sorted(set(a))

count=0
for i in num:
    idx_dict[i]=count
    count+=1


for i in a:
    print(idx_dict[i], end=' ')
    
    


