#Write a Python function that takes a list of words and return the longest word and the length of the longest one
a=['Maharashtra','kerala','odisha','gujarat']
for i in a:
    length=len(a[0])
    word=a[0]
    if length<len(i):
        length=len(i)
        word=i
print(f'Longest word is {word} and length is {length}')