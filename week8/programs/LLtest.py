class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
            
        itr.next=Node(data,None)
        
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
        
    def delete(self,value):
        if self.head is None:
            print("linked list is empty")
            return
        
        if self.head.data==value:
            self.head=self.head.next
            return
        
        prev=None
        itr=self.head
        while itr and itr.data!=value:
            prev=itr
            itr=itr.next
            
        if itr is None:
            print("value is not found")
            return
        
        prev.next=itr.next
        
        
    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr=self.head
        listr=''
        while itr:
            listr+=str(itr.data) + "->"
            itr=itr.next
            
        print(listr)
        
    
            
        
        
if __name__=="__main__":
    ll=LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_end(10)
    ll.insert_at_beginning(80)
    ll.insert_at_end(50)
    ll.insert_at_beginning(20)
    ll.print()
    
    print("Length:", ll.get_length())
    
    ll.delete(10)
    ll.print()