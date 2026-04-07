#Write a Python program that creates a list of names and uses the filter function to extract names that start with a vowel (A, E, I, O, U).

# def show(n):
#     if n.startswith('A') or n.startswith('E') or n.startswith('I') or n.startswith('O') or n.startswith('U'):
#         print(n)

# a=filter(show,['Apple','Ink','Banana'])
# print(list(a))


print(list(filter(lambda n:True if n.startswith('A') or n.startswith('E') or n.startswith('I') or n.startswith('O') or n.startswith('U') else False,['Apple','Ink','Banana','Oil'])))


# print(list(filter(lambda x:True for i in 'aeiouAEIOU' if x.startswith(i) else )))