#Write a Python program to find the key of the maximum value in a dictionary.
# d = {'a': 10, 'b': 50, 'c': 30}
# max_key = max(d, key=d.get)
# print("Key with maximum value:", max_key)

#----------------------------------------------------------

s = {'a': 10, 'b': 50, 'c': 30}
for i,j in s.items():
    if j == max(s.values()):
        print("Key with maximum value:", i)