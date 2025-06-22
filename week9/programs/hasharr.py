#implementing Hash table with array without collision Handling
class Hash:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
        
    def hash_function(self,key):
        return key % self.size #simple modulo hash
        
    def insert(self,key,value):
        index=self.hash_function(key)
        self.table[index] = value 
    
    def get(self,key):
        index=self.hash_function(key)
        return self.table[index] if self.table is not None else "Key not found"
    
    
    def delete(self,key):
        index=self.hash_function(key)
        if self.table[index]:
            self.table[index] = None
        else:
            print("Not found")
            
            
    def display(self):
        for i,val in enumerate(self.table):
            print(f"Index {i} : {val} ")
            
ht=Hash(10)
ht.insert(12,"Apple")
ht.insert(22,"Banana")
ht.display()
print("get 12",ht.get(12))