#Write a Python program to listify the list of given strings individually using map
#method 1
print(list(map(lambda x:print(list(x)),['kolhapur','pune','satara'])))

#method 2
# print(list(map(lambda x:list(x),['kolhapur','pune','satara'])))