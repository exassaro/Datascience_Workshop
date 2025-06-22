# Independent t-Test (Manual)

sample1 = [22, 24, 27, 23, 26]
sample2 = [30, 28, 25, 29, 24]

n1, n2 = len(sample1), len(sample2)

mean1 = sum(sample1) / n1
mean2 = sum(sample2) / n2

# Calculate variances
var1 = sum((x - mean1) ** 2 for x in sample1) / (n1 - 1)
var2 = sum((x - mean2) ** 2 for x in sample2) / (n2 - 1)

#pooled variance
pooled_variance=((n1-1)*var1+(n2-1)*var2)/(n1+n2-2)

#pooled standard deviation
pooled_std=pooled_variance**0.5

t_score=(mean1-mean2)/(pooled_std * ((1/n1+1/n2)**0.5))

print("T-Statistic:", t_score)