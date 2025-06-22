#Remove duplicate elements from a list by converting to set
list=[1,5,6,9,8,4,5,1,2]
remove_duplicate = set(list)

print(remove_duplicate)

#removing by for loop
list2=[1,5,6,9,8,4,5,1,2]
new_list=[]
for i in list2:
    if i not in new_list:
        new_list.append(i)

print(new_list)