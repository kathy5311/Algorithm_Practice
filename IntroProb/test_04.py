import heapq
operations=["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

def solution(operations):
    answer=[]
    max_heap=[]
    min_heap=[]
    vistited={}
    id_counter=0

    for i in operations:
        op,num = i.split()
        num = int(num)
        
        if op=="I":
            heapq.heappush(max_heap,(-num,id_counter))
            heapq.heappush(min_heap, (num,id_counter))
            vistited[id_counter]=True
            id_counter+=1
        
        elif op=="D":
            if num==1:
                while not vistited[max_heap[0][1]] and max_heap:
                    heapq.heappop(max_heap)
                if max_heap:
                    _,idx = heapq.heappop(max_heap)
                    vistited[idx]=False
            
            elif num==-1:
                while not vistited[min_heap[0][1]] and min_heap:
                    heapq.heappop(min_heap)
                if min_heap:
                    _,idx = heapq.heappop(min_heap)
                    vistited[idx]=False
        
    while max_heap and not vistited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not vistited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if not min_heap or not max_heap:
        return [0, 0]
    else:
        return [-max_heap[0][0], min_heap[0][0]]



            
