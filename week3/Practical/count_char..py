def count_char(str):
    char_count={}
    for char in str:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char]=1
            
    return char_count

string = input("enter a string: ")

result = count_char(string)

print(result)


string="My name is shahin"
string=string.lower()
char_count={}
for  char in string:
    if char != " ":
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
print(char_count)