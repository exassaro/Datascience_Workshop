# Two-Sample Z-Test (Manual)

mean1 = 53
mean2 = 47
sd1 = 3
sd2 = 4

n1 = 40
n2 = 40

# Compute Z-score
z_score = (mean1 - mean2) / (((sd1 ** 2) / n1 + (sd2 ** 2) / n2) ** 0.5)

print("Z-Score:", z_score)

