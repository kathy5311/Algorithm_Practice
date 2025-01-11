import sys

N,M = map(int, sys.stdin.readline().split())

Mat=[list(input()) for i in range(N)]
result=[]
for i in range(N-7):
    for j in range(M-7):
        draw0=0
        draw1=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if Mat[a][b] != 'B':
                        draw0+=1
                    if Mat[a][b] != 'W':
                        draw1+=1
                else:
                    if Mat[a][b] != 'W':
                        draw0+=1
                    if Mat[a][b] != 'B':
                        draw1+=1
        result.append(draw0)
        result.append(draw1)
print(min(result))


    
        