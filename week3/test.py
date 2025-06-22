def decorator(func):
    def wrapper(string):
        print("Before")
        result=func(string)
        print("after")
        return result.upper()
    return wrapper

@decorator
def greet(string):
    return f"Hello {string}!"
    
x=greet("shahin")
print(x)

def decorator(func):
    def wrapper(string):
        print("Before")
        result = func(string)
        print (result)
        print("After")  # ✅ Now it runs when the function is actually executed
        return result.upper()
    return wrapper

@decorator
def greet(string):
    return f"Hello {string}!"
    
x = greet("shahin")
print(x)
