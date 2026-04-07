# find the sum of digit of the given number using function
def addition(s):
    
    add=0
    while s>0:
        digit=s%10
        add=add+digit
        s=s//10
    print(f'Addition of digits : {add}')
    
a=int(input('enter no. : '))
addition(a)
