#Implement program to extract numbers from a given string.
a='prathamesh12345'
b=''
for i in a:
    if i.isdigit():
        b=b+i
print(b)