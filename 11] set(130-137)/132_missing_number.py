#Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa
a={1,2,3,4}
b={1,3,4,5}
# for i in list(b):
#     if i not in a:
#         print(f'{i} is missing in set a')
# for j in list(a):
#     if j not in b:
#         print(f"{j} is missing in set b")

print("missing in b is ",a-b)
print("missing in a is ",b-a)