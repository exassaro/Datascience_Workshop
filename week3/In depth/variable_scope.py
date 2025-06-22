#local scope
def function():
    x=10
    print(x)
function()  


#Enclosing scope
def outer_function():
    x = 10

    def inner_function():
        nonlocal x  # Modify the enclosing variable
        x += 1
        print(x)

    inner_function()
    print(x)

#glabal scope
x = 20

def modify_global():
    global x  # Declare x as global to modify it
    x += 10

modify_global()
print(x)  # Output: 30


