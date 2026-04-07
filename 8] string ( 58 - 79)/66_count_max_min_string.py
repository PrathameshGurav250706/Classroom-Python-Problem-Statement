#Implement program to find the smallest and largest words in a given string.
s = "hello my name is prathamesh gurav"

words = s.split()
smallest_word = words[0]
largest_word = words[0]

for i in words:
    if len(i) < len(smallest_word):
        smallest_word = i
    if len(i) > len(largest_word):
        largest_word = i

print("Smallest word:", smallest_word)
print("Largest word:", largest_word)