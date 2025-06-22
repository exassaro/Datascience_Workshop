class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
        
    def enqueue(self,data):
        node=Node(data)
        self.count+=1
        if not self.head:
            self.head=node
            self.tail=self.head
        else:
            self.tail.next=node
            self.tail=self.tail.next
        
    def dequeue(self):
        if not self.head:
            raise IndexError("Queue is underflow")
        dequeued_value=self.head.data
        self.head=self.head.next
        self.count-=1
        if self.head is None:
            self.tail=None
        return dequeued_value
        
    def is_empty(self):
        return self.head is None
    
    def peek(self):
        if not self.head:
            return None
        return self.head.data
    
    def __len__(self):
        return self.count
    
    def __iter__(self):
        temp=self.head
        while temp:
            yield temp.data
            temp=temp.next
            
que=Queue()
print(len(que))
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)

for i in que:
    print(i)
    
que.dequeue()

print(list(que))  # Converts to list before printing

        