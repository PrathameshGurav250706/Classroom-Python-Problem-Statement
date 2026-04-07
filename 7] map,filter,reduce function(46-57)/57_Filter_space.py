#Write a Python function that filters out all empty strings from a list of strings using the filter functionE.g. 
# I/p is [' ', 'Pune', 'Kolhapur', ' ', 'Satara', ' ']
# O/P is is ['Pune', 'Kolhapur', 'Satara']


# def show(n):
#     if n!=' ':
#         print(n)

# a=filter(show,[' ', 'Pune', 'Kolhapur', ' ', 'Satara', ' '])
# print(list(a))



print(list(filter(lambda x:False if x==' ' else True,[' ', 'Pune', 'Kolhapur', ' ', 'Satara', ' '])))

