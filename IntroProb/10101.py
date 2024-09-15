import sys

len_list={}
total=0
for _ in range(3):
    a = int(sys.stdin.readline())

    if a not in len_list:
        len_list[a]=1
    
    elif a in len_list:
        len_list[a]+=1
    
    total+=a

if total!=180:
    print('Error')
else:
    if (60 in len_list) and (len_list[60]==3):
        print('Equilateral')
    elif len(len_list.keys())==2:
        print('Isosceles')
    else:
        print('Scalene')

