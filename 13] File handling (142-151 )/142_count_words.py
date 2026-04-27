#Write a Python program to count the frequency of words in a file.
f1=open("C:\\Users\\Prathamesh\\OneDrive\\Desktop\\Language\\Python\\142.txt")
a=f1.read()
print(a)
b=a.split()
c={}
for i in b:
    if i in c:
        c[i]=c[i]+1
    else:
        c[i]=1
print(c)

f1.close()