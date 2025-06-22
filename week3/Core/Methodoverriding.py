class Animal:
    def speak(self):
        print("animal class")
        
class Dog(Animal):
    def speak(self):
        print("dog class")
        
class Cat(Animal):
    def speak(self):
        print("cat class")
        
        
animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
cat.speak()
dog.speak()
        
        