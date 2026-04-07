#Write a Python program to get the frequency of elements in a given list of lists. Original list of lists: [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]] Frequency of the elements in the said list of lists: {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

data=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
add1=[]
add2=[]
for i in data:
    for j in i:
        add1.append(j)
print(add1)

for i in add1:
    if i not in add2:
        add2.append(i)
        print(i,":",add1.count(i),end=" , ")
       
            
           




#method 2   
# Original list of lists
# list_of_lists = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# frequency = {}
# for sublist in list_of_lists:
#     for element in sublist:
#         if element in frequency:
#             frequency[element] += 1
#         else:
#             frequency[element] = 1

# print("Original list of lists:", list_of_lists)
# print("Frequency of the elements:", frequency)