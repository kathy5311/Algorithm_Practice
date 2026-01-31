#dfs 활용 풀이
'''answer=0
idx=-1
alpha=['A','E','I','O',"U"]
def dfs(cnt, s, word):
    global answer, idx
    if cnt>5:
        return
    
    if cnt<=5:
        idx+=1
        if s==word:
            answer=idx
            return
        
    for i in range(5):
        dfs(cnt+1, s+alpha[i],word)

def solution(word):
    dfs(0,'',word)
    return answer
print(solution("I"))'''

#수학적 풀이

def solution(word):
    alpha = ['A','E','I','O','U']
    weight=[781, 156, 31, 6, 1]
    result=0
    for i, char in enumerate(word):
        result+=alpha.index(char)*weight[i]+1
    return result
print(solution("I"))
