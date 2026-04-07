#Write a Python program to get unique values from a list.
a=[1,2,3,4]
b=[1,2,3,4,5,6]
c=[]
for i in a:
    if i in b:
        c.append(i)

print('Unique words are :',c)

