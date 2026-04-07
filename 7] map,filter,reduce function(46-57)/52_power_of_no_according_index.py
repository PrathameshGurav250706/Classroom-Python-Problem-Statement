# Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using map i.p [[10, 20, 30, 40] index=[1,2,3,4] o/p =[10,400, 2700…]

print(list(map(lambda i,j:i**j,[10,20,30,40,50,],[1,2,3,4,5])))

