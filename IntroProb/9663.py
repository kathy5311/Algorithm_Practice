import sys

N = int(sys.stdin.readline())
cols = [0]*N
count=0

def check(row,col):
    for i in range(col): #i=col, cols[i]=row
        if (cols[i]==row) or (abs(cols[i]-row)==abs(i-col)):
            return False
    return True 
    
def queen(col):
    global count
    if col == N:
        count+=1
        return count
    
    for row in range(N):
        if check(row,col):
            cols[col]=row
            queen(col+1)
            cols[col]=0
queen(0)
print(count)



