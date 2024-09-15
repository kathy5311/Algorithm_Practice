import sys

while 1:
    a = list(map(int, sys.stdin.readline().split()))

    dict_a={}
    max_a=max(a)
    total=0

    if 0 in a:
        break

    for i in a:
        total+=i
    
    if total-max_a <= max_a:
        print('Invalid')

    else:
        for i in a:
            if i not in dict_a:
                dict_a[i]=1
        
        if len(dict_a.keys())==1:
            print('Equilateral')
        elif len(dict_a.keys())==2:
            print('Isosceles')
        else:
            print('Scalene')
    

        
    