def larg(*arr):
    lg= arr[0][0]
    # lg = float('-inf')# Initialize with negative infinity to handle any number comparison
    for sublist in arr:
        for i in sublist:
            if i>lg:
                lg = i
    return lg
            
            
arr1=[10,28,37,87,6,41]
arr2=[24,15,9,42,63]
arr3=[25,12,36,85,96]

print(larg(arr1,arr2,arr3))

def larg(*arr):
    lg=arr[0][0]
    max_arr=arr[0]
    for sub in arr:
        for i in sub:
            if i>lg:
                lg=i
                max_arr=sub
    return lg,max_arr
    
arr1=[10,28,37,87,6,41]
arr2=[24,15,900,42,63]
arr3=[25,12,36,85,96]

print(larg(arr1,arr2,arr3))
