# w.a.p to input marks , student name & percentage of student and display appropriate grade ; percentage should not be 100 %, zero , negative
a=input('Enter name : ')
b=int(input('Enter marks : '))
c=float(input('Enter percentage : '))
if c==100 or c<=0:
    print('Enter valid percentage')
print('----------------------')
print('name :',a)
print('Marks :',b)
print('Percentage :',c)
if c>=85:
    print('grade : A')
elif c>=60 and c<85:
    print('grade : B')
elif c>=40 and c<60:
    print('grade : C')
else:
    print('grade : D')