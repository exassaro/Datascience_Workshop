# Reverse a string
alpha = "shibily"
item = ""
for x in alpha:
    item = x+item
#####################
#
#
#
#
#
#
#
#
#
# # #find the longest word in the sentence
# # sentence = "hi my name is shibily and i am studying in brototype"
# # longest = ""
# # words = sentence.split()
# # for x in words:
# #     if len(x) > len(longest):
# #         longest = x
# # print(longest)
# #######################
#
#
#
#
#
#
#
#
#
#
# #check whether a given string is palindrome or not:
#
# # def isPal(word):
# #     dupe = ""
# #     for item in word:
# #         dupe = item + dupe
# #     print(dupe)
# #     return word==dupe
# # print(isPal(input("enter a word")))
# #######################
#
#
#
#
#
#
#
#
# #remove dupes from an array
# # def remDupe(listOne):
# #     newList = []
# #     for x in listOne:
# #         if x not in newList:
# #             newList.append(x)
# #     return newList
# #
# # listOne = [1,2,3,4,5,6,1,2,3,8,9,2,5,6,8,9,7,4,5,2,56,96,666688,2,5,85,5,6,4,8,5,5,8,4,5,]
# # print(remDupe(listOne))
# #########################
#
#
#
#
#
#
#
#
# #check two strings are anagram or not
#
# # def isAnagram(alpha,beta):
# #     count = 0
# #     for non in alpha:
# #         for pop in beta:
# #             if pop == non:
# #                 count += 1
# #     return count == len(alpha)
# #
# # alpha = "silent"
# # beta = "ntelsi"
# # print(isAnagram(alpha,beta))
# ############################
#
#
#
#
#
#
#
# #return the number of vowels in a string
#
# # def vowelCheck(word):
# #     word = word.lower()
# #     count = 0
# #     vowel = "aeiou"
# #     for x in word:
# #         for y in vowel:
# #             if x ==y:
# #                 count+=1
# #     print(f"No of vowels in word is {count}")
# # word = "hello this is me shibily checking vowel count"
# # vowelCheck(word)
#
# ###############################
#
#
#
#
#
#
# #find the largest number in an array
#
# # def checkLargest(numbers):
# #     largest = numbers[0]
# #     for item in numbers:
# #         if item > largest:
# #             largest = item
# #     return largest
# #
# # numbers = [1,2,4,5,6,888,2,3,9,9,8,8,55,5,9999,52,3,5]
# # print(checkLargest(numbers))
#
# ###############################
#
#
#
#
#
#
#
#
#
# #check if the number is prime or not
#
# # def isPrime(number):
# #     if number < 2:
# #         return "is a prime numberfdf"
# #
# #     for item in range(2,number):
# #         if number % item ==0:
# #             return "not a prime number"
# #     return "is a prime number"
# #
# #
# #
# # print(isPrime(18))
#
# ####################################
#
#
#
#
#
#
#
# #function to calculate facrorial of anumber
#
# # def factorial(num):
# #     sum = 1
# #     for item in range(1,num+1):
# #         sum = sum*item
# #     return sum
# # print(factorial(5))
#
# #factorial using recursion
#
# # def factorial(num):
# #     if num <=1:
# #         return 1
# #     return num* factorial(num - 1)
# # print(factorial(1))
#
# ############################
#
#
#
#
#
# #Remove all white space charechters in a string
#
# # def remove(word):
# #     new = ""
# #     for item in word:
# #         if item != " ":
# #            new = new+item
# #     print(new)
# #
# # remove("hi iam shibily")
#
# #############################
#
#
#
#
#
# #find even or odd numbers in an array
#
# # def find(numbers):
# #     odd = []
# #     even = []
# #     for item in numbers:
# #         if item % 2 == 0:
# #             even.append(item)
# #         else:
# #             odd.append(item)
# #     return f"odd numbers are {odd} and even numbers are {even}"
# #
# # numbers = [1,2,3,4,5,6,7,8,9,10]
# # print(find(numbers))
# #################################
#
#
#
#
#
#
#
# #count the occurence of each charechter in a string
#
# # def countChar(alpha):
# #     dict = {}
# #     for letter in alpha:
# #         if letter != " ":
# #             if letter in dict:
# #                 dict[letter] += 1
# #             else:
# #                 dict[letter] = 1
# #     return dict
# #
# # alpha = "hi my name is shibily"
# # print(countChar(alpha))
# #####################################
#
#
#
#
#
#
# #reverse a list without using the reverse method
#
# # def rev(alpha):
# #     beta = []
# #     for y in range(len(alpha) -1, -1, -1):
# #         values = alpha[y]
# #         beta.append(values)
# #     return beta
# #
# # alpha = [1,2,3,4,5,6,7,8]
# # print(rev(alpha))
#
# ########################################
#
#
#
#
#
#
#
#
# #print the frequency of words in a string
#
# # letters = "babbcccnnnbbbtttyyccbacc"
# # counted = ""
# # count = 1
# #
# # for item in range(0,len(letters)):
# #     if letters[item]== letters[item -1]:
# #         count +=1
# #         # counted += letters[item] + str(count)
# #     else:
# #
# #         counted += letters[item] + str(count)
# #         count = 1
# #
# # counted += letters[-1] + str(count)
# #
# # print(counted)
#
#
# # letter = "b1a1b1c2n3b3t3y3c2b2a1c1c2"
# # word = ""
# #
# # for item in range(0,len(letter),2):
# #     letters = letter[item]
# #     count = int(letter[item +1])
# #     word += letters*count
# # print(word)
#
#
#
#
#
#
#
#
#
# #####################################
# ###       DECORATOR FUNCTION      ###
# #####################################
# # def DecoRator(alpha):
# #     def wrapper():
# #         print("start")
# #         alpha()
# #         print("stop")
# #     return wrapper
# #
# # @DecoRator
# # def hello():
# #     print("hellowww!!!")
# #
# #
# # hello()
# #####################################
#
#
#
#
#
# #####################################
# ###       GENERATOR FUNCTION      ###
# #####################################
# #
# # def generator(num):
# #     count = 1
# #     while count<= num:
# #         yield count
# #         count+=1
# # counter = generator(5)
# # for i in counter:
# #     print(i)
# #
#
#
#
#
#
# # list = [55,11,22,33,44,7,5,6,9,5,45,7777,4,22,8888,5,5,652]
# #
# # largest = float('-inf')
# # second = 0
# # for item in list:
# #     if item > largest:
# #         second = largest
# #         largest = item
# #
# #
# #
# #
# # print(second)
# # print(largest)
#
#
#
#
#
# ###################################
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #program to merge  two dicrioneries
#
# # def merge(alpha,beta):
# #     tango = alpha w beta
# #     return tango
# # alpha = {'name':"shibily",'age':25}
# # beta = {'name' : "shibily",'place': 'thuvuur' }
# #
# # print(merge(alpha,beta))
#
#
#
#
#
# ####################################
#
#
#
#
#
#
#
# #program to peint the largest key value in dicrt of list
#
# # mylist = [{'a':4},{'b': 5},{'c':6}]
# #
# # high = max(mylist, key = lambda d : list(d.values()))
# # print(high)
#
#
#
#
# #get highest value in a dictionery and remove it
# ###################################################
#
#
#
# #############################################
#
#
# #merging 2 lists into dictionry key values using zip(
# # list1 = [1,2,3,4,5,6,7]
# # list2 = [7,8,9,10,11,12,13]
# #
# # new = zip(list1,list2)
# #
# # print(next(new))
# # print(next(new))
# # print(next(new))
# # print(next(new))
# # print(next(new))
# #
#
#
#
#
# #currying example 2
#
# # def chickencurry(a):
# #     def addA(b):
# #         def addB(c):
# #             def addD(d):
# #                 def addE(e):
# #                     return a+b+c+d+e
# #                 return addE
# #             return addD
# #         return addB
# #     return addA
# #
# # alpha = chickencurry(1)
# # beta = alpha(5)
# # teta = beta(8)
# # tango = teta(3)
# # print(tango(9))
# #
# #
#
#
#
#
# #
# # #closure example
# # def outer_function(message):
# #     def inner_function():
# #         print(message)
# #     return inner_function
# #
# # closure_example = outer_function("Hello, World!")
# #
# # closure_example()
#
#
#
#



