#Write a Python program to find the list in a list of lists whose sum of elements is the highest. I/P lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9] Expected Output: [10, 11, 12]
l1=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
add=0
empty=[]    
for i in l1:
    for j in i:
        add+=j
    empty.append(add)
    add=0   
print(empty)
max1=max(empty)
index=empty.index(max1)
print(l1[index])
