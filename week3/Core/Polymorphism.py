#class polymorphism
class Car:
    def __init__(self,brand,model):
        self.Brand=brand
        self.Model=model
        
    def move(self):
        print("Move!")
        
class Boat:
    def __init__(self,brand,model):
        self.Brand=brand
        self.Model=model
        
    def move(self):
        print("Sail")
        
car = Car("mustang",1998)
boat = Boat("Ibiza",2020)

for x in (car,boat):
    x.move()