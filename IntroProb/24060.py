import sys
cnt=0
LenN, res = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))

def merge_sort(A, p, r):
    if (p<r):
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)


def merge(A, p,q,r):
    global cnt
    global res
    i=p
    j=q+1
    t=0
    tmp=[]

    while (i <= q) and (j<=r):
        if A[i] <= A[j]:
            tmp.append(A[i])
            t+=1
            i+=1
        else:
            tmp.append(A[j])
            t+=1
            j+=1
    while (i<=q):
        tmp.append(A[i])
        t+=1
        i+=1
    while (j<=r):
        tmp.append(A[j])
        t+=1
        j+=1
    i=p
    t=0
    while (i<=r):
        cnt+=1
        A[i]= tmp[t]
        if cnt==res:
            print(A[i])
        i+=1
        t+=1

merge_sort(A,0,LenN-1)
if cnt< res:
    print(-1)