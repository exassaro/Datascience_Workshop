# Manual caculation for covariance and correlation
def mean(data):
    return sum(data)/len(data)

def covariance(X,Y):
    n=len(X)
    mean_x,mean_y=mean(X),mean(Y)
    return sum((x-mean_x)*(y-mean_y) for x,y in zip(X,Y))/(n-1)
    
def population_covariance(X,Y):
    n=len(X)
    mean_x,mean_y=mean(X),mean(Y)
    return sum((x-mean_x)*(y-mean_y) for x,y in zip(X,Y))/n
    
def variance(data):
    m=mean(data)
    return sum((x-m)**2 for x in data)/(len(data)-1)
    
def standard_deviation(data):
    return variance(data)**0.5
    
def correlation(X,Y):
    return covariance(X,Y)/(standard_deviation(X)*standard_deviation(Y))
    
    
X = [3, 5, 7, 9, 11]
Y = [2, 4, 6, 8, 10]

print("Covariance:", covariance(X, Y))
print("Population Covariance:", population_covariance(X, Y))
print("Correlation:", correlation(X, Y))