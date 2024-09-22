import sys

N = int(sys.stdin.readline())

#arr 만들기
arr=[int(sys.stdin.readline()) for _ in range(N)]

def counting_sort(arr):
    max_arr = max(arr)
    count = [0] * (max_arr + 1)
    
    for i in arr:	# 카운팅
        count[i] += 1

    sorted_arr=[i for i in range(max_arr+1) for _ in range(count[i])]
        #for _ in range(count[i]): #count[i]==0이어도 문법상 오류는 없다.
            #sorted_arr.append(i)
    return sorted_arr

print(counting_sort(arr))