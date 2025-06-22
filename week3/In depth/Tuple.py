tup1=(1,5,4,7,8,5,1)
tup2=(5,4,8,7,12,10)
tup3 = tup1 +tup2 #coccatenate
tup4 = tup1*3 #Repeat
print(tup1)
print(tup1[1:2])
print(tup3)#coccatenate
print(tup4)#Repeat

tup5 = (4,5,6,4)
a,b,c,d =tup5 #tuple destructing or tuple unpacking
print(a)
print(b, c)
tup6 = tup5.index(4)
tup7 = tup5.index(4,1,4)
a,b,_,d=tup5
print(a,b, d)
print(tup6)
print(tup7)