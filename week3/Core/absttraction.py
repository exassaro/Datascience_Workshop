from abc import ABC , abstractmethod #abstractmethod is a decorator that marks methods as abstract, 
#meaning they must be implemented in any subclass of the abstract base class.
class animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
class Dog(animal):
    def speak(self):
        return "bark"
    
dog = Dog()
print(dog.speak())