'''
입출력 예
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

입출력 예 설명
입출력 예 #1
첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 
하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.

따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

입출력 예 #2
모든 기능이 하루에 1%씩 작업이 가능하므로, 
작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 
어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.
따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.
'''
from collections import deque
import math

def solution(progresses, speeds):
    ans = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    for i in range(len(speeds)):
        progresses[i] = math.ceil((100-progresses[i])/speeds[i])
    
    day = 1
    count = progresses.popleft()
    while progresses:
        a =  progresses.popleft()
        if count >= a:
            day+=1
        else:
            ans.append(day)
            day=1
            count=a
    ans.append(day)

    return ans
print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]))


