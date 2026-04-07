#print 
# A B C  
# A B C  
# A B C  
s=int(input('Enter how many times to print : '))
for i in range(s+1):
    for j in range(65,65+s):
        print(chr(j),end=" ")
    print()
  