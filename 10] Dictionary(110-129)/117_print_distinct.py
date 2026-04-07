#Write a Python program to print all distinct values in a dictionary.
d = {'a': 10, 'b': 20, 'c': 10, 'd': 30}

distinct_values = set(d.values())
print("Distinct Values:", distinct_values)