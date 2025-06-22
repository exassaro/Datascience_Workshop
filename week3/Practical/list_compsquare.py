#list comprehension Square elements

lst=[1,2,4,5,8,9,6]

sqrd_lst = [x**2 for x in lst]

print(f"original list= {lst}")

print(f"squared list= {sqrd_lst}")




#square odd even cube

lst=[1,5,4,8,7,9,2,7]

result=[x**2 if x%2!=0 else x**3 for x in lst]

print(result)