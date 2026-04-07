#print
# A B C D E
# A B C D
# A B C
# A B
# A

s=int(input('Enter how many times to print : '))
for i in range(s,0,-1):
    ch=65
    for j in range(i):
        print(chr(ch),end=" ")
        ch=ch+1
    print()