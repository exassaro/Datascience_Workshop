# from abc import ABC,abstractmethod
#
# class abstract(ABC):
#     @abstractmethod
#     def parameter(self):
#         pass
# class name(abstract):
#     def _init_(self,name,age):
#         self.name=name
#         self.age=age
#     def parameter(self):
#         return f"name:{self.name},age:{self.age}"
# v=name("sheikh",21)
# print(v.parameter())
# import copy
# from array import array



# students = [
#     {"name": "Alice", "math": 85, "science": 90, "english": 78},
#     {"name": "Bob", "math": 92, "science": 88, "english": 95},
#     {"name": "Charlie", "math": 70, "science": 65, "english": 72},
#     {"name": "Daisy", "math": 95, "science": 92, "english": 89}
# ]
# for student in students:
#     student["average"]=(student["math"]+student["science"]+student["english"])/3
# students.sort(key=lambda x:x["average"],reverse=True)
# for student in students:
#   print(student["name"],student["average"])
#
# print("high")
# print(students[0]["name"],students[0]["average"])

# def vovel():
#     text=str(input("enter a text"))
#     list=[]
#     count=0
#     vov="aeiouAEIOU"
#     for i in text:
#         if i in vov:
#             list.append(i)
#             count+=1
#     print(list)
#     print(count)
# vovel()


# dic1={'a':21,'b':32}
# dic2={'c':31}
# for i,j in dic2.items():
#     dic1[i]=j
# print(dic1)


# def decorator(func):
#     def wrapping():
#         print("hello")
#         func()
#     return wrapping
# @decorator
# def name():
#     print("sheikh")
# name()

# class forest():
#     def _init_(self,animal_name):
#         self.animal_name=animal_name
# class animal(forest):
#     def _init_(self,name,age,animal_name):
#         self.name=name
#         self.age=age
#         super()._init_(animal_name)
# aniaml1=animal("tiger",21,"periyar")
# print(f"name:{aniaml1.name},age:{aniaml1.age},place:{aniaml1.animal_name}")


# class mark():
#     def _init_(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def _add_(self, other):
#         x=self.m1+self.m2
#         y=other.m1+other.m2
#         z=x+y
#         return z
# result=mark(21,34)
# result2=mark(32,43)
# v=result+result2
# print(v)

# method over riding
# class calculator():
#     def add(self,x,y=0,z=0):
#         self.x=x
#         self.y=y
#         self.z=z
#         return x+y+z
# numbers=calculator()
# print(numbers.add(10))
# print(numbers.add(10,20))
# print(numbers.add(10,20,30))

# method overloading
# class dog():
#     def sound(self):
#         return "dow"
# class cat():
#     def sound(self):
#         return "meoww"
# dog=dog()
# cat=cat()
# print(dog.sound())
# print(cat.sound())



# def first(a):
#     def second(b):
#         return a+b
#     return second
# v=first(10)
# w=v(20)
# print(w)


# class itrator():
#     def _iter_(self):
#         self.x=1
#         return self
#     def _next_(self):
#         x=self.x
#         self.x+=1
#         return x
# value=itrator()
# v=iter(value)
# print(next(v))
# print(next(v))



# class itrator():
#     def _iter_(self):
#         self.x=1
#         return self
#     def _next_(self):
#         x=self.x
#         self.x*=2
#         return x
# value=itrator()
# v=iter(value)
# print(next(v))
# print(next(v))
# print(next(v))




# def generator():
#     yield 2
#     yield 4
#     yield 6
# gen=generator()
# print(next(gen))
# print(next(gen))


# def generator():
#     yield 2
#     yield 4
#     yield 6
# gen=generator()
# for i in gen:
#     print(i)


# array=[1,2,4,5,6]
# expect_sum=(len(array)+1)*(len(array)+2)//2
# actual_sum=0
# for i in array:
#     actual_sum+=i
# missing_num=expect_sum-actual_sum
# print(missing_num)



