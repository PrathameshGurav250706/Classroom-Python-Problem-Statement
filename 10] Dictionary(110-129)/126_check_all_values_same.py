#Write a Python program to verify that all values in a dictionary are the same
# {'a’: 12, ‘b': 12, ‘c’: 12} Check all are 12 in the dictionary. True False
s = {'a': 12, 'b': 12, 'c': 12}
key=s['a']
for i,j in s.items():
    if j != key:
        print("False")
        break
else:
    print("True")