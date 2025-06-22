string="swiss"
char_count={}
for i in string:
    if i in char_count:
        char_count[i]+=1
    else:
        char_count[i]=1
        
for i in string:
    if char_count[i]==1:
        print(i)
        break
    
string="swiss"
char_count={}
for i in string:
    if i in char_count:
        char_count[i]+=1
    else:
        char_count[i]=1
        
for i in string:
    if char_count[i]==1:
        print(i)
        break
        
