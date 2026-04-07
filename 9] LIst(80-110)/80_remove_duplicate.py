#remove duplicate
a=[1,2,3,2,3,5,6]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)