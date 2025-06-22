def new_decorator (func):
    def wrapper():
        result = func() #call original function and store it's result
        return result.upper() #modify by converting to upper case
    return wrapper

@new_decorator
def greet():
    return "hello"
print(greet())

def decarator(func):
    def wrapper(str):
        result=func(str)
        return result.upper()
    return wrapper
        
@decarator
def greet(x):
    return x
        
x="Ajmal"
print(greet(x))



def decarator(func):
    def wrapper(str):
        x=str.upper()
        result=func(x)
    return wrapper
        
@decarator
def greet(x):
    print(f"hloo {x}")
        
x="Ajmal"
print(greet(x))