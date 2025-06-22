x = lambda a:a+10
print(x(5))

y = lambda a,b:a*b
print(y(15,2))


#calling as an anonymous function
def myfunct(n):
    return lambda a : a*n

mydoubler=myfunct(2)
mytripler=myfunct(3)

print(mydoubler(4))
print(mytripler(5))