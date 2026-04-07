#Write a Python program that takes a list of integers and finds all pairs of integers that differ by three. Return all pairs of integers in a list. 
# Sample Data: ([0, 3, 4, 7, 9]) -> [[0, 3], [4, 7]]
#  [0, -3, -5, -7, -8] -> [[-3, 0], [-8, -5]] 
# ([1, 2, 3, 4, 5]) -> [[1, 4], [2, 5]]

data=[0, 3, 4, 7, 9]
empty=[]
for i in data:
    for j in data:
        if (i-j)==3:
            empty.append([j,i])
print("pairs of integers that differ by three :",empty)