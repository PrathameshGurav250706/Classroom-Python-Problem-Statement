#Write a Python program to sum all the items in a dictionary
# s = {'a': 10, 'b': 20, 'c': 30}
# total = sum(s.values())
# print("Sum of values:", total)

s = {'a': 10, 'b': 20, 'c': 30}
count = 0
for i,j in s.items():
    count = count + j
print("Sum of values:", count)
    