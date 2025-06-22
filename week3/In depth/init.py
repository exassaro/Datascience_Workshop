class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greeet(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")
        
person = Person("alice",20)
person.greeet()