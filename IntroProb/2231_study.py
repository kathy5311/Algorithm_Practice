import sys
'''
N = int(sys.stdin.readline())

for i in range(N):
    strnum = str(i)
    listnum = list(strnum)

    sumup=0
    for j in listnum:
        sumup+=int(j)
    sumup+=i

    if i == N-1:
        print(0)
        break

    if sumup==N:
        print(i)
        break'''
n = int(input())  # 분해합을 입력값으로 받음

for i in range(1, n+1):   # 해당 분해합의 생성자 찾기
    num = list((map(int, str(i))))  # i의 각 자릿수를 더함
print(num)









