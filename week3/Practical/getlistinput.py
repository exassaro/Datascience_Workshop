lst=input("Enter values: ")
lst2=lst.split()
positive=[]
for x in lst2:
    num=int(x)
    if num>0:
        positive.append(x)
        
print(f"positive = {positive}")
        