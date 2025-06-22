def mean(data):
    total = sum(data)
    count = len(data)
    return total / count

def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - 1)  # Sample variance

def standard_deviation(data):
    return variance(data) ** 0.5


def clt_simulation(population,sample_size,num_samples):
    sample_means=[]
    for _ in range (num_samples):
        sample=[population[i%len(population)] for i in range(sample_size)]
        
        sample_means.append(mean(sample))
    return mean(sample_means),variance(sample_means)

population = [1, 2, 3, 4, 5, 6]
print("CLT Mean, Variance:", clt_simulation(population, 10, 100))