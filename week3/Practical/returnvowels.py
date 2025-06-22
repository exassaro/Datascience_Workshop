def count_vowel(s):
    vowels = set("aeiouAEIOU")
    vow=[]
    for char in s:
        if char in vowels:
            vow.append(char)
    return set(vow)

str="Shahinsha"
vowels1=count_vowel(str)
print(vowels1)