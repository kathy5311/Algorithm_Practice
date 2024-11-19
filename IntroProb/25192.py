import sys

N = int(sys.stdin.readline().strip())

count=0
talk_set=set()
for _ in range(N):
    p = sys.stdin.readline().strip()
    if p=='ENTER':
        talk_set=set()
    elif p not in talk_set:
        count+=1
        talk_set.add(p)
print(count)



    

