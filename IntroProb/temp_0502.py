from collections import deque
#내일 스택으로 풀어보기
number="4177252841"
number_queue=deque([i for i in number])
k=4
answer = ''
new_stack=deque([number_queue[0]])
for i in number:
    if k==0:
        break
    a=number_queue.popleft()
    for i in range(len(new_stack)):
        m = new_stack.pop()
        if m > a:
            new_stack.append(m)
        elif m < a:
            new_stack.append(a)
            k-=1
        else:
            new_stack.append(m)
            new_stack.append(a)
print(new_stack)
print(number_queue)
        





