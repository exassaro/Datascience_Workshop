

class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

#Createing Double Linked List
class Dll:
    def __init__(self):
        self.head=None
        
    #insert end
    def insert_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=node
        node.prev=curr
        
    #insert begin
    def insert_beg(self,data):
        node=Node(data,self.head)
        if self.head:
            self.head.prev=node
        self.head=node
    
    #insert before an element
    def insert_bef(self,target,data):
        if self.head is None:
            print("List is empty!")
            return
        curr=self.head
        while curr and curr.data!=target:
            curr=curr.next
        if curr is None:
            print(f"Element {target} not found")
            return
        node=Node(data,curr,curr.prev)
        if curr.prev:
            curr.prev.next=node
        else:
            self.head=node # If inserting before head, update head
        curr.prev=node
    
    #insert after a given elemnt
    def insert_aft(self,target,data):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head
        while curr and curr.data!=target:
            curr=curr.next
        if curr is None:
            print(f"Element {target} not found")
            return
        node=Node(data,curr.next,curr)
        if curr.next:
            curr.next.prev=node
        curr.next=node
        
    #insert array
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
        
    
    #insert in specific position
    def insert_pos(self,pos,data):
        if pos<1:
            print("Invalid")
            return
        node=Node(data)
        if pos==1:
            node.next=self.head
            if self.head:
                self.head.prev=node
            self.head=node
            return
        curr=self.head
        count=1
        while curr and count < pos-1:
            curr=curr.next
            count+=1
        if curr is None:
            print("position out of range")
            return
        node.next=curr.next
        node.prev=curr
        if curr.next:
            curr.next.prev=node
        curr.next=node
    #delete begining
    def delete_beg(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next
        if self.head:
            self.head.prev=None
    
    #delete at end        
    def delete_end(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        curr = self.head
        while curr.next:
            curr=curr.next
        curr.prev.next=None
    
    #delete specific element    
    def delete_elmnt(self,target):
        if self.head is None:
            print("List is empty")
            return
        curr=self.head
        while curr and curr.data!=target:
            curr =curr.next
        if curr is None:
            print(f"Element {target} not found")
            return
        if curr.prev:
            curr.prev.next=curr.next
        if curr.next:
            curr.next.prev=curr.prev
        if curr==self.head:
            self.head=curr.next
            
    #delete specific position
    def delete_pos(self,pos):
        if self.head is None:
            print("List is empty")
            return
        if pos<1:
            print("Invalid pos")
            return
        curr=self.head
        count=1
        while curr and count<pos:
            curr=curr.next
            count+=1
        if curr is None:
            print("Position out of range")
            return
        if curr.prev:
            curr.prev.next=curr.next
        if curr.next:
            curr.next.prev=curr.prev
        if curr==self.head:
            self.head=curr.next
    #serch element
    def search(self,target):
        curr=self.head
        pos=1
        while curr:
            if curr.data==target:
                return pos
            curr=curr.next
            pos+=1
        return "Element not found"
     
    #find element in specific position  
    def find_pos(self,pos):
        if pos<1:
            print("Invalid position")
            return None
        curr=self.head
        count=1
        while curr:
            if count==pos:
                return curr.data
            curr=curr.next
            count+=1
        print("Pos out of range")
        return None
        
    #Find middle
    def find_mid(self):
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data if slow else None
        
    #delete middle
    def delete_mid(self):
        if self.head is None:
            return
        slow=fast=self.head
        prev=None
        while fast and fast.next:
            prev=slow
            slow =slow.next
            fast=fast.next.next
        if prev:
            prev.next=slow.next
        if slow.next:
            slow.next.prev=prev
        if slow==self.head:
            self.head=slow.next
            
    #remove duplicate
    def rmv_dup(self):
        if self.head is None:
            return
        seen=set()
        curr=self.head
        while curr:
            if curr.data in seen:
                curr.prev.next=curr.next
                if curr.next:
                    curr.next.prev=curr.prev
            else:
                seen.add(curr.data)
            curr=curr.next
            
    #remove adjacent duplicate
    def rmv_adjdup(self):
        curr=self.head
        while curr and curr.next:
            if curr.data==curr.next.data:
                curr.next=curr.next.next
                if curr.next:
                    curr.next.prev = curr
            else:
                curr=curr.next
    
    #find length
    def length(self):
        curr=self.head
        count=0
        while curr:
            curr=curr.next
            count+=1
        return count
        
    #reverse
    def reverse(self):
        curr=self.head
        prev=None
        while curr:
            next_node=curr.next
            curr.next=prev
            curr.prev=next_node
            prev=curr
            curr=next_node
        self.head=prev
    
    #sort
    def sort(self):
        if self.head is None:
            return
        curr=self.head
        while curr:
            next_node=curr.next
            while next_node:
                if curr.data>next_node.data:
                    curr.data,next_node.data=next_node.data,curr.data
                next_node=next_node.next
            curr=curr.next
    #Split 
    def split(self):
        if self.head is None:
            return None,None
        slow=fast=self.head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        first_half=Dll()
        second_half=Dll()
        first_half.head=self.head
        second_half.head=slow
        if prev:
            prev.next=None
        if slow:
            slow.prev=None
        
        print("First half:")
        first_half.display()
        print("Second half:")
        second_half.display()
        
        return first_half, second_half
    
    #Detect Cycle
    def detect_cycle(self):
        slow=fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        
        
    #display
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="<-->")
            temp=temp.next
        print("none")
        
        
        
dll=Dll()
dll.insert_beg(10)
dll.insert_beg(22)
dll.insert_end(45)
dll.insert_aft(10,15)
dll.insert_bef(22,12)
dll.insert_pos(5,86)
print("Insertion operations(beggining/end/after element/before element/position): ")
dll.display()
dll.delete_pos(2)
dll.delete_beg()
dll.delete_end()
dll.delete_elmnt(15)
print("Deletion operations(pos/beggining/end/element): ")
dll.display()
x=[3,4,5,87,65,21,34]
dll.insert_arr(x)
print("array inserted: ")
dll.display()
print(dll.find_pos(4))
print("find element at position 4: ")
print(dll.search(65))
print("Find position of element 65: ")
dll.display()
print("find mid: ")
print(dll.find_mid())
dll.delete_mid()
print("Mid deleted: ")
dll.display()
x=[34,41,5,87,87,65,21,34,34]
dll.insert_arr(x)
print("array inserted: ")
dll.display()
print("adjacent duplicate removed: ")
dll.rmv_adjdup()
dll.display()
print("duplicates removed:")
dll.rmv_dup()
dll.display()
print("length of list:")
print(dll.length())
dll.reverse()
print("reversed list:")
dll.display()
print("sorted List: ")
dll.sort()
dll.display()
dll.split()
print("Cycle detected:", dll.detect_cycle())
