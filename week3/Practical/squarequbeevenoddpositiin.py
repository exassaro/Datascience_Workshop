list1=[1,2,3,4,5,6,7]
list2=[x**2 if i%2==0 else x**3 for i, x in enumerate(list1)]
print(list2)