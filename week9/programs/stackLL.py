class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
    
class Stack:
    def __init__(self):
        self.top=None
        self.__size=0
        
    def push(self,data):
        node=Node(data)
        node.next=self.top
        self.top=node
        self.__size+=1
        
    def pop(self):
        if not self.top:
            return "Stack is empty"
        popped_data=self.top.data
        self.top=self.top.next
        return popped_data
    def peek(self):
        if not self.top:
            return "Stack is empty"
        return self.top.data
        
    def length(self):
        return self.__size
    
    def display(self):
        if not self.top:
            return "stack is empty"
        temp=self.top
        while temp:
            print(temp.data,end="-->" if temp.next else "\n")
            temp=temp.next
            
stack=Stack()
stack.push(45)
stack.push(78)
stack.push(44)
stack.push(5)
stack.push(12)
stack.push(49)
stack.display()
print("Popped: ",stack.pop())
stack.peek()
stack.display()
stack.length()




 