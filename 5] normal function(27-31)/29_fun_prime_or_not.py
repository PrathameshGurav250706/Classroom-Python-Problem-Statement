#check the entered no. is prime or not using function
def fun():
    a=int(input('Enter a no. to check prime or not : '))
    if a==0 or a==1:
        print('not prime')
    for i in range(2,a):
        if a%i==0:
            print('not prime')
            break
    else:
        print('prime')
fun()