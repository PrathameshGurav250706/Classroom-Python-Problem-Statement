# w.a.p to find out entered number is present or not in array
num=int(input('Enter to check present or not : '))      #Enter no.
import array as data         #required to immport array
s=data.array('i',[1,2,3,4,5,6,7,8,9,10])          #Sample array
for i in s:
    if num==i:                  #check condition
        print('present')
        break
else:
    print("Not present")
    