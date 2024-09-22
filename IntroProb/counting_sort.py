arr=[1,3,2,5,2,1,3,5]

def count_sort(arr):
    max_arr= max(arr)
    count_arr=[0]*(max_arr+1)
    sort_arr=[]

    for i in arr:
        count_arr[i]+=1
    
    for j in range(max_arr+1):
        for _ in range(count_arr[j]):
            sort_arr.append(j)
    return sort_arr

print(count_sort(arr))