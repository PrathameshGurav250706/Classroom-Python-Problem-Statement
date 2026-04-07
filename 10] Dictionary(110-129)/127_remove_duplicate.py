#WAP to remove same element from list of values from dictionary.
# 1:[11,12,13,11,5,12],2:[‘a’,’b’,’a’,’c’}
# d = {1: [11,12,13,11,5,12], 2: ['a','b','a','c']}

# for key in d:
#     d[key] = set(d[key])

# print("After removing duplicates:", d)
#----------------------------------------------------------
s = {1: [11,12,13,11,5,12], 2: ['a','b','a','c']}
empty = {}
for i,j in s.items():
    empty[i] = set(j)
print(empty)

#----------------------------------------------------------
# s = {1: [11,12,13,11,5,12], 2: ['a','b','a','c']}
# empty = {}

# for i, j in s.items():
#     new_list = []
#     for item in j:
#         if item not in new_list:
#             new_list.append(item)
#     empty[i] = new_list

# print(empty)