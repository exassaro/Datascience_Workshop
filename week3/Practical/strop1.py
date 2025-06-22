name="my name is shahinsha"
new=name.split()
now=""
for i in new:
    capital=i[0].upper()+i[1:]
    now+=capital+" "
    
print(now)

def reversed_words(st):
    return " ".join(word[0].upper()+word[1:] for word in st.split())
    
x="How are you"
print(reversed_words(x))