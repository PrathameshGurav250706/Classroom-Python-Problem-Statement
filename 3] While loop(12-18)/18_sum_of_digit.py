# find the sum of digits of the given number using while
s=int(input('Enter a number : '))
add=0
while s>0:
    digit=s%10
    add=add+digit
    s=s//10
print('Sum of digits is',add)
