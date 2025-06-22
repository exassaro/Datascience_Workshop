# from collections import Counter
# def heapify(arr,n,i):
#     smallest=i
#     left_node=2*i+1
#     right_node=2*i+2
#     if left_node<n and arr[smallest][0]>arr[left_node][0]:
#         smallest=left_node
#     if right_node<n and arr[smallest][0]>arr[right_node][0]:
#         smallest=right_node    
#     if smallest!=i:
#         arr[smallest],arr[i]=arr[i],arr[smallest]
#         heapify(arr,n,smallest)
    
# def heapsort(arr):
#     n=len(arr)
#     ran=(n//2)-1
#     for i in range(ran,-1,-1):
#         heapify(arr,n,i)
#     for i in range(n-1,0,-1):
#         arr[i],arr[0]=arr[0],arr[i]
#         heapify(arr,i,0)
        
# def k_freq(arr,k):
#     counter=Counter(arr)
#     freq_list=[(freq,num) for num,freq in counter.items()]
#     heapsort(freq_list)
#     result = [num for freq, num in reversed(freq_list[-k:])]
#     return result
            
# A1= [1,1,1,2,2,3]

# A2=[4,4,4,6,6,7,7,7,7]

# print(k_freq(A1,2))

# print(k_freq(A2,2))




# from collections import Counter
# import heapq

# def topKFrequent(nums, k):
#     freq_map = Counter(nums)
#     min_heap = []
    
#     for num, freq in freq_map.items():
#         heapq.heappush(min_heap, (freq, num)) 
#         if len(min_heap) > k:
#             heapq.heappop(min_heap) 
#     result = [num for freq, num in sorted(min_heap, reverse=True, key=lambda x: x[0])]
    
#     return result

# print(topKFrequent([1,1,1,2,2,3], 2))


# print(topKFrequent([4,4,4,6,6,7,7,7,7], 2))  

    


# def heapify(arr,n,i):
#     smallest=i
#     left_node=2*i+1
#     right_node=2*i+2
#     if left_node<n and arr[smallest]>arr[left_node]:
#         smallest=left_node
#     if right_node<n and arr[smallest]>arr[right_node]:
#         smallest=right_node    
#     if smallest!=i:
#         arr[smallest],arr[i]=arr[i],arr[smallest]
#         heapify(arr,n,smallest)
    
# def heapsort(arr):
#     n=len(arr)
#     ran=(n//2)-1
#     for i in range(ran,-1,-1):
#         heapify(arr,n,i)
#     for i in range(n-1,0,-1):
#         arr[i],arr[0]=arr[0],arr[i]
#         heapify(arr,i,0)
        
# def k_freq(arr,k):
#     dic={}
#     for i in arr:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     freq_list=[(freq,nums) for nums,freq in dic.items()]
#     heapsort(freq_list)
#     res=[num for freq,num in freq_list[:k]]
#     return res
    
            

# A1= [1,1,1,2,2,3,3,3,3,4,4,4,4,4]

# A2=[4,4,4,6,6,6,6,6,7,7,7,7]

# print(k_freq(A1,2))
# print(k_freq(A2,2))


