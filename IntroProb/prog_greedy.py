#조이스틱
name='JBAAN'

def solution(name):
    answer=0
    
    for ch in name:
        answer+=min(ord(ch)-ord('A'),ord('Z')-ord(ch)+1)
    
    cursor_move=len(name)-1
    for i in range(len(name)):
        next_i = i+1

        while (next_i<len(name)) and (name[next_i]=='A'):
            next_i+=1
        
        distance = min(i, len(name)-next_i)
        cursor_move = min(cursor_move, i+len(name)-next_i+distance)
    answer+=cursor_move

    return answer

print(solution(name))