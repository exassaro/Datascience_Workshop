lst=[1,"shahin",2,"muhammed",6,8,"lami","redro",5]

strings= list(filter(lambda x : type(x)==str,lst))
integers=list(filter(lambda x : type(x)==int,lst))
added=sum(filter(lambda x : type(x)==int,lst))
sum=sum(integers)

print(strings)
print(integers)
print(sum)
print(added)

add=0
for i in integers:
    add+=i

print(add)