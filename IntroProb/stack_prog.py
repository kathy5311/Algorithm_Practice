import sys
from collections import deque

def solution(progresses, speeds):
    queue = deque([])
    for progress in range(len(progresses)):
        quan = (100-progresses[progress])
        if quan % speeds[progress] !=0:
            day= (quan//speeds[progress])+1
        else:
            day = (quan//speeds[progress])
        queue.append(day)
    
    count=1
    answer=[]
    while queue:
        if len(queue)==1:
            answer.append(count)
            return answer
        curr = queue.popleft()
        if curr >= queue[0]:
            count+=1
            queue.popleft()
        elif curr < queue[0]:
            answer.append(count)
            count=1


progresses=list(map(int, sys.stdin.readline().split()))
speeds = list(map(int,sys.stdin.readline().split()))
print(solution(progresses, speeds))