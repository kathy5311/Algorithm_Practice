#소수 찾기
from itertools import permutations
def find_sosu(number):
    if number==0 or number == 1:
        return False
    i=2
    while i<(number):
        if (number % i ==0):
            return False
        i+=1
    return True

def solution(numbers):
    answer=0
    numbers_list = list(numbers)
    tmp_list=[]
    final_list=[]
    for i in range(1,len(numbers_list)+1):
        tmp_list.extend(list(permutations(numbers_list,i)))

    for bef in tmp_list:
        bef = int("".join(bef))
        if bef not in final_list:
            final_list.append(bef)

    for number in final_list:
        if find_sosu(number):
            answer+=1
    return answer
print(solution("011"))
