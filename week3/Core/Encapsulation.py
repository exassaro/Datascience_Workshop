class person:
    def __init__(self,name,age):
        self.name = name #public attribute
        self.__age= age #private attribute
        
    def get_age(self):
        return self.__age
        
    def set_age (self,age):
        if age>0:
            self.__age=age
        else:
            print("invalid")
    
Person = person("alice",25)

print (Person.name)
print (Person.get_age())

Person.set_age(30)
print(Person.get_age())