import sys

N,M = list(map(int, sys.stdin.readline().split()))
I,J = list(map(int, sys.stdin.readline().split()))

tail = M*J
head = (N*J)+(I*M)

def gcd(M,J):
    if M==0:
        return J
    elif J == 0:
        return M
    if M>=J:
        return gcd(M%J,J)
    elif M<J:
        return gcd(M,J%M)
    
eq = gcd(head,tail)
print(head//eq, tail//eq)
