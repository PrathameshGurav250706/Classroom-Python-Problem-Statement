#Implement program to change a given string to a newly string where the first and last chars have been exchanged.
a=input('Enter string :')

print('Original :',a)
print('New string:',a[-1]+a[1:-1]+a[0])