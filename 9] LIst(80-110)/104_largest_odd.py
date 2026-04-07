#Write a Python program to find the largest odd number in a given list of integers.
#  Sample Data: ([0, 9, 2, 4, 5, 6]) ans 9
#  ([-4, 0, 6, 1, 0, 2]) ans 1

data=[0, 9, 2, 4, 5, 6]
odd=[]
for i in data:
    if i%2!=0:
        odd.append(i)

print('Maximum odd no. is',max(odd))