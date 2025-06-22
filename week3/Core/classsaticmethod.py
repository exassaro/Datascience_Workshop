class Person:
    # Class attribute
    species = "Homo sapiens"

    # Instance method — operates on a particular instance
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def say_name(self):
        print(f"My name is {self.name}")

    # Class method — operates on the class itself
    @classmethod
    def info_species(cls):
        print(f"We are {cls.species}")

    # Static method — independent of class or instance
    @staticmethod
    def add_numbers(a, b):
        return a + b


# Create an instance
p = Person("Alice", 25)

# Call instance method
p.say_name()

# Call class method
Person.info_species()

# Call static method
result = Person.add_numbers(5, 10)
print(result)





class BankAccount:
    total_accounts = 0  # Class variable to track the total number of accounts

    def __init__(self, name, account_number, balance=0):
        if not BankAccount.validate_account_number(account_number):
            raise ValueError("Invalid account number format!")
        
        self.name = name
        self.account_number = account_number
        self.balance = balance
        BankAccount.total_accounts += 1  # Increment account count

    @staticmethod
    def validate_account_number(account_number):
        """Check if the account number is exactly 10 digits."""
        return isinstance(account_number, str) and account_number.isdigit() and len(account_number) == 10

    @classmethod
    def get_total_accounts(cls):
        """Returns the total number of accounts created."""
        return cls.total_accounts

# ✅ Creating valid bank accounts
acc1 = BankAccount("Alice", "1234567890", 5000)
acc2 = BankAccount("Bob", "0987654321", 3000)

# ❌ Trying to create an account with an invalid account number
try:
    acc3 = BankAccount("Charlie", "12345", 2000)  # Invalid (not 10 digits)
except ValueError as e:
    print(e)  # Output: Invalid account number format!

# ✅ Getting total accounts
print(f"Total accounts created: {BankAccount.get_total_accounts()}")  # Output: 2


class Example:
    class_variable = "I am a class variable"

    def __init__(self, value):
        self.instance_variable = value  # Instance variable

    @staticmethod
    def static_method():
        print("I am a static method! I do not need access to class or instance variables.")

    @classmethod
    def class_method(cls):
        print(f"I am a class method! I can access class variables like this: {cls.class_variable}")

# Creating an object
obj = Example("Hello")

# Calling Static Method (No access to class or instance variables)
Example.static_method()  # ✅ Can be called without an instance
obj.static_method()      # ✅ But can also be called via an instance

# Calling Class Method (Accesses class variables)
Example.class_method()  # ✅ Uses `cls` to access class-level data
obj.class_method()      # ✅ Can also be called from an instance
