
import heapq
A=[1,2,33,4,3,2,56,5]
heapq.heapify(A)
heapq.heappush(A,4)
print(A)
min=heapq.heappop(A)
print(A)
print(min)




def heapsort(arr):
    heapq.heapify(arr)
    n=len(arr)
    new_list=[]
    for i in range (n):
        minn=heapq.heappop(arr)
        new_list.append(minn)
    return new_list
    
arr=[1,3,6,2,43,89,7]
print(heapsort(arr))