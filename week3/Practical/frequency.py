lst=[1,2,3,5,4,3,87,1,1,2,5,4]

dict={}

for x in lst:
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1
print(dict)