# num=int(input("enter  a number"))
# for i in range(1,11):
#     print(f"{i}*{num}={i*num}")



# list=[["sheikh"]]
# shallow=copy.copy(list)
# shallow[0][0]=[["shamil"]]
# print(list)
# print(shallow)


# list=["sheikh"]
# deep=copy.deepcopy(list)
# deep[0]=[["sarfras"]]
# print(list)
# print(deep)


# list=[1,2,3,3,4,5,6,6,7,8]
# dic={}
# for i in list:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)


# def reverse(name):
#     list=""
#     for i in range(len(name)-1,-1,-1):
#         list+=name[i]
#     return list
# name=str(input("enter a name"))
# v=reverse(name)
# print(v)


# def name_reverse(name):
#     list=name.split()
#     new=""
#     for i in range(len(list)-1,-1,-1):
#         new+=list[i]+" "
#     return new
# name=str(input("enter a word"))
# v=name_reverse(name)
# print(v)


# def two_sum(num):
#     target=9


# target=9
# list=[1,2,3,4,5,6,7,8,9]
# new=[]
# for i in range(len(list)):
#     for j in range(i,len(list)):
#         if list[i]+list[j]==target:
#             new.append((list[i],list[j]))
# print(new)




# class calculator():
#     def add(self,x,y):
#         return x+y
#     def add_tree(self,x,y,z):
#         return x+y+z
#     def add_four(self,x,y,z,w):
#         return x+y+z+w
#
# numbers=calculator()
# print(numbers.add(10,21))
# print(numbers.add_tree(10,20,54))
# print(numbers.add_four(10,20,30,45))


# def factorial(num):
#     count=1
#     for i in range(1,num+1):
#         count*=i
#     return count
# num=int(input("enter a number"))
# v=factorial(num)
# print(v)


# list=[1,2,3,4,5,6,7]
# list_comp=[i for i in list if i%2==0]
# print(list_comp)



# list=[1,2,3,4,5,6,7]
# list_comp=["1" if i%2==0 else "0" for i in list]
# print(list_comp)


# list1=[1,2,3,4,55,6]
# list2=[1,2,3,4,5,6]
# result=list(map(lambda x,y:x+y,list1,list2))
# print(result)


# list1=[1,2,3,4,5,6,7]
# list2=[1,2,4,3,6,5,7,6]
# result=list(map(lambda x,y:x+y,list1,list2))
# print(result)


# list1=[1,2,3,4,55,6]
# list2=[1,2,3,4,5,6]
# result=list(zip(list1,list2))
# print(result)

# list1=[1,2,3,4,5,6]
# list2=[1,2,3,4,5,6]
# result=list(zip(list1,list2))
# print(result)



# x=lambda x,y:x+y
# print(x(10,20))




# def positive(num):
#     positive=0
#     for i in range(len(num)):
#         if num[i]>0:
#             positive+=num[i]
#     return positive
# num=[1,2,3,4,5,-4,3,-4,-3,-2,-2,2,-3]
# v=positive(num)
# print(v)


# class a:
#     pass
# class b(a):
#     pass
# class c(b):
#     pass
# print(c.mro())

# fruits=["apple","orange","grape"]
# print("pinaple" in fruits)
# print("pinaple" not in fruits)


# class constructor:
#     def _init_(self, name,age):
#         self.name = name
#         self.age=age
#         print( "object has created")
#     def _del_(self):
#         print("object has deleted")
# obj=constructor("sheikh",21)
# del obj.age
# try:
#     print(obj.name)
#     print(obj.age)
# except:
#     print(" age is deleted")


# class private():
#     def _init_(self,name,age):
#         self.__name=name
#         self.__age=age
#     def namee(self):
#         return self.__name
#     def agee(self):
#         return self.__age
# obj=private("sheikh",21)
# v=obj
# print(v.namee(),v.agee())



# class public():
#     def _init_(self,name,age):
#         self.name=name
#         self.age=age
#     def main(self):
#         return {f"name":{self.name},"age":{self.age}}
# obj=public("sheikh",21)
# print(obj.name)
# print(obj.age)
# print(obj.main())


