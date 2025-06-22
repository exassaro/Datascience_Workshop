 #heap sort ascending
def heapify(arr,n,i):
    largest=i
    left_node=i*2 +1
    right_node=i*2 +2
    if left_node<n and arr[left_node]>arr[largest]:
        largest=left_node
    if right_node<n and arr[right_node]>arr[largest]:
        largest=right_node
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)
        
        
def heap_sort(arr):
    n=len(arr)
    ran=(n//2)-1
    for i in range(ran,-1,-1):
        heapify(arr,n,i)
    print (arr)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
        
        
arr=[4,5,1,9,11,10,2]
heap_sort(arr)
print("Ascending: ",arr)

#heap sort descending
def heapify(arr,n,i):
    smallest=i
    left_node=i*2 +1
    right_node=i*2 +2
    if left_node<n and arr[left_node]<arr[smallest]:
        smallest=left_node
    if right_node<n and arr[right_node]<arr[smallest]:
        smallest=right_node
    if smallest!=i:
        arr[smallest],arr[i]=arr[i],arr[smallest]
        heapify(arr,n,smallest)
        
        
def heap_sort(arr):
    n=len(arr)
    ran=(len(arr)//2)-1
    for i in range(ran,-1,-1):
        heapify(arr,n,i)
    print (arr)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
        
        
arr=[1,3,4,2,5,2,10,3]
heap_sort(arr)
print("Descending:",arr)

#Max Heap
class MaxHeap:
    def __init__(self):
        self.heap=[]
    def insert(self,value):
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)
    def _heapify_up(self,idx):
        parent_idx=(idx-1)//2
        if idx>0 and self.heap[parent_idx]<self.heap[idx]:
            self.heap[parent_idx],self.heap[idx]=self.heap[idx],self.heap[parent_idx]
            self._heapify_up(parent_idx)
            
    def delete(self):
        if not self.heap:
            return False
        if len(self.heap)==1:
            return self.heap.pop()
        del_node=self.heap[0]
        self.heap[0]=self.heap.pop()
        self._heapify_down(0)
        return del_node
    
    def _heapify_down(self,idx):
        large_idx=idx
        left_idx=2*idx + 1
        right_idx=2*idx + 2
        if left_idx<len(self.heap) and self.heap[large_idx]<self.heap[left_idx]:
            large_idx=left_idx
        if right_idx<len(self.heap) and self.heap[large_idx]<self.heap[right_idx]:
            large_idx=right_idx
        if large_idx!=idx:
            self.heap[large_idx],self.heap[idx]=self.heap[idx],self.heap[large_idx]
            self._heapify_down(large_idx)
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    def get_heap(self):
        return self.heap
    
    def clear(self):
        self.heap=[]
        
    def get_size(self):
        return len(self.heap)
    
    def is_Empty(self):
        return len(self.heap)==0
    

max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(30)
max_heap.insert(4)
max_heap.insert(25)
heap_values = max_heap.get_heap()
print(heap_values)
max_heap.delete()
heap_values = max_heap.get_heap()
print(heap_values)
print(max_heap.get_size())
print(max_heap.peek())

#Using Builtin Lib
import heapq

class InbuiltMaxHeap:
    def __init__(self):
        self.heap = []  # Python heapq is a MinHeap, so we store negative values

    def insert(self, value):
        heapq.heappush(self.heap, -value)  # Push negative value to simulate MaxHeap

    def delete(self):
        if self.heap:
            return -heapq.heappop(self.heap)  # Pop and return as positive
        return None

    def peek(self):
        if self.heap:
            return -self.heap[0]  # Peek max element
        return None

    def get_heap(self):
        return [-val for val in self.heap]  # Convert back to normal values

    def build_heap(self, arr):
        self.heap = [-val for val in arr]  # Convert all values to negative
        heapq.heapify(self.heap)  # Heapify in O(n)

    def heap_sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(-heapq.heappop(self.heap))  # Extract max one by one
        return sorted_list


# Example Usage
max_heap = InbuiltMaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(30)
max_heap.insert(4)
max_heap.insert(25)

print("Heap:", max_heap.get_heap())  # [30, 25, 20, 4, 10]
print("Deleted:", max_heap.delete())  # 30 (max element)
print("Heap after delete:", max_heap.get_heap())  # [25, 10, 20, 4]

# Building heap from list
max_heap.build_heap([3, 1, 5, 10, 2])
print("Built Heap:", max_heap.get_heap())  # [10, 3, 5, 1, 2]

# Heap Sort
print("Heap Sort Result:", max_heap.heap_sort())  # [10, 5, 3, 2, 1]


#min Heap
class MinHeap():
    def __init__(self):
        self.heap=[]
        
    def insert(self,value):
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)
        
    def _heapify_up(self,idx):
        parent_idx=(idx-1)//2
        if idx>0 and self.heap[parent_idx]>self.heap[idx]:
            self.heap[parent_idx],self.heap[idx]=self.heap[idx],self.heap[parent_idx]
            self._heapify_up(parent_idx)
            
    def delete(self):
        if not self.heap:
            return False
        if len(self.heap)==1:
            return self.heap.pop()
        del_node=self.heap[0]
        self.heap[0]=self.heap.pop()
        self._heapify_down(0)
        return del_node
    
    def _heapify_down(self,idx):
        small_idx=idx
        left_idx=2*idx + 1
        right_idx=2*idx + 2
        if left_idx<len(self.heap) and self.heap[small_idx]>self.heap[left_idx]:
            small_idx=left_idx
        if right_idx<len(self.heap) and self.heap[small_idx]>self.heap[right_idx]:
            small_idx=right_idx
        if small_idx!=idx:
            self.heap[small_idx],self.heap[idx]=self.heap[idx],self.heap[small_idx]
            self._heapify_down(small_idx)
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    def get_heap(self):
        return self.heap
    
    def clear(self):
        self.heap=[]
        
    def get_size(self):
        return len(self.heap)
    
    def is_Empty(self):
        return len(self.heap)==0

            
            
            