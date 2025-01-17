import sys

N = [list(map(int,(sys.stdin.readline().split()))) for _ in range(5)]

Bin = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

bingo=0
case1=[0]*5
count1=0
case2=[0]*5
count2=0
count3=0
count4=0
num=0
while bingo<4:
    
    for i in range(5):
        for j in range(5):
            check = Bin[i][j]
            num+=1

            for n in range(5):
                for m in range(5):
                    if check == N[n][m]:
                        case1[m]+=1
                        case2[n]+=1
                        if n==m:
                            count3+=1
                            if n+m==4:
                                count4+=1
                            if count3==5:
                                bingo+=1

                        elif n+m==4 and n!=m:
                            count4+=1
                            if count4==5:
                                bingo+=1
                        
                        elif case1[m]==5 or case2[n]==5:
                            bingo+=1


                    if bingo ==3:
                        print(num)
                        exit()





