import sys

n,B = list(map(int, sys.stdin.readline().split()))
total=''
while True:
    if n==0:
        break
    
    if n%(B) > 9:
        total += chr(((n)%(B))+55)
    else:
        total+=str((n)%(B))
    n=n//B


print(total[::-1]) 
