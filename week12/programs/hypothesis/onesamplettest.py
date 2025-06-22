#One-sample t-test
sample = [22, 24, 27, 23, 26, 30, 28, 25, 29, 24]
n = len(sample)
population_mean = 25

#calculate mean
sample_mean=sum(sample)/n

#calulate standard deviation
variance = sum((x - sample_mean) ** 2 for x in sample) / (n - 1)
sample_std = variance ** 0.5

#calculate t_score
t_score=(sample_mean-population_mean)/(sample_std/(n**0.5))


print("T-Statistic:", t_score)