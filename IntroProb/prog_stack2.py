#프로세스
#enumerate 사용하면 좀 더 쉽게 풀 수 있다.
from collections import deque
#ascii 코드 이용해서 알파벳 파악하자
def solution(priorities, location):
    answer = 0
    excu=deque([])
    queue = deque(priorities)
    num_list = deque([chr(65+i) for i in range(len(priorities))])
    word=num_list[location]
    
    while queue:
        match=0
        x=queue.popleft()
        num=num_list.popleft()
        for i in queue:
            if i > x:
                match+=1
        if match!=0:
            queue.append(x)
            num_list.append(num)
        elif match==0:
            excu.append(num)

    answer=(excu.index(word)+1)
    
    return answer