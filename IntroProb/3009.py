import sys

comp_x={}
comp_y={}
for _ in range(3):
    a,b=list(map(int, sys.stdin.readline().split()))

    if a not in comp_x:
        comp_x[a]=1
    elif a in comp_x:
        comp_x[a]+=1
    if b not in comp_y:
        comp_y[b]=1
    elif b in comp_y:
        comp_y[b]+=1
   
final_x=[k for k, v in comp_x.items() if v == 1]
final_y=[k for k,v in comp_y.items() if v==1]
print(final_x[0], final_y[0])

    
    
    