# class Public:
#     def _init_(self, name, age):
#         self.name = name  # Public attribute
#         self.age = age  # Public attribute
#
#     # Public method
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# # Creating an object of the Public class
# obj = Public("Sheikh", 21)
#
# # Accessing public attributes directly
# print(obj.name)  # Output: Sheikh
# print(obj.age)  # Output: 21
#
# # Calling the public method
# obj.display_info()  # Output: Name: Sheikh, Age: 21



# class duplicates():
#     def dupli(self,array):
#         self.array=array
#     def multi(self):
#         dic={}
#         for i in self.array:
#             if i in dic:
#                 dic[i]+=1
#             else:
#                 dic[i]=1
#         return dic
# array=[1,2,3,3,4,5,5,6,7,7]
# v=duplicates()
# v.dupli(array)
# result=v.multi()
# print(result)


# class remove_duplicate():
#     def duplicate(self,array):
#         self.array=array
#     def remove(self):
#         list=[]
#         for i in self.array:
#             if i not in list:
#                 list.append(i)
#         return list
# array=[1,2,3,3,4,5,6,6,7,8]
# v=remove_duplicate
# v.remove(array)
# result=v.remove()
# print(result)




# list=[1,2,3,4,4,5,6,7]
# new=[]
# for i in list:
#     if i not in new:
#         new.append(i)
# print(new)



# class duplicate():
#     def _init_(self,array):
#         self.array=array
#     def remove(self):
#         list=[]
#         for i in self.array:
#             if i not in list:
#                 list.append(i)
#         return list
# array=[1,2,2,3,4,4,5,6,7,7,8]
# v=duplicate(array)
# result=v.remove()
# print(result)



# class longesttt():
#     def _init_(self,word):
#         self.word=word
#     def longest(self,n):
#         self.n=n
#         list=self.word.split()
#         new=[]
#         for i in list:
#             if len(i)>self.n:
#                 new.append(i)
#         return new
# word=str(input("enter a word"))
# v=longesttt(word)
# result=v.longest(4)
# print(result)


# class longest():
#     def _init_(self,word):
#         self.word=word
#     def long(self):
#         list=self.word.split()
#         new=" "
#         for i in list:
#             if len(i)>len(new):
#                 new=i
#         return new
# word=str(input("enter a name"))
# v=longest(word)
# result=v.long()
# print(result)


# list=[1,2,3,4,5,6,7]
# max=list[0]
# for i in range(1,7):
#     if max<list[i]:
#         max=list[i]
# print(max)
# second_max=list[0]
# for i in range(1,7):
#     if second_max<list[i]!=max:
#         second_max=list[i]
# print(second_max)


from abc import ABC,abstractmethod
from itertools import count
from math import factorial

from django.core.files.locks import kernel32
from django.db.models.fields import return_None

# class abstract(ABC):
#     @abstractmethod
#     def parameter(self):
#         pass
# class benz(abstract):
#     def _init_(self,name,model):
#         self.name=name
#         self.model=model
#     def parameter(self):
#         return f"name:{self.name},model:{self.model}"
# obj=benz("cclass",221)
# v=obj
# print(v.parameter())



# try:
#     print(2/0)
# except:
#     print(2+2)
# else:
#     print("2+1 is working")
# finally:
#     print("working properly")



# name=[["sheikh"]]
# shallow=copy.copy(name)
# shallow[0][0]=["shamil"]
# print(shallow)
# print(name)



# name=["shamil"]
# deep=copy.deepcopy(name)
# deep[0]=[["sheikh"]]
# print(deep)
# print(name)



