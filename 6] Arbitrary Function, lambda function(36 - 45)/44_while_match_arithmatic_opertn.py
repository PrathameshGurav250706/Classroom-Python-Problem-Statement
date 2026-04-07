# Arithmatic operation using menu driven using  while & match
while True:
    a=int(input('Enter first number : '))
    b=int(input('Enter second number : '))
    print('----------operations--------')
    print('1-Addition')
    print('2-Subtraction')
    print('3-multiplication')
    print('4-division')
    
    num=int(input('Enter number according to menu : '))
    match num:
        case 1:
            print(a+b)
        case 2:
            print(a-b)
        case 3:
            print(a*b)
        case 4:
            print(a/b)
        case _:
            print('Enter valid no.')
        
    s=input('Do you want to continue y/n : ')
    n='n'
    if s.lower()==n:
     break

           

        