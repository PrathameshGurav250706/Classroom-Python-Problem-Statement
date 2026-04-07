#print number in sorted order without inbuilt function
a=[5,2,88,25,1,6,3]
# for i in range(len(a)):
#     for j in range(len(a)-1-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]

# print(a)
a.sort()
print(a)