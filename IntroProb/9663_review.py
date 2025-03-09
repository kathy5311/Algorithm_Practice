import sys

N = int(input())
cols = [0]*N
count=0

def check(row, col):
    for i in range(col):
        if row==cols[i] or (abs(row-cols[i])==abs(col-i)):
            return False
    return True


def queen(col):
    global count
    if N==col:
        count+=1
        return 
    
    for row in range(N):
        if check(row,col):
            cols[col]=row
            queen(col+1)
            cols[col]=0
queen(0)
print(count)

    
        






            


