lst = ["apple","banana","grape"]
lst1=[1,2,3,5,[4,5],[5,6]]
print(lst[0:2]) #slicing
print(lst1[-1][0]) #print nested list
print(lst1[:])
print(lst1[::-1]) #reverse
lst1.append([4,5])
print(lst1)
lst1.insert(1,[5,4]) #either single element
print(lst1)
lst1.extend({1,4,5,8}) #any iterable since it is set the order may vary
print(lst1)

lst3=[1,2,3,2,4,8,9,45,12,35,7,89,45]
lst3.remove(2)#remove first  occurence
print(lst3)
print(lst3.pop(-1)) #output last item
print(lst3)# output removed list
lst3.clear() #remove all 
print(lst3) #empty list


lst4 =[4,8,9,7,5,7,4]
print(lst4.index(7))
print(lst4.index(7,4,6)) #index only goes from left to right and start must be lesser than end

lst5= [4,5,8,9,7,9,7,4]
print(lst5.count(7))
lst5.sort(key=None, reverse=False)
print(lst5)
lst.sort(key=len) #key to sort in specific order
print(lst)
lst.reverse()
print(lst)

lst5=[4,8,7,9,5,4,6,4,4]
lst6=lst5.copy()
print(lst6)
lst6.append(5)
print(lst5)
print(len(lst6))
del lst6[-3]
print (lst6)
del lst6
#print(lst6) # name error

lst7=[1,2,4,5,4,6,4,8,7]
lst8= [x**2 for x in lst7]
print (lst8)
lst9=[x for x in lst7 if x%2==0]
print(lst9)
lst10=["apple","banana","grape","peach"]
lst11=[x.upper() for x in lst10]
print(lst11)