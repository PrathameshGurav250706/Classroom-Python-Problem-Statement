#Write a Python program to create a dictionary from a string. i/p hello o/p : {‘h’:1,’e’:1,’l’:2…}
a='hello'
b={}
for i in a:
    b[i]=a.count(i)
print(b)