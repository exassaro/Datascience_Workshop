lst = [1,5,4,8,7,9,2,5,7,2]

odd_numbers = [x for x in lst if x%2!=0]
even_numbers = [x for x in lst if x%2==0]

even_sum=0
for x in even_numbers:
    even_sum+=x

print(odd_numbers)
print(even_numbers)
print(even_sum)