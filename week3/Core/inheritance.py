class Person:
    def __init__(self,f_name,l_name):
        self.firstname=f_name
        self.lastname=l_name
    def printname(self):
        print(self.firstname, self.lastname)
        
x = Person("jhon","Doe")
x.printname()

# calling child class with parent class as parameter inside child class
class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

class Student2(Person):
    def __init__(self,f_name,l_name): #called init functiion but inheritance broken
        Person.__init__(self,f_name,l_name) #kept inheritance back (also we can use= super().__init__(f_name,l_name))
        
        
x = Student2("Rodri", "Matts")
x.printname()

class Student3(Person):
    def __init__(self,f_name,l_name,year): 
        super().__init__(f_name,l_name)
        self.graduationyear=year #Added new property year
        
    def welcome(self):
        print("welcome" , self.firstname , self.lastname , "passed in" , self.graduationyear) #method inside child class function
        
x = Student3("Cristiano","ronaldo",2019) 
print(x.graduationyear)
x.welcome()