# students = [
#     {"name": "Alice", "math": 85, "science": 90, "english": 78},
#     {"name": "Bob", "math": 92, "science": 88, "english": 95},
#     {"name": "Charlie", "math": 70, "science": 65, "english": 72},
#     {"name": "Daisy", "math": 95, "science": 92, "english": 89}
# ]
# for student in students:
#     student["average"]=(student["math"]+student["science"]+student["english"])/3
# students.sort(key=lambda x:x["average"],reverse=True)
# for student in students:
#     print(student["name"],student["average"])
# print("student who scored high mark")
# print(students[0]["name"],students[0]["average"])


# word=open('simple.txt','r')
# r=word.read()
# print(r)
#
# def total_lines(r):
#     count=1
#     for j in r:
#         if j=='\n':
#             count+=1
#     return count
# v=total_lines(r)
# print("total number of lines:",v)
#
# def total_words(r):
#     new=r.split()
#     count=0
#     for i in new:
#         count+=1
#     return count
# w=total_words(r)
# print("total words:",w)
#
# def total_words_excludingspace(r):
#     now=r.split()
#     count=0
#     for i in now:
#         count+=len(i)
#     return count
# y=total_words_excludingspace(r)
# print("excluding space",y)
# print("\n")
# print("top 5 most freequent words")
#
# def freequency(r):
#     shh=r.split()
#     dic={}
#     for i in shh:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     return dic
# def most_freequent(r):
#     dict=freequency(r)
#     lis=sorted(dict.items(),key=lambda x:x[1],reverse=True)
#     return lis[:5]
# top5=most_freequent(r)
# for i,count in top5:
#     print(f"{i}:{count}")



# dic1={1:2,2:3}
# dic2={3:4,4:5}
# for i,j in dic2.items():
#     dic1[i]=j
# print(dic1)



# dic = {1: 2, 3: 4}
# dic[5] = 6
# print(dic)


# dic1 = {1: 2, 3: 4}
# dic2 = {5: 6, 7: 8}
# dic1.update(dic2)
# print(dic1)



# dic = {1: 2, 3: 4, 5: 6}
# print(3 in dic)




# dic = {1: 2, 3: 4, 5: 6}
# del dic[3]
# print(dic)


# dic={1:2,2:3,3:4}
# for i,j in dic.items():
#     print(f"{i}:{j}")



# dic1={1:2,2:3,3:4}
# dic2={5:6,6:7}
# for i,j in dic2.items():
#     dic1[i]=j
# print(dic1)

# k=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k+=1
#     print()


# k=5
# for i in range(3,0,-1):
#     print(" "*(3-i),end=" ")
#     for j in range(i,0,-1):
#         print(k,end=" ")
#         k-=1
#     print()



# def decorator(fun):
#     def wrapping(name1,name2):
#         print("hello sheikh")
#         fun(name1,name2)
#         print("goodbye")
#     return wrapping
#
# @decorator
# def name(firstname,secondname):
#     print(f"name:{firstname} \nlastname:{secondname}")
# name("sheikh","ahmed")



# def decorator(fund):
#     def wrapping():
#         print("hello")
#         fund()
#     return wrapping
# @decorator
# def name():
#     print("sheikh")
# name()



# def decorator(func):
#     def wrapping(name1,name2):
#         print("hello")
#         func(name1,name2)
#         print("goodbye")
#     return wrapping
# @decorator
# def name(first_name,last_name):
#     print(f"first name: {first_name} \nlast name: {last_name}")
# name("sheikh","rahiman")
#


# class add():
#     def _init_(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def adding(self):
#         return self.m1+self.m2
# obj=add(21,43)
# print(obj.adding())



# class forest():
#     def _init_(self,forest_name):
#         self.forest_name=forest_name
# class animal(forest):
#     def _init_(self,forest_name,name,age):
#         self.name=name
#         self.age=age
#         super()._init_(forest_name)
#         print( f"name:{self.name}age:{self.age}")
#
# obj=animal("tiger",21)
# print(obj)




# class mark():
#     def _init_(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def _add_(self, other):
#         x=self.m1+self.m2
#         y=other.m1+other.m2
#         z=x+y
#         return z
# stu1=mark(23,45)
# stu2=mark(25,87)
# v=stu1+stu2
# print(v)



