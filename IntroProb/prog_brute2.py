#타일
#메모:프로그래머스 상에서는 모든 조합의 가능성을 다 검사해야 함
#line 12에서 바로 끝에만 확인하면 안되고 모든 yellow_sep의 col,row를 조사해야함!
import math
def solution(brown, yellow):
    answer=[]
    yellow_sep=[]
    for i in range(1,int(math.sqrt(yellow))+1):
        if yellow % i ==0:
            yellow_sep.append([i,yellow//i])

    col, row = yellow_sep[-1]

    if (col+2)*(row+2)==yellow+brown:
        answer=[row+2, col+2]
    return answer
    

print(solution(24,24))
    