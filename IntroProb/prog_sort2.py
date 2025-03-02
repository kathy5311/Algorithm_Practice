#H-index
citations = [0,0,0,0,5]
'''def solution(citations):
    citations.sort()
    pivot = len(citations)//2

    #초기 pivot이 조건을 만족하는지 확인
    for _ in range(len(citations)):
        large_idx = citations[pivot:]
        if (pivot == len(citations)-1) and (citations[pivot]==0):
            return 0
        elif (pivot == len(citations)-1) and (citations[pivot]!=0):
            return 1

        if len(large_idx)>= citations[pivot]:
            pivot+=1
        else:
            pivot-=1
            return citations[pivot]
    return citations[pivot] 
def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        large_idx=citations[:i+1]
        if len(large_idx)>=citations[i]:
            if citations[i]==0:
                return 1
            return citations[i]'''
def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    h_index=0

    for i,c in enumerate(citations):
        if c >= i+1:
            h_index+=1
        else:
            return h_index

print(solution(citations))