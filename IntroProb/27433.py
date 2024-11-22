import sys
N=int(sys.stdin.readline().strip())
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(N))