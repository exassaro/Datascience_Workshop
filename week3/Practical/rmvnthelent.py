def rmv_ele(lst,n):
    if n<0 or n>=len(lst):
        return "invalid syntax"
    lst.pop(n)
    return lst

list=[1,6,5,8,4,9,7,2,7,5]

num=int(input("Enter index of element to remove: "))

print (rmv_ele(list,num))

#remove element
def remv(lst,n):
    while n in lst:
        lst.remove(n)
    return lst
    
lst=[1,2,3,5,6,4,5]
print(remv(lst,5))
    