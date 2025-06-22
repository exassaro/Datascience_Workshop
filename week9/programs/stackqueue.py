from collections import deque

class Stack:
    def __init__(self):
        self.q1=deque()
        self.q2=deque()
        
    def push(self,x):
        self.q1.append(x)
        
        
    def pop(self):
        if self.isEmpty():
            return None
        while len(self.q1)>1:
            self.q2.append(self.q1.popleft())
        value=self.q1.popleft()
        self.q1,self.q2=self.q2,self.q1
        return value

    def display(self):
        """Displays the stack elements (top to bottom)."""
        if self.isEmpty():
            return "Stack is empty"
        print("Stack (top to bottom):", list(self.q1)[::-1])
        
    def isEmpty(self):
        return len(self.q1)==0
        
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
stack.display()