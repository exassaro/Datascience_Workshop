#implementing Hash table with array with collision Handling
class Hash:
    def __init__(self,size):
        self.size=size
        self.table=[[]for i in range(size)]
        
    def hash_function(self,key):
        return hash(key) % self.size #simple modulo hash
        
    def insert(self,key,value):
        index=self.hash_function(key)
        self.table[index].append((key,value))
    
    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove key-value pair
                return "Key deleted"
        return "Key not found"
    
    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:  # Iterate correctly
            if k == key:
                return v
        return "Not found"  # Should be outside the loop
       
    def display(self):
        for i,val in enumerate(self.table):
            print(f"Index {i} : {val} ")
            
ht=Hash(9)
ht.insert(34,'dfdf')
ht.insert((234,34),"sggaiu")
ht.display()
print("get 34",ht.get(34))
print("Get (234, 34):", ht.get((234, 34)))  # Should return 'sggaiu'
ht.delete(34)
ht.display()