#One way Anova
group1 = [70, 75, 80, 85, 90]
group2 = [60, 65, 70, 75, 80]
group3 = [50, 55, 60, 65, 70]
all_data=group1 + group2 + group3
k=3
n=len(all_data)

#calculate means
group_means=[sum(g)/len(g)for g in [group1,group2,group3]]
grand_mean=sum(all_data)/n

#between_group variance (SSB)
ssb=sum(len(g) * (mean-grand_mean)**2 for g,mean in zip([group1,group2,group3],group_means))

#within-group variance (SSW)
ssw=sum(sum((x-mean)**2 for x in g) for g,mean in zip([group1,group2,group3],group_means))

#degrees of freedom
df_between=k-1
df_within=n-k

# Mean Squares
msb = ssb / df_between
msw = ssw / df_within

f_statistics=msb/msw

print("F-Statistic:", f_statistics)
