def reversed(sentence):
    words = sentence.split()
    str=""
    for word in words[::-1]:
        
    str.append(word)
    
    return str

str1="How are you"

print(reversed(str1))
    