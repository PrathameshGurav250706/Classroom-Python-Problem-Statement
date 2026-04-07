# find a factorial of a given number using function

def fact():                     #function 
    n=int(input('Enter no. for factorial : '))
    result=1
    for i in range(1,n+1):      #loop run upto n
        result=result*i
    print("Factorial is ",result)
fact()                          #function calling
