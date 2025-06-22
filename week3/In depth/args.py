
def greet(name,age):
    print(f"You name is {name} your age is {age}")
    
greet("Sanil",24)#positional arguments
greet(age=40,name="Alana")#key word arguments

def greet(name,age=100):
    print(f"You name is {name} your age is {age}")

greet("Rohan")#default value used


#Variable lenght position
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(2,4,5,7,8))

#Variablle length keyword
def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
        
info(name="Alice",age=25,place="Calicut")
    
def example_func(a, b, /, c, d, *, e, f):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}, f: {f}")

# Explanation:
# a, b -> Positional-only (before /)
# c, d -> Simple arguments (can be passed by position or keyword)
# e, f -> Keyword-only (after *)