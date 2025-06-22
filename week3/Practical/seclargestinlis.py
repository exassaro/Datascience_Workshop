#second largest in list without sorting

list=[1,5,8,9,7]
first=list[0]
for i in range (1,len(list)):
        if list[i]>first:
            second=first
            first=list[i]
        elif list[i]>second and list[i] != first:
            second = list[i]
            
print(second)