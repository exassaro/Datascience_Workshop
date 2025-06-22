#chi_square test
observed=[[50,30],[20,40]]


# Calculate row and column sums
row_sums=[sum(row) for row in observed]
col_sums=[sum(col) for col in zip(*observed)]
total=sum(row_sums)

#Expected values
expected=[[(row_sums[i] * col_sums[j])/total for j in range(len(col_sums))] for i in range(len(observed[0]))] 

#compute chi_square statistics
chi_square=sum((observed[i][j]-expected[i][j])**2/expected[i][j] for i in range(len(observed)) for j in range(len(observed[0])))

print("Chi-Square Statistic:", chi_square)