str="I have been very much happy"

word = str.split()
lrg_word=max(word, key=len)
print(lrg_word)


#without max keyword
str2="Muhammed shahinsha"
word = str2.split()
largest_word = ""
max_length = 0

for words in word:
    if len(words) > max_length:
        largest_word = words
        max_length = len(words)
        
print (largest_word)