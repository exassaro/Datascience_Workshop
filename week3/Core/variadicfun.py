def sum_and_average(*args):
    # Check if any arguments are provided
    if len(args) == 0:
        return 0, 0  # Return 0 for both sum and average when no arguments are passed

    total = sum(args)          # Calculate the sum of all arguments
    average = total / len(args)  # Calculate the average
    return total, average       # Return both sum and average as a tuple


result = sum_and_average(1,2,4,5,8,9,7)
print(result)