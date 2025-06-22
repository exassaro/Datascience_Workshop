set1={1,3,5,4,8,5}
print(set1) #unique and unordered
set1.add(45)# single value
print(set1)
set1.update((48,53,81,9)) #from any iterable
print(set1)
set1.remove(48)
print(set1)
set1.discard(100)#doesn't raise error
print(set1)
removed_element=set1.pop()#remove arbitar element
print(removed_element)
print(set1)
set2 = set1.copy()
print(set2)#shallow copy
set2.clear()
print(set2)#empty set

set3={1,5,4,8,7,9,15}
set4={45,8,7,95,63,1,5}
union_set=set4.union(set3)
print(union_set)
union_pipe= set3 | set4
print(union_pipe)
inter_set=set4.intersection(set3)
print(inter_set)
inter_pipe= set3 & set4
print(inter_pipe)
diff_set=set4.difference(set3)
print(diff_set)
diff_pipe= set3 - set4
print(diff_pipe)
symm_set=set4.symmetric_difference(set3)
print(symm_set)
symm_pipe= set3 ^ set4
print(symm_pipe)

set7={1,5,8}
set8={45,8,7,95,63,1,5}
print(set7.issubset(set8))

set7={1,5,8}
set8={45,8,7,95,63,1,5}
print(set8.issuperset(set7))

set7={1,5,8}
set8={45,8,7,95,63,1,5}
print(set8.isdisjoint(set7))

set7={1,5,8}
set8={45,8,7,95,63,1,5}
set8.intersection_update(set7)
print(set8)

set7={1,5,8}
set8={45,8,7,95,63,1,5}
set8.difference_update(set7)
print(set8)

set7={1,5,8,49,78}
set8={45,8,7,95,63,1,5}
set7.symmetric_difference_update(set8)
print(set8)

