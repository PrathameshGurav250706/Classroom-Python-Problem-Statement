#print 
# A  
# A B  
# A B C 
# A B C D
# A B C D E
s=int(input('Enter how many times print : '))
for i in range(1,s+1):
    ch=65
    for j in range(i):
        print(chr(ch),end=" ")
        ch=ch+1
    print()




