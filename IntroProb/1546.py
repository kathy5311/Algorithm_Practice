import sys

n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

def mean_func(*score):
    a= max(score[0])
    #print(score)
    score1 = score[0]
    #print(score1)
    summing=0
    for i in range(len(score1)):
        score1[i] = (score1[i])/a*100
        summing+=score1[i]
    return summing/len(score1)
print(mean_func(score))   