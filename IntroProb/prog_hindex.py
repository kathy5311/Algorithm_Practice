#index 복습

def solution(citations):
    citations.sort(reverse=True)
    h_index=0

    for idx,c in enumerate(citations):
        if idx+1<=c:
            h_index+=1
        else:
            break
            
    return h_index

print(solution([6, 5, 3, 1, 0]))