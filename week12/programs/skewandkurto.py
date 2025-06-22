def mean(data):
    total = sum(data)
    count = len(data)
    return total / count

def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - 1)  # Sample variance

def standard_deviation(data):
    return variance(data) ** 0.5

def skewness(data):
    n=len(data)
    m=mean(data)
    s=standard_deviation(data)
    return sum((x-m)**3 for x in data)/(n*s**3)
    
def kurtosis_manual(data):
    n=len(data)
    m=mean(data)
    s=standard_deviation(data)
    return sum((x-m)**4 for x in data)/(n*s**4)-3
    
data=[5,2,3,6,74,9,86,21,22,385]
print("Skewness:", skewness(data))
print("Kurtosis:", kurtosis_manual(data))