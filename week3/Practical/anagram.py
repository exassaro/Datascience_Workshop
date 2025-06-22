#by sorting

def anagram(str1,str2):
    str1=str1.replace(" ", "").lower()
    str2=str2.replace(" ", "").lower()
    
    return sorted(str1)==sorted(str2)

str1="Silent"
str2="Listen"

print(anagram(str1,str2))

