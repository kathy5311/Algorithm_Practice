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
    
    
    answer=[]
    while queue:
        count=1
        deploy_day = queue.popleft()

        while queue and queue[0]<=deploy_day:
            queue.popleft()
            count+=1

        
        answer.append(count)

    return answer