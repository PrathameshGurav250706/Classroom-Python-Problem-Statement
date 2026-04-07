# find largest no.between 2 numbers using lamda
a=lambda x,y:print(x,'is largest no.') if x>y else print(y,'is largest no.')
c=int(input('Enter first no. : '))
d=int(input('Enter second no. : '))
a(c,d)