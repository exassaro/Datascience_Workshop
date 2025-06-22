def outer_function(x):
    def inner_function(y):
        return x + y  # 'x' is captured from the enclosing scope
    return inner_function

closure = outer_function(10)  # outer_function returns inner_function
print(closure(5))  # Output: 15 (10 + 5)
print(closure(7))  # Output: 17 (10 + 7)
