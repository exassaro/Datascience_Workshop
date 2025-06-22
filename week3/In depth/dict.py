dict1={
    "name":"Alice",
    "age" : 21,
    "city":"Newyork"
}

print(dict1)
print(dict1["name"])# acessing values using keys
print(dict1.get("age")) # using get to acess
print(dict1.get("gender", "Not Found"))  # Output: Not Found
dict1["gender"]="male"
print(dict1)
dict1["age"]= 28
print(dict1)

my_dict = {"name": "Alan", "age": 25, "city": "New Jersey"}
del my_dict["age"]
print (my_dict)
city=my_dict.pop("city")
print(city)#return removedd value
print (my_dict)
my_dict.clear()
print(my_dict)

dict4 = {"name": "Aleena", "age": 50, "city": "USA"}
for key in dict4:
    print (key)
    
for values in dict4.values():
    print (values)
    
for key, values in dict4.items():
    print (key, ":" ,values)
    
    
keys =["a","b","c"]
new_dict=dict.fromkeys(keys,0)
print(new_dict)

dict24={
    "name":"shahin",
    "age":24,
    "class":"BCK225"
}
print(dict24.get("name"))
print(dict24.get("height","Not found"))
print(dict24.items())#output dict as tuples
print(dict24.keys())#output all keys as set inside tuple
print(dict24.values())#output all values as set inside tuple
gender = dict24.pop("gender","N/A") # check for value to remove if not present output default
print(gender)
last_item=dict24.popitem()#removes last inserted key value
print(last_item)
print(dict24)
print(dict24.setdefault("name", "bob"))#check if present not present it willadd
print(dict24.setdefault("gender", "male"))
print(dict24)
dict24.update({"height":"164 cm","weight": "60kg"}) #update as dict
print(dict24)
dict24.update([("mark",10),("grade","A+")])#  update using iterables
print(dict24)
print("mark" in dict24)

numbers=[1,2,4,5]
squares={num : num**2 for num in numbers } #dict comprehension
print(squares)
even_squares = {num : num**2 for num in numbers if num%2==0}
print(even_squares)
odd_even = {num : "even" if num%2==0 else "odd" for num in numbers}
print(odd_even)
key=[1,2,3,4,5]
values =["one","two","three","four","five"]
created_dict={key : values for key,values in zip(key,values)}
print(created_dict)