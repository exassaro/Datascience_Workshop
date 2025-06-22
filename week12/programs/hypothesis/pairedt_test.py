
# Paired t-Test (Manual)

before = [22, 24, 28, 23, 26]
after = [30, 28, 25, 29, 24]

n = len(before)

# Calculate differences
differences = [after[i] - before[i] for i in range(n)]

# Calculate mean of differences
mean_diff = sum(differences) / n

# Calculate standard deviation of differences
variance = sum((x - mean_diff) ** 2 for x in differences) / (n - 1)
std_diff = variance ** 0.5

# Compute t-score
t_score = mean_diff / (std_diff / (n ** 0.5))

print("T-Statistic:", t_score)

