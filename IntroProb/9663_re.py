import sys

N = int(input())
cols = [0]*N
#i->row, cols[i]->col
count=0
def check(col,row):
    for i in range(row):
        if (cols[i] == col) or (abs(col-cols[i])==abs(row-i)):
            return False
    return True

def queen(row):
    global count
    if N==row:
        count+=1
        return count
    for col in range(N):
        if check(col,row):
            cols[row]=col
            queen(row+1)
            cols[row]=0

queen(0)
print(count)
