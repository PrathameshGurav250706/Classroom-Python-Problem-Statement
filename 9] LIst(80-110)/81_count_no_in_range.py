#Write a Python program to count the number of elements in a list within a specified range.
s=[1,2,3,4,5,6,7,8]
count=0
for i in s:
    if i in range(1,6):
        count+=1
print(f'elements in range 1-6 are :',count)