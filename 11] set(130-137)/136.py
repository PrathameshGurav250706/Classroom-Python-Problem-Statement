#WAP to find the longest common prefix of all strings in given set
a={'flight','flow','flower'}
a=list(a)
prefix=a[0]

for i in range(1,len(a)):
    while a[i].find(prefix)!=0:
        prefix=prefix[:-1]
print("Longest common prefix :",prefix)