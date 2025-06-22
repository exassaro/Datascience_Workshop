
# Two-Way ANOVA (Manual)

groups = {
    "A_short": [88, 85, 87],
    "A_long": [75, 78, 80],
    "B_short": [90, 92, 89],
    "B_long": [70, 72, 68],
    "C_short": [80, 78, 82],
    "C_long": [60, 63, 59],
}

all_data = sum(groups.values(), [])
total_mean = sum(all_data) / len(all_data)

# Calculate means
group_means = {k: sum(v) / len(v) for k, v in groups.items()}

# Between-group variance (SSB)
ssb = sum(len(v) * (mean - total_mean) ** 2 for v, mean in group_means.items())

# Within-group variance (SSW)
ssw = sum(sum((x - mean) ** 2 for x in v) for v, mean in zip(groups.values(), group_means.values()))


# Compute F-statistic
f_statistic = (ssb / (len(groups) - 1)) / (ssw / (len(all_data) - len(groups)))

print("F-Statistic:", f_statistic)

