try:
    num = int(input("Enter a number: "))  # Taking user input
    result = 10 / num  # Attempting division
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")  # Handling division by zero
except ValueError:
    print("Error: Please enter a valid number!")  # Handling invalid input
else:
    print("Division successful! Result:", result)  # Executes if no exception occurs
finally:
    print("Execution completed.")  # Always executes
