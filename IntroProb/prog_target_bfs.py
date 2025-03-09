#타겟단어찾기
from collections import deque

begin ="hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
def solution(begin,target,word):
    return bfs(begin,target,word)

def bfs(begin,target):
    queue = deque()
    queue.append((begin,0))
    visited=set()

    while queue:
        wrd,step=queue.popleft()
        if wrd == target:
            return step
        
        for word in words:
            if word not in visited:
                match=0
                for i in range(len(word)):
                    if word[i]!=wrd[i]:
                        match+=1
                if match==1:
                    visited.add(word)
                    queue.append((word,step+1))