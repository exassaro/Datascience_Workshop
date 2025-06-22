class Deque:
    def __init__(self,size):
        self.size=size
        self.deque=[None]*size
        self.front=-1
        self.rear=-1
        self.count=0
        
    def is_full(self):
        return self.count==self.size
        
    def is_empty(self):
        return self.front == -1
        
    def enqueue_front(self,data):
        if self.is_full():
            print("Deque is full")
            return
        
        if self.front==-1:
            self.front=self.rear=0
        else:
            if self.front==0:
                self.front=self.size-1
            else:
                self.front-=1
        self.deque[self.front]=data
        
    def enqueue_rear(self,data):
        if self.is_full():
            print("Deque is full")
            return
        
        if self.rear==-1:
            self.front=self.rear=0
        else:
            if self.rear==self.size-1:
                self.rear=0
            else:
                self.rear +=1
        self.deque[self.rear]=data
    
    def dequeue_front(self):
        if self.is_empty():
            print("Deque is empty")
            return
        deleted_value=self.deque[self.front]
        self.deque[self.front]=None
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front+=1
        return deleted_value
    
    def dequeue_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return
        deleted_value=self.deque[self.rear]
        self.deque[self.rear]=None
        if self.rear==self.front:
            self.front=-1
            self.rear=-1
        else:
            self.rear-=1
        return deleted_value
        
    def peek_front(self):
        if self.is_empty():
            return None
        return self.deque[self.front]
        
    def peek_rear(self):
        if self.is_empty():
            return None
        return self.deque[self.rear]
        
    def display(self):
        if self.is_empty():
            return
        current=self.front
        while current != self.rear:
            print(self.deque[current])
            if current==self.size-1:
                current=0
            else:
                current+=1
        print(self.deque[current])
        
        
dq=Deque(10)
dq.is_empty()
dq.enqueue_front(20)
dq.enqueue_front(21)
dq.enqueue_front(22)
dq.enqueue_front(23)
print("deque front: ",dq.dequeue_front())
dq.enqueue_rear(45)
dq.enqueue_rear(49)
dq.enqueue_rear(48)
dq.enqueue_rear(46)
print("deque rear: ",dq.dequeue_rear())
print("Deque")
dq.display()
print("Front:",dq.peek_front())
print("Rear: ",dq.peek_rear())




    
        
# using collections.deque
from collections import deque

# Create a deque
dq = deque()

# Insert at both ends
dq.append(10)   # Add to rear
dq.append(20)
dq.appendleft(5)  # Add to front

print(dq)  # Output: deque([5, 10, 20])

# Remove from both ends
dq.pop()      # Remove from rear
dq.popleft()  # Remove from front

print(dq)  # Output: deque([10])
      
        
        
        
        
        
        