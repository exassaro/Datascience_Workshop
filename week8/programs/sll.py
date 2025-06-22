class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Sll:
    def __init__(self):
        self.head=None
        
    #insert at end
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
        
    #insert in beginning
    def insert_begin(self,data):
        new_node=Node(data,self.head)
        self.head=new_node
    
    
    #length
    def length(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        return count
        
    #retrieve from specific index
    def get(self,index):
        if index>=self.length():
            print("Index out of range")
            return None
        curr_idx=0
        curr_node=self.head
        while curr_node:
            if curr_idx==index:
                return curr_node.data
            curr_node=curr_node.next
            curr_idx+=1
    
    #erase from specific index
    def erase(self,index):
        if index>=self.length():
            print("Index out of range")
            return None
        if index==0:
            self.head=self.head.next
            return
        curr_idx=0
        curr_node=self.head
        prev_node=None
        while curr_node:
            if curr_idx==index:
                prev_node.next=curr_node.next
                return
            prev_node=curr_node
            curr_node=curr_node.next
            curr_idx+=1
            
    #reverse
    def reverse(self):
        if not self.head:
            return None
        if self.head.next is None:
            return self.head
        curr=self.head
        prev=None
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev
    
    #find the num and position
    def find(self,data):
        pos=1
        curr=self.head
        while curr:
            if curr.data==data:
                print(pos)
                return
            curr=curr.next
            pos+=1
        print("Not found")  # If not found
        return -1
    
    #find middle
    def middle(self):
        if not self.head:
            return
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
            
    #delete middle
    def del_middle(self):
        if not self.head:
            return
        slow=self.head
        fast=self.head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
    
    #split
    def split(self):
        if not self.head:
            return None
        slow=self.head
        fast=self.head
        prev=None
        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next
        first_half=Sll()
        second_half=Sll()
        first_half.head=self.head
        second_half.head=slow
        prev.next=None
        return first_half,second_half
        
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
        
sll=Sll()
sll.append(12)
sll.append(28)
sll.append(87)
sll.append(18)
sll.append(26)
sll.append(41)
sll.insert_begin(40)
print(sll.length())
print(sll.get(0))
sll.display()
sll.erase(1)
sll.display()
sll.reverse()
sll.display()
sll.split()