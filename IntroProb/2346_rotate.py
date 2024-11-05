from collections import deque
import sys

N = int(input())
queue = deque(list(enumerate(map(int, sys.stdin.readline().split()))))

temp=[]
while True:
    pivot = queue[0][1]
    temp.append((queue[0][0])+1)
    queue.popleft()

    if pivot>0:
        queue.rotate(-(pivot-1))
    else:
        queue.rotate(-pivot)

    if len(queue)==0:
        break

for i in temp:
    if i == temp[-1]:
        print(i)
    else:
        print(i, end=' ')