# class mark():
#     def _init_(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#     def _add_(self, other):
#         x=self.m1+self.m2
#         y=other.m1+other.m2
#         z=x+y
#         return z
# result=mark(21,34)
# result2=mark(32,43)
# v=result+result2
# print(v)




# class calculator():
#     def add(self,x,y=None,z=None):
#         if y is None and z is None:
#             return x
#         elif z is None:
#             return x+y
#         else:
#             return x+y+z
# cal=calculator()
# print(cal.add(10,20,30))
# print(cal.add(10))





# dic1={'a':21}
# dic2={'b':43}
# for i,j in dic2.items():
#     dic1[i]=j
# print(dic1)



# list=['sheikh',21,'shamil',21]
# count=0
# for i in list:
#     if type(i)==int:
#         count+=i
# print(count)


# lambda 2 even


# x=lambda x,y:x+y
# print(x(10,20))



# list=[1,'sheikh',32,'shamil']
# count=0
# for i in list:
#     if type(i)==int:
#         count+=i
# print(count)


# word=open('simple.txt','r')
# n=word.read()
# print(n)



# name="my name is sheikh"
# n=name.split()
# dic={}
# for i in n:
#     dic[i]=len(i)
# print(dic)



# name="my name is sheikh"
# n=name.split()
# new=[]
# for i in n:
#     capital=i[0].upper()+i[1:]
#     new.append(capital)
# print(new)



# name="my name is sheikh"
# n=name.split()
# new={}
# for i in n:
#     new[i]=len(i)
# print(new)




# for i in range(5,0,-1):
#     print(" "*(5-i),end=" ")
#     for j in range(1,i+1):
#         print(j,end="")
#     print()



for i in range(1,4):
    for j in range(5,5-i,-1):
        print(j,end=" ")

    print()


# dic={'a':200,'b':1000,'c':3000}
# max=None
# key=None
# dict={}
# for i,j in dic.items():
#     if max is None or j>max:
#         max=j
#         key=i
# # print(key,":",max)
# for i,j in dic.items():
#     if max!=j:
#         dict[i]=j
# print(dict)



# word=open('simple.txt','r')
# n=word.read()
# print(n)
#
#
# def total_lines(n):
#     count=1
#     for i in n:
#         if i=="\n":
#             count+=1
#     return count
# v=total_lines(n)
# print("total number of words:",v)
#
# def total_words(n):
#     count=0
#     new=n.split()
#     for i in new:
#         count+=1
#     return count
# v=total_words(n)
# print("total number of words",v)
#
# def total_charecter(n):
#     new=n.split()
#     count=0
#     for i in new:
#         count+=len(i)
#     return count
# v=total_charecter(n)
# print("total charecters wxcluding space:",v)
#
# print("MOST FREEQUENT WORDS")
# def frequency(n):
#     new=n.split()
#     dict={}
#     for i in new:
#         if i in dict:
#             dict[i]+=1
#         else:
#             dict[i]=1
#     return dict
# def most_freequent(n):
#     dic=frequency(n)
#     list=sorted(dic.items(),key=lambda x:x[1],reverse=True)
#     return list[:5]
# top_5=most_freequent(n)
# for i,count in top_5:
#     print(f"{i}{count}")




# class bank():
#     def _init_(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposite(self,amount):
#         self.balance+=amount
#         print(f"balance:{self.balance}amount deposite:{amount}")
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("you dont have enough balance")
#         else:
#             self.balance-=amount
#             print(f"balace:{self.balance}amount withdrawen{amount}")
# v=bank("sheikh",20000)
# print(v.name,v.balance)
# deposite=int(input("enter despoite amount"))
# v.deposite(deposite)
# withdraw=int(input("enter the withdraw amount"))
# v.withdraw(withdraw)



# list=[1,2,3,3,4,5,6,7,7,8]
# new=[]
# for i in list:
#     if i not in new:
#         new.append(i)
# print(new)



