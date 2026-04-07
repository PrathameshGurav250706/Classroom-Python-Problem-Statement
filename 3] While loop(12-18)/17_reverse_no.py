# w.a.p to reverse the given number using while
s=int(input('Enter a number : '))
reverse=0
while s>0:
    digit=s%10
    reverse=reverse*10+digit
    s=s//10
print('Reverse of number is : ',reverse)