#단어변환-bfs 복습
from collections import deque
begin='hit'
target='cog'
words=['hot','dot','dog','lot','log','cog']
def solutions(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin, target, words)

def bfs(begin,target,words):
    queue = deque([(begin,0)])
    visited = set()
    while queue:
        now, step = queue.popleft()
        if now == target:
            return step
        
        for word in words:
            if word not in visited:
                match=0

                for i in range(len(begin)):
                    if now[i]!=word[i]:
                        match+=1
                if match==1:
                    queue.append((word,step+1))
                    visited.add(word)
               
    return 0
print(solutions(begin,target,words))



