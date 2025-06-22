class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class CLL:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
            self.head.next=self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=node
            node.next=self.head
    def display(self):
        if not self.head:
            return
        temp=self.head
        while True:
            print(temp.data,end="->")
            temp=temp.next
            if temp==self.head:
                break
        print("(Back to head)")
    
cll=CLL()
cll.append(51)
cll.append(40)
cll.append(20)
cll.display()    
