#To finnd factorial number
def fact_num(n):
    if (n<0):
        return "factorial is not defined"
    result=1
    for i in range(1,n+1):
            result *=i
    return result
        
num=int(input("enter your number:"))
print(f"The factorial of {num} is {fact_num(num)}")


# by recursion
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(6))