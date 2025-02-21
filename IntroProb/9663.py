import sys

N = int(sys.stdin.readline())
cols = [0]*N
count=0

def check(row,col):
    for i in range(row): #i=row, cols[i]=col
        if (cols[i]==col) or (abs(cols[i]-col)==abs(i-row)):
            return False
    return True 
    
def queen(row):
    global count
    if row == N:
        count+=1
        return count
    
    for col in range(N):
        if check(row,col):
            cols[row]=col
            queen(row+1)
            cols[row]=0
queen(0)
print(count)



