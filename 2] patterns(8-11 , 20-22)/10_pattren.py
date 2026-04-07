# A 
# B B 
# C C C 
# D D D D 
# E E E E E
n=int(input('enter number : '))    #give number of rows
for i in range(65,65+n):           #outer loop for rows
    for j in range(65,i+1):        #inner loop for characters
        print(chr(i),end=" ")       #print character using ascii value
    print()
    