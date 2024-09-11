import sys

n = (sys.stdin.readline())

#make matrix
A=[]
for _ in range(100):
    a=[]
    for _ in range(100):
        a.append(0)
    A.append(a)
#print(A)
count=0
for _ in range(int(n)):
    b,c= list(map(int, sys.stdin.readline().split()))
    end_b=b+10
    end_c=c+10
    for i in range(c,end_c):
        for j in range(b, end_b):
            if A[i][j]==0:
                count+=1       
                A[i][j]=1
print(count)






    

