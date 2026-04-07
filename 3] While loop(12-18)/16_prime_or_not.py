#check the entered no. is prime or not
n=int(input('Enter no. to check no. is prime or not : '))
i=2
if n==0 or n==1:
        print('not prime')
result=0 
while i<n:
    
    if n%i==0:
        result=1
        break
    i=i+1
if  result==1:
     print("not prime")
else:
     print("prime")
    
    
    
   


