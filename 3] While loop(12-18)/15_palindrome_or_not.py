# w.a.p to check whether number is palindrome or not using while
s=int(input('Enter a number : '))
reverse=0
original=s

while s>0:
    digit=s%10
    reverse=reverse*10+digit
    s=s//10
if original==reverse:
    print('Palindrome')
else:
    print('not')

