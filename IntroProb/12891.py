import sys

ideallist = [0]*4
currentlist=[0]*4
checksecret=0


def addDNA(i):
    global currentlist, ideallist, checksecret
    if i=='A':
        currentlist[0]+=1
        if currentlist[0]==ideallist[0]:
            checksecret+=1

    elif i=='C':
        currentlist[1]+=1
        if currentlist[1]==ideallist[1]:
            checksecret+=1

    elif i=='G':
        currentlist[2]+=1
        if currentlist[2]==ideallist[2]:
            checksecret+=1
    else:
        currentlist[3]+=1
        if currentlist[3]==ideallist[3]:
            checksecret+=1

def removeDNA(s):
    global currentlist, ideallist, checksecret
    if s=='A':
        if currentlist[0]==ideallist[0]:
            checksecret-=1
        currentlist[0]-=1

    elif s=='C':
        if currentlist[1]==ideallist[1]:
            checksecret-=1
        currentlist[1]-=1

    elif s=='G':
        if currentlist[2]==ideallist[2]:
            checksecret-=1
        currentlist[2]-=1

    else:
        if currentlist[3]==ideallist[3]:
            checksecret-=1
        currentlist[3]-=1

Result=0
len_DNA, sub_len = map(int,(sys.stdin.readline().split()))
A = list(input())
ideallist = list(map(int,(sys.stdin.readline().split())))

for i in range(4):
    if ideallist[i]==0:
        checksecret+=1

for j in range(sub_len):
    addDNA(A[j])

if checksecret==4:
    Result+=1

for k in range(sub_len, len_DNA):
    addDNA(A[k])
    removeDNA(A[k-sub_len])
    if checksecret==4:
        Result+=1




'''시간초과
#GATA
s=0
e=sub_len-1
Result=0
while e<=len_DNA-1:
    sub_list=strDNA[s:e+1]
    countA=0
    countC=0
    countG=0
    countT=0
    for i in range(len(sub_list)):
        if sub_list[i]=='A':
            countA+=1
        elif sub_list[i]=='C':
            countC+=1
        elif sub_list[i]=='G':
            countG+=1
        else:
            countT+=1
    if (countA==numA) and (countC==numC) and (countG==numG) and (countT==numT):
        Result+=1
    s+=1
    e+=1'''

print(Result)


