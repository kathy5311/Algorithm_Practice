import sys

k=int(sys.stdin.readline())
n=1
i=0
n_dict={}
pat='666'
while n<=10000:
    if pat in str(i):
        if str(i) not in n_dict:
            n_dict[n]=i
        n+=1
    i+=1
print(n_dict[k])

