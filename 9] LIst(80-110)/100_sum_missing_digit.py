#Write a Python program to sum the missing numbers in a given list of integers. 
# Sample Data: ([0, 3, 4, 7, 9]) ans is
#  22 ([44, 45, 48]) ans is 93
add=0
data=[0, 3, 4, 7, 9]
empty=[]
for i in range(data[0], data[-1]+1):
    if i not in data:
        empty.append(i)
print(sum(empty))

