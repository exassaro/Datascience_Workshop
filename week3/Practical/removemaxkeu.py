data={'a':2000,'b':4000,'c':1000}

max_key=None
max_value=None
for i,j in data.items():
    if max_key is None or j>max_value:
        max_key=i
        max_value=j
        
print(max_key, ":", max_value)
        
del data[max_key]

print(data)