

def even_odd(lst):
    evens=[]
    odds=[]
    for num in lst:
        if num%2==0:
            evens.append(num)
        else:
            odds.append(num)
    return evens, odds

lst = [1,2,5,7,8,6,3]

even_numebrs, odd_numbers = even_odd(lst)

print(even_numebrs)
print(odd_numbers)