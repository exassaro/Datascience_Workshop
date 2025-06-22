sample_mean=50
population_mean=50
population_sd=3
n=40

z_score=(sample_mean-population_mean)/(population_sd)/(n**0.5)

print("Z-Score:", z_score)
