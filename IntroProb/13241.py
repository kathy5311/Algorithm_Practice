import sys

N,M = list(map(int,(sys.stdin.readline().split())))

def gcd(n,m):
    if n==0:
        return m
    elif m==0:
        return n
    if n>=m:
        return gcd(n%m,m)
    elif n<m:
        return gcd(n,m%n)

eq = gcd(N,M)
a, b = (N//eq), (M//eq)
print(eq*a*b)
    
    
    

