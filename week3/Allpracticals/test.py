dic1={'a':21,'b':32}
dic2={'c':31,'a':10}
for i,j in dic2.items():
    if i in dic1:
        dic1[i]=dic1[i]+ j
    else:
        dic1[i]=j
print(dic1)