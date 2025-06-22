#Hash implementation using Linked List

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
        self.table[index]=Node(key,value)#Overwrites if collision
        
    def delete(self,key):
        index=self.hash_function(key)
        if self.table[index] and self.table[index].key==key:
            self.table[index]=None
            return "key deleted"
        return "key not found"
    
    def get(self,key):
        index=self.hash_function(key)
        if self.table[index] and self.table[index].key==key:
            return self.table[index].value
        return "key not found"
    
    def display(self):
        for i ,node in enumerate(self.table):
            print(f"Index {i} : {(node.key,node.value) if node else None}")
            
            
ht=Hash(10)
ht.insert(12,"Apple")
ht.insert(33,"Banana")
ht.display()
print("Get 12:",ht.get(12))
    