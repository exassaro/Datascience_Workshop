def count_vowel(s):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char in vowels:
            count+=1
    return count

str="Shahinsha"
vowels1=count_vowel(str)
print(f"{vowels1}")