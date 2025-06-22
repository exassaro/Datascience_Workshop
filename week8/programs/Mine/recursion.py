#sum of digit
def dsum(x):
    if x==0:
        return 0
    return x%10+dsum(x//10)
    
print(dsum(1914))

#factorial
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
    
print(fact(3))

#fibonacci (generate nth fibanocci number)
def fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fib(n-1)+fib(n-2)

print(fib(10))

#reverse string
def rev_str(text):
    if len(text)==1:
        return text
    return rev_str(text[1:])+text[0]

print(rev_str("shahinsha"))

#sum of fibonacci
def fib(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    return fib(num-1) + fib(num-2)


print(fib(5))


def sum_fib(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    return sum_fib(num-1) + fib(num)


print(sum_fib(6))



#Remove sepecific letter from string
def remov(word):
    if len(word)==0:
        return ""
    elif word[0]=="l":
        return remov(word[1:])
    else:
        return word[0]+remov(word[1:])
word1="helloworld"
print(remov(word1))

# sum of array
def summ(liss):
    if len(liss)==0:
        return 0
    else:
        return liss[0]+summ(liss[1:])
liss1=[1,2,4,5,6,7]
print(summ(liss1))


# smallest by recursion
def smallest(liss,last,small):                 # n is assign small
    if last<0:
        return small
    elif liss[last]<small:
        small=liss[last]
    return smallest(liss,last-1,small)
liss1=[1,2,3,4,5,6]
print(smallest(liss1,len(liss1)-1,liss1[0]))

#smallest way
def smallest(liss):
    if len(liss)==1:
        return liss[0]
    small=smallest(liss[1:])
    return liss[0] if liss[0]<small else small

liss = [3, 45, 6, 4,2,35, 8]
print(smallest(liss))

#string permutation
def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    
    for i in range(len(s)):
        ch = s[i]
        rest = s[:i] + s[i+1:]  
        permute(rest, answer + ch)

permute("abc")


# secsmallest by recursion
def secsmallest(arr,last,small,secsmall):
    if last<0:
        return secsmall
    elif arr[last]<small:
        secsmall=small
        small=arr[last]
    elif arr[last]<secsmall and arr[last]!=small:
        secsmall=arr[last]
    return secsmallest(arr,last-1,small,secsmall)
arr1=[1,2,3,4,5]
print(secsmallest(arr1,len(arr1)-1,arr1[0],max(arr1)))

#Array reverse using recursion
def reve(arr,start,end):
    if start>=end:
        return
    else:
        arr[start],arr[end]=arr[end],arr[start]
        reve(arr,start+1,end-1)
arr1=[1,2,3,4,45,7]
reve(arr1,0,len(arr1)-1)
print(arr1)


#binary seacrh by recursion
def binary(arr, left, right, target):
    if left > right:
        return -1  # Base case: element not found
    
    mid = (left + right) // 2  # Calculate mid index

    if arr[mid] == target:
        return mid  # Target found at mid index
    elif arr[mid] < target:
        return binary(arr, mid + 1, right, target)  # Search in the right half
    else:
        return binary(arr, left, mid - 1, target)  # Search in the left half

# Example usage
arr = [1, 3, 5, 7, 9, 11, 15]
target = 7
result = binary(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")




