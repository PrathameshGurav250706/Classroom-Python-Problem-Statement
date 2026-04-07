#WAP to remove an item from a set if it is present in the between two sets.
a={1,2,3,4,5}
b={3,4,5,6,7,8}

# for i in list(a):
#     if i in b:
#         a.remove(i)
# print(a)       
#----------
a={1,2,3,4,5}
b={3,4,5,6,7,8}
for i in a.intersection(b):
    a.remove(i)
print(a)


c=a-b
print(c)