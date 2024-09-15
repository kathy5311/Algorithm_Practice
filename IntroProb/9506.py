import sys


while 1:
    yak_list=[]
    n = int(sys.stdin.readline())
    if n == -1: break
    for i in range(1,n+1):
        if i != n:
            if n%i==0:
                yak_list.append(i)
    #print(yak_list)
    total=0
    for j in range(len(yak_list)):
        total+=int(yak_list[j])
    #print(total)
    if total==n:
        print(f'{n} = ', end='')
        for i in range(len(yak_list)):
            if i == len(yak_list)-1:
                print(yak_list[i],end='')
                print()
            else:
                print(yak_list[i], end=' + ')
    elif total!=n:
        print(f'{n} is NOT perfect.')
    