#########################################################################################









#
#
#
#
#
# ####################################
# #          slicing mmethods        #
# ####################################
#
#
# #        sequence[start:stop:step]
#
#
# #####    1 slicing a list
# mylist = [0,1,2,3,4,5,6,7,8,9]
#
#     #from index 2 to 5
# print(mylist[2:5])
#
#     #slicing from start to index 5
# print(mylist[:5])
#     #slicing with step
# print(mylist[::2])
#
#
# #####   2 slicing a string
#
# mystring = "hello world"
#
#     # slicing from 7 to 12
#
# print(mystring[7:12])
#
#     #first 5 charechters
#
# print(mystring[:5])
#
#     #slicing with neative index
#
# print(mystring[-6:])
#
#     #reverse using slice
#
# print(mystring[::-1])
#


##################################################################3









































###################################
#        dict comprehension       #
#############333#########333333###3



# # 1   dictionery to crete pairs of squares of numbers from 1 to 10
# dictnew = {k: k**2 for k in range(1,10)}
# print(dictnew)
#





#2 Write a dictionary comprehension that counts the frequency of each character in the string "hello world"

#
# word = "hello world"
# dictcount = {k: word.count(k) for k in word}
# print(dictcount)
#




# 3Create a dictionary that converts temperatures from Celsius (0 to 10) to Fahrenheit using the formula

