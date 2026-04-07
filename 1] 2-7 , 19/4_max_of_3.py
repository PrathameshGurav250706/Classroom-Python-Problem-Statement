# w.a.p to find max of three number
a=int(input('Enter first number : '))
b=int(input('Enter second number : '))
c=int(input('Enter third number : '))
if a>b and a>c:
    print('first is greater')
elif b>c:
    print('second is greater')
else:
    print('third is greater')