class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class DLL:
    def __init__(self):
        self.head=None
    def insert(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=node
        node.prev=curr
        
    def insert_beg(self,data):
        node=Node(data,self.head)
        self.head.prev=node
        self.head=node
        
    def insert_arr(self,arr):
        for data in arr:
            if self.head is None:
                self.head=Node(data)
            else:
                curr=self.head
                while curr.next:
                    curr=curr.next
                node=Node(data)
                curr.next=node
                node.prev=curr
    def insert_pos(self,pos,data):
        node=Node(data)
        if pos==1:
            node.next=self.head
            if self.head:
                self.head.prev=node
            self.head=node
            return
        curr=self.head
        count=1
        while curr and count<pos-1:
            curr=curr.next
            count+=1
        node.next=curr.next
        node.prev=curr
        if curr.next:
            curr.next.prev=node
        curr.next=node
    
    def insert_bef(self,target,data):
        curr=self.head
        while curr and curr.data!=target:
            curr=curr.next
        node=Node(data,curr,curr.prev)
        if curr.prev:
            curr.prev.next=node
        else:
            self.head=node
        curr.prev=node
    
    def insert_aft(self,target,data):
        curr=self.head
        while curr and curr.data!=target:
            curr=curr.next
        node=Node(data,curr.next,curr)
        if curr.next:
            curr.next.prev=node
        curr.next=node
    
    def delete_beg(self):
        self.head=self.head.next
        if self.head:
            self.head.prev=None
    def delete_end(self):
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.prev.next=None
        
    def delete_pos(self,pos):
        curr=self.head
        count=1
        while curr and count< pos:
            curr=curr.next
            count+=1
        if curr.prev:
            curr.prev.next=curr.next
        if curr.next:
            curr.next.prev:curr.prev
        if curr==self.head:
            self.head=curr.next
            
    def delete_elmnt(self,target):
        curr=self.head
        while curr and curr.data!=target:
            curr=curr.next
        if curr.prev:
            curr.prev.next=curr.next
        if curr.next:
            curr.next.prev:curr.prev
        if curr==self.head:
            self.head=curr.next
    
    def middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
        
    def del_middle(self):
        slow=self.head
        fast=self.head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev:
            prev.next=slow.next
        if slow.next:
            slow.next.prev=prev
        if slow==self.head:
            self.head=slow.next
    def search(self,target):
        curr=self.head
        count=1
        while curr.data!=target:
            curr=curr.next
            count+=1
        return count
        
    def find_pos(self,pos):
        curr=self.head
        count=1
        while curr:
            if count==pos:
                return curr.data
            cur==curr.next
            count+=1
      
    def adj_dup(self):
        curr=self.head
        while curr and curr.next:
            if curr.data==curr.next.data:
                curr.next=curr.next.next
                if curr.next:
                    curr.next.prev=curr
            else:
                curr=curr.next
    def rmv_dup(self):
        seen=set()
        curr=self.head
        while curr.next:
            if curr.data in seen:
                curr.prev.next=curr.next
                if curr.next:
                    curr.next.prev=curr.prev
            else:
                seen.add(curr.data)
            curr=curr.next
            
    def reverse(self):
        curr=self.head
        prev=None
        while curr:
            next=curr.next
            curr.next=prev
            curr.prev=next
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
        firsthalf=DLL()
        sechalf=DLL()
        firsthalf.head=self.head
        sechalf.head=slow
        if prev:
            prev.next=None
        if slow:
            slow.prev=None
            
        print("First half:")
        firsthalf.display()
        print("Second half:")
        sechalf.display()
        
        return firsthalf, sechalf
            
        
    
    def length(self):
        curr=self.head
        count=0
        while curr:
            curr=curr.next
            count+=1
        return count
            
                
            
        
        
        
        
    def display(self):
        if self.head is None:
            return
        curr=self.head
        while curr:
            print(curr.data,end="<-->")
            curr=curr.next
        print("None")


dll=DLL()
dll.insert(45)
dll.insert(41)
dll.insert(42)
dll.insert_beg(56)
dll.insert_pos(2,100)
x=[2,3,4,4,5,6,7,71,71,2,1,100]
dll.insert_arr(x)
dll.insert_bef(5,800)
dll.insert_aft(7,850)
dll.display()
dll.delete_end()
dll.delete_pos(5)
dll.delete_elmnt(850)
dll.display()
print(dll.middle())
dll.del_middle()
dll.display()
print(dll.search(7))
print(dll.search(100))
dll.adj_dup()
dll.rmv_dup()
dll.display()
print(dll.length())
dll.reverse()
dll.display()
dll.sort()
dll.display()
dll.split()