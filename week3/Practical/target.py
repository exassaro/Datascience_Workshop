def find_num(lst,n):
    position=[i for i, num in enumerate(lst) if num==n]
    if n in lst:
        return (f"number {n} is present in {position}")
    else:
        return (f"number {n} not present")
    
lst=[1,5,4,6,8,2,8,7,4]

target=int(input("Enter the numbr to find: "))

print(find_num(lst,target))



def findnum(lst,*args):
    res=[num for i,num in enumerate(lst) if i in args ]
    return res if res else "Not found"
    
lst=[4,4,32,5,6,4,3]
print(findnum(lst,4,5,2))