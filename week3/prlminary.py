# CONSTRUCTOR AND DESTRUCTOR
# class conanddes:
#     def _init_(self,name,age):
#         self.name=name
#         self.age=age
#     def _del_(self):
#         pass
# obj1=conanddes("shamil",21)
# del obj1.age
# try:
#     print(obj1.name)
#     print(obj1.age)
# except:
#     print("age is deleted")
from platform import platform


# GENERATOR
# class Generator:
#     def generator(self):
#         yield 32
#         yield 65
#         yield 78
#         yield 34
# obj=Generator()
# v=obj.generator()
# # print(next(v))
# # print(next(v))
# # print(next(v))
# # print(next(v))
# # OR
# for i in v:
#     print(i)

# ITERATOR
# class Iterator:
#     def _iter_(self):
#         self.y=1
#         return self
#     def _next_(self):
#         y=self.y
#         self.y+=2
#         return y
# obj=Iterator()
# v=iter(obj)
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))

## OOPS CONCEPT##
# INHERITANCE
# class parent:
#     def _init_(self,father,mother):
#         self.father=father
#         self.mother=mother
# class child(parent):
#     def _init_(self,name,age,father,mother):
#         self.name=name
#         self.age=age
#         super()._init_(father,mother)
# child1=child("shamil",21,"gafoor","sabira")
# child2=child("ashmil",17,"gafoor","sabira")
# print("1:",child1.name,child1.age,child1.father,child1.mother)
# print("2:",child2.name,child2.age,child2.father,child2.mother)

#MULTILEVEL INHERiITENCE
# class Multiinheritnece:
#     def _init_(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
# class child(Multiinheritnece):
#     def _init_(self,name,age,place,gender):
#         self.gender=gender
#         super()._init_(name,age,place)
# class detailed(child):
#     def _init_(self,name,age,place,gender):
#         super()._init_(name,age,place,gender)
#     def display(self):
#         print(f"name is:{self.name}")
#         print(f"age is:{self.age}")
#         print(f"place is:{self.place}")
#         print(f"gender is:{self.gender}")
#
# childs=detailed("sheikh","21","thachanna","non disclosable")
# print(childs.display())

# ABSTRACTION
# from abc import ABC,abstractmethod
#
# class Abstraction(ABC):
#     @abstractmethod
#     def parameter(self):
#         pass
# class Toyota(Abstraction):
#     def _init_(self,name,model):
#         self.name=name
#         self.model=model
#     def parameter(self):
#         return f"name:,{self.name}, model: {self.model}"
# car1=Toyota("fortuner",2024)
# car2=Toyota("Hilux",2020)
# print(car1.parameter())
# print(car2.parameter())

#ENCAPSULATON
# class Encapsulation:
#     def _init_(self,name,age,place):
#         self.name=name
#         self._age=age
#         self.__place=place
#
# name1=Encapsulation("shamil",21,"omassery")
# name2=Encapsulation("sheikh",21,"areekode")
# print(name1.name,name1.age,name1._Encapsulation_place)
# print(name2.name,name2.age,name2._Encapsulation_place)

# POLYMORPHISM ( methods with the same name behaving differently depending on the object calling them)
# class bird:
#     def sound(self):
#         return "Bird crack"
# class cat:
#     def sound(self):
#         return "Cat mweow"
# Bird1=bird()
# Cat1=cat()
# print(Bird1.sound())
# print(Cat1.sound())

# OVERRIDIING (Allow subclasses to customize methods that is already provide by parent class)
# class Animal:
#     def sound(self):
#         pass
# class bird(Animal):
#     def sound(self):
#         return "Bird crack"
# class cat(Animal):
#     def sound(self):
#         return "Cat mweow"
# Bird1=bird()
# Cat1=cat()
# print(Bird1.sound())
# print(Cat1.sound())

# METHOD OVERLOADING (Saame name different paramter)
# class calculator():
#     def add(self,a,b=None,c=None):
#         if b is None and c is None:
#             return a
#         elif c is None:
#             return a+b
#         else:
#             return a+b+c
# cal=calculator()
# print(cal.add(10))
# print(cal.add(10,20,30))

# Bank example
# class Bank:
#     def _init_(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposite(self,amount):
#         self.balance+=amount
#         print(f"{self.name} deposited {amount} and your balance is {self.balance}")
#     def withdrawn(self,amount):
#         if amount<self.balance:
#             self.balance-=amount
#             print(f"{self.name} withdrawn {amount} and your balance is {self.balance}")
#         else:
#             print("you have no enough money")
# cus1=Bank("ashmil",1000)
# print(cus1.name,cus1.balance)
# cus1.deposite(500)
# cus1.withdrawn(3300)

# RECURSION ( a function that calling inside in that function)
# ex: febinocci
# def feb(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return feb(num-1)+feb(num-2)
# for i in range(11):
#     print(feb(i))

# example:factorial
# def factorial(num):
#     if num<=1:
#         return 1
#     else:
#         return num*factorial(num-1)
#
# print(factorial(5))

# error handling
# try:
#     result=10/5
# except ZeroDivisionError:
#     print("not divisible by zero")
# else:
#     print("division succesfull",result)
# finally:
#     print("execution complete")