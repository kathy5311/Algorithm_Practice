#리스트 크기 정해주기
#다시 해보기
(n),m = input().split()
a=[]
for i in range(1, int(n)+1):
   a.append(i)
copy_a=a.copy()
for j in range(int(m)):
    b,c = input().split() 
    a[int(b)-1]=copy_a[int(c)-1]
    a[int(c)-1]=copy_a[int(b)-1]
    
    #print(copy_a)
print(a)