import sys
import math
n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

def mean_func(*score):
    a= max(score)
    for i in range(len(score)):
        score[i] = score[i]/a*100
    summing=score.sum()
    return summing/len(score)
print(mean_func(score))   