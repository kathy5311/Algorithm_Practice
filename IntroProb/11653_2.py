import sys

n = int(sys.stdin.readline())

i=2
while 1:
    if n % i ==0:
        print(i)
        n = n //i
    
    elif n==1:
        break

    else:
        i+=1

    

