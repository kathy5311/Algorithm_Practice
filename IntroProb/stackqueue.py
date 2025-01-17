class Stack:
    def __init__(self):
        self.stack=[]
    
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack)==0:
            return "Stack is Empty"
        else:
            self.stack.pop()
    
    def top(self):
        if len(self.stack)==0:
            return "Stack is Empty"
        else:
            return self.stack[-1]

#LinkedList
class Node:
    def __init__(self, data):
        self.data= data
        self.next=None
    
class SinglyLinkedStack:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        data=None
        if self.isEmpty():
            return "Stack is Empty"
        else:
            data = self.head.data
            self.head = self.head.next
        return data
    
    def top(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            data = self.head.data
        return data
'''
if __name__ == "__main__":
    a = SinglyLinkedStack()
    print(a.top())
    a.push(10)
    print(a.top())
    a.push(20)
    print(a.top())
    a.push(30)
    print(a.pop())
    print(a.top())'''

class Queue:
    def __init__(self):
        self.queue=[]
    
    def isEmpty(self):
        if not self.queue:
            return True
        else:
            return False
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            dequeued = self.queue[0]
            self.queue = self.queue[1:]
            return dequeued
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue[0]

class LinkedListQueue:
    def __init__(self, data):
        self.front = data
        self.rear = None
    
    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False
        
    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next=new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            dequeued = self.front
            self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.front.data
queue = LinkedListQueue(None)
queue.enqueue(10)
queue.enqueue(20)

print(queue.dequeue())  # Node 객체가 반환됨