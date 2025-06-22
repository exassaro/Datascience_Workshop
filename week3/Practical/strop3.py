string = "ball ball bat bat ball apple apple apple apple apple ink ink ink ink"
words = string.split()
dic = {}
res = set()

# Count occurrences
for i in words:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)



# Collect words that appear at least twice
for i in words:
    if dic[i] >= 2:
        res.add(i)

# Convert set to list
result = list(res)

# Sort result based on original word frequency in descending order
result.sort(key=lambda x: dic[x], reverse=True)
print(result)

# Print the two most frequently occurring words
print(result[:2])





#another method

# def most_frequent_words(string):
#     words = string.split()
#     word_counts = {}

#     # Count occurrences of each word
#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1

#     # Sort the dictionary by occurrences in descending order
#     sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

#     # Extract the top 2 words
#     result = [sorted_words[i][0] for i in range(min(2, len(sorted_words)))]

#     return result

# # Example usage
# string = "ball ball bat bat ball apple ink ink ink"
# print(most_frequent_words(string))


#using yield

# def most_frequent_words(string):
#     words = string.split()
#     word_counts = {}

#     # Count occurrences of each word
#     for word in words:
#         word_counts[word] = word_counts.get(word, 0) + 1

#     # Sort the dictionary by occurrences in descending order
#     sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

#     # Yield the top 2 words
#     for i in range(min(2, len(sorted_words))):
#         yield sorted_words[i][0]

# # Example usage
# string = "ball ball bat bat ball apple ink ink ink"
# top_words = most_frequent_words(string)

# # Printing words one by one
# for word in top_words:
#     print(word)
