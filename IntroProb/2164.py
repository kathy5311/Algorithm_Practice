from collections import deque
import sys

queue=deque([i for i in range(int(sys.stdin.readline()),0,-1)])
while(True):
    if len(queue)==1:
        print(queue[0])
        break
    queue.pop()
    queue.appendleft(queue[-1])
    queue.pop()


    
    

