#Write a Python function to reverse a string if its length is a multiple of 4.
word=input('Enter string:')
if len(word)%4==0:
    print('Reverse :',word[::-1])
