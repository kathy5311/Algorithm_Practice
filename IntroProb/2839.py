import sys

N =int(sys.stdin.readline())


if (N%5==0):
    print(N//5)
else:
    if N%5 >= 3:
        raw=5*(N//5)
        if (N-raw)%3==0:
            print(((N-raw)//3)+(N//5))
        else:
            print(-1)
    
    elif N%5 <3:
        raw=5*((N//5)-1)
        if (N-raw)%3==0:
            print(((N-raw)//3)+((N//5)-1))
        else:
            if ((N-(N//5))%3==0):
                print(N//3)
            else:
                print(-1)
