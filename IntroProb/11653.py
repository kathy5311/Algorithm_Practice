import sys

n=int(sys.stdin.readline())

yak_list=[]

for i in range(2, n+1):
    if n % i ==0:
        yak_list.append(i)
print(yak_list)
if len(yak_list)!= 1:
    yak_list=yak_list[:-1]
new_list=[]
for j in yak_list:
    i=2
    m=j
    while 1:
        if m==i:
            new_list.append(m)
            #print(new_list)
            break
        elif m % i == 0:
            m = m // i
            if m ==i:
                new_list.append(m)
                break
            elif m % i == 0:
                m = m // i
            else:
                i+=1
        else:
            i+=1
new_list.sort()
print(new_list)

        
    
    
    


