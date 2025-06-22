#Hash implementation using Linked List with chain handling

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        
class Hash:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size #array storing head in nodes
    
    def hash_function(self,key):
        return key % self.size
        
    def insert(self,key,value):
        index=self.hash_function(key)
        node=Node(key,value)#Overwrites if collision
        if self.table[index] is None:
            self.table[index]=node
        else:
            curr=self.table[index]
            while curr:
                if curr.key==key:
                    curr.value=value
                    return
                if curr.next is None:
                    break
                curr=curr.next
            curr.next=node
            
            
    def delete(self,key):
        index = self.hash_function(key)
        curr = self.table[index]
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next  # Remove node from the chain
                else:
                    self.table[index] = curr.next  # Update head
                return True  # Key deleted
            prev = curr
            curr = curr.next
        return False 
    
    def get(self,key):
        index=self.hash_function(key)
        curr=self.table[index]
        while curr:
            if curr.key==key:
                return curr.value
            curr=curr.next
        return "key Not found"
    
    

        
    def display(self):
        for i,node in enumerate(self.table):
            values=[]
            current=node
            while current:
                values.append(f"({current.key},{current.value})")
                current=current.next
            print(f"Index {i} : {'-->'.join(values) if values else None}")
        
        
            
            
ht=Hash(10)
ht.insert(12,"Apple")
ht.insert(22,"Banana")
ht.insert(32, "Cherry") 
ht.display()
print("Get 22:",ht.get(22))
    