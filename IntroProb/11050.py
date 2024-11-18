from itertools import combinations
import sys

N,K = list(map(int, sys.stdin.readline().split()))
print(len(list(combinations([0 for _ in range((N))],K))))