# def first(a):
#     def second(b):
#         return a+b
#     return second
# v=first(10)
# w=v(20)
# print(w)



# list1=[1,2,3]
# list2=[4,5,6]
# result=list(map(lambda x,y:x+y,list1,list2))
# print(result)


# list1=[1,2,3]
# list2=[4,5,6]
# result=list(zip(list1,list2))
# print(result)


# class bird():
#     def _init_(self,name,color):
#         self.name=name
#         self.color=color
#     def _del_(self):
#         print("object has deleted")
# obj=bird("kingfisher","red")
# del obj.color
#
# try:
#     print(obj.name)
#     print(obj.color)
# except:
#     print("object color is deleted")
#


# a=5
# b=2.5
# c=a+b
# print(type(c))


# a=5
# b=int(6)
# c=a+b
# print(type(c))


# name=[["sheikh"]]
# shallow=copy.copy(name)
# shallow[0][0]=["shamil"]
# print(name)
# print(shallow)


# name=[["sheikh"]]
# shallow=copy.deepcopy(name)
# shallow[0][0]=["shamil"]
# print(name)
# print(shallow)



# class itrator():
#     def _iter_(self):
#         self.x=1
#         return self
#     def _next_(self):
#         x=self.x
#         self.x+=2
#         return x
# v=itrator()
# w=iter(v)
# print(next(w))
# print(next(w))
# print(next(w))




# def generator():
#     yield 1
#     yield 2
#     yield 3
# gen=generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))



# name="my name is sheikh"
# n=name.split()
# new=[]
# for i in n:
#     capital=i[0].upper()+i[1:]
#     new.append(capital)
# print(new)




# name="sheikh"
# new=[]
# for i in name:
#     capital=i[:-1]+i[-1].upper()
#     new.append(capital)
# print(new)


# name="sheikh"
# new=name[:-1]+name[-1].upper()
# print(new)


# dic1={'a':21}
# dic2={'b':43}
# for i,j in dic2.items():
#     dic1[i]=j
# print(dic1)


# list=[1,2,3,4,5,5,6]
# dict={}
# for i in list:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)



# def vovels(name):
#     new=[]
#     count=0
#     vov="aeiouAEIOU"
#     for i in name:
#         if i in vov:
#             new.append(i)
#             count+=1
#     return new,count
# name=str(input("enter a name"))
# v,w=vovels(name)
# print(v,w)


# def largest(list):
#     max=list[0]
#     for i in range(len(list)):
#         if max<list[i]:
#             max=list[i]
#     return max
# list=[1,2,3,4,5,6,7]
# v=largest(list)
# print(v)
# def second(list):
#     s_max=list[0]
#     for i in range(len(list)):
#         if s_max<list[i]!=v:
#             s_max=list[i]
#     return s_max
# w=second(list)
# print(w)



# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



# for i in range(1,6):
#     print(" "*(5-i),end=" ")
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# k=1
# for i in range(5,0,-1):
#     print(" "*(5-i),end=" ")
#     for j in range(i,0,-1):
#         print(k,end=" ")
#         k+=1
#     print()



# num=int(input("enter a number"))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")



# def missing_num(list):
#     exp=(len(list)+1)*(len(list)+2)//2
#     act=0
#     for i in list:
#         act+=i
#     missing=exp-act
#     return missing
# list=[1,2,3,4,5,6,8,9]
# v=missing_num(list)
# print(v)



# dic={'a':200,'b':500,'c':6000}
# max=None
# key=None
# dict={}
# for i,j in dic.items():
#     if max is None or max<j:
#         max=j
#         key=i
# print(key,":",max)
# for i,j in dic.items():
#     if max!=j:
#         dict[i]=j
# print(dict)



# k=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k+=1
#     print()



# def requertion(num):
#     if num==0:
#         return 1
#     else:
#         return num*factorial(num-1)
# num=int(input("enter a number"))
# v=requertion(num)
# print(v)


# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#     i=i+1