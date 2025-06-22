#reverse sentence

def reversed_word(sentence):
    words = sentence.split()
    reversed_word = words[::-1]
    return " ".join(reversed_word)

sentence =input("Enter a sentence: ")
print(reversed_word(sentence))


#reverse words

    
def reversed_word(sentence):
    words = sentence.split()
    reversed_word = [word[::-1] for word in words]
    return " ".join(reversed_word)

sentence =input("Enter a sentence: ")

print(reversed_word(sentence))
    
    
