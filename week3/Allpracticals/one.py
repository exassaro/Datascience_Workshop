# from itertools import count
#
#
# def lines(text):
#     n=3
#     new=text.split()
#     count=0
#     for i in new:
#         if len(i)>n:
#             count+=1
#     return count
# text=("This is a simple text file.  "
#       "The file is used for testing the Python script.  "
#       "Python is amazing, and this file helps demonstrate its power.  ")
# v=lines(text)
# print("total words",v)
# def space(text):
#     new=text.split()
#     count=0
#     for i in new:
#         if new:
#             count+=1
#     return count
# text=("This is a simple text file.  "
#       "The file is used for testing the Python script.  "
#       "Python is amazing, and this file helps demonstrate its power.  ")
# w=space(text)
# print("total words:",w)
# def num_oflines(text):
#     new=[]
#     count=0
#     for j in text:
#         new.append(j)
#         count+=
#     return count
# text=("This is a simple text file.  "
#       "The file is used for testing the Python script.  "
#       "Python is amazing, and this file helps demonstrate its power.  ")
# g=space(text)
# print("total words:",g)
from idlelib.rpc import RPCHandler
from itertools import count

# import os
# import string
# from collections import Counter
#
# # Predefined list of common stop words
# STOP_WORDS = {"and", "the", "is", "in", "this", "a", "of", "for", "its", "to", "on", "an"}
#
#
# def analyze_file(file_path):
#     try:
#         # Check if file exists
#         if not os.path.exists(file_path):
#             print("Error: File does not exist.")
#             return
#
#         # Read the file content
#         with open(file_path, 'r') as file:
#             lines = file.readlines()
#
#         # Handle empty file
#         if not lines:
#             print("Error: File is empty.")
#             return
#
#         # Initialize variables
#         total_lines = len(lines)
#         total_words = 0
#         total_characters = 0
#         word_counts = Counter()
#
#         # Process each line
#         for line in lines:
#             # Remove punctuation and convert to lowercase
#             cleaned_line = line.translate(str.maketrans('', '', string.punctuation)).lower()
#             words = cleaned_line.split()
#             total_words += len(words)
#             total_characters += sum(len(word) for word in words)
#             word_counts.update(word for word in words if word not in STOP_WORDS)
#
#         # Get the top 5 most frequent words
#         top_words = word_counts.most_common(5)
#
#         # Display results
#         print("\nFile Analysis:")
#         print("-" * 18)
#         print(f"Total Lines: {total_lines}")
#         print(f"Total Words: {total_words}")
#         print(f"Total Characters (Excluding Spaces): {total_characters}")
#         print("Top 5 Most Frequent Words:")
#         for i, (word, count) in enumerate(top_words, 1):
#             print(f"{i}. {word} - {count}")
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
#
# # Accept file path from the user
# file_path = input("Enter the file path to analyze: ")
# analyze_file(file_path)





# from collections import Counter
# import string
#
# # Predefined list of common stop words
# STOP_WORDS = {"and", "the", "is", "in", "this", "a", "of", "for", "its", "to", "on", "an"}
#
# # Function to count lines in the text
# def num_of_lines(text):
#     return text.count("\n") + 1  # Counting the number of lines
#
# # Function to count words greater than n characters
# def count_words_greater_than(text, n):
#     words = text.split()
#     count = 0
#     for word in words:
#         if len(word) > n:
#             count += 1
#     return count
#
# # Function to count total words
# def total_words(text):
#     words = text.split()
#     return len(words)
#
# # Function to count total characters excluding spaces
# def total_characters(text):
#     words = text.split()
#     return sum(len(word) for word in words)
#
# # Function to find the top 5 most frequent words
# def top_frequent_words(text):
#     words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
#     word_counts = Counter(word for word in words if word not in STOP_WORDS)
#     return word_counts.most_common(5)
#
# # Main function to analyze the text
# def analyze_text(text):
#     lines_count = num_of_lines(text)
#     words_count = total_words(text)
#     characters_count = total_characters(text)
#     frequent_words = top_frequent_words(text)
#
#     # Print the results
#     print("\nFile Analysis:")
#     print("-" * 18)
#     print(f"Total Lines: {lines_count}")
#     print(f"Total Words: {words_count}")
#     print(f"Total Characters (Excluding Spaces): {characters_count}")
#     print("Top 5 Most Frequent Words:")
#     for i, (word, count) in enumerate(frequent_words, 1):
#         print(f"{i}. {word} - {count}")
#
# # Sample Text
# text = ("This is a simple text file.  "
#         "The file is used for testing the Python script.  "
#         "Python is amazing, and this file helps demonstrate its power.  ")
#
# # Analyze the text
# analyze_text(text)

