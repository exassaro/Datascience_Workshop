class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    def is_empty(self):
        return len(self.stack)==0
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
        
    def size(self):
        return len(self.stack)
        
    def display(self):
        print("Stack :",self.stack)
        
stack=Stack()
stack.push(4)
stack.push(5)
stack.push(10)
stack.push(14)
stack.push(51)
stack.push(19)
stack.display()
print("Popped: ",stack.pop())
stack.peek()
stack.size()
stack.display()


