#Implement program to remove duplicate words from a given string.
s = "hello my name is prathamesh hello "
words = s.split()
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

result = " ".join(unique_words)
print(result)