import sys

N = int(sys.stdin.readline())

a=[]
for _ in range(N):
    a.append(int(sys.stdin.readline()))

count=[0]*(max(a)+1)

for i in a:
    if count[i] != 0:

        count[i]=i

result=[0]*len(a)
for i in count[1:]:
    result[i+1]=i
print(a)
print(count)
print(result)