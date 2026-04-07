#Write a Python program to convert a list of characters into a string.
#method 1
# List of characters
# char_list = ['P', 'y', 't', 'h', 'o', 'n']
# result = ''.join(char_list)
# print("Converted String:", result)

#method 2
char_list = ['P', 'y', 't', 'h', 'o', 'n']
result = ""

for ch in char_list:
    result += ch

print("Converted String:", result)