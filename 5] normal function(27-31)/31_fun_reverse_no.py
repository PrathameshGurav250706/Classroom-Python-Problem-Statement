# reverse the number using function
def reverse(a):
    org=a
    rev=0
    while a>0:
        digit=a%10
        rev=rev*10+digit
        a=a//10
    print(f'Reverse of number {org} is',rev)

    
num=int(input("enter no. : "))
reverse(num)