#bubblesort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[1,4,5,6,7,8,9]
x=bubble_sort(arr)    
print("Bubble sort = ",x)         
    
#Quick sort

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr[:-1] if x<=pivot]
    right=[x for x in arr[:-1] if x>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)

arr=[1,54,15,56,87,8,91]
x=quick_sort(arr)    
print("Quick sort =",x) 

#merge sort
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    
    return merge(left,right)

def merge(left,right):
    sorted_arr=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
            
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr


arr=[100,5,105,76,947,80,91]
x=merge_sort(arr)    
print("merge sort =",x) 


#Linear Search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=[2,3,4,45,56,7]
print("Linear search position = ",linear_search(arr,45))

#Binary search
def binary_search(arr,target):
    left,right=0, len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left= mid+1
        else:
            right=mid-1
    return -1

arr=[3,5,6,7,8,54,32,40]
target=54

print("Binary search position = ",binary_search(arr,target))