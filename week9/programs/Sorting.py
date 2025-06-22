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

#insertion sort
def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

ls = [3, 1, 5, 6, 90, 2]
print("Insertion sort: ",insertion(ls))

    
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

#Selection sort
def selection(arr):
    n=len(arr)
    for i in range(n):
        key=i
        for j in range(i+1,n):
            if arr[key]>arr[j]:
                key=j
        if key!=i:  
            arr[i],arr[key]=arr[key],arr[i]
    return arr

lst=[2,5,4,91,67,100,45]
print("selection sort : ",selection(lst))