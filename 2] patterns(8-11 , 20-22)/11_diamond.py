#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * 
#   * * * * * * *
#     * * * * * 
#       * * *
#         *



n=int(input('Enter number : '))    #give number of rows
for i in range(1,n+1):          #outer loop for rows
    for j in range(n-i):        #inner loop for spaces
        print(' ',end=" ")
    for k in range(2*i-1):      #inner loop for stars
        print('*',end=" ")
    print()

# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(' ',end=" ")
#     for k in range(2*i-1):
#         print('*',end=" ")
#     print()