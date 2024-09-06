import sys

a = sys.stdin.readline()
count=int(a)
for _ in range(int(a)):
    word = sys.stdin.readline()
    unique_list=[]
    for i in range(len(word)-1):
        if word[i] not in unique_list:
            unique_list.append(word[i])
        
        elif word[i] in unique_list:
            if unique_list[-1]!=word[i]:
                count-=1
                break

print(count)