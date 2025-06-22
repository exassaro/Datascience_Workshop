#DEQUE double ended queue
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class Deque:
    
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
        
    def enqueue_front(self,data):
        node=Node(data)
        if not self.front:
            self.front=self.rear=node
        else:
            node.next=self.front
            self.front.prev=node
            self.front=node
        self.count+=1
        
    def enqueue_rear(self,data):
        node=Node(data)
        if not self.rear:
            self.front=self.rear=node
        else:
            node.prev=self.rear
            self.rear.next=node
            self.rear=node
        self.count+=1
        
    def dequeue_front(self):
        if not self.front:
            raise IndexError("Deque is Empty")
        data=self.front.data
        self.front=self.front.next
        if self.front:
            self.front.prev=None
        else:
            self.rear=None # If deque becomes empty
        self.count-=1
        return data
        
    def dequeue_rear(self):
        if not self.rear:
            raise IndexError("Deque is Empty")
        data=self.rear.data
        self.rear=self.rear.prev
        if self.rear:
            self.rear.next=None
        else:
            self.front=None # If deque becomes empty
        self.count-=1
        return data
        
    def is_empty(self):
        return self.front is None
        
    def peek_front(self):
        return self.front.data if self.front else None
        
    def peek_rear(self):
        return self.rear.data if self.rear else None
        
    def __len__(self):
        return self.count
        
    def display(self):
        if self.is_empty():
            print("Deque is Empty")
            return
        temp=self.front
        while temp:
            print(temp.data,end="<->" if temp.next else "\n")
            temp=temp.next
        
dq=Deque()
dq.is_empty()
dq.enqueue_front(10)
dq.enqueue_rear(20)
dq.enqueue_front(5)
dq.enqueue_rear(30)
dq.enqueue_front(8)
dq.enqueue_front(54)
print("Length:", len(dq))  # Output: 3

print(dq.dequeue_rear())  # 20
print("Length:", len(dq))  # Output: 2

print(dq.dequeue_front())  # 5
print("Length:", len(dq)) 

dq.display()
        
        
        
        
        