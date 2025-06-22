#  Implement queue using two stack

class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,x):
        self.s1.append(x)
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequemfrom empty queue")
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        
    def peek(self):
        if not self.s1 and not self.s2:
            raise IndexError("Dequemfrom empty queue")
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        
    def printQueue(self):
        """Prints the queue elements in FIFO order."""
        temp = self.s2[::-1] + self.s1  # Reverse s2 (already in correct order) and keep s1 as is
        print("Queue:", temp)
        
    def isEmpty(self):
        return not (self.s2 or self.s1)
        
queue=Queue()
queue.enqueue(10)
queue.enqueue(20) # queue using stack(first drop)
queue.enqueue(30)
queue.printQueue()
print(queue.dequeue())  # stack using queue(last drop)
print(queue.dequeue())
        
        
