#단어 변환
from collections import deque
def solution(begin, target, words):
    
    return bfs(begin, target, words)

def bfs(begin, target, words):
    queue = deque([(begin,0)])
    vistied=set()

    while queue:
        now, step = queue.popleft()
        
        if now == target:
            return step
        
        for word in words:
            if word not in vistied:
                match=0


                for i in range(len(word)):
                    if word[i]!=now[i]:
                        match+=1

                if match==1:
                    queue.append((word,step+1))
                    vistied.add(word)
    return 0
        

print(solution("hit","cog",["hot", "lot", "dot", "dog", "cog", "log"]))