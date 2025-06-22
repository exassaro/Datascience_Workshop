def word_occur(sentence):
    words = sentence.lower().split()

    word_count={}

    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count

sentence=input("enter a sentence : ")

print(word_occur(sentence))

            