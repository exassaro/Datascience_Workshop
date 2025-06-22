#valid parenthesis

def is_valid_parenthesis(s):
    stack=[]
    mapping={")":"(","}":"{","]":"["}
    
    for char in s:
        if char in mapping:
            top_element=stack.pop() if stack else "#"
            if mapping[char]!=top_element:
                return False
        else:
            stack.append(char)
            
    return not stack
    
print(is_valid_parenthesis("({[]})"))
print(is_valid_parenthesis("({[})"))

#Two sum-hash table
def two_sum(nums,target):
    hash_table={}
    
    for i, num in enumerate(nums):
        diff=target-num
        if diff in hash_table:
            return [hash_table[diff],i]
        hash_table[num]=i
    return None
    
    
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)


#Function to find the first non repeating character using hash table
def first_non_repeating_char(s):
    char_count={}
    for char in s:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
        
    for char in s:
        if char_count[char]==1:
            return char
        
    return None

#another way
# def first_non_repeating_char(s):
#     char_count = {}
    
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1  # Cleaner way to update count
        
#     for char in s:
#         if char_count[char] == 1:
#             return char
        
#     return None

print(first_non_repeating_char("hello"))  
print(first_non_repeating_char("swiss")) 


#Count frequency of charcters in a string using hash table
def freq(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1  # Cleaner way to update count
        
        
    return char_count

print(freq("banana"))


