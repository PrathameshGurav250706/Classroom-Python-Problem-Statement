#WAP to write 1 to 20 numbers to file and read only odd numbers
f1=open("C:\\Users\\Prathamesh\\OneDrive\\Desktop\\Language\\Python\\148.txt","w")
for i in range(1,21):
    f1.write(str(i) + " ")
f1.close()

f2=open("C:\\Users\\Prathamesh\\OneDrive\\Desktop\\Language\\Python\\148.txt","r")
s=f2.read()
t=s.split()
for i in t:
    num=int(i)
    if num%2!=0:
        print(num)
        
f2.close()