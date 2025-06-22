class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
        
class Dll:
    def __init__(self):
        self.head=None
    def insert(self,data):
        node=Node(data,self.head)
        if self.head:
            self.head.prev=node
        self.head=node
        
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="<-->")
            temp=temp.next
        print("None")
        
dll=Dll()
dll.insert(20)
dll.insert(30)
dll.insert(10)
dll.display()