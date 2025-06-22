#subarray insert

lst=[[1,2,3],[2,3,4],[9,8,7]]
lst[1].insert(2,25)
print(lst)

#deletion
lst=[[1,2,3],[2,3,4],[9,8,7]]
lst[1].remove(2)
lst.pop(2)
print(lst)

#traversal
lst=[[1,2,3],[2,3,4],[9,8,7]]
for i in lst:
    print(i)