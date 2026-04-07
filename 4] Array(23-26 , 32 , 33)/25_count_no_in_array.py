# w.a.p to count how many times entered number is present
num=int(input("Enter no. to count : "))
count=0
import array as data
d=data.array('i',[1,2,3,4,2,4,5,6,2])          #Sample array
for i in d:
    if num==i:                                  #check condition
        count=count+1                           #coutn increase by 1 if no.is found
print(f"{num} is present {count} times")