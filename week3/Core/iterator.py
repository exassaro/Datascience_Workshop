class Infinite():
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
        
    def __next__(self):
        num=self.num
        self.num+=1
        return num
        
x=Infinite()
print(next(x))