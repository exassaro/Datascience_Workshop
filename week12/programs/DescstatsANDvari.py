# Manual Calculation of Mean, Median, Mode, Range, Variance, Standard Deviation, and IQR
def mean(data):
    total=sum(data)
    count=len(data)
    return total/count

def median(data):
    sorted_data=sorted(data)
    n=len(sorted_data)
    mid=n//2
    if n%2==0:
        return (sorted_data[mid-1]+sorted_data[mid])/2
    else:
        return sorted_data[mid]
    
def mode(data):
    freq={}
    for num in data:
        freq[num]=freq.get(num,0)+1
    max_freq=max(freq.values())
    modes=[key for key,val in freq.items() if val==max_freq]
    return modes

def data_range(data):
    return max(data)-min(data)

def variance(data):
    m=mean(data)
    return sum((x-m)**2 for x in data) / (len(data)-1)

def standard_deviation(data):
    return variance(data)**0.5

def calculate_iqr(data):
    sorted_data=sorted(data)
    n=len(sorted_data)
    
    def find_median(values):
        size=len(values)
        mid=size//2
        return (values[mid - 1] + values[mid]) / 2 if size % 2 == 0 else values[mid]
    
    lower_half = sorted_data[:n//2] if n % 2 == 0 else sorted_data[:n//2]
    upper_half = sorted_data[n//2:] if n % 2 == 0 else sorted_data[n//2+1:]
    q1 = find_median(lower_half)
    q3 = find_median(upper_half)
    return q3 - q1, q1, q3



data = [5, 2, 3, 6, 74, 9, 86, 21, 22, 385]

print("Mean:", mean(data))
print("Median:", median(data))
print("Mode:", mode(data))
print("Range:", data_range(data))
print("Variance:", variance(data))
print("Standard Deviation:", standard_deviation(data))
iqr, q1, q3 = calculate_iqr(data)
print(f"IQR: {iqr}, Q1: {q1}, Q3: {q3}")



