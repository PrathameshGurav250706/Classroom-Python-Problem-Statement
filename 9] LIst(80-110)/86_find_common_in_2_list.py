#WAP to take two lists and find common elements in the list.
s=[11,12,13,14,15]
t=[21,12,23,14,25]
u=[]
for i in s:
    if i in t:
        u.append(i)
print(u)