# dictnew = {k: k*9/5+32 for k in range(1,11)}
# print(dictnew)


#4    Generate a dictionary from a list of numbers, keeping only the even numbers
#     and multiplying them by 2. For example, for the list [1, 2, 3, 4, 5, 6],
#     he output should be {2: 4, 4: 8, 6: 12}.

# listOne = [1,2,3,4,5,6,7]
# dictnew = {k: k*2 for k in listOne if k%2==0}
# print(dictnew)
#



#5    Write a dictionary comprehension that takes a list of words
# (e.g., ["apple", "banana", "cherry"]) and creates a dictionary with
# ech word as the key and its length as the value.

# listone = ["apple","banana","cherry"]
#
# dictnew = { k: len(k) for k in listone }
# print(dictnew)



#6    program to print enumerated key values pairs of a list

#
# listone = ["apple","banana","cherry"]
#
# # dictnew = { k : v for k,v in enumerate(listone) }
# dictone = enumerate(listone)
# print(dictone)
#
# for items in dictone:
#     print(items)





#7     Given two lists, one of keys and one of values
# (e.g., keys = ['a', 'b', 'c'] and values = [1, 2, 3]),
# create a dictionary that maps keys to values.

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
#
# dictone = zip(keys,values)
#
# new = {}
# for x,y in dictone:
#     new[x] = y
#
# print(new)






#8       Nested Dictionary Comprehension: Create a nested dictionary
# comprehension that generates a multiplication table for numbers 1
# through 5. The outer keys should be the multipliers, and the inner
# keys should be the multiplicands.

#
# dictOne = { outer:{k:k*outer for k in range (1,6)} for outer in range(1,6)}
# print(dictOne)









# 9    Create a dictionary from two lists: one with names and the other with ages
# , where the names are keys and the ages are values.

# #method 1
# alpha = ["shibily","hemdan","shamil","nihal","akhil","jinan"]
# beta = [25,23,22,20,20,19]
#
# dict = dict(zip(alpha,beta))
# print(dict)
#
# #method 2
# alpha = ["shibily","hemdan","shamil","nihal","akhil","jinan"]
# beta = [25,23,22,20,20,19]
#
# dict = {k:v for k,v in zip(alpha,beta)}
























































