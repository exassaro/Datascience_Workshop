# by remove()

def remv_wht(str):
    return str.replace(" ","")
str=input("enter a string: ")
print(remv_wht(str))

#by split
def remv_whtsp(str):
    return "" .join(str.split())
str2=input("enter a string: ")
print(remv_whtsp(str2))

#by for loop
def rmv_whtspc(str):
    result=""
    for i in str:
        if i != " ":
            result += i
    return result

string = input("enter a string")
print (rmv_whtspc(string))
        