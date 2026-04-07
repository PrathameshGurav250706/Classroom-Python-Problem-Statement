#Write a Python program to remove duplicate words from a given list of strings.
#  Original String: ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises'] 
# After removing duplicate words from the said list of strings: ['Python', 'Exercises', 'Practice', 'Solution']

org=['Python', 'Exercises', 'Practice', 'Solution', 'Exercises'] 
data=[]
for i in org:
    if i not in data:
        data.append(i)
    else:
        org.remove(i)


# print('After removing duplicate :',data)
print(org)