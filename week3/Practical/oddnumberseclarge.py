lst=[1,2,4,5,6,8,7,11,13]
first=lst[0]
second=lst[1]
for i in range(1,len(lst)):
    if lst[i]%2!=0:
        if lst[i]>first:
            second=first
            first=lst[i]
        elif lst[i]>second and lst[i]!=first:
            second=lst[i]
        
print(second)