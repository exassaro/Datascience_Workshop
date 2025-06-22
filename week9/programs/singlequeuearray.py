#single Queue using array
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)  # Add item to the back of the queue

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)  # Remove item from the front of the queue
        else:
            return "Queue is empty"

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]  # View the front element without removing it
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0  # Check if the queue is empty

    def size(self):
        return len(self.queue)
        
    def display(self):
        if self.queue is None:
            return "Queue is empty"
        print(self.queue)
        
q = Queue()
q.display()
q.is_empty()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.dequeue())
print(q.peek()) 
q.display()