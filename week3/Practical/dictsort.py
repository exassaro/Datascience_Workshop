dict1={'a':3, 'b':1, 'c':2 }
sorted_dict=sorted(dict1.items(),key=lambda x:x[1])
converted_dict=dict(sorted_dict)
print(converted_dict)