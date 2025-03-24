from collections import deque
def solution(prices):
    answer = []
    price=deque(prices)
    
    while price:
        tmp=price.popleft() #비교대상 설정
        time=0
        for i in price:
            time+=1
            if tmp > i:
                break
            
        answer.append(time)

        
    return answer