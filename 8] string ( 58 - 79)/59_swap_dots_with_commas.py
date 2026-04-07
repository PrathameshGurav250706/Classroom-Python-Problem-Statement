# Implement program to swap commas and dots in a string.
#  I/P string: "abc.pqr.xyz"
#  Output: " abc,pqr,xyz "

#method 1
# s='prathamesh.raj.rahul.atharav'
# t=s.replace('.',',')
# print(t)

#method 2
a='prathamesh.raj.rahul.atharav'
b=a.split('.')
print(','.join(b))

