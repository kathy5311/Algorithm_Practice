import sys

def recursion(s, l, r,count):
    count+=1
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else:
        return recursion(s, l+1, r-1,count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1,0)

N = int(sys.stdin.readline().strip())

for _ in range(N):
    n = sys.stdin.readline().strip()
    a,b =isPalindrome(n)
    print(a,b)
