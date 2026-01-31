number="4177252841"
k=4
answer = ''
len_num=len(number)-k 
start_temp=0
temp=k
start,end = number[:temp], number[k+1:]
temp= number.index(max(start))
answer+=max(start)
number=number[number.index(max(start))+1:]

start_2,end_2 = number[:k-1], number[k-1:]
print(start_2,end_2)
answer+=max(start_2)
number = number[number.index(max(start_2))+1:]
print(number)
start_3, end_3 = number[:k-1], number[k-1:]
print(start_3,end_3)
