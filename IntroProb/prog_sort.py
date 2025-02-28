# 가장 큰 수
# 탐색/정렬 알고리즘은 보통 O(nlgn)을 넘어가면 안된다.
from itertools import permutations
numbers=[0,0,0]
def solution(numbers):
    answer=''
    num = list(map(str, numbers))
    num.sort(key=lambda x:x*3,reverse=True)
    print(num)
    return type("".join(num))
print(solution(numbers))