#Write a Python program to find the key of the even value and should be greater than 25 in a dictionary
s={'a': 10, 'b': 50, 'c': 30, 'd': 25}
for i,j in s.items():
    if j%2==0 and j>25:
        print("Key with even value greater than 25:", i)