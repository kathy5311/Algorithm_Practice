#소수 찾기-개선

from itertools import permutations
import math

def find_sosu(number):
    if number==1 or number ==0:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer=0
    tmp_set=set()
    num_list=list(numbers)
    new_list=[]
    for i in range(1,len(numbers)+1):
        new_list.extend(list(permutations(num_list,i)))

    for i in new_list:
        tmp_set.add(int("".join(i)))

    for i in tmp_set:
        if find_sosu(i):
            answer+=1

    return answer

print(solution("011"))