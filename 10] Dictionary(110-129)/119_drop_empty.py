#Write a Python program to drop empty elements(None) from a given dictionary
s = {'a': 1, 'b': None, 'c': 3}

for i,j in list(s.items()):
    if j is None:
        s.pop(i)
print(s)
