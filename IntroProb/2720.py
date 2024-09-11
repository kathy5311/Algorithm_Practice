import sys

n = sys.stdin.readline()

A=25
B=10
C=5
D=1
coin_list_fin=[]
for _ in range(int(n)):
    coin_list=[]
    coin = int(sys.stdin.readline())
    
    coin_list.append(coin//A)
    coin = coin%A
    coin_list.append(coin//B)
    coin = coin%B
    coin_list.append(coin//C)
    coin=coin%C
    coin_list.append(coin//D)
    coin_list_fin.append(coin_list)

for i in coin_list_fin:
    for j in i:
        print(j, end=' ')
    print()
