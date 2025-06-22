def is_prime (n):
    if n<=1:
        return "number is not prime"
    for i in range (2,int(n ** 0.5)+1):
        if n%i==0:
            return "Number is not prime"
    return "Number is prime"

num = int(input("Enter a number: "))

print(is_prime(num))
        