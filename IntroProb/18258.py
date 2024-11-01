class Queue():
    def __init__(self):
        self.item=[]

    def push(self, value):
        self.item.append(value)

    def pop(self):
        if self.item:
            return self.item.pop(0)
        else:
            return -1

    def size(self) -> int:
        return len(self.item)

    def empty(self):
        if len(self.item)==0:
            return 1
        else:
            return 0
    
    def front(self):
        if self.item:
            return self.item[0]
        else:
            return -1
    
    def back(self):
        if self.item:
            return self.item[-1]
        else:
            return -1

Q = Queue()
print(Q.push(1))
print(Q.push(2))
print(Q.front())
print(Q.back())
print(Q.size())
print(Q.empty())
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.size())
print(Q.empty())
print(Q.pop())
print(Q.push(3))
print(Q.empty())
print(Q.front())