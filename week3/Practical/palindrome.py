#with slice method
def is_Palindrome(s):
    if (s==s[::-1]):
        print("String is palindrome")
    else:
        print("String is not palindrome")

str1="radar"
str2="hello"

is_Palindrome (str1)
is_Palindrome (str2)

#by for loop
def is_pal(str):
    dupe=""
    for x in str:
        dupe = x + dupe
    print(dupe)
    return str == dupe

x=input("enter a string: ")
result = is_pal(x)

if result:
    print("String is palindrome")
else:
    print("Not palindrome")

#another method
def palindrome(str):
    str=str.lower()
    if (str==str[::-1]):
        print("string is palindrome")
    else:
        print("string is not palindrome")
        
str=input("Enter a string: ")

palindrome(str)