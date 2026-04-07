#w.a.p print fibonacci series upto n using function
def fibo():
    a=int(input('Enter first no. : '))
    b=int(input('Enter second no. : '))
    c=int(input("Enter upto print : "))

    print(a)
    print(b)
    add=a+b
    for i in range(a,c-1):
        print(add)
        a=b
        b=add
        add=a+b
fibo()


    