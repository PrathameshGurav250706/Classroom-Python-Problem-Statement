#WAP to generate and print a dictionary that contains a number (between 1 and n) in the form {1:12, 2:22,…..n}.i.e {1:1,2:4,3:9,…..}
num=int(input('Enter number : '))
a={}
for i in range(1,num+1):
    a[i]=i*i
print(a)

