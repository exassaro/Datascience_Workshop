def generator(num):
    count = 1
    while count <= num:
        yield count #return next value but duration pauses
        count +=1
        
gen =generator(4) #generator object

print(next(gen))
print(next(gen))