#
# text = ("This is a simple text file.  \n"
#         "The file is used for testing the Python script. \n "
#         "Python is amazing, and this file helps demonstrate its power.\n  ")
# def total_line(text):
#     count=0
#     for j in text:
#         if j=="\n":
#             count+=1
#     return count
# v=total_line(text)
# print("number of lines:",v)
#
# def total_word(text):
#     list=text.split()
#     count=0
#     for i in list:
#         count+=1
#     return count
# w=total_word(text)
# print("total words:",w)
#
# def total_charecters(text):
#     new=text.split()
#     count=0
#     for i in new:
#         count+=len(i)
#     return count
# z=total_charecters(text)
# print("excluding space:",z)
# print("\n")
# stop_word= {"and", "the", "is", "in", "this", "a", "of", "for", "its", "to", "on", "an"}
# print("top 5 freequently using words")
#
#
# main = ("This is a simple text file."
#         "The file is used for testing the Python script. "
#         "Python is amazing, and this file helps demonstrate its power.")
#
# def freequent_python(main):
#     new=main.split()
#     count=0
#     for i in new:
#         if i=="Python":
#             count+=1
#     return count
#
# c=freequent_python(main)
# print("Python:",c)
#
#
#
# def freequent_file(main):
#     new=main.split()
#     count=0
#     for i in new:
#         if i=="file":
#             count+=1
#     return count
# a=freequent_file(main)
# print("file:",a)
#
#
# def freequent_is(main):
#     new=main.split()
#     count=0
#     for i in new:
#         if i=="is":
#             count+=1
#     return count
# b=freequent_is(main)
# print("is:",b)
#
# def freequent_this(main):
#     new = main.split()
#     count = 0
#     for i in new:
#         if i.lower() == "this":
#             count += 1
#     return count
# g = freequent_this(main)
# print("this:", g)


# def large(list):
#     max=list[0]
#     for i in range(len(list)):
#         if max<list[i]:
#             max=list[i]
#     return max
# list=[1,2,3,4,5,6,7]
# v=large(list)
# print(v)



# class calculator():
#     def add(self,a,b=None,c=None):
#         if b is None and c is None:
#             return a
#         elif c is None:
#             return a+b
#         else:
#             return a+b+c
# cal=calculator()
# print(cal.add(10,20,30))


# word=open('into.txt','r')
# n=word.read()
# print(n)


# class bank:
#     def _init_(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposite(self,amount):
#         self.balance+=amount
#         print(f"you balance:{self.balance} deposite amount:{amount}")
#     def withdrawn(self,amount):
#         if amount>self.balance:
#             print(f"dont have enough balance")
#         else:
#             self.balance-=amount
#             print(f"your balnce:{self.balance} you withdrawn {amount}")
# name1=bank("sheikh",400)
# print(f"account holder: {name1.name}, \nbalance: {name1.balance}")
# deposit=int(input("enter deposit amount"))
# name1.deposite(deposit)
# withdraw=int(input("enter withdraw amount"))
# name1.withdrawn(withdraw)




# class bank:
#     def _init_(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposite(self,amount):
#         self.balance+=amount
#         print(f"balance:{self.balance},deposite amount:{amount}")
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print(f"not enough cash,your balance{self.balance}")
#         else:
#             self.balance-=amount
#             print(f"balance:{self.balance},withrow amount:{amount}")
# name1=bank("sheikh",200)
# print(name1.name,name1.balance)
# deposite=int(input("enter you amount"))
# name1.deposite(deposite)
# withdrow=int(input("enter you amount"))
# name1.withdraw(withdrow)



# word=open('simple.txt','r')
# n=word.read()
# print(n)
#
# def total_line(n):
#     count=1
#     for i in n:
#         if i=='\n':
#             count+=1
#     return count
# v=total_line(n)
# print("total line:",v)
#
# def total_words(n):
#     list=n.split()
#     count=0
#     for i in list:
#         count+=1
#     return count
# w=total_words(n)
# print("total words:",w)
#
# def total_words_excluding_space(n):
#     list=n.split()
#     count=0
#     for i in list:
#         count+=len(i)
#     return count
# z=total_words_excluding_space(n)
# print("excluding space:",z)
# print("\n")
#
# print("top 5 freequent repeated words")
#
# def freequency(n):
#     list=n.split()
#     dic={}
#     for i in list:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     return dic
#
# def most_repeated(n):
#     dic=freequency(n)
#     list=sorted(dic.items(),key=lambda x:x[1],reverse=True)
#     return list[:5]
# top_5=most_repeated(n)
# for i,cou in top_5:
#     print(f"{i}={cou}")


# ls=[1,2,2,3,4,5,6,4]
# list=[]
# new=[]
# for i in range(len(ls)):
#     for j in range(i,len(ls)):
#         if ls[i]==ls[j]:
#             list.append((i,j))
#         else:
#             new.append(ls[i])
# s



# class bank():
#     def _init_(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposite(self,amount):
#         self.balance+=amount
#         print(f"balance:{self.balance}amount:{amount}")
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("issufficiant balnae")
#         else:
#             self.balance-=amount
#             print(f"balance:{self.balance},amount:{amount}")
# obj=bank("sheikh",2000)
# print(obj.name,obj.balance)
# deposite=int(input("enter deposite amount"))
# obj.deposite(deposite)
# withdrow=int(input("enter withdraw amount"))
# obj.withdraw(withdrow)



# list="my name is sheikh"
# new=list.split()
# dic={}
# for i in new:
#     dic[i]=len(i)
# print(dic)



# list="my name is sheikh"
# new=list.split()
# now=[]
# for i in new:
#     capital=i[0].upper()+i[1:]
#     now.append(capital)
# print(now)



# list="my name is sheikh"
# capital=list[:-1]+list[-1].upper()
# print(capital)


# dic={'a':200,'b':400,'c':6000}
# max=None
# key=None
# dict={}
# for i,j in dic.items():
#     if max is None or j>max:
#         max=j
#         key=i
# print(key,":",max)
# for i,j in dic.items():
#     if max!=j:
#         dict[i]=j
# print(dict)