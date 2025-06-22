class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

# Creating an object
calc = Calculator(10, 5)

# Using methods
print(calc.add())        # Output: 15
print(calc.subtract())   # Output: 5
