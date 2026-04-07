#WAP to check if two given sets have no elements in common
a={1,2,3,4,5,6}
b={6,7,8,9,10}
# for i in list(a):
#     if i in b:
#         print("sets contains common elements")
#         break
# else:
#     print('No common element')

if a.isdisjoint(b):
    print('No comon')
else:
    print("common")