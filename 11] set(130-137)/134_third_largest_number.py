#Write a Python program to find the third largest number from a given set of numbers
a={3,1,5,2,4,25}
b=list(sorted(a))
length=len(b)
print(b)
print(f"{b[length-3]} is the 3rd largest no.")