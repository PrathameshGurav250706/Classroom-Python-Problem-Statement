'''
if we can use a.pop(2), it can remove element at index 2 and
if we can use a.remove(2), it can remove element of value 2

'''

#WAP to remove Even Numbers from List
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i%2==0:
        a.remove(i)
print(a)
