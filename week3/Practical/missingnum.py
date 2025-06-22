lst=[1,2,3,5]
n = len(lst)+1
new_lst=(n *(n+1)) // 2

actual_sum=0
for i in lst:
    actual_sum+=i

missing_num=new_lst - actual_sum

print(missing_num)