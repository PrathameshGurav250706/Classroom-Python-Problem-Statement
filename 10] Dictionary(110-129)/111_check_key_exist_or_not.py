#WAP to check whether a given key already exists in a dictionary
a={1:'abc',"s":25}
key=input("Enter no.(key) to check present or not :")
if key.isalnum():
    key=int(key)

flag=0
for i in a:
    if key==i:
        flag=1
if flag==1:
    print('The given no.(key) is present ')
else:
    print('Not present')
        
#------------------------
print(key in a.keys())