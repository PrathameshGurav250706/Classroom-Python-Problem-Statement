#w.a.p print fibonacci series upto n using while
n=int(input('Enter upto print fibonacci series : '))
a=int(input('Enter first no. : '))
b=int(input('Enter second no. : '))
i=1

print(a)
print(b)
add=a+b
while i<=n:
    print(add)
    a=b
    b=add
    add=a+b
    
    i=i+1


