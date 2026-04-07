# find largest no.between 3 numbers using lamda
a=lambda x,y,z:print(x) if x>y and x>z else (print(y) if y>z else print(z)) 

c=int(input('Enter first no. : '))
d=int(input('Enter second no. : '))
e=int(input('Enter third no. : '))
a(c,d,e)