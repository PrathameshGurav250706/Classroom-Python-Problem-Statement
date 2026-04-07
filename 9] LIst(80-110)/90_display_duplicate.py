#Display duplicate numbers from list
show=[1,1,2,2,3,4,5,5]
list1=[]
for i in show:
    if show.count(i)>=2:
        if i not in list1:
            list1.append(i)
print(list1)