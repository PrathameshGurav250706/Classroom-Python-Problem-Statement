#Write a Python program to swap the first and last element of the list
a=[10,20,30,40,50]
org=a.copy()
a[0],a[-1]=a[-1],a[0]
print(f"original : {org}")
print(f"After swap : {a}")