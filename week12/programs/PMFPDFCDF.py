#PMF

def calculate_pmf(data,x):
    total_count=len(data)
    occurence=sum(1 for i in data if i==x)
    return occurence/total_count
    
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]  # Discrete values
x = 3  # Find probability of 3 occurring

print("Manual PMF for X=3:", calculate_pmf(data, x))

#PDF
def power(base,exp):
    result=1
    for _ in range(abs(exp)):
        result*=base
    return result if exp>=0 else 1/result
    
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    
def sqrt(n,precision=10):
    x=n
    for _ in range(precision):
        x=0.5*(x+n/x)#babylonian method
    return x
        
        
def exp_manual(x,terms=20):
    total=1
    for n in range(1,terms):
        total+=power(x,n)/factorial(n)#taylor series expansion
    return total
    
def normal_pdf(x,mean,std):
    pi=3.1415
    e=exp_manual(1)
    
    coeff=1/(std*sqrt(2*pi))
    exponent=exp_manual(-((x-mean)**2)/(2*std**2))
    return coeff*exponent
    
mean = 50
std = 10
x_value = 55  # Find probability at X = 55

print("Manual Normal PDF for X=55:", normal_pdf(x_value, mean, std))

#CDF
def erf_manual(x,terms=10):
    pi = 3.1415926535
    sum_erf = 0
    
    for n in range(terms):
        sum_erf+=((-1)**n*power(x,2*n+1))/((2*n+1)*factorial(n))
        
    return (2/sqrt(pi))*sum_erf   #Maclaurin series
        
        
def normal_cdf(x,mean,std):
    return 0.5 * (1+erf_manual((x-mean)/(std*sqrt(2))))
    
print("Manual Normal CDF for X=55:", normal_cdf(x_value, mean, std))
        
        