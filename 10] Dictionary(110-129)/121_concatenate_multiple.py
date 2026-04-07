#Write a Python script to concatenate the following dictionaries to create a new one
d1 = {'a': 1}
d2 = {'b': 2}
d3 = {'c': 3}

new_dict = {}
for d in (d1, d2, d3):
    new_dict.update(d)

print("Concatenated Dictionary:", new_dict)