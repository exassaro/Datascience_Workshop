def count_consecutive(string):
    result=[]
    count=1
    for i in range(1, len(string)):
        if string[i]==string[i-1]:
            count+=1
        else:
            result.append((string[i-1],count))
            count=1
            
            
    result.append((string[-1],count)) 
    
    return result
    
string="aabbccaabbc"
output=count_consecutive(string)
print(output)
