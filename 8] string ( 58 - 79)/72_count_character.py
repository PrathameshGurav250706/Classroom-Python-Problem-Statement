#Implement program to count the number of characters (character frequency) in a string
a='hello!@#$!'
LIST1=[]
count=0
for i in a:
    if not i.isalnum():
        if i not in LIST1:
            print(i,":",a.count(i))
            LIST1.append(i)
        