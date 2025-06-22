lst=[1,3,"muh",5,66,"shahin"]
string=[x for x in lst if type(x)==str ]
intger=[x for x in lst if type(x)==int ]
print(string)
print(intger)