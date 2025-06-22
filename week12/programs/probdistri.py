#Manual Probability distribution
def factorial(n):
    return 1 if n<=1 else n*factorial(n-1)

def uniform_probability(n):
    return 1/n

def combination(n,k):
    return 