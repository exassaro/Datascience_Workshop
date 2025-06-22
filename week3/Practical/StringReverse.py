#reverse without reverse()method
str="Shahinsha"
rev_str=str[::-1]#slice notation[start:end:step]
print(rev_str)

#using reverse method
str="shahinsha"
lst=list(str)
lst.reverse()
str2=''.join(lst) #join back to string

print(str2)