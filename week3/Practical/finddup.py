def  find_duplicate(lst):
    seen = set()
    duplicate = []
    
    for i in lst:
        if i in seen:
            duplicate.append(i)
        else:
            seen.add(i)
    return  duplicate
            
lst1=[1,2,5,4,61,5,4]
print(find_duplicate(lst1))