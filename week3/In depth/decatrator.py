def fragment(func):
    def wrapper():
        print("First execution")
        func()
        print("After function")
    return wrapper

@fragment
def greet():
    print("Hello World")
    
greet()