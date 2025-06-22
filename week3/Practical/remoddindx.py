#slicing

list=[1,6,5,4,3,2]
del list[0::2]

print(list)


#condition len()
list2=[50,46,86,95,52]

result=[list2[i] for i in range (len(list2)) if i%2==0]

print(result)