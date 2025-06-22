#class
class myClass:
    x = 5   
#calling the class
p1 = myClass() #object
print(p1.x)

#class with init init is used to initialise values executeed always when class is created
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
        
p1 = Person("jhon",31) # object created
print(p1.name) #object called
print(p1.age) #object called

#string representation


class Person2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person2("jhoncena", 36)

print(p1)

 #object methods
class Person3:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myfun(self):
        print("Hello my name is "+ self.name)
        
p1 = Person3("may",40)
p1.age=60
p1.myfun() #modify object properties
print(p1.age) 
del p1.age #show errror since deleted
print(p1.age)


        