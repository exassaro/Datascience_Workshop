def mean(data):
    return sum(data)/len(data)#bias variance trade-off



def bias_variance_simulation(true_value,samples):
    n=len(samples)
    sample_means=[mean(sample) for sample in samples]
    estimator_mean=mean(sample_means)
    bias=estimator_mean-true_value
    variance = sum((m - estimator_mean) ** 2 for m in sample_means) / (n - 1)
    return bias, variance   


true_mean = 10
samples = [[9, 10, 11], [8, 9, 12], [10, 11, 12]]
bias, var = bias_variance_simulation(true_mean, samples)
print(f"Bias: {bias}, Variance: {var}")


