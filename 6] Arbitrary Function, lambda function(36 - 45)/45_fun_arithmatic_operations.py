# Arithmatic operation using menu driven using function

#    functions
def add():
    print('Addition :',a+b)
def sub():
    print('Subtraction :',a-b)
def multi():
    print('Multiplication :',a*b)
def div():
    print('Division :',a/b)

#     menu
a=int(input('Enter first number : '))
b=int(input('Enter second number : '))
print()
print('----------operations--------')
print('1-Addition')
print('2-Subtraction')
print('3-multiplication')
print('4-division')
print()
num=int(input('Enter number according to menu : '))
if num==1:
    add()
elif num==2:
    sub()
elif num==3:
    multi()
else:
    div()

