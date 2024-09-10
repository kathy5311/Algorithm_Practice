import sys

A=[]
m=''
for _ in range(5):
    a = list(map(str,sys.stdin.readline()))
    A.append(a[:-1]) #readline은 개행문자까지 붙이게 된다
#print(A)
#print(A[0][0]+A[1][0])

for j in range(15):
    for i in range(5):
        if j >= len(A[i]): continue
        print(A[i][j],end='')




