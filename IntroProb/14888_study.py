import sys
from itertools import permutations
import operator

def change(compute_list):
    ops = {
        "+":operator.add,
        "-":operator.sub,
        "*":operator.mul,
        "//":operator.floordiv
    }
    tmp=compute_list[0]
    for i in range(1,len(compute_list),2):

        if tmp < 0 and compute_list[i]=='//':
            result=(ops[compute_list[i]](abs(tmp),compute_list[i+1]))*(-1)
        else:
            result=(ops[compute_list[i]](tmp,compute_list[i+1]))
        tmp = result
    return result


N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

list_op = list(map(int, sys.stdin.readline().split()))

list_re=[]
for i in range(len(list_op)):
    if i ==0:
        if int(list_op[i]==0):
            pass
        else:
            for _ in range(int(list_op[i])):
                list_re.append("+")
    elif i ==1:
        if int(list_op[i]==0):
            pass
        else:
            for _ in range(int(list_op[i])):
                list_re.append("-")
    elif i==2:
        if int(list_op[i]==0):
            pass
        else:
            for _ in range(int(list_op[i])):
                list_re.append("*")
    elif i==3:
        if int(list_op[i]==0):
            pass
        else:
            for _ in range(int(list_op[i])):
                list_re.append("//")

list_comb = list(permutations(list_re))

k = 0
result=[]
compute_list=[0]*((2*N)-1)
for i in range(0,N):
    compute_list[(2*i)]=num[i]

while k < len(list_comb):
    for i in range(0,N):
        if i == N-1:
            pass
        else:
            compute_list[(2*i)+1]=(list_comb[k])[i]

    result.append(change(compute_list))
    k+=1
print(max(result))
print(min(result))

