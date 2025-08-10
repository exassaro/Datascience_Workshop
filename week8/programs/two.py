from ftplib import error_temp


# SEARCH
# Binary search
def binary(liss,target):
    left=0
    right=len(liss)-1
    while left<=right:
        mid=(left+right)//2
        if liss[mid]==target:
            return mid
        elif liss[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
liss1=[22,23,24,25,26,27,28]
target1=26
print(binary(liss1,target1))

# Linear search
# def linear(liss,target):
#     for i in range(len(liss)):
#         if liss[i]==target:
#             return i
#     return -1
# liss1=[22,4,5,77,8,9,45,54]
# target1=9
# v=linear(liss1,target1)
# print(v)

#RECURSION
# 1.febinocci (binary-function call twise)
# def febi(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return febi(num-1)+febi(num-2)
# for i in range(6):
#     print(febi(i))

# 2.factorial (direct-fuction call itself, normalone)
# def factorial(num):
#     if num<=1:
#         return 1
#     else:
#         return num*factorial(num-1)
# num1=factorial(5)
# print(num1)

# 3.remove sepecif letter from string
def remov(word):
    if len(word)==0:
        return ""
    elif word[0]=="l":
        return remov(word[1:])
    else:
        return word[0]+remov(word[1:])
word1="helloworld"
print(remov(word1))

# 4.array reverse using recursion
# def reve(arr,start,end):
#     if start>=end:
#         return
#     else:
#         arr[start],arr[end]=arr[end],arr[start]
#         reve(arr,start+1,end-1)
# arr1=[1,2,3,4,45,7]
# reve(arr1,0,len(arr1)-1)
# print(arr1)

# 5.smallest by recursion
# def smallest(liss,last,small):                 # n is assign small
#     if last<0:
#         return small
#     elif liss[last]<small:
#         small=liss[last]
#     return smallest(liss,last-1,small)
# liss1=[1,2,3,4,5,6]
# print(smallest(liss1,len(liss1)-1,liss1[0]))

# 6.secsmallest by recursion
# def secsmallest(arr,last,small,secsmall):
#     if last<0:
#         return secsmall
#     elif arr[last]<small:
#         secsmall=small
#         small=arr[last]
#     elif arr[last]<secsmall and arr[last]!=small:
#         secsmall=arr[last]
#     return secsmallest(arr,last-1,small,secsmall)
# arr1=[1,2,3,4,5]
# print(secsmallest(arr1,len(arr1)-1,arr1[0],max(arr1)))

# 7.sumofarray
def summ(liss):
    if len(liss)==0:
        return 1
    else:
        return liss[0]+summ(liss[1:])
liss1=[1,2,4,5,6,7]
print(summ(liss1))

# 7. Binary using revursion
# def binary(arr,left,right,target):
#     mid=(left+right)//2
#     if left>right:
#         return -1
#     elif arr[mid]==target:
#         return mid
#     elif arr[mid]<target:
#         return binary(arr,mid+1,right,target)
#     else:
#         return binary(arr,left,mid-1,target)

# STRING
# 1.flatten multidimensional arry(neste list to list)
# def flat(nested):
#     new=[]
#     for lis in nested:
#         for i in lis:
#             new.append(i)
#     return new
# lis=[[1,2,3],[3,4,7],[9,66,54]]
# print(flat(lis))

# 2.extract number from string
# def string(word):
#     spli=word.split()
#     new=""
#     for i in spli:
#         if "0"<=i<="9":
#             new+=i+" "
#     return new
# word1=("The 12 apples cost 25 dollars and 40 cents.")
# print(string(word1))