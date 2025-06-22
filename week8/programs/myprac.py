class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SLL:
    def __init__(self):
        self.head=None
        
    def insert_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=node
        
    def insert_beg(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def insert_arr(self,arr):
        for i in arr:
            node=Node(i)
            if self.head is None:
                self.head=node
                return
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=node
            
    def insert_bef(self,target,data):
        if self.head.data==target:
            node=Node(data,self.head)
            self.head=node
            return
        itr=self.head
        while itr.next and itr.next.data!=target:
            itr=itr.next
        node=Node(data,itr.next)
        itr.next=node
    
    def insert_aft(self,target,data):
        itr=self.head
        while itr and itr.data!=target:
            itr=itr.next
        node=Node(data,itr.next)
        itr.next=node
        
    def insert_pos(self,pos,data):
        if pos==1:
            node=Node(data,self.head)
            self.head=node
            return
        count=1
        itr=self.head
        while itr and count < pos-1:
            itr=itr.next
        node=Node(data,itr.next)
        itr.next=node
        
    def delete_beg(self):
        node=Node(self.head.next.data,self.head.next.next)
        self.head=node
        
    def delete_end(self):
        if self.head.next is None:
            self.head=None
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None
    
    def delete_elm(self,target):
        if self.head.data==target:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next and itr.next.data!=target:
            itr=itr.next
        itr.next=itr.next.next
        
    def delete_pos(self,pos):
        if pos==1:
            self.head=self.head.next
            return
        count=1
        itr=self.head
        while itr.next and count < pos-1:
            itr=itr.next
            count+=1
        itr.next=itr.next.next
        
    def middle(self):
        slow=self.head
        fast=self.head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
        
    def middle_del(self):
        slow=self.head
        fast=self.head
        prev=None
        while fast.next and fast.next.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
    
    def rmv_adjdup(self):
        itr=self.head
        while itr and itr.next:
            if itr.data==itr.next.data:
                itr.next=itr.next.next
            else:
                itr=itr.next
        return
    
    def rmv_dup(self):
        seen=set()
        itr=self.head
        prev=None
        while itr:
            if itr.data in seen:
                prev.next=itr.next
            else:
                seen.add(itr.data)
                prev=itr
            itr=itr.next
            
    def search(self,target):
        if self.head.data==target:
            print(f"{target} in 1")
            return
        
        itr=self.head
        pos=1
        while itr:
            if itr.data==target:
                print(f"{target} in {pos}")
                return
            itr=itr.next
            pos+=1
        return "Not found"
    
    def find_pos(self,pos):
        count=1
        itr=self.head
        while itr:
            if count==pos:
               return itr.data
            itr = itr.next
            count+=1
            
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
        
    def sort(self):
        curr=self.head
        while curr:
            next=curr.next
            while next:
                if curr.data>next.data:
                    curr.data,next.data=next.data,curr.data
                next=next.next 
            curr=curr.next
    
    def split(self):
        slow=self.head
        fast=self.head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        firsthalf=SLL()
        secondhalf=SLL()
        firsthalf.head=self.head
        secondhalf.head=slow
        prev.next=None
        return firsthalf,secondhalf
    
    def length(self):
        count=0
        curr=self.head
        while curr:
            curr=curr.next
            count+=1
        return count
    
    def to_circular(self):
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=self.head
        
    def detect_cycle(self):
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        
        
    def display(self):
        if self.head is None:
            return 
        itr=self.head
        while itr:
            print(itr.data,end="-->")
            itr=itr.next
        print("None")
        
    
        
sll=SLL()
sll.insert_end(40)
sll.insert_end(41)
sll.insert_end(42)
sll.insert_beg(52)
sll.insert_pos(2,200)
x=[1,3,3,4,2,5,8,6,10,200,5]
sll.insert_arr(x)
sll.insert_bef(5,10)
sll.insert_aft(2,100)
sll.display()
sll.delete_beg()
sll.delete_end()
sll.delete_elm(42)
sll.display()
sll.delete_pos(3)
sll.display()
print(sll.middle())
sll.middle_del()
sll.display()
sll.rmv_adjdup()
sll.display()
sll.rmv_dup()
sll.display()
sll.search(100)
print(sll.find_pos(5))
sll.reverse()
sll.display()
sll.sort()
sll.display()
print(sll.length())

print("Split to two:")
first_half, second_half = sll.split()

print("First Half:")
first_half.display()

print("Second Half:")
second_half.display()

sll.to_circular()
print(sll.detect_cycle())