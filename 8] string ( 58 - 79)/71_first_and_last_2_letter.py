#Implement program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
a='prathamesh'
if len(a)<2:
    print('')
else:
    print(a[0:2],a[-2:])

