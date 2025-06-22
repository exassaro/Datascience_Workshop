def curry_add(a):
    def add_b(b):
        def add_c(c):
            return a+b+c
        return add_c
    return add_b


curried_add=curry_add(2) #a=2
add_two_and_five=curried_add(5) #b=5 here func name changed to previously assigned so pass argiment into that
result=add_two_and_five(3)#c=3

print(result)