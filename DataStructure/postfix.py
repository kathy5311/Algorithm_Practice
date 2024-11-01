import sys

# 6 * (3+5) * 7 을 postfix로 나타내기

N = input()
outstack =[]
opstack=[]
operator=['-','+','*','/','(',')']

for i in N:
    if i not in operator:
        outstack.append(i)
    
    if i in operator:
        if i =='(':
            opstack.append(i)
        elif i == ')':
            while True:
                if opstack[-1]=='(':
                    opstack.pop()
                    break
                a=opstack.pop()
                outstack.append(a)
        elif i == '-' or i=='+':
            k=len(opstack)
            while k>0:
                if opstack[-1]=='*' or opstack[-1]=='/':
                    a=opstack.pop()
                    outstack.append(a)
                k-=1
            opstack.append(i)
        else:
            opstack.append(i)
if opstack:
    k=len(opstack)
    while k>0:
        a=opstack.pop()
        outstack.append(a)
        k-=1
print(outstack)

                


                       
    