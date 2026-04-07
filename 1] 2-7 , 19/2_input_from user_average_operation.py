# # take three integers from keyboard and calculate its average[validation-number should not be -ve,zero,string]
a=input('Enter first number : ')
b=input('Enter second number : ')
c=input('Enter third number : ')
print('Enterd numbers are',a,b,c)

if a.isdigit() and b.isdigit() and c.isdigit():
    a=int(a)
    b=int(b)
    c=int(c)

    if a>0 and b>0 and c>0:
        print('Average :',(a+b+c)/3)
    else:
        print('Enter valid numbers')
        
else:
    print('Enter valid numbers')
    




 