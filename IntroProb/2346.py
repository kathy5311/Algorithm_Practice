import sys
from collections import deque

N = int(input())

num = list(enumerate(map(int, sys.stdin.readline().split())))
queue = deque(num)

temp=[]
pivot=queue[0][1]
temp.append((queue[0][0])+1)
queue.popleft()

while True:

    if pivot>0:
        for i in range(pivot):
            if len(queue)==0:
                break
            queue.append(queue.popleft())

    elif pivot<0:
        for i in range(abs(pivot)-1):
            if len(queue)==0:
                break
            queue.appendleft(queue.pop())


    if len(queue)==0:
        break

    pivot=queue[-1][1]
    temp.append((queue[-1][0])+1)
    queue.pop()

for i in temp:
    print(i, end=' ')



