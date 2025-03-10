#같은 숫자는 싫어
from collections import deque

def solution(arr):
    answer = [-1]
    queue=deque(arr)
    while queue:
        x=queue.popleft()
        if answer[-1]==x:
            continue
        else:
            answer.append(x)
    return answer[1:]