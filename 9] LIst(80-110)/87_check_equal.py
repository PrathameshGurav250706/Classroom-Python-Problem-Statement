#Write a Python program to check if all items in a given list of strings are equal to a given string. E.g.Lsit1=[“Hello”, “Hello”] & input string=”Hello” it returns True otherwise False

text='hi'
list1=['hi','hi','hi']
for i in list1:
    if i!=text:
        print('False')
else:
    print('true')