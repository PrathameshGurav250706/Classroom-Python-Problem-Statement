#Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same
a=['mom','dad','madam','prathamesh']
count1=0
for i in a:
    if len(i)>=2 and i[0]==i[-1] :
        count1+=1

print('Count is :',count1)