#Write a Python program to find the first even and odd number in a given list of numbers. Original list: [1, 3, 5, 7, 4, 1, 6, 8]

a=[1, 3, 5, 7, 4, 1, 6, 8]
even=None
odd=None
for i in a:
    if i%2!=0:
        odd=i
        break
for j in a:
    if j%2==0:
        even=j
        break
print('First even no. is :',even)
print('First odd no. is:',odd)