def common_element(arr1, arr2):
    common = list(set(arr1)&set(arr2))
    return common

list1=[1,5,8,7.6,6,4,2]
list2=[1,5,23,4,6,3,4]

print(common_element(list1, list2))     

def common_elmnt(arr1,arr2):
    common=[]
    for i in arr1:
        for j in arr2:
            if i==j:
                common.append(i)
    return common
    
arr1=[5,12,4,9,35,8]
arr2=[2,5,6,7,13,4]

print(common_elmnt(arr1,arr2)) 